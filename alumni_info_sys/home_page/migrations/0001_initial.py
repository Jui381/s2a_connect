# Generated by Django 4.0.2 on 2022-04-06 19:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_first_name', models.CharField(max_length=20)),
                ('admin_last_name', models.CharField(max_length=20)),
                ('admin_email', models.EmailField(max_length=50, primary_key=True, serialize=False)),
                ('admin_number', models.CharField(max_length=15)),
                ('admin_password', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'Admin',
            },
        ),
        migrations.CreateModel(
            name='Reg_alumni',
            fields=[
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('collage_id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=10)),
                ('sem', models.CharField(default=False, max_length=6)),
            ],
            options={
                'db_table': 'Reg_alumni',
            },
        ),
        migrations.CreateModel(
            name='Reg_student',
            fields=[
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('collage_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'Reg_student',
            },
        ),
        migrations.CreateModel(
            name='Residencial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('res_country', models.CharField(max_length=50)),
                ('res_state', models.CharField(max_length=50)),
                ('res_city', models.CharField(max_length=50)),
                ('res_address', models.TextField()),
                ('res_rent', models.CharField(max_length=50)),
                ('res_utility_exp', models.CharField(max_length=50)),
                ('res_monthly_exp', models.CharField(max_length=50)),
                ('useful_things', models.TextField()),
                ('collage_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='home_page.reg_alumni')),
            ],
            options={
                'db_table': 'Residencial',
            },
        ),
        migrations.CreateModel(
            name='Resetpass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forget_password_token', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Resetpass',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('passout_year', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=6)),
                ('permanent_address', models.TextField()),
                ('home_town', models.CharField(max_length=100)),
                ('collage_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='home_page.reg_alumni')),
            ],
            options={
                'db_table': 'Profile',
            },
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_name', models.CharField(max_length=50)),
                ('site_name', models.CharField(max_length=100)),
                ('airport_exp', models.CharField(max_length=30)),
                ('from_where', models.CharField(max_length=30)),
                ('to_where', models.CharField(max_length=30)),
                ('leave_over_place', models.CharField(max_length=30)),
                ('leave_over_time', models.CharField(max_length=30)),
                ('collage_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='home_page.reg_alumni')),
            ],
            options={
                'db_table': 'Flight',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gre', models.CharField(max_length=10)),
                ('toefl', models.CharField(max_length=10)),
                ('ielts', models.CharField(max_length=10)),
                ('cpi6', models.CharField(max_length=10)),
                ('cpi7', models.CharField(max_length=10)),
                ('backlog6', models.CharField(max_length=10)),
                ('backlog7', models.CharField(max_length=10)),
                ('collage', models.CharField(max_length=50)),
                ('collage_country', models.CharField(max_length=20)),
                ('collage_city', models.CharField(max_length=20)),
                ('collage_branch', models.CharField(max_length=50)),
                ('collage_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='home_page.reg_alumni')),
            ],
            options={
                'db_table': 'Education',
            },
        ),
        migrations.CreateModel(
            name='Consultancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=50)),
                ('service_city', models.CharField(max_length=20)),
                ('service_address', models.TextField()),
                ('service_number', models.CharField(max_length=15)),
                ('service_fees', models.CharField(max_length=10)),
                ('consulting_countries', models.TextField()),
                ('collage_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='home_page.reg_alumni')),
            ],
            options={
                'db_table': 'Consultancy',
            },
        ),
        migrations.CreateModel(
            name='Coaching',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name_gre', models.CharField(max_length=50)),
                ('center_name_gre', models.CharField(max_length=50)),
                ('center_city_gre', models.CharField(max_length=50)),
                ('coaching_fees_gre', models.CharField(max_length=10)),
                ('feedback_gre', models.TextField()),
                ('course_name_toefl', models.CharField(max_length=50)),
                ('center_name_toefl', models.CharField(max_length=50)),
                ('center_city_toefl', models.CharField(max_length=50)),
                ('coaching_fees_toefl', models.CharField(max_length=10)),
                ('feedback_toefl', models.TextField()),
                ('course_name_ielts', models.CharField(max_length=50)),
                ('center_name_ielts', models.CharField(max_length=50)),
                ('center_city_ielts', models.CharField(max_length=50)),
                ('coaching_fees_ielts', models.CharField(max_length=10)),
                ('feedback_ielts', models.TextField()),
                ('course_name_other', models.CharField(max_length=50)),
                ('center_name_other', models.CharField(max_length=50)),
                ('center_city_other', models.CharField(max_length=50)),
                ('coaching_fees_other', models.CharField(max_length=10)),
                ('feedback_other', models.TextField()),
                ('collage_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='home_page.reg_alumni')),
            ],
            options={
                'db_table': 'Coaching',
            },
        ),
        migrations.CreateModel(
            name='AppliedClg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country1', models.CharField(max_length=30)),
                ('c1_clg1', models.CharField(max_length=50)),
                ('c1_state1', models.CharField(max_length=30)),
                ('c1_city1', models.CharField(max_length=30)),
                ('c1_appfees1', models.CharField(max_length=30)),
                ('c1_coursefees1', models.CharField(max_length=30)),
                ('c1_course1', models.CharField(max_length=30)),
                ('c1_gre1', models.CharField(max_length=10)),
                ('c1_toefl1', models.CharField(max_length=10)),
                ('c1_ielts1', models.CharField(max_length=10)),
                ('c1_clg2', models.CharField(max_length=50)),
                ('c1_state2', models.CharField(max_length=30)),
                ('c1_city2', models.CharField(max_length=30)),
                ('c1_appfees2', models.CharField(max_length=30)),
                ('c1_coursefees2', models.CharField(max_length=30)),
                ('c1_course2', models.CharField(max_length=30)),
                ('c1_gre2', models.CharField(max_length=10)),
                ('c1_toefl2', models.CharField(max_length=10)),
                ('c1_ielts2', models.CharField(max_length=10)),
                ('c1_clg3', models.CharField(max_length=50)),
                ('c1_state3', models.CharField(max_length=30)),
                ('c1_city3', models.CharField(max_length=30)),
                ('c1_appfees3', models.CharField(max_length=30)),
                ('c1_coursefees3', models.CharField(max_length=30)),
                ('c1_course3', models.CharField(max_length=30)),
                ('c1_gre3', models.CharField(max_length=10)),
                ('c1_toefl3', models.CharField(max_length=10)),
                ('c1_ielts3', models.CharField(max_length=10)),
                ('country2', models.CharField(max_length=30)),
                ('c2_clg1', models.CharField(max_length=50)),
                ('c2_state1', models.CharField(max_length=30)),
                ('c2_city1', models.CharField(max_length=30)),
                ('c2_appfees1', models.CharField(max_length=30)),
                ('c2_coursefees1', models.CharField(max_length=30)),
                ('c2_course1', models.CharField(max_length=30)),
                ('c2_gre1', models.CharField(max_length=10)),
                ('c2_toefl1', models.CharField(max_length=10)),
                ('c2_ielts1', models.CharField(max_length=10)),
                ('c2_clg2', models.CharField(max_length=50)),
                ('c2_state2', models.CharField(max_length=30)),
                ('c2_city2', models.CharField(max_length=30)),
                ('c2_appfees2', models.CharField(max_length=30)),
                ('c2_coursefees2', models.CharField(max_length=30)),
                ('c2_course2', models.CharField(max_length=30)),
                ('c2_gre2', models.CharField(max_length=10)),
                ('c2_toefl2', models.CharField(max_length=10)),
                ('c2_ielts2', models.CharField(max_length=10)),
                ('c2_clg3', models.CharField(max_length=50)),
                ('c2_state3', models.CharField(max_length=30)),
                ('c2_city3', models.CharField(max_length=30)),
                ('c2_appfees3', models.CharField(max_length=30)),
                ('c2_coursefees3', models.CharField(max_length=30)),
                ('c2_course3', models.CharField(max_length=30)),
                ('c2_gre3', models.CharField(max_length=10)),
                ('c2_toefl3', models.CharField(max_length=10)),
                ('c2_ielts3', models.CharField(max_length=10)),
                ('collage_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='home_page.reg_alumni')),
            ],
            options={
                'db_table': 'AppliedClg',
            },
        ),
        migrations.CreateModel(
            name='All',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=15)),
                ('branch', models.CharField(max_length=15)),
                ('passout_year', models.CharField(max_length=4)),
                ('gender', models.CharField(max_length=6)),
                ('permanent_address', models.TextField(max_length=130)),
                ('home_town', models.CharField(max_length=15)),
                ('gre', models.CharField(max_length=5)),
                ('toefl', models.CharField(max_length=5)),
                ('ielts', models.CharField(max_length=5)),
                ('cpi6', models.CharField(max_length=5)),
                ('cpi7', models.CharField(max_length=5)),
                ('backlog6', models.CharField(max_length=3)),
                ('backlog7', models.CharField(max_length=3)),
                ('collage', models.CharField(max_length=20)),
                ('collage_country', models.CharField(max_length=15)),
                ('collage_city', models.CharField(max_length=15)),
                ('collage_branch', models.CharField(max_length=15)),
                ('country1', models.CharField(max_length=15)),
                ('c1_clg1', models.CharField(max_length=20)),
                ('c1_state1', models.CharField(max_length=15)),
                ('c1_city1', models.CharField(max_length=15)),
                ('c1_appfees1', models.CharField(max_length=6)),
                ('c1_coursefees1', models.CharField(max_length=7)),
                ('c1_course1', models.CharField(max_length=15)),
                ('c1_gre1', models.CharField(max_length=5)),
                ('c1_toefl1', models.CharField(max_length=5)),
                ('c1_ielts1', models.CharField(max_length=5)),
                ('c1_clg2', models.CharField(max_length=20)),
                ('c1_state2', models.CharField(max_length=15)),
                ('c1_city2', models.CharField(max_length=15)),
                ('c1_appfees2', models.CharField(max_length=6)),
                ('c1_coursefees2', models.CharField(max_length=7)),
                ('c1_course2', models.CharField(max_length=15)),
                ('c1_gre2', models.CharField(max_length=5)),
                ('c1_toefl2', models.CharField(max_length=5)),
                ('c1_ielts2', models.CharField(max_length=5)),
                ('c1_clg3', models.CharField(max_length=20)),
                ('c1_state3', models.CharField(max_length=15)),
                ('c1_city3', models.CharField(max_length=15)),
                ('c1_appfees3', models.CharField(max_length=6)),
                ('c1_coursefees3', models.CharField(max_length=7)),
                ('c1_course3', models.CharField(max_length=15)),
                ('c1_gre3', models.CharField(max_length=5)),
                ('c1_toefl3', models.CharField(max_length=5)),
                ('c1_ielts3', models.CharField(max_length=5)),
                ('country2', models.CharField(max_length=20)),
                ('c2_clg1', models.CharField(max_length=15)),
                ('c2_state1', models.CharField(max_length=15)),
                ('c2_city1', models.CharField(max_length=15)),
                ('c2_appfees1', models.CharField(max_length=6)),
                ('c2_coursefees1', models.CharField(max_length=7)),
                ('c2_course1', models.CharField(max_length=15)),
                ('c2_gre1', models.CharField(max_length=5)),
                ('c2_toefl1', models.CharField(max_length=5)),
                ('c2_ielts1', models.CharField(max_length=5)),
                ('c2_clg2', models.CharField(max_length=20)),
                ('c2_state2', models.CharField(max_length=15)),
                ('c2_city2', models.CharField(max_length=15)),
                ('c2_appfees2', models.CharField(max_length=6)),
                ('c2_coursefees2', models.CharField(max_length=7)),
                ('c2_course2', models.CharField(max_length=15)),
                ('c2_gre2', models.CharField(max_length=5)),
                ('c2_toefl2', models.CharField(max_length=5)),
                ('c2_ielts2', models.CharField(max_length=5)),
                ('c2_clg3', models.CharField(max_length=20)),
                ('c2_state3', models.CharField(max_length=15)),
                ('c2_city3', models.CharField(max_length=15)),
                ('c2_appfees3', models.CharField(max_length=6)),
                ('c2_coursefees3', models.CharField(max_length=7)),
                ('c2_course3', models.CharField(max_length=15)),
                ('c2_gre3', models.CharField(max_length=5)),
                ('c2_toefl3', models.CharField(max_length=5)),
                ('c2_ielts3', models.CharField(max_length=5)),
                ('course_name_gre', models.CharField(max_length=15)),
                ('center_name_gre', models.CharField(max_length=10)),
                ('center_city_gre', models.CharField(max_length=15)),
                ('coaching_fees_gre', models.CharField(max_length=6)),
                ('feedback_gre', models.TextField(max_length=60)),
                ('course_name_toefl', models.CharField(max_length=15)),
                ('center_name_toefl', models.CharField(max_length=10)),
                ('center_city_toefl', models.CharField(max_length=15)),
                ('coaching_fees_toefl', models.CharField(max_length=6)),
                ('feedback_toefl', models.TextField(max_length=60)),
                ('course_name_ielts', models.CharField(max_length=15)),
                ('center_name_ielts', models.CharField(max_length=10)),
                ('center_city_ielts', models.CharField(max_length=15)),
                ('coaching_fees_ielts', models.CharField(max_length=6)),
                ('feedback_ielts', models.TextField(max_length=60)),
                ('course_name_other', models.CharField(max_length=15)),
                ('center_name_other', models.CharField(max_length=10)),
                ('center_city_other', models.CharField(max_length=15)),
                ('coaching_fees_other', models.CharField(max_length=6)),
                ('feedback_other', models.TextField(max_length=60)),
                ('service_name', models.CharField(max_length=15)),
                ('service_city', models.CharField(max_length=15)),
                ('service_address', models.TextField(max_length=60)),
                ('service_number', models.CharField(max_length=14)),
                ('service_fees', models.CharField(max_length=5)),
                ('consulting_countries', models.TextField(max_length=50)),
                ('res_country', models.CharField(max_length=15)),
                ('res_state', models.CharField(max_length=15)),
                ('res_city', models.CharField(max_length=15)),
                ('res_address', models.TextField(max_length=50)),
                ('res_rent', models.CharField(max_length=5)),
                ('res_utility_exp', models.CharField(max_length=5)),
                ('res_monthly_exp', models.CharField(max_length=6)),
                ('useful_things', models.TextField(max_length=80)),
                ('flight_name', models.CharField(max_length=15)),
                ('site_name', models.CharField(max_length=15)),
                ('airport_exp', models.CharField(max_length=5)),
                ('from_where', models.CharField(max_length=15)),
                ('to_where', models.CharField(max_length=15)),
                ('leave_over_place', models.CharField(max_length=15)),
                ('leave_over_time', models.CharField(max_length=15)),
                ('collage_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='home_page.reg_alumni')),
            ],
            options={
                'db_table': 'All',
            },
        ),
    ]
