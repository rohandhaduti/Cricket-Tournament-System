from django.db import models

# Create your models here.
class userlogin(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=50)
    utype = models.CharField(max_length=50)

class newuser(models.Model):
    username = models.CharField(max_length=20)
    emailid= models.CharField(max_length=30, )
    mobileno = models.CharField(max_length=30)
    city= models.CharField(max_length=35)

class forget(models.Model):
    username= models.CharField(max_length=30)


class organizer(models.Model):
    match_details = models.CharField(max_length=20)
    suspect_details = models.CharField(max_length=200)
    add_players = models.CharField(max_length=200)
    team_details = models.CharField(max_length=200)


class match_details(models.Model):
    match_no = models.CharField(max_length=20)
    ipl_no = models.CharField(max_length=50)
    date = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)
    team1 = models.CharField(max_length=200)
    team2 = models.CharField(max_length=200)
    start_time = models.CharField(max_length=200)


from django.db import models


class PlayerDetails(models.Model):
    player_id = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    age = models.IntegerField()
    player_type = models.CharField(max_length=200)   # renamed from 'type' (best practice)
    photo = models.ImageField(upload_to='player_photos/', null=True, blank=True)
    debut = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class awards(models.Model):
    player_id = models.CharField(max_length=20)
    award_name = models.CharField(max_length=50)
    date = models.CharField(max_length=200)



class user_details(models.Model):
    user_id = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    email_id = models.CharField(max_length=200)
    adhaar_no = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=200)


class player_statics(models.Model):
    player_id = models.CharField(max_length=20)
    match_id = models.CharField(max_length=50)
    total_score = models.CharField(max_length=200)
    no_of_catches = models.CharField(max_length=200)
    no_of_wickets = models.CharField(max_length=200)
    awards = models.CharField(max_length=200)


class match_statics(models.Model):
    match_id = models.CharField(max_length=20)
    team1 = models.CharField(max_length=50)
    team2 = models.CharField(max_length=200)
    team1_score = models.CharField(max_length=200)
    team2_score = models.CharField(max_length=200)
    captain_team1 = models.CharField(max_length=200)
    captain_team2 = models.CharField(max_length=200)
    result = models.CharField(max_length=200)
    match_type = models.CharField(max_length=200)
    no_of_overs = models.CharField(max_length=200)

