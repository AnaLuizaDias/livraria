# Generated by Django 3.2.12 on 2022-09-28 19:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_auto_20220928_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'Carrinho'), (2, 'Realizado'), (3, 'Pago'), (4, 'Entregue')], default=1)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='compras', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterModelOptions(
            name='autor',
            options={'verbose_name_plural': 'autores'},
        ),
        migrations.RenameField(
            model_name='editora',
            old_name='descricao',
            new_name='nome',
        ),
        migrations.CreateModel(
            name='ItensCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('Compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='core.compra')),
                ('livros', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='core.livro')),
            ],
        ),
    ]