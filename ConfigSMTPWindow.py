#!/usr/bin/python

from pyforms.utils.settings_manager import conf;
import settings
conf+=settings

import configparser
import smtplib

import os.path

import pyforms
from   pyforms          import BaseWidget
from   pyforms.controls import ControlText
from   pyforms.controls import ControlButton
from   pyforms.controls import ControlImage



smtp_config_file = 'smtp.ini'
parser = configparser.ConfigParser()

if not os.path.exists(smtp_config_file):
    parser['SMTP'] = {'servidor': '', 'porta': '', 'usuario': '', 'senha': ''}

    parser.write(open(smtp_config_file, 'w'))

parser.read(smtp_config_file)


class ConfigSMTPWindow(BaseWidget):

    def __init__(self):
        super(ConfigSMTPWindow, self).__init__('Con de SMTP')

        # Definition of the forms fields
        self._servidor = ControlText('Servidor', 'Default value')
        self._porta = ControlText('Porta')
        self._usuario = ControlText('Usuário')
        self._senha = ControlText('Senha')
        self._btTestar = ControlButton('Testar SMTP')
        self._imgSinal = ControlImage('Image')

        self._btSalvar = ControlButton('Gravar configurações')

        self._servidor.value = parser['SMTP']['servidor']
        self._porta.value = parser['SMTP']['porta']
        self._usuario.value = parser['SMTP']['usuario']
        self._senha.value = parser['SMTP']['senha']

        self._imgSinal.value = 'imagens/grayLight.png'

        # Define the button action
        self._btTestar.value = self.__btTestarAction
        self._btSalvar.value = self.__btSalvarAction

        # self.formset = [('_servidor', '_porta'), ('_usuario', '_senha'), ('_btTestar', '_imgSinal'), ' ', '_btSalvar']

    def __btTestarAction(self):

        try:
            conn = smtplib.SMTP_SSL(self._servidor.value, self._porta.value)
            conn.login(self._usuario.value, self._senha.value)
            conn.close()
            self._imgSinal.value = 'imagens/greenLight.png'
            print("Conexao ativa")
        except:  # smtplib.SMTPServerDisconnected
            self._imgSinal.value = 'imagens/redLight.png'
            print("Conexao inativa")

    def __btSalvarAction(self):
        parser['SMTP']['servidor'] = self._servidor.value
        parser['SMTP']['porta'] = self._porta.value
        parser['SMTP']['usuario'] = self._usuario.value
        parser['SMTP']['senha'] = self._senha.value

        with open(smtp_config_file, 'w') as configfile:
            parser.write(configfile)

        self.close()


if __name__ == "__main__":
    pyforms.start_app(ConfigSMTPWindow, geometry=(300, 150, 400, 500))