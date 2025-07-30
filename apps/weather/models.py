from django.db import models

# Create your models here.
# ------------------------
class WeatherEntry(models.Model):
    # Search informations
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    # Response data
    response_data = models.JSONField()
    
    # Timestamp
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.created_at.strftime('%Y-%m-%d %H:%M:%S')}] {self.city}, {self.state} - {self.country}"

    class Meta:
        verbose_name = "Weather Entry"
        verbose_name_plural = "Weather Entries"
