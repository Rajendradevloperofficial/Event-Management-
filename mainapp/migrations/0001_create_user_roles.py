from django.db import migrations


def create_user_roles(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')

    Group.objects.get_or_create(name='Admin')
    Group.objects.get_or_create(name='Analyst')


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.RunPython(create_user_roles),
    ]
