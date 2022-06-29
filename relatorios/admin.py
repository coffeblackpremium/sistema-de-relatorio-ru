from django.contrib import admin
from relatorios.models import User

#Adicionando o Modelo de Banco de dados no Site da Administração
admin.site.register(User)


# Create your tests here.

user = User.objects.create_user('myusername', 'myemail@crazymail.com', 'mypassword')

# Update fields and then save again
user.first_name = 'John'
user.last_name = 'Citizen'
user.save()