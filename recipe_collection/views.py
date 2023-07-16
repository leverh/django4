from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Recipe, Profile
from django.contrib.auth.views import PasswordChangeView, PasswordResetCompleteView, PasswordResetConfirmView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.http import HttpResponseRedirect, JsonResponse
from .models import Profile, Recipe
from .forms import ProfileForm, RecipeForm, UserRegisterForm
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.


class RecipeListView(ListView):
    model = Recipe
    template_name = template_name = 'home.html'
    context_object_name = 'recipes'
    paginate_by = 10

    def get_queryset(self):
        return Recipe.objects.order_by('-id')


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = self.get_object()
        context['likes_count'] = recipe.get_likes_count()
        context['author'] = recipe.posted_by
        return context

    def get_object(self, queryset=None):
        recipe = super().get_object(queryset=queryset)
        return get_object_or_404(Recipe, pk=recipe.pk)


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'create.html'
    success_url = '/'
 
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        form.instance.image = form.cleaned_data['image']
        messages.success(self.request, 'Recipe has been created successfully! Thank you for your contribution!')
        return super().form_valid(form)

    def get_success_url(self):
        return self.success_url

    def render_to_response(self, context, **response_kwargs):
        response = super().render_to_response(context, **response_kwargs)
        if self.request.POST and self.request.is_ajax():
            response.status_code = 278
        return response
    

class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'update.html'
    success_url = 'home.html'  

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        recipe = self.get_object()
        if self.request.user == recipe.posted_by:
            return True
        return False

    def get_form_class(self):
        form_class = super().get_form_class()
        form_class.exclude = ['posted_by']  
        return form_class
    

class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Recipe
    template_name = 'delete.html'
    success_url = '/'
    success_message = "Recipe deleted successfully."

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.posted_by

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(self.request, self.success_message)
        return HttpResponseRedirect(success_url)

  
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
    return render(request, 'registration/login.html', {'error_message': error_message})


def logout_view(request):
    logout(request)
    return redirect('login')
    #return render(request, 'recipe_collection/logout.html')


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


class CustomPasswordChangeView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'registration/password_change_form.html'
    success_url = reverse_lazy('login')
    success_message = "Your password has been changed successfully!"


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    #email_template_name = 'recipe_collection/password_reset_email.html'
    template_name = 'password_reset.html'


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    def get_success_url(self):
        return reverse_lazy('password_reset_done')

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


def signup_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')  # Redirect to the login page after successful signup???
    else:
        form = UserRegisterForm()
    return render(request, 'signup.html', {'form': form})


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profile_update.html'
    
    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.request.user.pk})

    def get_object(self, queryset=None):
        return self.request.user.profile

    def form_valid(self, form):
        response = super().form_valid(form)
        self.request.session['profile_updated'] = True
        return response
    
@method_decorator(login_required, name='dispatch')
class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        recipes = Recipe.objects.filter(posted_by=profile.user)
        context['recipes'] = recipes
        return context
    

class RecipeSearchView(ListView):
    model = Recipe
    template_name = 'search_results.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Recipe.objects.filter(Q(headline__icontains=query) | Q(description__icontains=query))
        else:
            return Recipe.objects.all()
        
        
class LikeView(LoginRequiredMixin, View):
    def post(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        if request.user in recipe.liked_by.all():
            recipe.liked_by.remove(request.user)
        else:
            recipe.liked_by.add(request.user)
        return redirect('recipe-detail', pk=pk)


def error_404(request, exception):
    return render(request, '404.html', status=404)


def error_500(request):
    return render(request, '500.html', status=500)


