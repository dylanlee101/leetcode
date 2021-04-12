

visited = set()
def dfs(node,visited):
    if node in visited:
        return

    visited.add(node)

    for next_node in node.children():
        if next_node not in visited:
            dfs(next_node,visited)


def dfs2(self,tree):
    if tree.root is None:
        return []
    visited,stack = [],[tree.root]
    while stack:
        node = stack.pop()
        visited.add(node)
        process(data)
        nodes = generate_related_nodes(nodes)
        stack.push(nodes)