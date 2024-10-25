from django.db import models
from django.contrib.auth.models import User  # Reutilizando o modelo de User do Django

class ActivityType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="activities")
    activity_type = models.ForeignKey(ActivityType, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.activity_type.name} by {self.user.username}'

class ActivityMetrics(models.Model):
    activity = models.OneToOneField(Activity, on_delete=models.CASCADE, related_name="metrics")
    distance_km = models.FloatField()
    duration_minutes = models.FloatField()
    avg_speed_kmh = models.FloatField()
    calories_burned = models.FloatField()
    elevation_gain = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f'Metrics for {self.activity}'

class ActivityHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'History for {self.user.username}'