class Professeur:
    _ppr = 0
    _grade = ""
    list_Modules = []
    def __init__(self, ppr, grade):
        self._ppr = ppr
        self._grade = grade
        self.list_Modules = []
    def get_ppr(self):
        return self._ppr
    def set_ppr(self, ppr):
        self._ppr = ppr
    def get_grade(self):
        return self._grade
    def set_grade(self, grade):
        self._grade = grade
    def set_list_Modules(self, list_Modules):
        self._list_Modules = list_Modules
    def get_list_Modules(self):
        return self._list_Modules
class Module:
    _nom = ""
    _volumehoraire = 0
    _semestre = ""
    Professeur
    def __init__(self, nom, volumehoraire, semestre):
        self._nom = nom
        self._volumehoraire = volumehoraire
        self._semestre = semestre
    def get_nom(self):
        return self._nom
    def set_nom(self, nom):
        self._nom = nom
    def get_volumehoraire(self):
        return self._volumehoraire
    def set_volumehora(self, volumehoraire):
        self._volumehoraire = volumehoraire
    def get_semestre(self):
        return self._semestre
    def set_semestre(self, semestre):
        self._semestre = semestre