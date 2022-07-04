from django.http import HttpRequest
from django.test import TestCase
from relatorios.forms import TableEventForm
from relatorios.models import TableActionModel, TableEventModel, User

class TestTableEventModel(TestCase):
    
    def test_empty_form(self):
        pass

    def test_it_form_fields_for_users(self):
        user = User.objects.create_user(
            username="test",
            email="email-for-testing@testing.com",
            password="password"
        )

        user2 = User.objects.create_user(
            username="masterchief",
            email="masterchieftest@testing.com",
            password="mast44"
        )

        request = HttpRequest()
        request2 = HttpRequest()
        request.POST = {
            "title_event":"Relatorio de Test",
            "event_feature": "Presencial",
            "date_initial":"01-07-2022",
            "date_final":"02-07-2022",
        }
        request2.POST = {
            "title_event":"Relatorio",
            "event_feature": "Presencial",
            "date_initial":"03-07-2022",
            "date_final":"05-07-2022",
        }

        form = TableEventForm(request.POST, user)
        form2 = TableEventForm(request2.POST, user2)

        if form.is_valid():
            form.save()
        if form2.is_valid():
            form2.save()

        tableInUser01 = TableEventModel.objects.filter(user=user).values()
        tableInUser02 = TableEventModel.objects.filter(user=user2).values()
        self.assertNotEqual(tableInUser01, tableInUser02)