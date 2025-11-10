# Grafo usando Lista de Adjacência
# Feito por: Arthur Martins Jorge, Gabriel de Castro Domingos e José Eduardo Sales

class GrafoListaAdj:
    def __init__(self):
        self.grafo = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []
        else:
            print("Vértice já existe!")

    def remover_vertice(self, vertice):
        if vertice in self.grafo:
            self.grafo.pop(vertice)
            for v in self.grafo:
                if vertice in self.grafo[v]:
                    self.grafo[v].remove(vertice)
        else:
            print("Vértice não encontrado!")

    def adicionar_aresta(self, v1, v2):
        if v1 in self.grafo and v2 in self.grafo:
            self.grafo[v1].append(v2)
            self.grafo[v2].append(v1)
        else:
            print("Um dos vértices não existe!")

    def remover_aresta(self, v1, v2):
        if v2 in self.grafo[v1]:
            self.grafo[v1].remove(v2)
            self.grafo[v2].remove(v1)
        else:
            print("Aresta não existe!")

    def grau(self):
        for v in self.grafo:
            print(f"Grau de {v}: {len(self.grafo[v])}")

    def existe_aresta(self, v1, v2):
        return v2 in self.grafo[v1]

    def vizinhos(self, v):
        print(f"Vizinhos de {v}: {self.grafo[v]}")

    def percurso_possivel(self, caminho):
        for i in range(len(caminho) - 1):
            if caminho[i+1] not in self.grafo[caminho[i]]:
                print("Percurso NÃO é possível")
                return
        print("Percurso é possível!")

