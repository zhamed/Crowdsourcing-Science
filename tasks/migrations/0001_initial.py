# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Definition'
        db.create_table('tasks_definition', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('term', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('explanation', self.gf('django.db.models.fields.CharField')(max_length=1024)),
        ))
        db.send_create_signal('tasks', ['Definition'])

        # Adding model 'Worker'
        db.create_table('tasks_worker', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('alias', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('reputation', self.gf('django.db.models.fields.DecimalField')(max_digits=2, decimal_places=2)),
            ('recruitment', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('tasks', ['Worker'])

        # Adding model 'Object'
        db.create_table('tasks_object', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('info', self.gf('django.db.models.fields.CharField')(default='', max_length=200)),
        ))
        db.send_create_signal('tasks', ['Object'])

        # Adding model 'Attribute'
        db.create_table('tasks_attribute', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('estimated_difficulty', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('example', self.gf('django.db.models.fields.CharField')(default='', max_length=200)),
        ))
        db.send_create_signal('tasks', ['Attribute'])

        # Adding model 'Attribute_State'
        db.create_table('tasks_attribute_state', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('attribute', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tasks.Attribute'])),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('example', self.gf('django.db.models.fields.CharField')(default='', max_length=200)),
        ))
        db.send_create_signal('tasks', ['Attribute_State'])

        # Adding model 'Association'
        db.create_table('tasks_association', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('object', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tasks.Object'])),
            ('attribute', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tasks.Attribute'])),
            ('attribute_state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tasks.Attribute_State'])),
            ('attribute_value', self.gf('django.db.models.fields.DecimalField')(max_digits=2, decimal_places=2)),
            ('certainty', self.gf('django.db.models.fields.DecimalField')(max_digits=2, decimal_places=2)),
            ('difficulty', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=2, decimal_places=2)),
            ('votes', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('tasks', ['Association'])

        # Adding model 'Task'
        db.create_table('tasks_task', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('input_object', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tasks.Object'])),
            ('attribute', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tasks.Attribute'])),
            ('max_workers', self.gf('django.db.models.fields.IntegerField')()),
            ('nb_workers', self.gf('django.db.models.fields.IntegerField')()),
            ('confirmation_code', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('tasks', ['Task'])

        # Adding model 'Classification'
        db.create_table('tasks_classification', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tasks.Task'])),
            ('worker', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tasks.Worker'])),
            ('association', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tasks.Association'])),
            ('value', self.gf('django.db.models.fields.DecimalField')(max_digits=2, decimal_places=2)),
            ('explanation', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('certainty', self.gf('django.db.models.fields.DecimalField')(max_digits=2, decimal_places=2)),
            ('difficulty', self.gf('django.db.models.fields.DecimalField')(max_digits=2, decimal_places=2)),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('info', self.gf('django.db.models.fields.CharField')(max_length=1024)),
        ))
        db.send_create_signal('tasks', ['Classification'])


    def backwards(self, orm):
        # Deleting model 'Definition'
        db.delete_table('tasks_definition')

        # Deleting model 'Worker'
        db.delete_table('tasks_worker')

        # Deleting model 'Object'
        db.delete_table('tasks_object')

        # Deleting model 'Attribute'
        db.delete_table('tasks_attribute')

        # Deleting model 'Attribute_State'
        db.delete_table('tasks_attribute_state')

        # Deleting model 'Association'
        db.delete_table('tasks_association')

        # Deleting model 'Task'
        db.delete_table('tasks_task')

        # Deleting model 'Classification'
        db.delete_table('tasks_classification')


    models = {
        'tasks.association': {
            'Meta': {'object_name': 'Association'},
            'attribute': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tasks.Attribute']"}),
            'attribute_state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tasks.Attribute_State']"}),
            'attribute_value': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '2'}),
            'certainty': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '2'}),
            'difficulty': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '2', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tasks.Object']"}),
            'votes': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'tasks.attribute': {
            'Meta': {'object_name': 'Attribute'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'estimated_difficulty': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'example': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'tasks.attribute_state': {
            'Meta': {'object_name': 'Attribute_State'},
            'attribute': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tasks.Attribute']"}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'example': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'tasks.classification': {
            'Meta': {'object_name': 'Classification'},
            'association': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tasks.Association']"}),
            'certainty': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '2'}),
            'difficulty': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '2'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {}),
            'explanation': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tasks.Task']"}),
            'value': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '2'}),
            'worker': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tasks.Worker']"})
        },
        'tasks.definition': {
            'Meta': {'object_name': 'Definition'},
            'explanation': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'term': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'tasks.object': {
            'Meta': {'object_name': 'Object'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'type': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'tasks.task': {
            'Meta': {'object_name': 'Task'},
            'attribute': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tasks.Attribute']"}),
            'confirmation_code': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'input_object': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tasks.Object']"}),
            'max_workers': ('django.db.models.fields.IntegerField', [], {}),
            'nb_workers': ('django.db.models.fields.IntegerField', [], {})
        },
        'tasks.worker': {
            'Meta': {'object_name': 'Worker'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'recruitment': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'reputation': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '2'})
        }
    }

    complete_apps = ['tasks']