from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500
from recipe_collection.views import error_404, error_500
from django.conf import settings
from django.urls import path
from recipe_collection.views import (
    RecipeListView,
    RecipeDetailView,
    RecipeCreateView,
    RecipeUpdateView,
    RecipeDeleteView,
    ProfileUpdateView,
    ProfileDetailView,
    CustomPasswordChangeView,
    RecipeSearchView,
    login_view,
    register,
    logout_view,
    signup_view,
    LikeView,
    about_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RecipeListView.as_view(), name='home'),
    path('home/', RecipeListView.as_view(), name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
    path('password_change/', CustomPasswordChangeView.as_view(),
         name='password_change'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset.html'
    ), name='password_reset'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
            template_name='registration/password_reset_complete.html'
         ),
         name='password_reset_done'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipe/new/', RecipeCreateView.as_view(), name='recipe-create'),
    path('recipe/<int:pk>/update/',
         RecipeUpdateView.as_view(),
         name='recipe-update'),
    path('recipe/<int:pk>/delete/',
         RecipeDeleteView.as_view(),
         name='recipe-delete'),
    path('register/', register, name='register'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile'),
    path('profile/<int:pk>/update/',
         ProfileUpdateView.as_view(),
         name='profile-update'),
    path('profile/<int:pk>/',
         ProfileDetailView.as_view(),
         name='profile-detail'),
    path('search/', RecipeSearchView.as_view(), name='recipe-search'),
    path('recipe/<int:pk>/like/', LikeView.as_view(), name='like'),
    path('about/', about_view, name='about'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL,
#  document_root=settings.STATIC_ROOT)
# else:
#     urlpatterns += static(settings.STATIC_URL,
#  document_root=settings.STATIC_ROOT, show_indexes=True)


handler404 = error_404
handler500 = error_500
