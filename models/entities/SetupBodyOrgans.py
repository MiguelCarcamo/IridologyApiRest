class SetupBodyOrgans():

    def __init__(self, IDSetupBodyOrgans, IDSetupSystems, BodyOrgans, Left, Right, Men, Womman, RangeMax, RangeMin, Lenguage) -> None:
        self.IDSetupBodyOrgans = IDSetupBodyOrgans
        self.IDSetupSystems = IDSetupSystems
        self.BodyOrgans = BodyOrgans
        self.Left = Left
        self.Right = Right
        self.Men = Men
        self.Womman = Womman
        self.RangeMax = RangeMax
        self.RangeMin = RangeMin
        self.Lenguage = Lenguage


    def to_JSON(self):
        return {
            'IDSetupBodyOrgans': self.IDSetupBodyOrgans,
            'IDSetupSystems': self.IDSetupSystems,
            'BodyOrgans': self.BodyOrgans,
            'Left': self.Left,
            'Right': self.Right,
            'Men': self.Men,
            'Womman': self.Womman,
            'RangeMax': self.RangeMax,
            'RangeMin': self.RangeMin,
            'Lenguage': self.Lenguage,
        }