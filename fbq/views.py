#-*- coding: utf-8 -*-
from django.shortcuts import render
from .forms import FacebookForm
from .query import facebook_post

def comments(request):
	result = ""
	if request.method == "POST":
		MyFacebookForm = FacebookForm(request.POST)
		if MyFacebookForm.is_valid():
			page_id = MyFacebookForm.cleaned_data['page_id']
			post_id = MyFacebookForm.cleaned_data['post_id']
			print('yay %s_%s' % (page_id, post_id))
			result = facebook_post(page_id, post_id)
			print(result)
	else:
		MyFacebookForm = FacebookForm()
		
	return render(request, 'comments.html', {"result" : result})