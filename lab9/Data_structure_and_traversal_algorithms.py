from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)  # For undirected graph
    
    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex}: {' '.join(map(str, self.graph[vertex]))}")
    
    # Depth-First Search (DFS)
    def dfs(self, start_vertex):
        visited = set()
        self._dfs_recursive(start_vertex, visited)
    
    def _dfs_recursive(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=' ')
        
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)
    
    # Breadth-First Search (BFS)
    def bfs(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    
    # Find all paths between two vertices
    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in self.graph:
            return []
        paths = []
        for neighbor in self.graph[start_vertex]:
            if neighbor not in path:
                new_paths = self.find_all_paths(neighbor, end_vertex, path)
                for new_path in new_paths:
                    paths.append(new_path)
        return paths
    
    # Check if the graph is connected
    def is_connected(self):
        if not self.graph:
            return True
        start_vertex = next(iter(self.graph))
        visited = set()
        self._dfs_recursive(start_vertex, visited)
        return len(visited) == len(self.graph)

# Testing Section
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)

    print("\n--- Graph Structure ---")
    g.print_graph()

    print("\n--- Depth-First Search (DFS) starting from vertex 0 ---")
    g.dfs(0)

    print("\n\n--- Breadth-First Search (BFS) starting from vertex 0 ---")
    g.bfs(0)

    print("\n\n--- All paths from vertex 0 to vertex 3 ---")
    all_paths = g.find_all_paths(0, 3)
    for path in all_paths:
        print(' -> '.join(map(str, path)))

    print("\n--- Is the graph connected? ---")
    print("Connected:", g.is_connected())

    # Add a disconnected vertex and test again
    g.add_vertex(4)
    print("\nAfter adding a disconnected vertex:")
    print("--- Is the graph connected? ---")
    print("Connected:", g.is_connected())
