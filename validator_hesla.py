class ValidatorHesla:
    @staticmethod
    def je_validni(heslo):
        # podmínka: délka musí být větší než 5
        if len(heslo) <= 5:
            return False
        for char in heslo:
            if '0' <= char <= '9':      # musí obsahovat aspoň jednu číslici
                return True
        return False                    # return musí byt mimo loop

        # Příklad použití:

if __name__ == "__main__":
    print(ValidatorHesla.je_validni("abc"))      # False (krátké)
    print(ValidatorHesla.je_validni("abcdef"))   # False (bez čísla)
    print(ValidatorHesla.je_validni("abc123"))   # True
    print(ValidatorHesla.je_validni("123456"))   # True



# nebo bez statické metody
"""    def validuj(self, heslo):
        if len(heslo) <= 5:
            return False
        for char in heslo:
            if '0' <= char <= '9': 
                return True
            return False """


