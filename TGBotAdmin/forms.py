from django import forms
from .models import Question, Category

class QuestionForm(forms.ModelForm):
    CategoryID = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    QuestionText = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    QuestionAnswer = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Question
        fields = ('CategoryID', 'QuestionText', 'QuestionAnswer',)
        exclude = ('id',)