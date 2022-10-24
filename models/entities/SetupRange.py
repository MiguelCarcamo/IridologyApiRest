class SetupRange():

    def __init__(self, idsetuprange, setuprange, rangemax, rangemin) -> None:
        self.idsetuprange = idsetuprange
        self.setuprange = setuprange
        self.rangemax = rangemax
        self.rangemin = rangemin


    def to_JSON(self):
        return {
            'id': self.idsetuprange,
            'setupsystems': self.setuprange,
            'rangemax': self.rangemax,
            'rangemin': self.rangemin,
        }