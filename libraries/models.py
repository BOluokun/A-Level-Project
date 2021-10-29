from django.db import models
from accounts.models import User
from django.utils import timezone

# Create your models here.

#Score model that creates the public library table in the database. Contains all scores.
#Has scoreID (primary key), title, author, date_created, last_modified, score_file,
#composition_file, music_file, pdf_file, user (foreign key) and
#public attributes
#Scores specific to users can be filtered with the user attribute
class Score(models.Model):
    scoreID = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)
    date_created = models.DateTimeField(default = timezone.now)
    last_modified = models.DateTimeField(auto_now = True)
    score_file = models.FileField(upload_to = "", max_length = 1000000)
    composition_file = models.FileField(upload_to = "", max_length =1000000, default = "None")
    music_file = models.FileField(upload_to = "", max_length = 10000000, default = "None")
    pdf_file = models.FileField(upload_to = "", max_length = 100000000, default = "None")
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    public = models.BooleanField(default = False)
    def __str__(self):
        return str(self.title) + ' - ' + str(self.author)
