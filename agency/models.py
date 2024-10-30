import requests
from django.core.exceptions import ValidationError
from django.db import models


def validate_breed(value):
	url = 'https://api.thecatapi.com/v1/breeds'
	response = requests.get(url)

	if response.status_code != 200:
		raise ValidationError('Invalid breed')

	breeds = response.json()
	breed_names = [b['name'].lower() for b in breeds]

	if value.lower() not in breed_names:
		raise ValidationError(f"The breed '{value}' is not valid.")


class Cat(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	years_of_experience = models.IntegerField()
	breed = models.CharField(max_length=50, validators=[validate_breed])
	salary = models.IntegerField()

	class Meta:
		db_table = 'cats'
		verbose_name = 'Cat'
		verbose_name_plural = 'Cats'

	def __str__(self):
		return self.name


class Mission(models.Model):
	id = models.AutoField(primary_key=True)
	cat = models.ForeignKey(Cat, on_delete=models.CASCADE, related_name='missions')
	is_completed = models.BooleanField(default=False)

	class Meta:
		db_table = 'missions'
		verbose_name = 'Mission'
		verbose_name_plural = 'Missions'

	def __str__(self):
		return f'Mission {self.id} assigned to {self.cat.name}'


class Target(models.Model):
	id = models.AutoField(primary_key=True)
	mission = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name='targets')
	name = models.CharField(max_length=50)
	country = models.CharField(max_length=50)
	notes = models.TextField(blank=True)
	is_completed = models.BooleanField(default=False)

	class Meta:
		db_table = 'targets'
		verbose_name = 'Target'
		verbose_name_plural = 'Targets'

	def __str__(self):
		return f'Target {self.name} for Mission {self.mission.id}'
