from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import Recipe, Profile
from django.contrib.auth.views import (
    PasswordChangeView, PasswordResetCompleteView, PasswordResetConfirmView,
    PasswordResetView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.http import HttpResponseRedirect, JsonResponse
from .models import Profile, Recipe
from .forms import ProfileForm, RecipeForm, UserRegisterForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import JsonResponse
from django.db import IntegrityError
from django.core.paginator import Paginator
from math import ceil

# Create your views here.


# Recipe List View: Displays a paginated list of all recipes,
# ordered by their IDs
class RecipeListView(ListView):
    model = Recipe
    template_name = 'home.html'
    context_object_name = 'recipes'
    paginate_by = 12

# Get the query set of recipes, ordering them by their IDs
    def get_queryset(self):
        return Recipe.objects.order_by('-id')

# Get the context data including pagination information
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5

        num_pages = paginator.num_pages
        current_page = context['page_obj'].number
        start_page = max(current_page - page_numbers_range, 1)
        end_page = min(current_page + page_numbers_range, num_pages)

        context['page_range'] = range(start_page, end_page + 1)
        context['current_page'] = current_page
        return context


# Recipe Detail View: Displays detailed information about a specific recipe
class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'
    context_object_name = 'recipe'

# Get the context data including likes count and author information
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = self.get_object()
        context['likes_count'] = recipe.get_likes_count()
        context['author'] = recipe.posted_by
        return context

# Get the specific recipe object or raise a 404 error if not found
    def get_object(self, queryset=None):
        recipe = super().get_object(queryset=queryset)
        return get_object_or_404(Recipe, pk=recipe.pk)


# Recipe Create View: Provides the functionality to create a new recipe
class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'create.html'
    success_url = '/'

# Ensure user is authenticated before proceeding with the request
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

# Validate and save the recipe form, displaying a success message
    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        form.instance.image = form.cleaned_data['image']
        messages.success(self.request, 'Recipe has been created successfully! '
                                       'Thank you for your contribution!')
        return super().form_valid(form)

# Define the URL to redirect to upon successful recipe creation
    def get_success_url(self):
        return self.success_url

# Render the response, handling AJAX requests if needed
    def render_to_response(self, context, **response_kwargs):
        response = super().render_to_response(context, **response_kwargs)
        if self.request.POST and self.request.is_ajax():
            response.status_code = 278
        return response


class FormInvalidRedirectMixin:
    def form_invalid(self, form):
        # Redirect to the home page when the form is invalid
        # (including when the user hasn't made any changes)
        return redirect('home')


# Recipe Update View: Provides the functionality to update an existing recipe
class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'update.html'
    success_url = reverse_lazy('home')

# Helper function to check if the form has any changes
    def has_form_changed(self, form):
        # Helper function to check if the form has any changes
        for field_name, field_value in form.cleaned_data.items():
            if field_value != form.initial.get(field_name):
                return True
        return False

# Handle the POST request for the update view
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            if self.has_form_changed(form):
                return self.form_valid(form)
        return self.form_invalid(form)

# Validate and save the updated recipe form
    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        recipe = self.get_object()

        # Check if a new image is provided in the form
        new_image = self.request.FILES.get('image')
        if new_image:
            # Delete the existing image, if any
            if recipe.image:
                recipe.image.delete()
            # Update the image with the new one
            recipe.image = new_image

        messages.success(self.request, 'Recipe has been updated successfully!')
        return super().form_valid(form)

# Test function to check if the logged-in user is the author of the recipe
    def test_func(self):
        recipe = self.get_object()
        if self.request.user == recipe.posted_by:
            return True
        return False

# Modify the form class to exclude the 'posted_by' field
    def get_form_class(self):
        form_class = super().get_form_class()
        form_class.exclude = ['posted_by']
        return form_class


# Recipe Delete View: Provides the functionality to delete a recipe
class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin,
                       SuccessMessageMixin, DeleteView):
    model = Recipe
    template_name = 'delete.html'
    success_url = '/'
    success_message = "Recipe deleted successfully."

