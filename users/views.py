from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib import messages
from django.core.exceptions import ValidationError
from profiles.utils import (
    get_profiles_for_user,
    create_profile,
    edit_profile,
    delete_profile,
    make_all_profiles_inactive,
    activate_profile_for_user,
    get_active_profile_for_user
)
from api.utils import search_jobs, add_job_search_entry, get_profile_history


def home_view(request):
    """
    Public home page view.
    """
    return render(request, 'home.html')


def register_view(request):
    """
    Handle user registration.
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    """
    Handle user login.
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    """
    Handle user logout.
    """
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')


@login_required
def dashboard_view(request):
    """
    Unified dashboard view that includes profile management, job searches,
    and job search history.

    :param request: The HTTP request object.
    :return: Rendered dashboard page.
    """
    profiles = get_profiles_for_user(request.user)
    active_profile = get_active_profile_for_user(request.user)
    profiles_count = len(profiles)
    profiles_history = get_profile_history(active_profile.id) if active_profile else None
    job_results = None

    if request.method == "POST":
        # Handle creating a profile
        if 'create_profile' in request.POST:
            handle_create_profile(request)

        # Handle activating a profile
        elif 'activate_profile' in request.POST:
            handle_activate_profile(request)

        # Handle editing a profile
        elif 'edit_profile' in request.POST:
            handle_edit_profile(request)

        # Handle deleting a profile
        elif 'delete_profile' in request.POST:
            handle_delete_profile(request)

        # Handle searching for jobs
        elif 'search_jobs' in request.POST:
            try:
                job_results = handle_search_jobs(request, active_profile)
            except Exception as e:
                messages.error(request, f"Error fetching jobs: {e}")
                print(e)

        # Reload the page unless it's a search
        if 'search_jobs' not in request.POST:
            return redirect("dashboard")

    return render(request, 'dashboard.html', {
        'profiles': profiles,
        'profiles_count': profiles_count,
        'active_profile': active_profile,
        'profiles_history': profiles_history,
        'job_results': job_results
    })


def handle_create_profile(request):
    """
    Process the creation of a new profile.
    """
    job_title = request.POST.get('job_title')
    min_salary = request.POST.get('min_salary')
    is_full_time = request.POST.get('is_full_time') == 'on'
    city = request.POST.get('city')

    try:
        create_profile(request.user, job_title, min_salary, is_full_time, city)
        messages.success(request, "Profile created successfully!")
    except ValidationError as e:
        messages.error(request, e.message)


def handle_activate_profile(request):
    """
    Process the activation of a user profile.
    """
    profile_id = request.POST.get('profile_id')
    try:
        make_all_profiles_inactive(request.user)
        activated_profile = activate_profile_for_user(request.user, profile_id)
        messages.success(request, f"Profile '{activated_profile.job_title}' is now active.")
    except Profile.DoesNotExist:
        messages.error(request, "The selected profile does not exist.")


def handle_edit_profile(request):
    """
    Process the editing of an existing profile.
    """
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


def handle_delete_profile(request):
    """
    Process the deletion of a user profile.
    """
    profile_id = request.POST.get('profile_id')
    delete_profile(profile_id, request.user)
    messages.success(request, "Profile deleted successfully!")


def handle_search_jobs(request, active_profile):
    """
    Process a job search for the currently active profile.

    :param request: The HTTP request object.
    :param active_profile: The currently active Profile instance.
    :return: JSON job results from the API.
    """
    if not active_profile:
        messages.error(request, "No active profile available for job search.")
        return None

    full_json_job_results = search_jobs(active_profile)
    job_results = full_json_job_results.get("results")
    for result in job_results:
        add_job_search_entry(
            active_profile.id,
            result.get("title"),
            result.get("redirect_url"),
            result.get("description"),
            result.get("company", {}).get("display_name"),
            result.get("location", {}).get("display_name"),
            result.get("salary_min"),
            result.get("salary_max")
        )
    return job_results
