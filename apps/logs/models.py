from django.db import models

# Create your models here.
# ------------------------
class StructuredLogs(models.Model):
    request_data = models.JSONField(null=True, blank=True)
    response_data = models.JSONField()
    url = models.URLField()
    status_code = models.IntegerField()
    
    request_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Log"
        verbose_name_plural = "Logs"
    
    def __str__(self):
        return f"[{self.request_date.strftime('%Y-%m-%d %H:%M:%S')}] {self.url} - {self.status_code}"