# Test function to check if the logged-in user is the author of the recipe
    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.posted_by

# Delete the recipe and redirect to the success URL
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(self.request, self.success_message)
        return HttpResponseRedirect(success_url)


# Login view function: Handles user authentication and login
def login_view(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid login credentials'
    return render(request, 'registration/login.html',
                  {'error_message': error_message})


# Logout view function: Logs out the user and redirects to the login page
def logout_view(request):
    logout(request)
    return redirect('login')
# return render(request, 'recipe_collection/logout.html')


# Register view function: Handles user registration
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/signup.html', {'form': form})


# Custom Password Change View: allows users to change their password
class CustomPasswordChangeView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'registration/password_change_form.html'
    success_url = reverse_lazy('login')
    success_message = "Your password has been changed successfully!"

# Save the updated password and log out the user
    def form_valid(self, form):
        form.save()
        messages.info(
            self.request, "Your password has been changed successfully. "
                          "You will be redirected to log in again."
        )

        logout(self.request)
        return super().form_valid(form)


# Custom Password Reset View: start the password reset process
class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset.html'
    email_template_name = 'registration/password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')


# Custom Password Reset Confirm View: handles password reset confirmation
class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

    def form_valid(self, form):
        print("CustomPasswordResetConfirmView - form is valid")
        response = super().form_valid(form)
        return response

    def form_invalid(self, form):
        print("CustomPasswordResetConfirmView - form is invalid")
        return super().form_invalid(form)


# Custom Password Reset Complete View: displays success message
# for password reset
class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'

# def signup_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('recipe-home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'recipe_collection/signup.html', {'form': form})


# Signup view function: handles user registration with JSON response
def signup_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user:
                return JsonResponse({'success': True})
            else:
                return JsonResponse({
                    'success': False,
                    'message': 'Failed to create an account.'
                })

        else:
            return JsonResponse({
                'success': False,
                'message': 'Form validation failed.'
            })

    else:
        form = UserRegisterForm()

    return render(request, 'signup.html', {'form': form})


# Profile Update View: allows users to update their profile information
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profile_update.html'

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.request.user.pk})

    def get_object(self, queryset=None):
        return self.request.user.profile

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            profile_image = self.request.FILES.get('profile_image')
            if profile_image:
                self.request.user.profile.profile_image = profile_image
                self.request.user.profile.save()

        return super().form_valid(form)


# Profile Detail View: Displays detailed user profile
@method_decorator(login_required, name='dispatch')
class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'profile'

# Add user's recipes
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        recipes = Recipe.objects.filter(posted_by=profile.user)
        context['recipes'] = recipes
        return context


# Recipe Search View: lets users search for recipes
class RecipeSearchView(ListView):
    model = Recipe
    template_name = 'search_results.html'
    context_object_name = 'recipes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        context['search_query'] = query

        if query:
            context['total_results'] = Recipe.objects.filter(
                Q(headline__icontains=query) |
                Q(description__icontains=query) |
                Q(ingredients__icontains=query)
            ).count()
        else:
            context['total_results'] = 0

        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Recipe.objects.filter(
                Q(headline__icontains=query) |
                Q(description__icontains=query) |
                Q(ingredients__icontains=query)
            )
        else:
            return Recipe.objects.none()


# Like View: allows users to like or unlike a recipe
class LikeView(LoginRequiredMixin, View):
    def post(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        if request.user in recipe.liked_by.all():
            recipe.liked_by.remove(request.user)
        else:
            recipe.liked_by.add(request.user)
        return redirect('recipe-detail', pk=pk)


# 404 Error page
def error_404(request, exception):
    return render(request, '404.html', status=404)


# 500 Error page
def error_500(request):
    return render(request, '500.html', status=500)


def about_view(request):
    return render(request, 'about.html')
