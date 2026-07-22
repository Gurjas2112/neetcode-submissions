from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list
        graph = defaultdict(list)
        for src, des in edges:
            graph[src].append(des)
            graph[des].append(src)
        
        visited = set()
        component_count = 0

        # DFS function
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)


        # Iterate over all nodes to find unvisited components
        for node in range(n):
            if node not in visited:
                component_count += 1
                dfs(node) # or bfs(node)

        return component_count
