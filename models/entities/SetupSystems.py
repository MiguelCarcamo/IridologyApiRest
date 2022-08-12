class SetupSystems():

    def __init__(self, idsetupsystems, setupsystems, rangemax, rangemin, lenguage) -> None:
        self.idsetupsystems = idsetupsystems
        self.setupsystems = setupsystems
        self.rangemax = rangemax
        self.rangemin = rangemin
        self.lenguage = lenguage


    def to_JSON(self):
        return {
            'id': self.idsetupsystems,
            'setupsystems': self.setupsystems,
            'rangemax': self.rangemax,
            'rangemin': self.rangemin,
            'lenguage': self.lenguage,
        }