import json

from django.utils.timezone import is_aware
from uuid import UUID
from datetime import datetime
from django.db import models

# Create your models here.
# ------------------------
class APILog(models.Model):
    log = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "API Log"
        verbose_name_plural = "API Logs"
    
    def __str__(self):
        return f"[{self.created_at.strftime('%Y-%m-%d %H:%M:%S')}] {self.log.get('method')} {self.log.get('status')}"

    @property
    def to_json(self):
        return json.dumps(self.log, ensure_ascii=False)