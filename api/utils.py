import os
import requests
from django.core.exceptions import ValidationError

# Retrieve Adzuna API credentials from the environment
ADZUNA_API_KEY = os.getenv('ADZUNA_API_KEY')
ADZUNA_APP_ID = os.getenv('ADZUNA_APP_ID')

# Define the number of results to retrieve per request
RESULTS_PER_REQUEST = 5

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
