import os
import requests
from profiles.models import Profile, JobSearchHistory
from django.core.exceptions import ValidationError

# Retrieve Adzuna API credentials from the environment
ADZUNA_API_KEY = os.getenv('ADZUNA_API_KEY')
ADZUNA_APP_ID = os.getenv('ADZUNA_APP_ID')

# Define the number of results to retrieve per request
RESULTS_PER_REQUEST = 5


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
    if job_search_exists(profile_id, description):
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


def job_search_exists(profile_id, description):
    """
    Check if a job search entry with the same description exists for the given profile.

    :param profile_id: ID of the Profile
    :param description: Description of the job search
    :return: True if a search with the same description exists, False otherwise
    """
    return JobSearchHistory.objects.filter(profile_id=profile_id, description=description).exists()


def get_profile_history(profile_id):
    """
    Retrieve the job search history for a specific profile.

    :param profile_id: ID of the Profile
    :return: Queryset of JobSearchHistory entries, ordered from newest to oldest
    """
    profile = Profile.objects.get(id=profile_id)
    return profile.history.all().order_by("-id")


def search_jobs(profile):
    """
    Search for jobs using the Adzuna API based on a Profile's attributes.

    :param profile: A Profile instance with fields like job_title, city, min_salary, and is_full_time
    :return: JSON response from the Adzuna API containing job listings
    :raises ValueError: If API credentials are missing
    :raises HTTPError: If the API request fails
    """
    if not ADZUNA_API_KEY or not ADZUNA_APP_ID:
        raise ValueError("API key or App ID is missing. Please set them in env.py.")

    # Construct the request URL
    url = (
        f"https://api.adzuna.com/v1/api/jobs/gb/search/1?"
        f"app_id={ADZUNA_APP_ID}&app_key={ADZUNA_API_KEY}"
        f"&results_per_page={RESULTS_PER_REQUEST}"
        f"&what={profile.job_title.replace(' ', '%20')}"
        f"&where={profile.city}"
        f"&salary_min={profile.min_salary}"
    )

    # Add full-time or part-time preference
    if profile.is_full_time:
        url += "&full_time=1"
    else:
        url += "&part_time=1"

    url += "&content-type=application/json"

    # Make the API request
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad HTTP responses

    return response.json()
