from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView

class IndexView(TemplateView):
    template_name = 'index.html'

class DadosJSONView(BaseLineChartView):

    def get_labels(self):
        """LABELS"""
        labels = [
            "Janeiro",
            "Fevereiro",
            "Março",
            "Abril",
            "Maio",
            "Junho",
            "Julho",
            "Agosto",
            "Setembro",
            "Outubro",
            "Novembro",
            "Dezembro"
        ]
        return labels

    def get_providers(self):
        """NOMES DOS DATASETS"""
        dataset = [
            "curso 01",
            "curso 02",
            "curso 03",
            "curso 04",
            "curso 05",
            "curso 06"
        ]
        return dataset

    def get_data(self):
        """QUANTIDADE DE DADOS IGUAL A AOS DATASETS / LABELS"""
        dados = []
        for l in range(6):
            for c in range(12):
                dado = [
                    randint(1, 100), #JAN
                    randint(1, 100), #FEV
                    randint(1, 100), #MAR
                    randint(1, 100), #ABR
                    randint(1, 100), #MAI
                    randint(1, 100), #JUN
                    randint(1, 100), #JUL
                    randint(1, 100), #AGO
                    randint(1, 100), #SET
                    randint(1, 100), #OUT
                    randint(1, 100), #NOV
                    randint(1, 100)  #DEZ
                ]
            dados.append(dado)
        return dados
