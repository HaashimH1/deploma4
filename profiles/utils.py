from django.core.exceptions import ValidationError, ObjectDoesNotExist
from .models import Profile, JobSearchHistory


def get_profiles_for_user(user):
    """
    Retrieve all profiles for a given user and ensure at least one profile is active.

    :param user: The user whose profiles are to be retrieved.
    :return: Queryset of Profile objects belonging to the user.
    """
    profiles = Profile.objects.filter(user=user)
    check_profiles_inactive(profiles)  # Ensure one profile is active
    return profiles


def get_active_profile_for_user(user):
    """
    Retrieve the active profile for a given user.

    :param user: The user whose active profile is to be retrieved.
    :return: The active Profile object, or None if no active profile exists.
    """
    try:
        return Profile.objects.get(user=user, active=True)
    except Profile.DoesNotExist:
        return None


def create_profile(user, job_title, min_salary, is_full_time, city):
    """
    Create a new profile for the user. Sets the new profile as active.

    :param user: The user for whom the profile is to be created.
    :param job_title: Desired job title for the profile.
    :param min_salary: Minimum salary preference for the profile.
    :param is_full_time: Boolean indicating full-time job preference.
    :param city: City preference for the profile.
    :raises ValidationError: If the user already has 5 profiles.
    :return: The created Profile object.
    """
    if Profile.objects.filter(user=user).count() >= 5:
        raise ValidationError("You can only create up to 5 profiles.")

    make_all_profiles_inactive(user)  # Set all other profiles as inactive
    return Profile.objects.create(
        user=user,
        job_title=job_title,
        min_salary=min_salary,
        is_full_time=is_full_time,
        city=city,
        active=True,
    )


def edit_profile(profile_id, user, job_title, min_salary, is_full_time, city):
    """
    Edit an existing profile for a user.

    :param profile_id: The ID of the profile to edit.
    :param user: The user who owns the profile.
    :param job_title: Updated job title.
    :param min_salary: Updated minimum salary preference.
    :param is_full_time: Updated boolean indicating full-time job preference.
    :param city: Updated city preference.
    :return: The updated Profile object.
    """
    profile = Profile.objects.get(id=profile_id, user=user)
    profile.job_title = job_title
    profile.min_salary = min_salary
    profile.is_full_time = is_full_time
    profile.city = city
    profile.save()
    return profile


def delete_profile(profile_id, user):
    """
    Delete a profile for a user.

    :param profile_id: The ID of the profile to delete.
    :param user: The user who owns the profile.
    """
    profile = Profile.objects.get(id=profile_id, user=user)
    profile.delete()


def make_all_profiles_inactive(user):
    """
    Set the 'active' field to False for all profiles belonging to a user.

    :param user: The user whose profiles are to be updated.
    """
    Profile.objects.filter(user=user).update(active=False)


def activate_profile_for_user(user, profile_id):
    """
    Activate a specific profile for a user and deactivate all others.

    :param user: The user who owns the profiles.
    :param profile_id: The ID of the profile to activate.
    :raises Profile.DoesNotExist: If the profile does not exist or does not belong to the user.
    :return: The activated Profile object.
    """
    make_all_profiles_inactive(user)  # Deactivate all other profiles

    profile = Profile.objects.get(id=profile_id, user=user)  # Activate the selected profile
    profile.active = True
    profile.save()
    return profile


def check_profiles_inactive(profiles):
    """
    Ensure there is at least one active profile in the given queryset.

    :param profiles: Queryset of Profile objects.
    """
    if not profiles.filter(active=True).exists():
        first_profile = profiles.first()  # Get the first profile in the queryset
        if first_profile:
            first_profile.active = True
            first_profile.save()

def add_job_search_entry(profile_id, job_title, redirect_url, description, company_name, location, salary_min, salary_max):
    """
    Add a job search entry to the database if it doesn't already exist.

    :param profile_id: ID of the Profile
    :param job_title: Title of the job
    :param redirect_url: URL of the job posting
    :param description: Description of the job
    :param company_name: Name of the company offering the job
    :param location: Location of the job
    :param salary_min: Minimum salary for the job
    :param salary_max: Maximum salary for the job
    :return: JobSearchHistory object if created, None if a duplicate exists
    """
    if job_search_exists(profile_id, description, job_title):
        return None  # Avoid duplicate entries

    profile = Profile.objects.get(id=profile_id)  # Fetch the Profile object
    return JobSearchHistory.objects.create(
        profile=profile,
        job_title=job_title,
        redirect_url=redirect_url,
        description=description,
        company_name=company_name,
        location=location,
        salary_min=salary_min,
        salary_max=salary_max,
    )


def job_search_exists(profile_id, description, job_title):
    """
    Check if a job search entry with the same description exists for the given profile.

    :param profile_id: ID of the Profile
    :param description: Description of the job search
    :return: True if a search with the same description exists, False otherwise
    """
    return JobSearchHistory.objects.filter(profile_id=profile_id, description=description, job_title=job_title ).exists()


def get_profile_history(profile_id):
    """
    Retrieve the job search history for a specific profile.

    :param profile_id: ID of the Profile
    :return: Queryset of JobSearchHistory entries, ordered from newest to oldest
    """
    profile = Profile.objects.get(id=profile_id)
    return profile.history.all().order_by("-id")

