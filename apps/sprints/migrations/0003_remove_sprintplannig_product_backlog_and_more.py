# Generated by Django 4.0 on 2021-12-18 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_productbacklog_name_alter_productbacklog_priority'),
        ('sprints', '0002_alter_sprintretrospective_project_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sprintplannig',
            name='product_backlog',
        ),
        migrations.RemoveField(
            model_name='sprintretrospective',
            name='project',
        ),
        migrations.RemoveField(
            model_name='sprintreview',
            name='sprint',
        ),
        migrations.RemoveField(
            model_name='sprint',
            name='sprint_planning',
        ),
        migrations.AddField(
            model_name='sprint',
            name='product_backlog',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projects.productbacklog', verbose_name='Product backlog'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='DailyScrum',
        ),
        migrations.DeleteModel(
            name='SprintPlannig',
        ),
        migrations.DeleteModel(
            name='SprintRetrospective',
        ),
        migrations.DeleteModel(
            name='SprintReview',
        ),
    ]
