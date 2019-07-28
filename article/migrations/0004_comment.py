# Generated by Django 2.2.3 on 2019-07-27 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20190726_1407'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentator', models.CharField(max_length=90)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='article.ArticlePost')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
