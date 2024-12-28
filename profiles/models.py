from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Validation function to enforce the 5-profile limit
def validate_profile_limit(user):
    if Profile.objects.filter(user=user).count() >= 5:
        raise ValidationError("You can only create up to 5 profiles.")

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profiles')  # Link to User
    job_title = models.CharField(max_length=100)  # Desired job title
    min_salary = models.PositiveIntegerField(null=True, blank=True)  # Minimum salary (optional)
    is_full_time = models.BooleanField(default=True)  # Full-time or part-time preference
    city = models.CharField(max_length=100)  # City preference
    active = models.BooleanField(default=True) # selected profile to be displayed/used

    def save(self, *args, **kwargs):
        """Enforce the 5-profile limit."""
        validate_profile_limit(self.user)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.job_title} in {self.city} (Full-Time: {self.is_full_time})"



class JobSearchHistory(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='history')  # Link to Profile
    job_title = models.CharField(max_length=255)  # Title of the job searched
    redirect_url = models.URLField()  # URL to the job posting
    description = models.TextField()  # Description of the job
    company_name = models.CharField(max_length=255, null=True, blank=True)  # Optional: Company name
    location = models.CharField(max_length=255, default="N/A")
    salary_min = models.PositiveIntegerField(null=True, blank=True)
    salary_max = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of when the job search occurred

    def __str__(self):
        return f"{self.job_title} for {self.profile.user.username} at {self.created_at}"

