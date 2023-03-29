from django.db import migrations

class Migration(migrations.Migration):

   dependencies = [
    ('auth', '0012_alter_user_first_name_max_length'),
    ('user', '0006_alter_follower_options'), # Update this line to reference the correct parent migration
]

operations = [
        migrations.DeleteModel(
            name='Follower',
        ),
    ]