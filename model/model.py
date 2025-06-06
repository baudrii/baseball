import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo=nx.Graph()
        self._idMapTeams={}
        self._nodes = DAO.getAllSquadreAnno(2015)
        for n in self._nodes:
            self._idMapTeams[n.ID]=n

        self._idMapTeamSalary={}
        for n1 in self._nodes:
            self._idMapTeamSalary[n1.ID]= DAO.getSalarioSquadra(2015, n1.teamCode)


        self._bestPath=[]
        self._pesoMassimo=0



    def creaGrafo(self):
        self._grafo.add_nodes_from(self._nodes)
        for n in self._nodes:
            for a in self._nodes:
                if a!=n:
                    self._grafo.add_edge(n,a, weight=(self._idMapTeamSalary[n.ID]+self._idMapTeamSalary[a.ID]))


    def getAnniDD(self):
        return DAO.getAllAnni()

    def getTeams(self,anno):
        self._nodes=DAO.getAllSquadreAnno(anno)
        return self._nodes

    def getVicini(self, n1):
       vicini =list(self._grafo.neighbors(n1))



    def ricorsione(self,parziale , rimanenti):

        if

        parziale=[n1]
        cc= [self._nodes]

        for nodo in cc:
            cc.pop(n1)
            parziale.append(nodo)
            self.ricorsione(parziale)
            parziale.pop(nodo)


    def ammissible(self):


