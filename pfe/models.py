from django.db import models

# Create your models here.

class Candidat(models.Model):
    id_c = models.AutoField(db_column='id_C', primary_key=True)  # Field name made lowercase.      
    nom = models.CharField(db_column='Nom', max_length=30)  # Field name made lowercase.
    prenom = models.CharField(db_column='Prenom', max_length=30)  # Field name made lowercase.     
    e_mail = models.CharField(max_length=200, unique=True)
    date_naissance = models.DateField(db_column='Date_naissance')  # Field name made lowercase.    
    num_tel = models.CharField(db_column='num_tel', unique=True, max_length=8)
    dispo = models.IntegerField(db_column='dispo')
    nb_ann_exp = models.IntegerField(db_column='nb_ann_exp')
    msg = models.CharField(max_length=255,db_column='msg')
    

    class Meta:
        db_table = 'candidat'



 
