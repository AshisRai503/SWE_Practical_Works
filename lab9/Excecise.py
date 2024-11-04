from collections import deque, defaultdict
import heapq

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.weights = {}  # For storing edge weights for Dijkstra's algorithm
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2, weight=None):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)  # For undirected graph
        if weight is not None:
            self.weights[(vertex1, vertex2)] = weight
            self.weights[(vertex2, vertex1)] = weight
    
    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex}: {' '.join(map(str, self.graph[vertex]))}")
    
    # Implementing BFS Shortest Path
    def bfs_shortest_path(self, start_vertex, end_vertex):
        if start_vertex not in self.graph or end_vertex not in self.graph:
            return None
        queue = deque([(start_vertex, [start_vertex])])
        visited = set([start_vertex])
        
        while queue:
            vertex, path = queue.popleft()
            for neighbor in self.graph[vertex]:
                if neighbor == end_vertex:
                    return path + [neighbor]
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        return None

    # Implementing Cycle Detection in an undirected graph
    def has_cycle(self):
        visited = set()
        
        def dfs(vertex, parent):
            visited.add(vertex)
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    if dfs(neighbor, vertex):
                        return True
                elif neighbor != parent:
                    return True
            return False
        
        for vertex in self.graph:
            if vertex not in visited:
                if dfs(vertex, None):
                    return True
        return False

    # Implementing Dijkstra's Algorithm
    def dijkstra(self, start_vertex):
        if start_vertex not in self.graph:
            return None
        distances = {vertex: float('inf') for vertex in self.graph}
        distances[start_vertex] = 0
        priority_queue = [(0, start_vertex)]
        
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            
            if current_distance > distances[current_vertex]:
                continue
            
            for neighbor in self.graph[current_vertex]:
                weight = self.weights.get((current_vertex, neighbor), 1)
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        return distances

    # Implementing Bipartite Check
    def is_bipartite(self):
        color = {}
        
        for vertex in self.graph:
            if vertex not in color:
                queue = deque([vertex])
                color[vertex] = 0
                
                while queue:
                    v = queue.popleft()
                    for neighbor in self.graph[v]:
                        if neighbor not in color:
                            color[neighbor] = 1 - color[v]
                            queue.append(neighbor)
                        elif color[neighbor] == color[v]:
                            return False
        return True

# Testing the Graph class with new methods
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4, weight=2)
g.add_edge(4, 5, weight=1)
g.add_edge(5, 0, weight=3)
g.print_graph()

# Test BFS Shortest Path
print("\nShortest path from 0 to 3:", g.bfs_shortest_path(0, 3))

# Test Cycle Detection
print("\nDoes the graph have a cycle?", g.has_cycle())

# Test Dijkstra's Algorithm
print("\nShortest distances from vertex 0 (Dijkstra):", g.dijkstra(0))

# Test Bipartite Check
print("\nIs the graph bipartite?", g.is_bipartite())
