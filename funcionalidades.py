
def desligar1():
    """
    Desliga o Computador controlando o mouse e clicando no botão para desligar.
    Precisa das posições de x e y de onde estão os botões na tela.
    """
    from pyautogui import click
    from pyautogui import press
    from time import sleep

    press('win')
    sleep(1)
    click(x=1204, y=983)
    sleep(1)
    click(x=1201, y=904)
    click(x=1201, y=904)


def desligar2():
    """
    Desliga o computador através do cmd.
    """
    import os

    os.system('shutdown -s')
