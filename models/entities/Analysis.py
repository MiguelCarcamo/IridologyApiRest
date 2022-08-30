class Analysis():

    def __init__(self, IDAnalysis, IDPatient=None, IDDoctor=None, Status=None, URLLeft=None, URLRight=None, CreateDate=None, FinishDate=None) -> None:
        self.IDAnalysis = IDAnalysis
        self.IDPatient = IDPatient
        self.IDDoctor = IDDoctor
        self.URLLeft = URLLeft
        self.URLRight = URLRight
        self.Status = Status
        self.CreateDate = CreateDate
        self.FinishDate = FinishDate

    def to_JSON(self):
        return {
            'id': self.IDAnalysis,
            'IDPatient': self.IDPatient,
            'IDDoctor': self.IDDoctor,
            'CreateDate': self.CreateDate,
            'FinishDate': self.FinishDate,
            'IDDoctor': self.IDDoctor,
            'Status': self.Status,
            'URLLeft': self.URLLeft,
            'URLRight': self.URLRight
        }