# Generated by Django 3.2.8 on 2021-10-09 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_employee_gender'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['-id'], 'verbose_name': 'Empleado', 'verbose_name_plural': 'Empleados'},
        ),
        migrations.AlterModelTable(
            name='employee',
            table='empleado',
        ),
    ]