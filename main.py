import timeit


def generate_matrix(filename):
    """Generate a matrix from an input text file.

    :param str filename: The name of the network file in .txt format
    :rtype dict network: The resulting matrix represented as a
    2D list of edge weights
    """

    network_file = open(filename, 'r')
    matrix = []
    for line in network_file:
        edges = list(map(lambda weight: 0 if weight == '-' else int(weight),
                         line.strip().split(',')))
        matrix.append(edges)

    return matrix


def total_weight(network):
    """Calculate the total weight of edges in a network.

    :param dict network: A network represented as a 2D list of edge weights
    :rtype int weight: the total weight of the network
    """
    weight = 0

    for node_connections in network:
        for edge in node_connections:
            if edge is not None:
                weight += edge

    return weight // 2


def generate_network_graph(network):
    """Generate a network graph from input network.

    :param list network: A network represented as a 2D list of weights
    :rtype dict network_graph: A 2D dictionary of {node: {neighbor: weight, ...}, ...}
    """
    num_nodes = len(network)
    network_graph = {}

    for y_node in range(num_nodes):
        neighbors = {}
        for x_node in range(num_nodes):
            if network[y_node][x_node] is not 0:
                neighbors[x_node] = network[y_node][x_node]
        network_graph[y_node] = neighbors

    return network_graph


def prim(network_graph):
    """Implementation of Prim's Minimum Spanning Tree Algorithm.

    :param dict network_graph: A 2D dictionary of
    {node: {neighbor: weight, ...}, ...}
    :rtype dict mst: A minimum spanning tree represented as {edge: weight}
    """
    seen_nodes = set()
    mst = set()
    edges = set()

    # Using the first node in the network graph as the root of the tree
    current_node = list(network_graph.keys())[0]

    while True:
        # Adding all edges from the root to the list of edges
        for current_neighbor in network_graph[current_node]:
            # Edge represented as (weight, [node, neighbor])
            edge = (network_graph[current_node][current_neighbor],
                    frozenset([current_node, current_neighbor]))
            if edge in mst:
                continue
            edges.remove(edge) if edge in edges else edges.add(edge)

        if edges:
            # Get the smallest edge in the list, remove & add to MST
            smallest_edge = min(edges)
            edges.remove(smallest_edge)
            mst.add(smallest_edge)

            # Get the next node to examine
            _, (new_node, new_neighbor) = smallest_edge
            seen_nodes.add(current_node)
            current_node = (new_node if new_neighbor in
                            seen_nodes else new_neighbor)
        else:
            break

    # Convert from sets to dictionary of {edge: weight}
    # 'final_weight' indicates the smallest weight for the given 'final_edge'
    # between two nodes that doesn't create a cycle
    return dict((final_edge, final_weight) for (final_weight, final_edge) in
                mst)


def main():
    """Solve Problem #107 from Project Euler."""

    # Generate the network from the given file, and get its original weight
    matrix = generate_matrix('network.txt')
    old_weight = total_weight(matrix)

    # Generate a network graph from the input network to be used in Prim's
    # algorithm
    graph = generate_network_graph(matrix)

    # Generate a minimum spanning tree from the network graph using Prim's
    # algorithm
    mst = prim(graph)

    print(f"Old network weight: {old_weight}")
    print(f"New network weight: {old_weight - sum(mst.values())}")

# Main method to solve the problem & indicate execution time in seconds
if __name__ == '__main__':
    start = timeit.default_timer()
    main()
    stop = timeit.default_timer()
    print(f"Execution time: {stop - start} seconds")
