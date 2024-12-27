from .models import Profile
from django.core.exceptions import ValidationError

def get_profiles_for_user(user):
    """Retrieve all profiles for a given user."""

    profiles = Profile.objects.filter(user=user) 
    check_profiles_inactive(profiles)
    return profiles

def create_profile(user, job_title, min_salary, is_full_time, city):
    """Create a new profile for a user."""
    if Profile.objects.filter(user=user).count() >= 5:
        raise ValidationError("You can only create up to 5 profiles.")
    make_all_profiles_inactive(user)   # only new profile is active/selected
    return Profile.objects.create(
        user=user,
        job_title=job_title,
        min_salary=min_salary,
        is_full_time=is_full_time,
        city=city,
        active=True
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


def make_all_profiles_inactive(user):
    """ Makes all profiles for given user active field to false"""
    profiles = Profile.objects.filter(user=user).update(active=False) # makes all profiles inactive


def activate_profile_for_user(user, profile_id):
    """
    Activates the specified profile for the given user.
    
    :param user: The user who owns the profiles.
    :param profile_id: The ID of the profile to activate.
    :raises Profile.DoesNotExist: If the profile ID is invalid or does not belong to the user.
    """

    # Activate the selected profile
    try:
        profile = Profile.objects.get(id=profile_id, user=user)
        profile.active = True
        profile.save()
        return profile  # Return the activated profile
    except ObjectDoesNotExist:
        raise Profile.DoesNotExist("The selected profile does not exist.")



def check_profiles_inactive(profiles):
    
    # Check if any profile is active
    if not profiles.filter(active=True).exists():
        # If no profiles are active, make the first profile active
        first_profile = profiles.first()  # Get the first profile in the queryset
        if first_profile:
            first_profile.active = True
            first_profile.save()


