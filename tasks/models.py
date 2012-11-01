from django.db import models
from django.contrib.auth.models import User
from django.utils.datetime_safe import datetime
import datetime as dt
from django.utils import timezone

class Project(models.Model):
    title = models.CharField(max_length=64)
    owner = models.ForeignKey(User)
    decription = models.TextField(null=True)
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()
    estimated = models.DateTimeField(null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    completed = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return self.title

    def was_published_recently(self):
        """
        @return: if object was created within a day
        """
        return self.created >= timezone.now() - dt.timedelta(days=1)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = datetime.today()
        self.modified = datetime.today()
        super(Project, self).save(*args, **kwargs)

class Task(models.Model):
    doer = models.ForeignKey(User)
    project = models.ForeignKey(Project, null=True, blank=True)
    task = models.CharField(max_length=144)
    notes = models.TextField(null=True, blank=True)
    private = models.BooleanField(default=True)
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()
    estimated = models.DateField(null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)
    completed = models.DateTimeField(null=True, blank=True)
    priority = models.IntegerField(blank=True, null=True)
    percent_complete = models.IntegerField(default=0, blank=False, null=False)
    previous_percent_complete = models.IntegerField(default=0, blank=False, null=False, editable=False)
    percent_update_time = models.DateTimeField(null=True, blank=True, editable=False)

    def __unicode__(self):
        return self.task

    def was_published_recently(self):
        """
        @return: if object was created within a day
        """
        return self.created >= timezone.now() - dt.timedelta(days=1)

    def percent_updated(self):
        """ return the percent difference in from the percent_complete and previous """
        return self.percent_complete - self.previous_percent_complete

    def percent_left(self):
        """ retun the numarical value of percentage left for task """
        return 100 - self.percent_complete

    def percent_update_date(self):
        """ only return month and day for hover stuff """
        d = self.percent_update_time.day
        return self.percent_update_time.strftime("%A %d{S}").replace('{S}', str(d) + 'th' if 11 <= d <= 13 else {1:'st', 2:'nd', 3:'rd'}.get(d % 10, 'th'))


    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = datetime.today()
            self.percent_update_time = datetime.today()
        else:
            old_task = Task.objects.get(id=self.id)
            if self.percent_complete != old_task.percent_complete:
                self.previous_percent_complete = old_task.percent_complete
            else:
                self.percent_update_time = datetime.today()
        self.modified = datetime.today()

        super(Task, self).save(*args, **kwargs)
