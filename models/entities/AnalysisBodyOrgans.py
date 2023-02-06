class AnalysisBodyOrgans():
    def __init__(self, ID, IdAnalysis=None, Sistems=None, bodyorgans=None, bodyorgansvalue=None, findings=None, symptoms=None, Comments=None, Left=None, Right=None, ValueLeft=None, ValueRight=None) -> None:
        self.ID = ID
        self.IdAnalysis = IdAnalysis
        self.Sistems = Sistems
        self.bodyorgans = bodyorgans
        self.bodyorgansvalue = bodyorgansvalue
        self.findings = findings
        self.symptoms = symptoms
        self.Comments = Comments
        self.Left = Left
        self.Right = Right
        self.ValueLeft = ValueLeft
        self.ValueRight = ValueRight

    def to_JSON(self):
        return {
            'id': self.ID,
            'IdAnalysis': self.IdAnalysis,
            'Sistems': self.Sistems,
            'bodyorgans': self.bodyorgans,
            'bodyorgansvalue': self.bodyorgansvalue,
            'findings': self.findings,
            'symptoms': self.symptoms,
            'Comments': self.Comments,
            'Left': self.Left,
            'Right': self.Right,
            'ValueLeft': self.ValueLeft,
            'ValueRight': self.ValueRight,
        }