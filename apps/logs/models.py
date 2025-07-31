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
        log = self.log
        if(type(self.log) == str):
            log = json.loads(self.log)

        return f"[{self.created_at.strftime('%Y-%m-%d %H:%M:%S')}] {log.get('method')} {log.get('status')}"

    @property
    def to_json(self):
        return json.dumps(self.log, ensure_ascii=False, indent=4)
    
    @property
    def method(self):
        log = self.log
        if(type(self.log) == str):
            log = json.loads(self.log)
        
        return log.get('method', '-')
    
    @property
    def status(self):
        log = self.log
        if(type(self.log) == str):
            log = json.loads(self.log)
        
        return log.get('status', '-')
