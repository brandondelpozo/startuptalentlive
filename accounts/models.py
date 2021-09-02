from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
#from django.utils.text import slugify

from taggit.managers import TaggableManager

from django.template.defaultfilters import linebreaksbr

# Create your models here.

class Talent(models.Model):
	ACCOUNTYPE = (
		("I'm a Talent", "I'm a Talent"),
		("I'm hiring Talent", "I'm hiring Talent")
	)
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE) #Those atributes are added to the deffault User model
	name = models.CharField(max_length=200, null=True)
	location = models.CharField(max_length=200, null=True, blank=True)
	accounttype = models.CharField(max_length=17, choices=ACCOUNTYPE, default=ACCOUNTYPE)
	website = models.URLField(max_length=200, null=True, blank=True)
	github = models.URLField(max_length=200, null=True, blank=True)
	twitter = models.URLField(max_length=200, null=True, blank=True)
	instagram = models.URLField(max_length=200, null=True, blank=True)
	phone = models.CharField(max_length=200, null=True, blank=True)
	emailprofile = models.CharField(max_length=200, null=True, blank=True)
	bio = models.TextField(max_length=2000, null=True, blank=True)
	
	sideproject = models.CharField(max_length=40, null=True, blank=True)
	position = models.CharField(max_length=40, null=True, blank=True)
	yearstart = models.CharField(max_length=40, null=True, blank=True)
	yearend = models.CharField(max_length=40, null=True, blank=True)
	sideproject_website = models.URLField(max_length=200, null=True, blank=True)

	current_employment = models.CharField(max_length=40, null=True, blank=True)
	position_employment = models.CharField(max_length=40, null=True, blank=True)
	yearstart_employment = models.CharField(max_length=40, null=True, blank=True)
	yearend_employment = models.CharField(max_length=40, null=True, blank=True)
	website_employment = models.URLField(max_length=200, null=True, blank=True)

	institution_education = models.CharField(max_length=40, null=True, blank=True)
	degree_education = models.CharField(max_length=70, null=True, blank=True)
	yearstart_education = models.CharField(max_length=40, null=True, blank=True)
	yearend_education = models.CharField(max_length=40, null=True, blank=True)
	website_institution = models.URLField(max_length=200, null=True, blank=True)

	profile_pic = models.ImageField(default="profile2.png", null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
#	slug = models.SlugField(default='', editable=False, max_length=200, null=False)
	tags = TaggableManager()
	
	mytalentstory = models.TextField(max_length=10000, null=True, blank=True)

	
	#def get_absolute_url(self):
	#	kwargs = {
	#		'pk_test': self.id,
	#		'slug': self.slug
	#	}
	#	return reverse('profiletesting', kwargs=kwargs)

	#def save(self, *args, **kwargs):
	#	value = self.user
	#	self.slug = slugify(value, allow_unicode=True)
	#	super().save(*args,**kwargs)

	def __str__(self):
		return self.name