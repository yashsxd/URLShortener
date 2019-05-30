from django.db import models

class Urls(models.Model):
    # Primary Key, Auto Incrementing
    short_id = models.BigAutoField(max_length = 5, primary_key = True)

    # Original URL, Limit = 200
    long_url = models.URLField(max_length = 200)

    # Date and Time of URL creation
    pub_date = models.DateTimeField(auto_now = True)

    # Count of times redirected
    count = models.IntegerField(default = 0)

def __str__(self):
    return self.url