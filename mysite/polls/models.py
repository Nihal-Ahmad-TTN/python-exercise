from django.db import models
from django.utils import timezone
import datetime
from django.contrib import admin
from django import forms

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    class Meta:
        permissions = [('view_result', 'view poll results')]

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']
        widgets = {
            'choice_text': forms.RadioSelect
        }

class UploadExcel(models.Model):
    file = models.FileField(upload_to="files/")
    uploaded_at = models.DateTimeField(auto_now_add=True)