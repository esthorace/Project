# Generated by Django 4.1.7 on 2023-03-02 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jerarquia', '0003_alter_jerarquíacategorías_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='composiciónobjeto',
            name='categoría',
        ),
        migrations.RemoveField(
            model_name='composiciónobjeto',
            name='nombre',
        ),
        migrations.AddField(
            model_name='composiciónobjeto',
            name='inferior_categoría_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='comp_inf', to='jerarquia.categoría'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='composiciónobjeto',
            name='superior_categoría_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='comp_sup', to='jerarquia.jerarquíacategorías'),
            preserve_default=False,
        ),
    ]
