import os
import requests

ADZUNA_API_KEY = os.getenv('ADZUNA_API_KEY')
ADZUNA_APP_ID = os.getenv('ADZUNA_APP_ID')




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

    url += f"&results_per_page=1"
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
