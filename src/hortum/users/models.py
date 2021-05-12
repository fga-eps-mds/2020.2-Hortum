from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from ..settings import EMAIL_HOST_USER as email_sender
from ..encode import encode_string

def upload_image(instance, filename):
    return f"Profile-{instance.username}-{filename}"

class User(AbstractUser):
    username = models.CharField(max_length=30)
    email = models.EmailField(unique=True, max_length=120)
    phone_number = models.CharField(unique=True, blank=False, null=True, max_length=13)
    is_productor = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to=upload_image, null=True, default="person-male.png")
    is_verified = models.BooleanField(default=False)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def send_verification_email(request, email):
        encoded_email = encode_string(email)
        url_verify = 'http://' + request.get_host() + '/users/verify/' + encoded_email
        send_mail(
            'Hortum - verifique seu email',
			'Você está a um passo de acessar o Hortum, clique no link abaixo para concluir seu registro:\n' + url_verify,
			email_sender,
			[email],
			fail_silently=False,
		)
