# Generated by Django 2.1.1(2018-09-27) + Manually Edited

import re
import uuid

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import swapper
from django.conf import settings
from django.db import migrations, models
from swapper import get_model_name

import immunity_users.mixins
import immunity_utils.base
import immunity_utils.utils
from immunity_radius.migrations import add_default_organization


class Migration(migrations.Migration):
    """
    Initial migration for immunity-radius models
    Note (It's Manually Edited):
    - settings._IMMUNITY
_DEFAULT_ORG_UUID must be set before
      running; as done in 'immunity_users'->'0003_default_organization'
    - Custom logic for setting default organization in all existing
      relevent records (read comments)
    """

    dependencies = [
        swapper.dependency(
            *swapper.split(settings.AUTH_USER_MODEL), version='0004_default_groups'
        ),
        ('immunity_radius', '0001_initial_freeradius'),
    ]

    operations = [
        migrations.CreateModel(
            name='RadiusBatch',
            fields=[
                (
                    'id',
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    'created',
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name='created',
                    ),
                ),
                (
                    'modified',
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name='modified',
                    ),
                ),
                (
                    'strategy',
                    models.CharField(
                        choices=[
                            ('prefix', 'Generate from prefix'),
                            ('csv', 'Import from CSV'),
                        ],
                        db_index=True,
                        help_text='Import users from a CSV or generate using a prefix',
                        max_length=16,
                        verbose_name='strategy',
                    ),
                ),
                (
                    'csvfile',
                    models.FileField(
                        blank=True,
                        help_text=(
                            'The csv file containing the user details to be uploaded'
                        ),
                        null=True,
                        upload_to="",
                        verbose_name='CSV',
                    ),
                ),
                (
                    'prefix',
                    models.CharField(
                        blank=True,
                        help_text=(
                            'Usernames generated will be of the format [prefix][number]'
                        ),
                        max_length=20,
                        null=True,
                        verbose_name='prefix',
                    ),
                ),
                (
                    'pdf',
                    models.FileField(
                        blank=True,
                        help_text=(
                            'The pdf file containing list of usernames and passwords'
                        ),
                        null=True,
                        upload_to="",
                        verbose_name='PDF',
                    ),
                ),
                (
                    'expiration_date',
                    models.DateField(
                        blank=True,
                        help_text='If left blank users will never expire',
                        null=True,
                        verbose_name='expiration date',
                    ),
                ),
                (
                    'name',
                    models.CharField(
                        db_index=True,
                        help_text='A unique batch name',
                        max_length=128,
                        verbose_name='name',
                    ),
                ),
                (
                    'organization',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=get_model_name('immunity_users', 'Organization'),
                        verbose_name='organization',
                    ),
                ),
                (
                    'users',
                    models.ManyToManyField(
                        blank=True,
                        help_text='List of users uploaded in this batch',
                        related_name='radius_batch',
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                'verbose_name': 'batch user creation',
                'verbose_name_plural': 'batch user creation operations',
                'db_table': 'radbatch',
                'abstract': False,
                'swappable': 'IMMUNITY
_RADIUS_RADIUSBATCH_MODEL',
            },
            bases=(immunity_users.mixins.ValidateOrgMixin, models.Model),
        ),
        migrations.CreateModel(
            name='RadiusGroup',
            fields=[
                (
                    'id',
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    'created',
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name='created',
                    ),
                ),
                (
                    'modified',
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name='modified',
                    ),
                ),
                (
                    'name',
                    models.CharField(
                        db_index=True,
                        max_length=255,
                        unique=True,
                        verbose_name='group name',
                    ),
                ),
                (
                    'description',
                    models.CharField(
                        blank=True, max_length=64, null=True, verbose_name='description'
                    ),
                ),
                (
                    'default',
                    models.BooleanField(
                        default=False,
                        help_text=(
                            'The default group is automatically assigned '
                            'to new users; changing the default group has only '
                            'effect on new users (existing users will keep '
                            'being members of their current group)'
                        ),
                        verbose_name='is default?',
                    ),
                ),
                (
                    'organization',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=get_model_name('immunity_users', 'Organization'),
                        verbose_name='organization',
                    ),
                ),
            ],
            options={
                'verbose_name': 'group',
                'verbose_name_plural': 'groups',
                'abstract': False,
                'swappable': 'IMMUNITY
_RADIUS_RADIUSGROUP_MODEL',
            },
            bases=(immunity_users.mixins.ValidateOrgMixin, models.Model),
        ),
        migrations.CreateModel(
            name='OrganizationRadiusSettings',
            fields=[
                (
                    'id',
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                (
                    'token',
                    immunity_utils.base.KeyField(
                        default=immunity_utils.utils.get_random_key,
                        help_text=None,
                        max_length=32,
                        validators=[
                            django.core.validators.RegexValidator(
                                re.compile('^[^\\s/\\.]+$'),
                                code='invalid',
                                message=(
                                    'This value must not contain spaces, '
                                    'dots or slashes.'
                                ),
                            )
                        ],
                    ),
                ),
                (
                    'organization',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=get_model_name('immunity_users', 'Organization'),
                        verbose_name='organization',
                    ),
                ),
            ],
            options={'abstract': False},
            bases=(immunity_users.mixins.ValidateOrgMixin, models.Model),
        ),
        migrations.AddField(
            model_name='radiuscheck',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='radiuscheck',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='radiuscheck',
            name='user',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name='radiuscheck',
            name='valid_until',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='radiusgroupcheck',
            name='group',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.IMMUNITY
_RADIUS_RADIUSGROUP_MODEL,
            ),
        ),
        migrations.AddField(
            model_name='radiusgroupreply',
            name='group',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.IMMUNITY
_RADIUS_RADIUSGROUP_MODEL,
            ),
        ),
        migrations.AddField(
            model_name='radiusreply',
            name='user',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name='radiususergroup',
            name='group',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.IMMUNITY
_RADIUS_RADIUSGROUP_MODEL,
            ),
        ),
        migrations.AddField(
            model_name='radiususergroup',
            name='user',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name='radiusaccounting',
            name='called_station_id',
            field=models.CharField(
                blank=True,
                db_column='calledstationid',
                db_index=True,
                max_length=50,
                null=True,
                verbose_name='called station ID',
            ),
        ),
        migrations.AlterField(
            model_name='radiusaccounting',
            name='calling_station_id',
            field=models.CharField(
                blank=True,
                db_column='callingstationid',
                db_index=True,
                max_length=50,
                null=True,
                verbose_name='calling station ID',
            ),
        ),
        migrations.AlterField(
            model_name='radiuscheck',
            name='username',
            field=models.CharField(
                blank=True, db_index=True, max_length=64, verbose_name='username'
            ),
        ),
        migrations.AlterField(
            model_name='radiusgroupcheck',
            name='groupname',
            field=models.CharField(
                blank=True, db_index=True, max_length=64, verbose_name='group name'
            ),
        ),
        migrations.AlterField(
            model_name='radiusgroupreply',
            name='groupname',
            field=models.CharField(
                blank=True, db_index=True, max_length=64, verbose_name='group name'
            ),
        ),
        migrations.AlterField(
            model_name='radiusreply',
            name='username',
            field=models.CharField(
                blank=True, db_index=True, max_length=64, verbose_name='username'
            ),
        ),
        migrations.AlterField(
            model_name='radiususergroup',
            name='groupname',
            field=models.CharField(
                blank=True, max_length=64, verbose_name='group name'
            ),
        ),
        migrations.AlterField(
            model_name='radiususergroup',
            name='username',
            field=models.CharField(
                blank=True, db_index=True, max_length=64, verbose_name='username'
            ),
        ),
        migrations.AlterUniqueTogether(
            name='radiusbatch', unique_together={('name', 'organization')}
        ),
        migrations.AlterModelOptions(
            name='organizationradiussettings',
            options={
                'verbose_name': 'Organization radius settings',
                'verbose_name_plural': 'Organization radius settings',
            },
        ),
        migrations.AlterField(
            model_name='organizationradiussettings',
            name='id',
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name='organizationradiussettings',
            name='organization',
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='radius_settings',
                to=get_model_name('immunity_users', 'Organization'),
                verbose_name='organization',
            ),
        ),
        # Set null=True for organization field to allow
        # creation without giving a default value
        migrations.AddField(
            model_name='nas',
            name='organization',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=get_model_name('immunity_users', 'Organization'),
                verbose_name='organization',
            ),
        ),
        migrations.AddField(
            model_name='radiusaccounting',
            name='organization',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=get_model_name('immunity_users', 'Organization'),
                verbose_name='organization',
            ),
        ),
        migrations.AddField(
            model_name='radiuscheck',
            name='organization',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=get_model_name('immunity_users', 'Organization'),
                verbose_name='organization',
            ),
        ),
        migrations.AddField(
            model_name='radiuspostauth',
            name='organization',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=get_model_name('immunity_users', 'Organization'),
                verbose_name='organization',
            ),
        ),
        migrations.AddField(
            model_name='radiusreply',
            name='organization',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=get_model_name('immunity_users', 'Organization'),
                verbose_name='organization',
            ),
        ),
        # Set default organization for all the existing records
        migrations.RunPython(
            add_default_organization, reverse_code=migrations.RunPython.noop
        ),
        # Set null=False for all organization fields that need
        # NOT NULL condition as per the immunity-radius model
        migrations.AlterField(
            model_name='nas',
            name='organization',
            field=models.ForeignKey(
                null=False,
                blank=False,
                on_delete=django.db.models.deletion.CASCADE,
                to=get_model_name('immunity_users', 'Organization'),
                verbose_name='organization',
            ),
        ),
        migrations.AlterField(
            model_name='radiusaccounting',
            name='organization',
            field=models.ForeignKey(
                null=False,
                blank=False,
                on_delete=django.db.models.deletion.CASCADE,
                to=get_model_name('immunity_users', 'Organization'),
                verbose_name='organization',
            ),
        ),
        migrations.AlterField(
            model_name='radiuscheck',
            name='organization',
            field=models.ForeignKey(
                null=False,
                blank=False,
                on_delete=django.db.models.deletion.CASCADE,
                to=get_model_name('immunity_users', 'Organization'),
                verbose_name='organization',
            ),
        ),
        migrations.AlterField(
            model_name='radiuspostauth',
            name='organization',
            field=models.ForeignKey(
                null=False,
                blank=False,
                on_delete=django.db.models.deletion.CASCADE,
                to=get_model_name('immunity_users', 'Organization'),
                verbose_name='organization',
            ),
        ),
        migrations.AlterField(
            model_name='radiusreply',
            name='organization',
            field=models.ForeignKey(
                null=False,
                blank=False,
                on_delete=django.db.models.deletion.CASCADE,
                to=get_model_name('immunity_users', 'Organization'),
                verbose_name='organization',
            ),
        ),
    ]
