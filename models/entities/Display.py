class Display():
    def __init__(self, id2, namedisplay, navigate, icon, access, Seccion)->None:
        self.id2 = id2
        self.namedisplay = namedisplay
        self.navigate = navigate
        self.icon = icon
        self.access = access
        self.Seccion = Seccion
    
    def to_JSON(self):
        return {
            'id': self.id2,
            'namedisplay': self.namedisplay,
            'navigate': self.navigate,
            'icon': self.icon,
            'access': self.access,
            'Seccion': self.Seccion,
        }