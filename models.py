# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Candidat(models.Model):
    nom = models.CharField(db_column='Nom', max_length=30)  # Field name made lowercase.
    prenom = models.CharField(db_column='Prenom', max_length=30)  # Field name made lowercase.
    e_mail = models.TextField(db_column='E-mail', unique=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_naissance = models.DateField(db_column='Date_naissance')  # Field name made lowercase.
    num_tel = models.IntegerField(unique=True)
    dispo = models.IntegerField()
    nb_ann_exp = models.IntegerField()
    msg = models.TextField()
    id_c = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'candidat'
