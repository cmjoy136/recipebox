from django.shortcuts import render, HttpResponseRedirect, reverse
from recipebox.models import Author, Recipe
from recipebox.forms import AuthorAddForm, RecipeAddForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def index(request):
    html = "index.html"
    recipes = Recipe.objects.all()


    return render(request, html, {'data': recipes})

def author(request, author_id):
    html = "author.html"
    author = Author.objects.filter(id=author_id).first()
    recipes = Recipe.objects.filter(author=author_id)

    return render(request, html, {"data": author, 'recipes': recipes})

def recipe(request, recipe_id):
    html = 'recipe.html'
    recipe = Recipe.objects.filter(id=recipe_id).first()

    return render(request, html, {"data": recipe})


def authoraddview(request):
    html = "generic_form.html"
    form = AuthorAddForm()

    if request.method == 'POST':
        form = AuthorAddForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                user = request.user,
                name = data['name'],
                bio = data['bio']
            )
            return HttpResponseRedirect(reverse('homepage'))

    return render(request, html, {'form': form})

@login_required
def recipeaddview(request):
    html = "generic_form.html"
    form = RecipeAddForm()
    if request.method == "POST":
        form  = RecipeAddForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                author = data["author"],
                title = data['title'],
                description = data['description'],
                time_required = data['time_required'],
                instructions = data['instructions']
            )
            return HttpResponseRedirect(reverse('homepage'))
    

    return render(request, html, {'form': form})

def login_view(request):
    html = "generic_form.html"
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            if user := authenticate(
                username=data['username'],
                password=data['password']
            ):
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', '/'))

    return render(request, html, {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))



