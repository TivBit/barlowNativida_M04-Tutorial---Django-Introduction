# -*- coding: utf-8 -*-
"""
Created on %(Date: 12 Feb 2023)s

@author: %(Tiv Barlow)s
Python Version 3.11.1
SDEV 220 Spring 2023
Assignment: M04 Tutorial - Django Introduction
"""
#this is the script for the admin.py file.  It registers the blog site (Post).
from django.contrib import admin
from .models import Post

admin.site.register(Post)