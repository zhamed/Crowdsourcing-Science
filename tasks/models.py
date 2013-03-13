from django.db import models

# data we need:
#   test_image

# Create your models here.
class Definition(models.Model):
	term = models.CharField(max_length=200);
	explanation = models.CharField(max_length=1024);

class Worker(models.Model):
	alias = models.CharField(max_length=200);
	password = models.CharField(max_length=200);
	reputation = models.DecimalField(max_digits=2, decimal_places=2);
	recruitment = models.CharField(max_length=200);

class Object(models.Model):
	# an object is an entity (e.g., text, image, video, graph).  It has a type and a content field.  
	# the content field can be the actual object itself, or a url pointing to where the object is located.
	type = models.IntegerField(default=0);
	content = models.CharField(max_length=1024);
	info = models.CharField(max_length=200, default='');

	def __unicode__(self):
 		return self.content;

class Attribute(models.Model):
	# an attribute is a function about some property about an object.  Each attribute may have a set of attribute states.  
	# Continuous attributes will not have any states.
	content = models.CharField(max_length=1024);
	estimated_difficulty = models.FloatField(default=0.0);
	example = models.CharField(max_length=200, default='');

class Attribute_State(models.Model):
	# an attribute might have multiple states
	attribute = models.ForeignKey(Attribute);
	content = models.CharField(max_length=200);
	example = models.CharField(max_length=200, default='');

class Association(models.Model):
	# each object is associated with multiple attributes, and is described by the extent (attribute_value) to it belongs to a particular attribute_state
	# example: is the nasal process fused?
	object = models.ForeignKey(Object);
	attribute = models.ForeignKey(Attribute);
	attribute_state = models.ForeignKey(Attribute_State);
	attribute_value = models.DecimalField(max_digits=2, decimal_places=2);
	certainty = models.DecimalField(max_digits=2, decimal_places=2);
	difficulty = models.DecimalField(max_digits=2, decimal_places=2, default=0.0);
	votes = models.IntegerField(default=0);

class Task(models.Model):
	# each task has a set of input object and a set of output object
	input_object = models.ForeignKey(Object);
	attribute = models.ForeignKey(Attribute);
	max_workers = models.IntegerField();
	nb_workers = models.IntegerField();
	confirmation_code = models.IntegerField(default=0);

	def __unicode__(self):
 		return self.attribute.content;

class Classification(models.Model):
	task = models.ForeignKey(Task);
	worker = models.ForeignKey(Worker);
	association = models.ForeignKey(Association);
	value = models.DecimalField(max_digits=2, decimal_places=2);
	explanation = models.CharField(max_length=1024);
	certainty = models.DecimalField(max_digits=2, decimal_places=2);
	difficulty = models.DecimalField(max_digits=2, decimal_places=2);
	start_time = models.DateTimeField();
	end_time = models.DateTimeField();
	info = models.CharField(max_length=1024);

