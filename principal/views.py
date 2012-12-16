# Create your views here.
# -*- coding: utf-8 -*-
from django.template import Context, loader, RequestContext
from principal.models import parkmarcadores
from django.core import serializers
from django.http import HttpResponse
import simplejson
from twython import Twython
import gdata.service


def index(request):
	data =  serializers.serialize("json", parkmarcadores.objects.all())
	data = simplejson.dumps(data)
	t = loader.get_template('templates/index.html')

	twitter = Twython()
	data_t = twitter.searchTwitter(q="#parkea")
	data_t = simplejson.dumps(data_t)
	c = RequestContext(request,{
	'title': 'Parkea',
	'json': data,
	'tweets': data_t,
	})
	return HttpResponse(t.render(c), content_type = 'charset=utf8')

def dologin(request):
	email = 'xogost@gmail.com'
	password = '5CCjF3k2Vqg='
	application_name = 'Parkea'

	try:
	  client.ClientLogin(email, password, source=application_name)
	except gdata.service.CaptchaRequired:
	  print 'Please visit ' + client.captcha_url
	  answer = raw_input('Answer to the challenge? ')
	  client.ClientLogin(email, password, source=application_name,
	                     captcha_token=client.captcha_token,
	                     captcha_response=answer)
	except gdata.service.BadAuthentication:
	  exit('Users credentials were unrecognized')
	except gdata.service.Error:
	  exit('Login Error')

	return HttpResponse("alert('Login');");