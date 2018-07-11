# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class items(models.Model):
      name = models.CharField(max_length=50)
      price = models.IntegerField()
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
