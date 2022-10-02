class AnalysisSistems():

    def __init__(self, ID, IdAnalysis=None, Sistems=None, Value=None, Comments=None) -> None:
        self.ID = ID
        self.IdAnalysis = IdAnalysis
        self.Sistems = Sistems
        self.Value = Value
        self.Comments = Comments

    def to_JSON(self):
        return {
            'id': self.ID,
            'IdAnalysis': self.IdAnalysis,
            'Sistems': self.Sistems,
            'Value': self.Value,
            'Comments': self.Comments,
        }