from djongo import models
from django.contrib import admin
from .models import Question,Category
from .forms import QuestionForm


# регистрируем модель Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'CategoryName', 'CategoryAnswer')

# регистрируем модель Question

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'CategoryID','QuestionText', 'QuestionAnswer')
    list_filter = ('CategoryID',)
    search_fields = ('QuestionText','QuestionAnswer')
    form = QuestionForm

admin.site.register(Question, QuestionAdmin)
