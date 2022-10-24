class SetupBodyOrgans():

    def __init__(self, IDSetupBodyOrgans, IDSetupSystems, SetupSystems, BodyOrgans, Left, Right, Men, Womman, RangeMax, RangeMin, Lenguage, importance_level) -> None:
        self.IDSetupBodyOrgans = IDSetupBodyOrgans
        self.IDSetupSystems = IDSetupSystems
        self.SetupSystems = SetupSystems
        self.BodyOrgans = BodyOrgans
        self.Left = Left
        self.Right = Right
        self.Men = Men
        self.Womman = Womman
        self.RangeMax = RangeMax
        self.RangeMin = RangeMin
        self.Lenguage = Lenguage
        self.importance_level = importance_level


    def to_JSON(self):
        return {
            'id': self.IDSetupBodyOrgans,
            'IDSetupSystems': self.IDSetupSystems,
            'SetupSystems': self.SetupSystems,
            'BodyOrgans': self.BodyOrgans,
            'Left': self.Left,
            'Right': self.Right,
            'Men': self.Men,
            'Womman': self.Womman,
            'RangeMax': self.RangeMax,
            'RangeMin': self.RangeMin,
            'Lenguage': self.Lenguage,
            'importance_level': self.importance_level,
        }