#-*- coding: utf-8 -*-
from django import forms

class FacebookForm(forms.Form):
   page_id = forms.CharField(max_length = 100)
   post_id = forms.CharField(max_length = 100)