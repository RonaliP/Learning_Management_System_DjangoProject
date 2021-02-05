from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import  get_current_site
from django.urls import reverse
import pyshorteners

class Util:
    @staticmethod
    def email_data(email_data):
        current_site = email_data['site']
        relative_link = reverse(email_data['reverse'])
        link = 'http://'+current_site+relative_link+"?token="+str(email_data['token'])
        shortener = pyshorteners.Shortener()
        short_url = shortener.tinyurl.short(link)
        email_body = email_data['message']+'\n'+short_url
        email_subject = email_data['subject']
        data = {'email_body':email_body ,'to_email':email_data['email'], 'email_subject':email_subject}
        return data

    @staticmethod
    def send_email(data):
        email = EmailMessage(subject=data['email_subject'],body=data['email_body'],to=[data['to_email']])
        email.send()