class Product:
    interest_rate = 0
    disqualified = False

    def __init__(self, name , interest_rate ):
        self.name = name
        self.interest_rate = interest_rate