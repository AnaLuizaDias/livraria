# Generated by Django 3.2.12 on 2022-09-28 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20220928_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('ISBN', models.CharField(max_length=32)),
                ('quantidade', models.IntegerField()),
                ('preco', models.FloatField()),
                ('autores', models.ManyToManyField(related_name='livros', to='core.Autor')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='livros', to='core.categoria')),
                ('editora', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='livros', to='core.editora')),
            ],
        ),
        migrations.DeleteModel(
            name='Livros',
        ),
    ]
