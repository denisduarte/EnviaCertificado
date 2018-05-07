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
from   pyforms.controls import ControlTextArea



email_config_file = 'email.ini'
parser = configparser.ConfigParser()

if not os.path.exists(email_config_file):
    parser['EMAIL'] = {'emitenteNome': '', 'emitenteEmail': '', 'assunto': '', 'mensagem': ''}

    parser.write(open(email_config_file, 'w'))

parser.read(email_config_file)


class ConfigEmailWindow(BaseWidget):

    def __init__(self):
        super(ConfigEmailWindow, self).__init__('Con de SMTP')

        # Definition of the forms fields
        self._emitenteNome = ControlText('Nome do emitente', 'Default value')
        self._emitenteEmail = ControlText('E-mail do emitente')
        self._assunto = ControlText('Assunto do email')
        self._mensagem = ControlTextArea('Mensagem do email')

        self._btSalvar = ControlButton('Gravar configurações')

        self._emitenteNome.value = parser['EMAIL']['emitenteNome']
        self._emitenteEmail.value = parser['EMAIL']['emitenteEmail']
        self._assunto.value = parser['EMAIL']['assunto']
        self._mensagem.value = parser['EMAIL']['mensagem']


        self._btSalvar.value = self.__btSalvarAction

        # self.formset = [('_servidor', '_porta'), ('_usuario', '_senha'), ('_btTestar', '_imgSinal'), ' ', '_btSalvar']

    def __btSalvarAction(self):
        parser['EMAIL']['EmitenteNome'] = self._emitenteNome.value
        parser['EMAIL']['emitenteEmail'] = self._emitenteEmail.value
        parser['EMAIL']['assunto'] = self._assunto.value
        parser['EMAIL']['mensagem'] = self._mensagem.value

        with open(email_config_file, 'w') as configfile:
            parser.write(configfile)

        self.close()


if __name__ == "__main__":
    pyforms.start_app(ConfigEmailWindow, geometry=(300, 150, 400, 500))