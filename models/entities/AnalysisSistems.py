class AnalysisSistems():

    def __init__(self, ID, IdAnalysis=None, Sistems=None, Value=None, Comments=None, Value_l=None, Value_r=None) -> None:
        self.ID = ID
        self.IdAnalysis = IdAnalysis
        self.Sistems = Sistems
        self.Value = Value
        self.Comments = Comments
        self.Value_l = Value_l
        self.Value_r = Value_r

    def to_JSON(self):
        return {
            'id': self.ID,
            'IdAnalysis': self.IdAnalysis,
            'Sistems': self.Sistems,
            'Value': self.Value,
            'Comments': self.Comments,
            'Value_l': self.Value_l,
            'Value_r': self.Value_r,
        }