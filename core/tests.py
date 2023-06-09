from django.test import TestCase
from django.urls import reverse
from .models import Professor, Presenca
from .forms import CadastroPresencaForm


class PresencaTests(TestCase):
    def setUp(self):
        self.professor = Professor.objects.create(nome='Orlando')
        self.presenca = Presenca.objects.create(nome_aluno='João', nome_professor=self.professor)

    def test_criar_presenca(self):
        presenca = Presenca.objects.get(nome_aluno='João')
        self.assertEqual(presenca.nome_aluno, 'João')
        self.assertEqual(presenca.nome_professor, self.professor)

    def test_listar_presenca(self):
        response = self.client.get(reverse('listar_presenca'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'João')
        self.assertContains(response, 'Orlando')

    def test_form_valid(self):
        form_data = {'nome_aluno': 'Maria', 'nome_professor': self.professor.id}
        form = CadastroPresencaForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        form_data = {'nome_aluno': '', 'nome_professor': self.professor.id}
        form = CadastroPresencaForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_cadastrar_presenca(self):
        form_data = {'nome_aluno': 'Carlos', 'nome_professor': self.professor.id}
        response = self.client.post(reverse('cadastrar_presenca'), data=form_data)
        self.assertEqual(response.status_code, 200)
        #self.assertContains(response, 'Presença cadastrada com sucesso.')
        self.assertTrue(Presenca.objects.filter(nome_aluno='Carlos').exists())
        #print(response.content)


