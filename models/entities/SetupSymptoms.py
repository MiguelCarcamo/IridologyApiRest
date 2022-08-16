class SetupSymptoms():

    def __init__(self, IDSetupSymptoms, IDSetupBodyOrgans, SetupBodyOrgans, Symptoms, RangeMax, RangeMin, Lenguage) -> None:
        self.IDSetupSymptoms = IDSetupSymptoms
        self.IDSetupBodyOrgans = IDSetupBodyOrgans
        self.SetupBodyOrgans = SetupBodyOrgans
        self.Symptoms = Symptoms
        self.RangeMax = RangeMax
        self.RangeMin = RangeMin
        self.Lenguage = Lenguage


    def to_JSON(self):
        return {
            'id': self.IDSetupSymptoms,
            'IDSetupBodyOrgans': self.IDSetupBodyOrgans,
            'SetupBodyOrgans': self.SetupBodyOrgans,
            'Symptoms': self.Symptoms,
            'RangeMax': self.RangeMax,
            'RangeMin': self.RangeMin,
            'Lenguage': self.Lenguage,
        }