from djongo import models


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    CategoryName = models.CharField(max_length=100)
    CategoryAnswer = models.CharField(max_length=500)

    def __str__(self):
        return str(self.CategoryName)


class Question(models.Model):
    CategoryID = models.ForeignKey(Category, on_delete=models.CASCADE, to_field='id', db_column='CategoryID',null=True)
    QuestionText = models.CharField(max_length=500)
    QuestionAnswer = models.CharField(max_length=600)