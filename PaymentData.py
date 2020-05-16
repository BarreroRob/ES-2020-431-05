class PaymentData:

    def __init__(self, tipus, titular):

        if tipus == "VISA" or "Mastercard":
            self.tipusTargeta = tipus
        else:
            print("Tipus de targeta no vàlid.")

        self.nomTitular = titular

        def _init_Datos(numero, codi, total):
            self.numeroTarjeta = numero
            self.codiSeguretat = codi
            self.importTotal = total
        pass

