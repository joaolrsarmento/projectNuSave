# Generated by Django 3.0.4 on 2020-03-12 02:12

from django.db import migrations
from data import data_API
import json

def create_data(apps, schema_editor):
    User = apps.get_model('users', 'StatisticsNuUser')
    db_alias = schema_editor.connection.alias

    filter_list = ['Alimentacao', 'Assinatura_e_servico', 'Educacao',
                   'Beleza', 'Saude', 'Transporte', 'Outros', 'Saques']

    data = data_API.DataAPI()
    for i in range(10000):
        print(i)
        user_data = {}
        for fil in filter_list:
            user_data[fil] = data.readInstructions(json.dumps({
                    "ID": i+1,
                    "feature": 'statistics',
                    "filter": fil
                }))
        user = User(user_filters = user_data)
        user.save()

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_statisticsnuuser'),
    ]

    operations = [
        migrations.RunPython(create_data)
    ]
