class Envio(object):

    def __init__(self, nome, email, situacao, tipo, arquivo):
        self._nome = nome
        self._email = email
        self._situacao = situacao
        self._tipo = tipo
        self._arquivo = arquivo


    @property
    def statusEnvio(self):
        return "{0} {1} {2}".format(self._nome, self._email, self._situacao)