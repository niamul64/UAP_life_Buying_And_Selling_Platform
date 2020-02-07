from django import forms
from .models import Question


class CreateQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject','department','question_type','exam_date','semester','session','image1','image2','image3','image4','image5']