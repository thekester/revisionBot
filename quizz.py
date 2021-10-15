class Matiere:
    def __init__(self):
        self.algo_quizz=[]
        self.anglais_quizz=[]
        self.archi_quizz=[]
        self.bdd_quizz=[]
        self.methode_quizz=[]
        self.prog_quizz=[]
        self.spec_quizz=[]
        self.sysInfo_quizz=[]
        self.sysReseau_quizz=["C'est quoi un système d'exploitation?","Quels sont les différentes couches d'un système informatique"]
        self.web_quizz=[]
        
    def getAlgoQuizz(self):
        return self.algo_quizz

    def addAlgoQuizz(self,str):
        self.algo_quizz.append(str)