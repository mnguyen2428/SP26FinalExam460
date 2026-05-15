# The Torchbearer

**Student Name:** Michelle Nguyen
**Student ID:** 130398967
**Course:** CS 460 – Algorithms | Spring 2026

---

## Part 1: Problem Analysis


- **Why a single shortest-path run from S is not enough:**
  A single shortest path run from S is not enough because you also need to consider the path costs after S. Choosing the cheapest from S can result in a larger cost because then you are limited to the paths chosen after S. 

- **What decision remains after all inter-location costs are known:**
  Choosing which relic to visit

- **Why this requires a search over orders (one sentence):**
  A search allows us to find the orders that provide the minimum cost. Different orders have different costs. 

---

## Part 2: Precomputation Design

### Part 2a: Source Selection


| Source Node Type | Why it is a source |
|---|---|
| Start | The Torchbearer starts here |
| Relic chamber | After choosing a path, a relic chamber is visited|

### Part 2b: Distance Storage



| Property | Your answer |
|---|---|
| Data structure name | Nested dictionary |
| What the keys represent | The source node and the destination node |
| What the values represent | Distance from source node to destination node |
| Lookup time complexity | O(1) |
| Why O(1) lookup is possible | Dictionay lookups in python are O(1) because of hashing |

### Part 2c: Precomputation Complexity



- **Number of Dijkstra runs:** k + 1 times because there are k relics and dijkstra runs once from the start node
- **Cost per run:** O(mlogn) where n = |V| and m = |E|
- **Total complexity:** O(k+1) * O(mlogn) = O(kmlogn)
- **Justification (one line):** At each source node, dijkstra is run. 

---

## Part 3: Algorithm Correctness



### Part 3a: What the Invariant Means



- **For nodes already finalized (in S):**
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



If a dist in dist_table was wrong, the search would pick a wrong relic and leads to a suboptimal path. 

---

## Part 4: Search Design

### Why Greedy Fails



- **The failure mode:** Greedy chooses the local optimum which is the cheapest path at the current step. This fails because you are stuck with this path and future paths may lead to a less optimal path. 
- **Counter-example setup:** Nodes: S, B, C, T  dist[S,B] = 1, dist[S, C] = 2, dist[B, C] = 100, dist[C, B] = 1, dist[B, T] = 1, dist[C, T] = 1
- **What greedy picks:** S -> B -> C -> T. Greedy starts at S and then picks B because the distance is smaller compared to S to C. Total Cost = 1. Then picks C. Total Cost = 101. Lastly picks T as the exit. Total Cost = 102
- **What optimal picks:** S -> C -> B -> T. Optimal starts at S and then picks C. Total Cost = 2. Then picks B. Total Cost = 1. Lastly picks T as the exit. TOtal Cost = 4
- **Why greedy loses:** Greedy chooses what looks best at its current node and does not account for future node costs. Starting from S, node B is closer so it chooses that one. But then to get to C, it costs 100 which is way more costly going to C from S and then B. 

### What the Algorithm Must Explore



- The algorithm must explore every order of relics to account for different costs of different orders. 

---

## Part 5: State and Search Space

### Part 5a: State Representation



| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | current_loc | node | The node where the Torchbearer is right now |
| Relics already collected | relics_remaining | Set | A set of relics that the Torchbearer need |
| Fuel cost so far | cost_so_far | int | The total fuel amount spent|

### Part 5b: Data Structure for Visited Relics



| Property | Your answer |
|---|---|
| Data structure chosen | Set |
| Operation: check if relic already collected | Time complexity: O(1)|
| Operation: mark a relic as collected | Time complexity: O(1)|
| Operation: unmark a relic (backtrack) | Time complexity: O(1)|
| Why this structure fits | Python set allows for this|

### Part 5c: Worst-Case Search Space



- **Worst-case number of orders considered:** k!
- **Why:** There are k amount of relics to choose from. After choosing 1, k-1 relics are left and this continues until k is 1. 

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking



- **What is tracked:** Minimum fuel cost
- **When it is used:** It is used to compare other routes that might be more fuel efficient at the beginning of the recursion. 
- **What it allows the algorithm to skip:** Routes that have greater costs than the minimum. 

### Part 6b: Lower Bound Estimation



- **What information is available at the current state:** Cost so far, relics visited, relics remaining, current location
- **What the lower bound accounts for:** The minimum cost to reach the relics and exit
- **Why it never overestimates:** We take the minimum cost path from current location to exit and this path is either greater than or equal to the optimal path. 

### Part 6c: Pruning Correctness



- Pruning is safe because any path that costs more than the best will be cut off, leaving for the optimal path to always be recorded. 

---

## References


- Lecture Notes
