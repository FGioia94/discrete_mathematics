"""
Tarjan’s algorithm, used to find Strongly Connected Components (SCCs) 
in a directed graph
"""

class TarjanSCC:
    def __init__(self, graph):
        self.graph = graph  # Adjacency list representation of the graph
        self.n = len(graph)  # Number of nodes
        self.index = 0  # Index counter
        self.stack = []  # Stack to keep track of visited nodes
        self.indices = [-1] * self.n  # Discovery time of nodes
        self.low_link = [-1] * self.n  # Lowest discovery time reachable
        self.on_stack = [False] * self.n  # Whether a node is in stack
        self.sccs = []  # List to store strongly connected components

    def find_sccs(self):
        """ Finds all SCCs in the graph using Tarjan's algorithm """
        for node in range(self.n):
            if self.indices[node] == -1:
                self._strong_connect(node)
        return self.sccs

    def _strong_connect(self, node):
        """ Recursive function to process nodes """
        self.indices[node] = self.index
        self.low_link[node] = self.index
        self.index += 1
        self.stack.append(node)
        self.on_stack[node] = True

        # Visit all neighbors
        for neighbor in self.graph[node]:
            if self.indices[neighbor] == -1:
                self._strong_connect(neighbor)
                self.low_link[node] = min(self.low_link[node], self.low_link[neighbor])
            elif self.on_stack[neighbor]:  # Back-edge found
                self.low_link[node] = min(self.low_link[node], self.indices[neighbor])

        # If the current node is a root of an SCC
        if self.low_link[node] == self.indices[node]:
            scc = []
            while True:
                popped_node = self.stack.pop()
                self.on_stack[popped_node] = False
                scc.append(popped_node)
                if popped_node == node:
                    break
            self.sccs.append(scc)  # Add SCC to the list

# Example usage
graph = {
    0: [1],
    1: [2],
    2: [0, 3],
    3: [4],
    4: [5],
    5: [3]
}

tarjan = TarjanSCC(graph)
sccs = tarjan.find_sccs()
print("Strongly Connected Components:", sccs)
