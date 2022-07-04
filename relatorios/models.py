
from datetime import timezone
from secrets import choice
from django.db import models
from .choices_coordenacao import LISTA_COORDENACAO
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    sector_name = models.CharField(max_length=100, choices=LISTA_COORDENACAO)

    def __str__(self):
        return f'{self.sector_name}'

class TableActionModel(models.Model):
    ACAO_REALIZADA_CHOICE = (
        ('Apoio Técnico Presencial (ATP)', 'Apoio Técnico Presencial (ATP)'),
        ('Apoio Técnico Não Presencial (ATNP)', 'Apoio Técnico Não Presencial (ATNP)'),
        ('Outras Ações', 'Outras Ações'),
    )

    TECNICO_PRESENCIAL_CHOICE = (
        ('Encontros de apoio técnico', 'Encontros de apoio técnico'),
        ('Apoio técnico individualizado no município', 'Apoio técnico individualizado no município'),
        ('Apoio técnico individualizado na SAAS', 'Apoio técnico individualizado na SAAS'),
        ('Monitoramento com periodicidade mínima anual', 'Monitoramento com periodicidade mínima anual'),
        ('Seminários e/ou Oficinas', 'Seminários e/ou Oficinas'),
        ('Visitas técnicas', 'Visitas técnicas'),
        ('(Não se aplica)', '(Não se aplica)'),
    )

    TECNICO_NAO_PRESENCIAL_CHOICE = (
        ('Centrais de relacionamento', 'Centrais de relacionamento'),
        ('E-mails, telefonemas e mensagens', 'E-mails, telefonemas e mensagens'),
        ('Normas, orientações técnicas e materiais informativos', 'Normas, orientações técnicas e materiais informativos'),
        ('Videoconferências e transmissões ao vivo', 'Videoconferências e transmissões ao vivo'),
        ('Instrumentos e ferramentas informacionais do SUAS', 'Instrumentos e ferramentas informacionais do SUAS'),
        ('Sítios eletrônicos e aplicativos', 'Sítios eletrônicos e aplicativos'),
        ('(Não se Aplica)', '(Não se Aplica)')
    )

    OUTRAS_ACOES_CHOICE = (
        ('Apuração de denúncias', 'Apuração de denúncias'),
        ('Fiscalizações e auditorias', 'Fiscalizações e auditorias'),
        ('Plano de Providências', 'Plano de Providências'),
        ('Capacitação', 'Capacitação'),
        ('Supervisão Técnica', 'Supervisão Técnica'),
        ('Formação', 'Formação'),
        ('Manifestação Técnica', 'Manifestação Técnica'),
        ('Audiência Pública','Audiência Pública'),
        ('(Não se aplica)', '(Não se aplica)'),
        ('Outros', 'Outros'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tabelaAcoes')
    acao_realizada = models.CharField(max_length=100, choices= ACAO_REALIZADA_CHOICE, default= 'Apoio Técnico Presencial (ATP)')
    tecnico_presencial = models.CharField(max_length=100, choices=TECNICO_PRESENCIAL_CHOICE)
    tecnico_nao_presencial = models.CharField(max_length=100, choices=TECNICO_NAO_PRESENCIAL_CHOICE)
    outras_acoes = models.CharField(max_length=100, choices=OUTRAS_ACOES_CHOICE)
    numbers_employee = models.IntegerField('Numero de Funcionario',blank=False, null=False)
    description_action = models.TextField('Descrição da Ação', max_length=100, blank=False, null=False)
    date_actions = models.DateField('Data', blank=False, null=False)
    date_to_publication = models.DateField('Data da Publicação', default=timezone.now)

    def __str__(self):
        return self.user.first_name

class TableEventModel(models.Model):

    EVENT_FEATURES_CHOICE = (
        ('Presencial', 'Presencial'),
        ('Híbrida', 'Híbrida'),
        ('Não Presencial', 'Não Presencial')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tabelaEventos')
    title_event = models.TextField('Titulo', max_length=150)
    event_feature = models.CharField(max_length=50, choices=EVENT_FEATURES_CHOICE, default='Híbrida')
    date_initial = models.DateField('Data Inicial')
    date_final = models.DateField('Data Final')
    date_to_publication = models.DateField('Data da Publicação', default=timezone.now)

