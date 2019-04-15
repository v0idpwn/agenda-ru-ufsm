# Imports
import requests
from datetime import datetime, timedelta

# Configs
matricula = "matricula"
senha = "senha"
RU = 2
refeicoes= ["café", "almoço", "jantar"]
modo = "semanal"
date = datetime.today()

# Os restaurantes tem ids internos
RU_1 = 1
RU_2 = 41
RU_SELECTED = RU_1 if RU == 1 else RU_2

# Faz login no portal, retorna a sessão obtida
def login(matricula, senha):
    target = "https://portal.ufsm.br/ru/j_security_check"
    login_data = {'j_username': matricula, 'j_password': senha}
    sessao = requests.session()
    sessao.post(target, login_data)
    return sessao


# Recebe os dados de um agendamento e o faz
def agenda(sessao, refeicao, ru, inicio, fim):
    inicio = inicio.strftime("%d/%m/%Y")
    fim = fim.strftime("%d/%m/%Y")

    target = "https://portal.ufsm.br/ru/usuario/agendamento/form.html"
    dados = {'periodo.fim': fim, 'periodo.inicio': inicio, 'restaurante': ru, 'tiposRefeicao': refeicao}
    r = sessao.post(target, dados)
    return sessao


# Fazendo login
s = login(matricula, senha)

# Adquirindo datas para modo
if(modo == "semanal"):
    inicio = date + timedelta(days=1)
    fim = date + timedelta(days=6)
else:
    inicio = date + timedelta(days=1)
    fim = date + timedelta(days=1)

# Fazendo as requisições
if "café" in refeicoes:
    agenda(s, 1, RU_1, inicio, fim)
if "almoço" in refeicoes:
    agenda(s, 2, RU_SELECTED, inicio, fim)
if "jantar" in refeicoes:
    agenda(s, 3, RU_1, inicio, fim)
