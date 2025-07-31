import json
from django import forms
from django.contrib import admin

from apps.logs.models import APILog

# Register your models here.
# --------------------------
class APILogForm(forms.ModelForm):
    log = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 20}))

    class Meta:
        model = APILog
        fields = '__all__'

    def get_initial_for_field(self, field, field_name):
        if field_name == 'log' and self.instance and self.instance.pk:
            return self.instance.to_json
        return super().get_initial_for_field(field, field_name)

    def clean_log(self):
        data = self.cleaned_data['log']
        try:
            return json.loads(data)
        except json.JSONDecodeError:
            raise forms.ValidationError('Formato JSON inválido.')


@admin.register(APILog)
class APILogAdmin(admin.ModelAdmin):
    form = APILogForm
    list_display = ('created_at', 'get_method', 'get_status')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)

    def get_method(self, obj):
        return obj.log.get('method', '-')
    get_method.short_description = 'Method'

    def get_status(self, obj):
        return obj.log.get('status', '-')
    get_status.short_description = 'Status'
