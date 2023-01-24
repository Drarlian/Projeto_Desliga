"""
Programa para desligar o computador depois de X horas/minutos/segundos.
"""

import datetime
from time import sleep
from funcionalidades import desligar1, desligar2

if __name__ == '__main__':
    modo = str(input('Digite a opção de desligamento: (1 ou 2) '))

    print('(s) = segundo | (m) = minuto | (h) = hora')
    escolha = str(input('Escolha a unidade de tempo para o contador: (s) | (m) | (h) '))

    if escolha.lower() == 's':
        segundos = int(input('Digite os segundos para desligar: '))

        sleep(segundos)

        if modo == '1':
            desligar1()
        else:
            desligar2()

    elif escolha.lower() == 'm':
        minutos = int(input('Digite os minutos para desligar: '))

        sleep(minutos * 60)

        if modo == '1':
            desligar1()
        else:
            desligar2()

        # FORMA DE DESLIGAR USANDO O MÓDULO DATETIME:
        """
        hora_agora = datetime.datetime.now()
        tempo_somado = datetime.timedelta(minutes=minutos)
        hora_final = hora_agora + tempo_somado

        while True:
            if (datetime.datetime.now().minute == hora_final.minute) and (datetime.datetime.now().second == hora_final.second):
                if modo == '1':
                    desligar1()
                else:
                    desligar2()
                break
        """

    elif escolha.lower() == 'h':
        horas = int(input('Digite a quantidade de horas para desligar: '))

        sleep(horas * 3600)

        if modo == '1':
            desligar1()
        else:
            desligar2()

        # FORMA DE DESLIGAR USANDO O MÓDULO DATETIME:
        """
        hora_agora = datetime.datetime.now()
        tempo_somado = datetime.timedelta(hours=horas)
        hora_final = hora_agora + tempo_somado

        while True:
            if (datetime.datetime.now().hour == hora_final.hour) and (datetime.datetime.now().minute == hora_final.minute):
                if modo == '1':
                    desligar1()
                else:
                    desligar2()
                break
        """
