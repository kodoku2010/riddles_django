from django.db import models


class Riddle(models.Model):
    rid_title = models.CharField(max_length=100)
    rid_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return str(self.rid_title)


class Option(models.Model):
    riddle = models.ForeignKey(Riddle, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return str(self.text)

