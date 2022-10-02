class AnalysisBodyOrgans():
    def __init__(self, ID, IdAnalysis=None, Sistems=None, bodyorgans=None, bodyorgansvalue=None, foods=None, notfoods=None, findings=None, symptoms=None, Comments=None) -> None:
        self.ID = ID
        self.IdAnalysis = IdAnalysis
        self.Sistems = Sistems
        self.bodyorgans = bodyorgans
        self.bodyorgansvalue = bodyorgansvalue
        self.foods = foods
        self.notfoods = notfoods
        self.findings = findings
        self.symptoms = symptoms
        self.Comments = Comments

    def to_JSON(self):
        return {
            'id': self.ID,
            'IdAnalysis': self.IdAnalysis,
            'Sistems': self.Sistems,
            'bodyorgans': self.bodyorgans,
            'bodyorgansvalue': self.bodyorgansvalue,
            'foods': self.foods,
            'notfoods': self.notfoods,
            'findings': self.findings,
            'symptoms': self.symptoms,
            'Comments': self.Comments,
        }