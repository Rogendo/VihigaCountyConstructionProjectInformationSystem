# Generated by Django 4.1.1 on 2023-06-20 13:15

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_minister', models.BooleanField(default=False)),
                ('is_accountant', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('ID_no', models.CharField(max_length=12)),
                ('main_contractor', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Procurement_Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Accountant',
            fields=[
                ('email', models.EmailField(max_length=254, verbose_name=users.models.User)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='accountant', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('ID_no', models.IntegerField()),
                ('staff_no', models.IntegerField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Minister',
            fields=[
                ('email', models.EmailField(max_length=254, verbose_name=users.models.User)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='minister', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('ID_no', models.IntegerField()),
                ('ministry', models.CharField(max_length=15)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('project_location', models.CharField(max_length=100)),
                ('sqm_rate_or_lm', models.CharField(max_length=50)),
                ('commencement_date', models.DateTimeField()),
                ('tender_no', models.CharField(max_length=20, unique=True)),
                ('site_location', models.CharField(max_length=80)),
                ('floor_area', models.CharField(max_length=20)),
                ('contract_sum', models.CharField(max_length=20)),
                ('payments_made', models.CharField(max_length=20)),
                ('payment_status', models.BooleanField(choices=[(0, 'Paid'), (1, 'Pending')], default=1)),
                ('work_status', models.BooleanField(choices=[(0, 'started'), (1, 'completed')], default=0)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('date', models.DateField()),
                ('contract_period_months', models.PositiveIntegerField()),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contracting_company', to='users.contractor')),
                ('procurrement_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='procurement', to='users.procurement_department')),
            ],
            options={
                'ordering': ['-updated_on'],
            },
        ),
        migrations.CreateModel(
            name='Checklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checklist_name', models.CharField(max_length=80)),
                ('checklist_document', models.FileField(upload_to='Checklist_Documents/')),
                ('contract_period_months', models.PositiveIntegerField()),
                ('date', models.DateField()),
                ('main_contractor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contractor', to='users.contractor')),
                ('procurrement_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='procuring_dpt', to='users.procurement_department')),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='users.project')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
