from .models import Profile
from django.core.exceptions import ValidationError

def get_profiles_for_user(user):
    """Retrieve all profiles for a given user."""
    return Profile.objects.filter(user=user)

def create_profile(user, job_title, min_salary, is_full_time, city):
    """Create a new profile for a user."""
    if Profile.objects.filter(user=user).count() >= 5:
        raise ValidationError("You can only create up to 5 profiles.")
    return Profile.objects.create(
        user=user,
        job_title=job_title,
        min_salary=min_salary,
        is_full_time=is_full_time,
        city=city,
    )

def edit_profile(profile_id, user, job_title, min_salary, is_full_time, city):
    """Edit an existing profile."""
    profile = Profile.objects.get(id=profile_id, user=user)
    profile.job_title = job_title
    profile.min_salary = min_salary
    profile.is_full_time = is_full_time
    profile.city = city
    profile.save()
    return profile

def delete_profile(profile_id, user):
    """Delete a profile for a user."""
    profile = Profile.objects.get(id=profile_id, user=user)
    profile.delete()
