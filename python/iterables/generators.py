class Bank:
    crisis = False

    def create_atm(self):
        while not self.crisis:
            yield '$100'

hsbc = Bank()
corner_street_atm = hsbc.create_atm()
