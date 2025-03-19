from django import forms # type: ignore
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["text"]
        labels = {"text": ""}


