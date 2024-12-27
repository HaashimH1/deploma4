from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib import messages
from profiles.utils import get_profiles_for_user, create_profile, edit_profile, delete_profile, make_all_profiles_inactive, activate_profile_for_user, get_active_profile_for_user

# Public Home Page
def home_view(request):
    return render(request, 'home.html')

# Registration View
def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})  # No 'users/' prefix

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})  # No 'users/' prefix

# Logout View
def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')

# Dashboard View (Requires Login)
@login_required
def dashboard_view(request):
    """Unified dashboard view that includes profile management."""

    if request.method == "POST":

        # Handle creating a profile
        if 'create_profile' in request.POST:
            job_title = request.POST.get('job_title')
            min_salary = request.POST.get('min_salary')
            is_full_time = request.POST.get('is_full_time') == 'on'
            city = request.POST.get('city')

            try:
                create_profile(request.user, job_title, min_salary, is_full_time, city)
                messages.success(request, "Profile created successfully!")
            except ValidationError as e:
                messages.error(request, e.message)
    
        # Handle activating a profile
        if 'activate_profile' in request.POST:
            profile_id = request.POST.get('profile_id')
            try:

                # make all proflies inactive
                make_all_profiles_inactive(request.user)

                # Use utility function to activate the selected profile
                activated_profile = activate_profile_for_user(request.user, profile_id)
                messages.success(request, f"Profile '{activated_profile.job_title}' is now active.")
            except Profile.DoesNotExist:
                messages.error(request, "The selected profile does not exist.")


        # Handle editing a profile
        if 'edit_profile' in request.POST:
            profile_id = request.POST.get('profile_id')
            job_title = request.POST.get('job_title')
            min_salary = request.POST.get('min_salary')
            is_full_time = request.POST.get('is_full_time') == 'on'
            city = request.POST.get('city')

            try:
                edit_profile(profile_id, request.user, job_title, min_salary, is_full_time, city)
                messages.success(request, "Profile updated successfully!")
            except ValidationError as e:
                messages.error(request, e.message)

        # Handle deleting a profile
        if 'delete_profile' in request.POST:
            profile_id = request.POST.get('profile_id')
            delete_profile(profile_id, request.user)
            messages.success(request, "Profile deleted successfully!")

        
        # After handling the POST request, redirect to reload the page
        return redirect("dashboard")

    profiles = get_profiles_for_user(request.user)  # Get all profiles for the user
    active_profile = get_active_profile_for_user(request.user)
    profiles_count = len(profiles) # Get the amount of profiles for the user

    return render(request, 'dashboard.html', {
        'profiles': profiles,
        "profiles_count": profiles_count,
        "active_profile": active_profile
        })

  




