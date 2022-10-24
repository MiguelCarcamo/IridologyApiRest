class SetupSystems():

    def __init__(self, idsetupsystems, setupsystems, rangemax, rangemin, lenguage, importance_level) -> None:
        self.idsetupsystems = idsetupsystems
        self.setupsystems = setupsystems
        self.rangemax = rangemax
        self.rangemin = rangemin
        self.lenguage = lenguage
        self.importance_level = importance_level


    def to_JSON(self):
        return {
            'id': self.idsetupsystems,
            'setupsystems': self.setupsystems,
            'rangemax': self.rangemax,
            'rangemin': self.rangemin,
            'lenguage': self.lenguage,
            'importance_level': self.importance_level,
        }