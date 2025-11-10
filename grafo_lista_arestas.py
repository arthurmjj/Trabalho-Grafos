# Grafo usando Lista de Arestas
# Feito por: Arthur Martins Jorge, Gabriel de Castro Domingos e José Eduardo Sales

class GrafoListaArestas:
    def __init__(self):
        self.vertices = []
        self.arestas = []

    def adicionar_vertice(self, v):
        if v not in self.vertices:
            self.vertices.append(v)
        else:
            print("Vértice já existe!")

    def remover_vertice(self, v):
        if v in self.vertices:
            self.vertices.remove(v)
            self.arestas = [a for a in self.arestas if v not in a]
        else:
            print("Vértice não encontrado!")

    def adicionar_aresta(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.arestas.append((v1, v2))
        else:
            print("Um dos vértices não existe!")

    def remover_aresta(self, v1, v2):
        if (v1, v2) in self.arestas:
            self.arestas.remove((v1, v2))
        elif (v2, v1) in self.arestas:
            self.arestas.remove((v2, v1))
        else:
            print("Aresta não existe!")

    def grau(self):
        for v in self.vertices:
            grau = sum(1 for a in self.arestas if v in a)
            print(f"Grau de {v}: {grau}")

    def existe_aresta(self, v1, v2):
        return (v1, v2) in self.arestas or (v2, v1) in self.arestas

    def vizinhos(self, v):
        viz = []
        for a in self.arestas:
            if a[0] == v:
                viz.append(a[1])
            elif a[1] == v:
                viz.append(a[0])
        print(f"Vizinhos de {v}: {viz}")

    def percurso_possivel(self, caminho):
        for i in range(len(caminho) - 1):
            if not self.existe_aresta(caminho[i], caminho[i+1]):
                print("Percurso NÃO é possível")
                return
        print("Percurso é possível!")



