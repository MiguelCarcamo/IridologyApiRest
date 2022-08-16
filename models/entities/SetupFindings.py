class SetupFindings():

    def __init__(self, IDSetupFindings, IDSetupBodyOrgans, SetupBodyOrgans, Foods, NotFoods, Findings, RangeMax, RangeMin, Lenguage) -> None:
        self.IDSetupFindings = IDSetupFindings
        self.IDSetupBodyOrgans = IDSetupBodyOrgans
        self.SetupBodyOrgans = SetupBodyOrgans
        self.Foods = Foods
        self.NotFoods = NotFoods
        self.Findings = Findings
        self.RangeMax = RangeMax
        self.RangeMin = RangeMin
        self.Lenguage = Lenguage

    def to_JSON(self):
        return {
            'id': self.IDSetupFindings,
            'IDSetupBodyOrgans': self.IDSetupBodyOrgans,
            'SetupBodyOrgans': self.SetupBodyOrgans,
            'Foods': self.Foods,
            'NotFoods': self.NotFoods,
            'Findings': self.Findings,
            'RangeMax': self.RangeMax,
            'RangeMin': self.RangeMin,
            'Lenguage': self.Lenguage,
        }