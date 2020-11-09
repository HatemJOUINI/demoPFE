from django import forms
from pfe.models import Candidat
class FormCan(forms.ModelForm):
    nom = forms.CharField( max_length=30)  # Field name made lowercase.
    prenom = forms.CharField( max_length=30)  # Field name made lowercase.     
    e_mail = forms.CharField(max_length=200)
    date_naissance = forms.DateField()  # Field name made lowercase.    
    num_tel = forms.CharField( max_length=8)
    dispo = forms.IntegerField( max_value=6, min_value=0)
    nb_ann_exp = forms.IntegerField( min_value=0)
    msg = forms.CharField(max_length=255)
    class Meta:  
        model = Candidat
        fields = "__all__" 
