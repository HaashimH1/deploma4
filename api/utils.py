import os
import requests
from profiles.models import Profile, JobSearchHistory
from django.core.exceptions import ValidationError

ADZUNA_API_KEY = os.getenv('ADZUNA_API_KEY')
ADZUNA_APP_ID = os.getenv('ADZUNA_APP_ID')

results_per_request = 5


# Adding a job search entry
def add_job_search_entry(profile_id, job_title, redirect_url, description, company_name, location, salary_min, salary_max):

    # Check if the job search already exists
    if job_search_exists(profile_id, description):
        return None  # Return None if a duplicate exists

    profile = Profile.objects.get(id=profile_id)  # Fetch the Profile object
    return JobSearchHistory.objects.create(
        profile=profile,
        job_title=job_title,
        redirect_url=redirect_url,
        description=description,
        company_name=company_name,
        location= location,
        salary_min=salary_min,
        salary_max=salary_max
    )

def job_search_exists(profile_id, description):
    """
    Check if a job search with the same description already exists for the given profile.
    
    :param profile_id: ID of the Profile
    :param description: Description of the job search
    :return: True if a search with the same description exists, False otherwise
    """
    return JobSearchHistory.objects.filter(profile_id=profile_id, description=description).exists()


def get_profile_history(profile_id):
    profile = Profile.objects.get(id=profile_id)
    return profile.history.all().order_by("-id")  # Fetch all history entries for the profile, reverse to get histroy new to old






def search_jobs(profile):
    """
    Search for jobs using the Adzuna API based on a Profile's attributes.

    :param country: Country code (e.g., 'gb' for Great Britain)
    :param profile: A Profile instance with fields like job_title, city, min_salary, and is_full_time.
    :param results_per_page: Optional: Number of results per page (default is 10)
    :return: JSON response from the API containing job listings
    """
    if not ADZUNA_API_KEY or not ADZUNA_APP_ID:
        raise ValueError("API key or App ID is missing. Please set them in env.py.")

    url = f"https://api.adzuna.com/v1/api/jobs/gb/search/1?app_id={ADZUNA_APP_ID}&app_key={ADZUNA_API_KEY}"

    url += f"&results_per_page={results_per_request}"
    url += f"&what={profile.job_title.replace(' ','%20')}"
    url += f"&where={profile.city}"
    url += f"&salary_min={profile.min_salary}"

    if profile.is_full_time:
        url += f"&full_time=1"
    else:
        url += f"&part_time=1"
    
    url += "&content-type=application/json"

    # Make the request
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad HTTP responses

    # Return the JSON response
    return response.json()
