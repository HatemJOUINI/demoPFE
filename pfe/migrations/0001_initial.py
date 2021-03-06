# Generated by Django 3.0.8 on 2020-11-08 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
            ],
            options={
                'db_table': 'admin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('eid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
        migrations.CreateModel(
            name='Etat_mail',
            fields=[
                ('id_E', models.AutoField(db_column='id_E', primary_key=True, serialize=False)),
                ('etat', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'etat_mail',
            },
        ),
        migrations.CreateModel(
            name='EtatC',
            fields=[
                ('id_EC', models.AutoField(db_column='id_C', primary_key=True, serialize=False)),
                ('etatC', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'etatc',
            },
        ),
        migrations.CreateModel(
            name='Candidat',
            fields=[
                ('id_c', models.AutoField(db_column='id_C', primary_key=True, serialize=False)),
                ('nom', models.CharField(db_column='Nom', max_length=30)),
                ('prenom', models.CharField(db_column='Prenom', max_length=30)),
                ('e_mail', models.CharField(max_length=200, unique=True)),
                ('date_naissance', models.DateField(db_column='Date_naissance')),
                ('num_tel', models.CharField(db_column='num_tel', max_length=8, unique=True)),
                ('dispo', models.IntegerField(db_column='dispo')),
                ('nb_ann_exp', models.IntegerField(db_column='nb_ann_exp')),
                ('msg', models.CharField(db_column='msg', max_length=255)),
                ('etatC', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pfe.EtatC')),
                ('etat_mail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pfe.Etat_mail')),
            ],
            options={
                'db_table': 'candidat',
            },
        ),
    ]
