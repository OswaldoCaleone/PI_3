from django.core.mail import EmailMultiAlternatives, send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings


def envia_email(resquest):
    
    html_content = render_to_string('emails/cadastro_confirmado.html', {'nome': ''})
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives('Cadastro confirmado', text_content, settings.EMAIL_HOST_USER, ['caleone@hotmail.com.br'] )
    email.attach_alternative(html_content, 'text/html')
    send_mail()
    
    return HttpResponse('Olá')
