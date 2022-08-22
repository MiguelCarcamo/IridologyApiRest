class AnalysisPatient():

    def __init__(self, IDPatient, IDUser=None, PatientName=None, PatientLastName=None, Lenguage=None, BirthDate=None, Gender=None, Weight=None) -> None:
        self.IDPatient = IDPatient
        self.IDUser = IDUser
        self.PatientName = PatientName
        self.PatientLastName = PatientLastName
        self.Lenguage = Lenguage
        self.BirthDate = BirthDate
        self.Gender = Gender
        self.Weight = Weight

    def to_JSON(self):
        return {
            'id': self.IDPatient,
            'IDUser': self.IDUser,
            'PatientName': self.PatientName,
            'PatientLastName': self.PatientLastName,
            'Lenguage': self.Lenguage,
            'BirthDate': self.BirthDate,
            'Gender': self.Gender,
            'Weight': self.Weight,
        }