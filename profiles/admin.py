from django.contrib import admin
from .models import Profile, JobSearchHistory

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'job_title', 'city', 'active')  # Display these fields in the admin list
    search_fields = ('user__username', 'job_title', 'city')  # Allow search by user, job title, or city
    list_filter = ('active', 'city', 'is_full_time')  # Add filters for easy navigation

    def get_queryset(self, request):
        """
        Customize queryset to prefetch related history for performance optimization.
        """
        queryset = super().get_queryset(request)
        return queryset.prefetch_related('history')  # Prefetch history to reduce queries


@admin.register(JobSearchHistory)
class JobSearchHistoryAdmin(admin.ModelAdmin):
    list_display = ('profile', 'job_title', 'company_name', 'created_at')  # Show these fields in the history admin
    search_fields = ('job_title', 'profile__user__username', 'company_name')  # Search by job title, profile's user, or company
    list_filter = ('created_at', 'company_name')  # Filters for date and company name
    ordering = ('-created_at',)  # Order by most recent first
