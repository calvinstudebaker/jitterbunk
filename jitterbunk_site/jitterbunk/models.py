from django.db import models
from django.contrib.auth.models import User

class Bunk(models.Model):
    """Represents a Bunk event; one user Bunking another."""

    #attributes
    from_user = models.ForeignKey(User, related_name="from_bunk")
    to_user = models.ForeignKey(User, related_name="to_bunk")
    time = models.DateTimeField()

    def __unicode__(self):
        return '{} -> {}'.format(self.from_user, self.to_user)

class Profile(models.Model):
    """Represents a profile for a user."""
    user = models.ForeignKey(User)
    photo = models.ImageField(upload_to="profile_pics/")
    
    def __unicode__(self):
        return str(self.user)
