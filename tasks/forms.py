from django.forms.models import ModelForm
from django import forms
from tasks.models import Task
from django.forms import extras
from django.utils.datetime_safe import datetime

class AddTaskForm(ModelForm):
    task = forms.CharField(label=(u'Task'))
    estimated = forms.DateField(widget=extras.SelectDateWidget(years=range(int(datetime.now().strftime('%Y')), int(datetime.now().strftime('%Y')) + 1)))

    def clean_task(self):
        task = self.cleaned_data['task']
        try:
            Task.objects.get(user=self.user)
        except:
            pass
