class SetupSymptoms():

    def __init__(self, IDSetupSymptoms, IDSetupBodyOrgans, Symptoms, RangeMax, RangeMin, Lenguage) -> None:
        self.IDSetupSymptoms = IDSetupSymptoms
        self.IDSetupBodyOrgans = IDSetupBodyOrgans
        self.Symptoms = Symptoms
        self.RangeMax = RangeMax
        self.RangeMin = RangeMin
        self.Lenguage = Lenguage


    def to_JSON(self):
        return {
            'IDSetupSymptoms': self.IDSetupSymptoms,
            'IDSetupBodyOrgans': self.IDSetupBodyOrgans,
            'Symptoms': self.Symptoms,
            'RangeMax': self.RangeMax,
            'RangeMin': self.RangeMin,
            'Lenguage': self.Lenguage,
        }