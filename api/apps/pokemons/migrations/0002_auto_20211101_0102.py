# Generated by Django 3.2.8 on 2021-11-01 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("pokemons", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="pokestats",
            old_name="baseStat",
            new_name="base_stat",
        ),
        migrations.AlterField(
            model_name="pokeabilities",
            name="pokemon",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="abilities",
                to="pokemons.pokemon",
            ),
        ),
        migrations.AlterField(
            model_name="pokeevolutions",
            name="pokemon",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="evolutions",
                to="pokemons.pokemon",
            ),
        ),
        migrations.AlterField(
            model_name="pokehelditems",
            name="pokemon",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="held_items",
                to="pokemons.pokemon",
            ),
        ),
        migrations.AlterField(
            model_name="pokestats",
            name="pokemon",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="stats",
                to="pokemons.pokemon",
            ),
        ),
        migrations.AlterField(
            model_name="poketypes",
            name="pokemon",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="types",
                to="pokemons.pokemon",
            ),
        ),
    ]
