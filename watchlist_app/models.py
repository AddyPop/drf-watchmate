from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import emoji
# Create your models here.
class streamplatform(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name

class watchlist(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    platform = models.ForeignKey(streamplatform, on_delete=models.CASCADE, related_name='watchlist')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class review(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    watchlist = models.ForeignKey(watchlist, on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        if self.rating == 1:
            return emoji.emojize(":star:")+ '-' +self.watchlist.title
        if self.rating == 2:
            return emoji.emojize(":star:")*2+" - "+self.watchlist.title
        if self.rating == 3:
            return emoji.emojize(":star:")*3+" - "+self.watchlist.title
        if self.rating == 4:
            return emoji.emojize(":star:")*4+" - "+self.watchlist.title
        if self.rating == 5:
            return emoji.emojize(":star:")*5+" - "+self.watchlist.title

        #return str(self.rating)+" - "+self.watchlist.title
