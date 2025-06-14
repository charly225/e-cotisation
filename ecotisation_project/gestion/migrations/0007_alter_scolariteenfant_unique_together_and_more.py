# Generated by Django 5.2.2 on 2025-06-12 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0006_remove_temoignage_photo'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='scolariteenfant',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='scolariteenfant',
            name='annee',
            field=models.CharField(choices=[('2020-2021', '2020-2021'), ('2021-2022', '2021-2022'), ('2022-2023', '2022-2023'), ('2023-2024', '2023-2024'), ('2024-2025', '2024-2025'), ('2025-2026', '2025-2026'), ('2026-2027', '2026-2027')], help_text='Exemple: 2023-2024', max_length=9),
        ),
        migrations.AlterUniqueTogether(
            name='scolariteenfant',
            unique_together={('enfant', 'annee')},
        ),
    ]
