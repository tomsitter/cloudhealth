# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Patient'
        db.create_table(u'signup_patient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('userID', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('dateOfBirth', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('profilePicture', self.gf('django.db.models.fields.files.ImageField')(default='/home/action/workspace/cloudhealth/static/images/cloud_dialog.png', max_length=100, null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=1, blank=True)),
            ('weight', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=1, blank=True)),
            ('country', self.gf('django_countries.fields.CountryField')(max_length=2, null=True, blank=True)),
        ))
        db.send_create_signal(u'signup', ['Patient'])

        # Adding model 'Caregiver'
        db.create_table(u'signup_caregiver', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('userID', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('profilePicture', self.gf('django.db.models.fields.files.ImageField')(default='/home/action/workspace/cloudhealth/static/images/cloud_dialog.png', max_length=100, null=True, blank=True)),
            ('country', self.gf('django_countries.fields.CountryField')(max_length=2, null=True, blank=True)),
        ))
        db.send_create_signal(u'signup', ['Caregiver'])

        # Adding model 'DiseaseChoices'
        db.create_table(u'signup_diseasechoices', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fullName', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('shortName', self.gf('django.db.models.fields.CharField')(unique=True, max_length=5)),
        ))
        db.send_create_signal(u'signup', ['DiseaseChoices'])

        # Adding model 'DiseaseList'
        db.create_table(u'signup_diseaselist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'signup', ['DiseaseList'])

        # Adding M2M table for field disease on 'DiseaseList'
        m2m_table_name = db.shorten_name(u'signup_diseaselist_disease')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('diseaselist', models.ForeignKey(orm[u'signup.diseaselist'], null=False)),
            ('diseasechoices', models.ForeignKey(orm[u'signup.diseasechoices'], null=False))
        ))
        db.create_unique(m2m_table_name, ['diseaselist_id', 'diseasechoices_id'])


    def backwards(self, orm):
        # Deleting model 'Patient'
        db.delete_table(u'signup_patient')

        # Deleting model 'Caregiver'
        db.delete_table(u'signup_caregiver')

        # Deleting model 'DiseaseChoices'
        db.delete_table(u'signup_diseasechoices')

        # Deleting model 'DiseaseList'
        db.delete_table(u'signup_diseaselist')

        # Removing M2M table for field disease on 'DiseaseList'
        db.delete_table(db.shorten_name(u'signup_diseaselist_disease'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'signup.caregiver': {
            'Meta': {'object_name': 'Caregiver'},
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profilePicture': ('django.db.models.fields.files.ImageField', [], {'default': "'/home/action/workspace/cloudhealth/static/images/cloud_dialog.png'", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'userID': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'signup.diseasechoices': {
            'Meta': {'object_name': 'DiseaseChoices'},
            'fullName': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'shortName': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '5'})
        },
        u'signup.diseaselist': {
            'Meta': {'object_name': 'DiseaseList'},
            'disease': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['signup.DiseaseChoices']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'signup.patient': {
            'Meta': {'object_name': 'Patient'},
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'dateOfBirth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '1', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profilePicture': ('django.db.models.fields.files.ImageField', [], {'default': "'/home/action/workspace/cloudhealth/static/images/cloud_dialog.png'", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'userID': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '1', 'blank': 'True'})
        }
    }

    complete_apps = ['signup']