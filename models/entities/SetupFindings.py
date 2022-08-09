class SetupFindings():

    def __init__(self, IDSetupFindings, IDSetupBodyOrgans, Foods, NotFoods, Findings, RangeMax, RangeMin, Lenguage) -> None:
        self.IDSetupFindings = IDSetupFindings
        self.IDSetupBodyOrgans = IDSetupBodyOrgans
        self.Foods = Foods
        self.NotFoods = NotFoods
        self.Findings = Findings
        self.RangeMax = RangeMax
        self.RangeMin = RangeMin
        self.Lenguage = Lenguage

    def to_JSON(self):
        return {
            'IDSetupFindings': self.IDSetupFindings,
            'IDSetupBodyOrgans': self.IDSetupBodyOrgans,
            'Foods': self.Foods,
            'NotFoods': self.NotFoods,
            'Findings': self.Findings,
            'RangeMax': self.RangeMax,
            'RangeMin': self.RangeMin,
            'Lenguage': self.Lenguage,
        }