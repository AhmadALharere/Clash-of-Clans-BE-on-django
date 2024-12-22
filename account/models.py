from django.db import models
import socialregistration 

# Create your models here.
def uploadfile(instance,filename):
    
    return "data/%s/%s"%(instance.id,filename)

StarReward = (
    ("no_stars","no_stars"),
    ("one_star","one_star"),
    ("tow_stars","tow_stars"),
    ("complete","complete")
) 
              
              
              



class profile(models.Model):
    
    name = models.CharField(default='',max_length=40)
    Lvl = models.IntegerField(default=1)
    links = models.OneToOneField("LinkWay", on_delete=models.CASCADE)
    village = models.FileField( upload_to=uploadfile, max_length=100000)
    dark_village = models.FileField( upload_to=uploadfile, max_length=100000,blank=True,null=True)
    #Resorses = models.OneToOneField("Resorses.Model", verbose_name=_(""), on_delete=models.CASCADE)    
    #AttackArch = models.OneToOneField("AttackArchive.Model", verbose_name=_(""), on_delete=models.CASCADE)
    #Clan = models.ForeignKey("Clan.Model", verbose_name=_(""), on_delete=models.CASCADE)
    SeassonProgress = models.FileField( upload_to=uploadfile, max_length=100000,blank=True,null=True)
    eventProgress = models.FileField( upload_to=uploadfile, max_length=100000,blank=True,null=True)
    starRewards = models.CharField(choices=StarReward, max_length=50,default="no_stars")
    league_cup = models.IntegerField(default=0)
    last_login = models.DateTimeField( auto_now=True)
    join_at = models.DateTimeField( auto_now=True)
    #reagon = 
    achivement = models.FileField( upload_to=uploadfile, max_length=100)
    #Statues = models.OneToOneField("statues.Model", verbose_name=_(""), on_delete=models.CASCADE)
    

class LinkWay(models.Model):
    
   google = models.CharField(default='' ,max_length=100)
   Facebook = models.CharField(default='' ,max_length=100)
   Supercell = models.CharField(default='' ,max_length=100)