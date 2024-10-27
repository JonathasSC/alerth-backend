# Generated by Django 5.1.1 on 2024-10-15 23:31

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_servicecategory_serviceentity_entitycategory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientevent',
            old_name='client_id',
            new_name='client',
        ),
        migrations.RenameField(
            model_name='clientevent',
            old_name='event_id',
            new_name='event',
        ),
        migrations.RenameField(
            model_name='entitycategory',
            old_name='entityCategory_id',
            new_name='entity_category_id',
        ),
        migrations.RenameField(
            model_name='entitycategory',
            old_name='serviceCategory_id',
            new_name='service_category',
        ),
        migrations.RenameField(
            model_name='entitycategory',
            old_name='serviceEntity_id',
            new_name='service_entity',
        ),
        migrations.RenameField(
            model_name='purchase',
            old_name='client_id',
            new_name='client',
        ),
        migrations.RenameField(
            model_name='purchase',
            old_name='item_id',
            new_name='item',
        ),
        migrations.RenameField(
            model_name='servicecategory',
            old_name='serviceCategory_id',
            new_name='service_category_id',
        ),
        migrations.RenameField(
            model_name='serviceentity',
            old_name='serviceEntity_id',
            new_name='service_entity_id',
        ),
        migrations.RemoveField(
            model_name='clientevent',
            name='id',
        ),
        migrations.RemoveField(
            model_name='event',
            name='category',
        ),
        migrations.RemoveField(
            model_name='event',
            name='exp_acquired',
        ),
        migrations.RemoveField(
            model_name='event',
            name='urgency',
        ),
        migrations.AddField(
            model_name='clientevent',
            name='client_event_id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='entitycategory',
            name='exp_acquired',
            field=models.PositiveIntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='service_category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.servicecategory'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('comment_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('comment', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.client')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.event')),
            ],
        ),
    ]