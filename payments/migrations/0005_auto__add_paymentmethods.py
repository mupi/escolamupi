# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PaymentMethods'
        db.create_table(u'payments_paymentmethods', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=300)),
            ('data', self.gf('django.db.models.fields.TextField')(max_length=500)),
        ))
        db.send_create_signal(u'payments', ['PaymentMethods'])

        # Adding M2M table for field payment_methods on 'Plans'
        m2m_table_name = db.shorten_name(u'payments_plans_payment_methods')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('plans', models.ForeignKey(orm[u'payments.plans'], null=False)),
            ('paymentmethods', models.ForeignKey(orm[u'payments.paymentmethods'], null=False))
        ))
        db.create_unique(m2m_table_name, ['plans_id', 'paymentmethods_id'])


    def backwards(self, orm):
        # Deleting model 'PaymentMethods'
        db.delete_table(u'payments_paymentmethods')

        # Removing M2M table for field payment_methods on 'Plans'
        db.delete_table(db.shorten_name(u'payments_plans_payment_methods'))


    models = {
        u'accounts.timtecuser': {
            'Meta': {'object_name': 'TimtecUser'},
            'accepted_terms': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'biography': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'payments.paymentmethods': {
            'Meta': {'object_name': 'PaymentMethods'},
            'data': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'payments.plans': {
            'Meta': {'object_name': 'Plans'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'description_markdown': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'payment_methods': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['payments.PaymentMethods']", 'symmetrical': 'False'}),
            'period': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'payments.userpayments': {
            'Meta': {'object_name': 'UserPayments'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'payment_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'payment_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'payment_status': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.TimtecUser']"})
        },
        u'payments.userplandata': {
            'Meta': {'object_name': 'UserPlanData'},
            'expiration_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_payment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['payments.UserPayments']", 'null': 'True'}),
            'plan': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['payments.Plans']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.TimtecUser']"}),
            'user_status': ('django.db.models.fields.BooleanField', [], {})
        }
    }

    complete_apps = ['payments']