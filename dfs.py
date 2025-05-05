graph = {"a": ["b", "c"],
         "b": ["a", "e", "d"],
         "c": ["a", "e"],
         "d": ["b"],
         "e": ["b", "c"],
         }

visited = set() # Tracks all nodes already checked
stack = set() # Tracks the current path of vertices in the DFS

def dfs(node:str, parent:str) -> bool:
    """
    Traverses the node graph and checks for cycles

        Parameters:
            node (str): The starting node
            parent (str): The parent node

        Returns:
            (bool): True if there is a cycle
    """
    print(node)
    visited.add(node) # Mark the current vertex as visited
    stack.add(node) # Add it to the current path

    for neightbor in graph[node]:
        if neightbor not in visited:
            if dfs(neightbor, node):
                return True
                
        elif neightbor != parent and neightbor in stack:
            return True
        
    stack.remove(node)
    return False

print(dfs("a", None))