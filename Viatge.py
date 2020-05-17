class Viatge:

    def __init__(self, idViatg, idCli, dataIni, dataFi):
        self.idViatge = idViatg
        self.idClient = idCli
        self.dataIni = dataIni
        self.dataFi = dataFi
        self.reserves = []

    def addReserva(self, reserv):
        self.reserves.append(reserv)
        return True