"""recipebox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from recipebox import views
from recipebox.models import Author, Recipe

admin.site.register(Author)
admin.site.register(Recipe)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='homepage'),
    path('author/<int:author_id>/', views.author, name='author'),
    path('recipe/<int:recipe_id>/', views.recipe, name='recipe'),
    path('recipeadd/', views.recipeaddview, name='recipeadd'),
    path('authoradd/', views.authoraddview, name='authoradd'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('edit/<int:id>/', views.editrecipeview, name='edit')
    # path('recipe_favorites/<int:id>/', views.favorites, name='favorites'),
]

'''
 if settings.DEBUG
    urlpatterns += static
'''
