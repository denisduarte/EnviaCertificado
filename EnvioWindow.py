
import pyforms
from   pyforms          import BaseWidget
from   pyforms.controls import ControlText
from   pyforms.controls import ControlButton
from   pyforms.controls import ControlFile
from   pyforms.controls import ControlEmptyWidget
from   pyforms.controls import ControlCheckBox

from ConfigSMTPWindow import ConfigSMTPWindow
from ConfigEmailWindow import ConfigEmailWindow
from ListaEnvios import ListaEnvios
from Enviador import Enviador


class EnvioWindow(BaseWidget):

    def __init__(self):
        super(EnvioWindow, self).__init__('Envio de certificados')

        #Definition of the forms fields

        self._nomeEvento = ControlText('Nome do evento', 'Default value')

        self._gerarParticipacao = ControlCheckBox('Gerar certificados de participação')
        self._gerarOrganizacao = ControlCheckBox('Gerar certificados de organização')




        self._templateParticipacao = ControlFile('Modelo do certificado de participação')
        self._csvParticipacao      = ControlFile('Relação de participantes')
        self._templateOrganizacao      = ControlFile('Modelo do certificado de organização')
        self._csvOrganizacao      = ControlFile('Relação de organizadores')
        self._btGerar       = ControlButton('Gerar certificados')

        self._painelEnvios = ControlEmptyWidget()

        self.formset = ['_nomeEvento', ('_gerarParticipacao', '_gerarOrganizacao'), ('_templateParticipacao', '_csvParticipacao'), ('_templateOrganizacao', '_csvOrganizacao'), ' ', '_btGerar', '_painelEnvios']

        self._templateParticipacao.hide()
        self._csvParticipacao.hide()
        self._templateOrganizacao.hide()
        self._csvOrganizacao.hide()

        # Define the button action
        self._btGerar.value = self.__btGerarAction
        self._gerarParticipacao.changed_event = self.__gerarParticipacao_changed_event
        self._gerarOrganizacao.changed_event = self.__gerarOrganizacao_changed_event

        self.mainmenu = [
            { 'Editar': [
                    {'SMTP': self.__configSmtpEvent},
                    {'E-mail': self.__configEmailEvent}
                ]
            }
        ]

    def __btGerarAction(self):
        winEnvios = ListaEnvios()
        winEnvios.parent = self
        self._painelEnvios.value = winEnvios

        enviador = Enviador()

        if self._gerarParticipacao.value:
            enviador.geraCertificados(self._painelEnvios, 'Participação', self._nomeEvento.value, self._templateParticipacao.value, self._csvParticipacao.value)

        if self._gerarOrganizacao.value:
            enviador.geraCertificados(self._painelEnvios, 'Organização', self._nomeEvento.value, self._templateOrganizacao.value, self._csvOrganizacao.value)


    def __gerarParticipacao_changed_event(self):
        if self._gerarParticipacao.value:
            self._templateParticipacao.show()
            self._csvParticipacao.show()
        else:
            self._templateParticipacao.hide()
            self._csvParticipacao.hide()

    def __gerarOrganizacao_changed_event(self):
        if self._gerarOrganizacao.value:
            self._templateOrganizacao.show()
            self._csvOrganizacao.show()
        else:
            self._templateOrganizacao.hide()
            self._csvOrganizacao.hide()

    def __configSmtpEvent(self):
        win = ConfigSMTPWindow()
        win.parent = self
        win.show()

    def __configEmailEvent(self):
        win = ConfigEmailWindow()
        win.parent = self
        win.show()



if __name__ == "__main__":
    pyforms.start_app(EnvioWindow, geometry=(300, 150, 400, 500))