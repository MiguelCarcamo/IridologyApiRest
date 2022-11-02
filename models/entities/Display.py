class Display():
    def __init__(self, id2, namedisplay, navigate, icon, access)->None:
        self.id2 = id2
        self.namedisplay = namedisplay
        self.navigate = navigate
        self.icon = icon
        self.access = access
    
    def to_JSON(self):
        return {
            'id': self.id2,
            'namedisplay': self.namedisplay,
            'navigate': self.navigate,
            'icon': self.icon,
            'access': self.access,
        }