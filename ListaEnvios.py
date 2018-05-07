import pyforms
from pyforms                import BaseWidget
from pyforms.controls       import ControlList
from Envio                 import Envio


class ListaEnvios(BaseWidget):
    """
    This applications is a GUI implementation of the People class
    """

    def __init__(self):
        BaseWidget.__init__(self,'People window')

        #Definition of the forms fields
        self._listaEnvios    = ControlList('Certificados',
            plusFunction    = self.__addEnvioBtnAction,
            minusFunction   = self.__rmEnvioBtnAction)

        self._listaEnvios.horizontal_headers = ['Nome', 'E-mail', 'Situação', 'Tipo', 'Arquivo']
        self._listaEnvios.autoscroll = True
        self._listaEnvios.readonly = True

    def addEnvio(self, envio):
        """
        Reimplement the addPerson function from People class to update the GUI
        everytime a new person is added.
        """
        self._listaEnvios += [envio._nome, envio._email, envio._situacao, envio._tipo, envio._arquivo]

    def updateLista(self):
        self._listaEnvios.tableWidget.model().dataChanged.connect(self._listaEnvios)

    def removePerson(self, index):
        """
        Reimplement the removePerson function from People class to update the GUI
        everytime a person is removed.
        """
        super(ListaEnvios, self).removeEnvio(index)
        self._listaEnvios -= index

    def __addEnvioBtnAction(self):
        """
        Add person button event.
        """
        # A new instance of the PersonWindow is opened and shown to the user.
        win = EnvioWindow()
        win.parent = self
        win.show()

    def __rmEnvioBtnAction(self):
        """
        Remove person button event
        """
        self.removeEnvio( self._listaEnvios.selected_row_index )

#Execute the application
if __name__ == "__main__":   pyforms.start_app( ListaEnvios )