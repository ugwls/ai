def get_neighbors(adjacency_list, v):
    return adjacency_list.get(v, [])

def h(n):
    # Heuristic function with equal values for all nodes
    return 1

def a_star_algorithm(adjacency_list, start_node, stop_node):
    
    # open_list is a list of nodes which have been visited, but who's neighbors
    # haven't all been inspected, starts off with the start node
    # closed_list is a list of nodes which have been visited
    # and who's neighbors have been inspected
    open_list = set([start_node])
    closed_list = set([])
    
    # g contains current distances from start_node to all other nodes
    # the default value (if it's not found in the map) is +infinity
    
    g = {start_node: 0}
    parents = {start_node: start_node}

    while open_list:
        n = None
        # Find a node with the lowest value of f()
        for v in open_list:
            if n is None or g[v] + h(v) < g[n] + h(n):
                n = v

        if n is None:
            print('Path does not exist!')
            return None

        if n == stop_node:
            # Reconstruct path if stop_node is reached
            reconst_path = []
            while parents[n] != n:
                reconst_path.append(n)
                n = parents[n]
            reconst_path.append(start_node)
            reconst_path.reverse()
            print('Path found:', reconst_path)
            return reconst_path
        
        
        for (m, weight) in get_neighbors(adjacency_list, n):
            if m not in open_list and m not in closed_list:
                open_list.add(m)
                parents[m] = n
                g[m] = g[n] + weight
            else:
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n
                    if m in closed_list:
                        closed_list.remove(m)
                        open_list.add(m)
                        
        


        open_list.remove(n)
        closed_list.add(n)

    print('Path does not exist!')
    return None


#list of tuples
adjacency_list = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5)],
    'C': [('D', 12)]
}

start_node = 'A'
stop_node = 'D'
path = a_star_algorithm(adjacency_list, start_node, stop_node)
