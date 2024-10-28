from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Character(models.Model):
    name = models.CharField(max_length=50, blank=False)
    biography = models.TextField()
    stats = models.JSONField()


class Stats(models.Model):
    character = models.OneToOneField(Character, on_delete=models.CASCADE)
    health = models.IntegerField(default=5, validators=[
                                 MinValueValidator(0), MaxValueValidator(5)])
    spirit = models.IntegerField(default=5, validators=[
                                 MinValueValidator(0), MaxValueValidator(5)])

    edge = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(3)])
    heart = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(3)])
    iron = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(3)])
    shadow = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(3)])
    wits = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(3)])
    momentum = models.IntegerField(
        validators=[MinValueValidator(-6), MaxValueValidator(10)])
