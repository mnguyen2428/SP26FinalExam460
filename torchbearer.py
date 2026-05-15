"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Michelle Nguyen
Student ID:   130389867

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.

    TODO
    """
    return """- **Why a single shortest-path run from S is not enough:**
            A single shortest path run from S is not enough because you also need to consider the path costs after S. Choosing the cheapest from S can result in a larger cost because then you are limited to the paths chosen after S. 

            - **What decision remains after all inter-location costs are known:**
            Choosing which relic to visit

            - **Why this requires a search over orders (one sentence):**
            A search allows us to find the orders that provide the minimum cost. """


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.

    TODO
    """
    sources = [spawn]
    for relic in relics: 
        if relic not in sources:
            sources.append(relic)
    return sources


def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').

    TODO
    """
    #Initialize all nodes to inf
    dist = {node: float('inf') for node in graph}
    #source node distance is 0
    dist[source] = 0
    pq = []
    heapq.heappush(pq, (0,source))
    visited = set()
   
    while pq:
        d, u = heapq.heappop(pq)
        if u in visited:
            continue
        #explore all neighbors of u
        for v, cost in graph[u]:
            if d + cost < dist[v]:
                dist[v] = d + cost
                heapq.heappush(pq, (dist[v], v))
        visited.add(u)
    return dist
        

def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.

    TODO
    """
    sources = select_sources(spawn, relics, exit_node)
    dist_table = {}
    for source in sources:
        dist_table[source] = run_dijkstra(graph, source)
    return dist_table


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.

    TODO
    """
    return """- **For nodes already finalized (in S):**
    The nodes in visited are the known cheapest distance

    - **For nodes not yet finalized (not in S):**
     The nodes in visited are the cheapest so far. There could be nodes that are not finalized that are cheaper. 

    ### Part 3b: Why Each Phase Holds

    - **Initialization : why the invariant holds before iteration 1:**
     Starting at S gives a distance of 0. Everything else is at infinity because no path is known yet. 

    - **Maintenance : why finalizing the min-dist node is always correct:**
    Popping from pq gives the smallest distance, u, among the not yet finalized nodes. Any other path to u has to reach some unfinilized node w where dist[w] >= u because of the nonnegative edge weights, so no future path costs less 

    - **Termination : what the invariant guarantees when the algorithm ends:**
    Every node that is finalized has its shortest path garunteed. Any node at infinity is unreachable. 

    ### Part 3c: Why This Matters for the Route Planner

    If a dist in dist_table was wrong, the search would pick a wrong relic and leads to a suboptimal path. """


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.

    TODO
    """
    return """### Why Greedy Fails

    > State the failure mode. Then give a concrete counter-example using specific node names
    > or costs (you may use the illustration example from the spec). Three to five bullets.

    - **The failure mode:** Greedy chooses the local optimum which is the cheapest path at the current step. This fails because you are stuck with this path and future paths may lead to a less optimal path. 
    - **Counter-example setup:** Nodes: S, B, C, T  dist[S,B] = 1, dist[S, C] = 2, dist[B, C] = 100, dist[C, B] = 1, dist[B, T] = 1, dist[C, T] = 1
    - **What greedy picks:** S -> B -> C -> T. Greedy starts at S and then picks B because the distance is smaller compared to S to C. Total Cost = 1. Then picks C. Total Cost = 101. Lastly picks T as the exit. Total Cost = 102
    - **What optimal picks:** S -> C -> B -> T. Optimal starts at S and then picks C. Total Cost = 2. Then picks B. Total Cost = 1. Lastly picks T as the exit. TOtal Cost = 4
    - **Why greedy loses:** Greedy chooses what looks best at its current node and does not account for future node costs. Starting from S, node B is closer so it chooses that one. But then to get to C, it costs 100 which is way more costly going to C from S and then B. 

    ### What the Algorithm Must Explore

    -  The algorithm must explore every order of relics to account for different costs of different orders. """


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    best = [float('inf'), []]  #min fuel cost, list of relic order
    relics_remaining = set(relics)
    relics_visited_order = []
    _explore(dist_table, spawn, relics_remaining, relics_visited_order, 0, exit_node, best)
    cost, order = best[0], best[1]
    if cost == float('inf'):
        return (float('inf'), [])
    return (cost, list(order))


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection, set
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    TODO
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """
    
    #base case
    #when base case? when every relic is visited
    if not relics_remaining:
        #calculate total cost, current_loc is where we stand after last relic
        total_cost = cost_so_far + dist_table[current_loc][exit_node]
        if total_cost < best[0]:
            best[0] = total_cost
            best[1] = list(relics_visited_order)
        return
    if cost_so_far >= best[0]:
        #pruning the big ones
        return

    #recursive case
    for relic in list(relics_remaining):
        relics_remaining.remove(relic)
        relics_visited_order.append(relic)
        #testing
        #print(relics_remaining)
        #print(relics_visited_order)
        #print(cost_so_far)
        _explore(dist_table, relic, relics_remaining, relics_visited_order, cost_so_far + dist_table[current_loc][relic], exit_node, best)
        #backtrack
        relics_visited_order.pop()
        relics_remaining.add(relic)





# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    dist_table = precompute_distances(graph, spawn, relics, exit_node)
    return find_optimal_route(dist_table, spawn, relics, exit_node)


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    
    graph_6 = {
        'S': [("A", 1), ("B", 1)],
        'A': [("C", 1)],
        'B': [("C", 1)],
        'C': [("T", 1)],
        'T': []
    }
    cost, order = solve(graph_6, 'S', ['A', 'B', 'C'], 'T')
    
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")
    
    


if __name__ == "__main__":
    _run_tests()
