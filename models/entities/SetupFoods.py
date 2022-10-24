class SetupFoods():

    def __init__(self, IDSetupFoods, idsetupsystems, SetupSystems, Foods, NotFoods, RangeMax, RangeMin, Lenguage) -> None:
        self.IDSetupFoods = IDSetupFoods
        self.idsetupsystems = idsetupsystems
        self.SetupSystems = SetupSystems
        self.Foods = Foods
        self.NotFoods = NotFoods
        self.RangeMax = RangeMax
        self.RangeMin = RangeMin
        self.Lenguage = Lenguage

    def to_JSON(self):
        return {
            'id': self.IDSetupFoods,
            'IDSetupBodyOrgans': self.idsetupsystems,
            'SetupSystems': self.SetupSystems,
            'Foods': self.Foods,
            'NotFoods': self.NotFoods,
            'RangeMax': self.RangeMax,
            'RangeMin': self.RangeMin,
            'Lenguage': self.Lenguage,
        }