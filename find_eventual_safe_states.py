def eventual_safe_nods(graph):
    n = len(graph)
    # 0 for not visited, 1 for cycle reachable or visiting node, 2 for non-cycle
    state = [0 for _ in range(n)]

    def dfs(node):
        """ return whether reach a cycle """
        if state[node] == 1:  # Cycle reachable, or a visiting node (which then form a cycle)
            return True
        if state[node] == 2:  # Reached a non cycle
            return False
        if state[node] == 0:

            state[node] = 1  # Say we are visiting it
            # reach_circle is true if any of next_node could reach or form a cycle
            reach_circle = any(dfs(next_node) for next_node in graph[node])
            # record the state of the node
            state[node] = 1 if reach_circle else 2
            return reach_circle

    for node in range(n):
        if state[node] == 0:
            dfs(node)

    return [node for node in range(n) if state[node] == 2]


if __name__ == "__main__":
    graph = [
        [1, 2],  # 0
        [2, 3],  # 1
        [5],     # 2
        [0],     # 3
        [5],     # 4
        [],      # 5
        []       # 6
    ]

    print(eventual_safe_nods(graph))
