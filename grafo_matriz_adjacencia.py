# Grafo usando Matriz de Adjacência
# Feito por: Arthur Martins Jorge, Gabriel de Castro Domingos e José Eduardo Sales

class GrafoMatrizAdj:
    def __init__(self):
        self.vertices = []
        self.matriz = []

    def adicionar_vertice(self, v):
        if v not in self.vertices:
            self.vertices.append(v)
            for linha in self.matriz:
                linha.append(0)
            self.matriz.append([0] * len(self.vertices))
        else:
            print("Vértice já existe!")

    def remover_vertice(self, v):
        if v in self.vertices:
            idx = self.vertices.index(v)
            self.vertices.remove(v)
            self.matriz.pop(idx)
            for linha in self.matriz:
                linha.pop(idx)
        else:
            print("Vértice não encontrado!")

    def adicionar_aresta(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            i, j = self.vertices.index(v1), self.vertices.index(v2)
            self.matriz[i][j] = 1
            self.matriz[j][i] = 1
        else:
            print("Um dos vértices não existe!")

    def remover_aresta(self, v1, v2):
        i, j = self.vertices.index(v1), self.vertices.index(v2)
        self.matriz[i][j] = 0
        self.matriz[j][i] = 0

    def grau(self):
        for i, v in enumerate(self.vertices):
            print(f"Grau de {v}: {sum(self.matriz[i])}")

    def existe_aresta(self, v1, v2):
        i, j = self.vertices.index(v1), self.vertices.index(v2)
        return self.matriz[i][j] == 1

    def vizinhos(self, v):
        i = self.vertices.index(v)
        viz = [self.vertices[j] for j in range(len(self.vertices)) if self.matriz[i][j] == 1]
        print(f"Vizinhos de {v}: {viz}")

    def percurso_possivel(self, caminho):
        for i in range(len(caminho) - 1):
            if not self.existe_aresta(caminho[i], caminho[i+1]):
                print("Percurso NÃO é possível")
                return
        print("Percurso é possível!")



