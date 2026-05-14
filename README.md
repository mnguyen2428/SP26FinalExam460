# The Torchbearer

**Student Name:** Michelle Nguyen
**Student ID:** 130389867
**Course:** CS 460 – Algorithms | Spring 2026

> This README is your project documentation. Write it the way a developer would document
> their design decisions , bullet points, brief justifications, and concrete examples where
> required. You are not writing an essay. You are explaining what you built and why you built
> it that way. Delete all blockquotes like this one before submitting.

---

## Part 1: Problem Analysis

> Document why this problem is not just a shortest-path problem. Three bullet points, one
> per question. Each bullet should be 1-2 sentences max.

- **Why a single shortest-path run from S is not enough:**
  A single shortest path run from S is not enough because you also need to consider the path costs after S. Choosing the cheapest from S can result in a larger cost because then you are limited to the paths chosen after S. 

- **What decision remains after all inter-location costs are known:**
  Choosing which relic to visit

- **Why this requires a search over orders (one sentence):**
  A search allows us to find the orders that provide the minimum cost. 

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

> List the source node types as a bullet list. For each, one-line reason.

| Source Node Type | Why it is a source |
|---|---|
| Start | The Torchbearer starts here |
| Relic chamber | After choosing a path, a relic chamber is visited|

### Part 2b: Distance Storage

> Fill in the table. No prose required.

| Property | Your answer |
|---|---|
| Data structure name | Nested dictionary |
| What the keys represent | The source node and the destination node |
| What the values represent | Distance from source node to destination node |
| Lookup time complexity | O(1) |
| Why O(1) lookup is possible | Dictionay lookups in python are O(1) because of hashing |

### Part 2c: Precomputation Complexity

> State the total complexity and show the arithmetic. Two to three lines max.

- **Number of Dijkstra runs:** k + 1 times because there are k relics and dijkstra runs once from the start node
- **Cost per run:** O(mlogn) where n = |V| and m = |E|
- **Total complexity:** O(k+1) * O(mlogn) = O(kmlogn)
- **Justification (one line):** At each source node, dijkstra is run. 

---

## Part 3: Algorithm Correctness

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.

### Part 3a: What the Invariant Means

> Two bullets: one for finalized nodes, one for non-finalized nodes.
> Do not copy the invariant text from the spec.

- **For nodes already finalized (in S):**
  The nodes in visited are the known cheapest distance

- **For nodes not yet finalized (not in S):**
  The nodes in visited are the cheapest so far. There could be nodes that are not finalized that are cheaper. 

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
  Starting at S gives a distance of 0. Everything else is at infinity because no path is known yet. 

- **Maintenance : why finalizing the min-dist node is always correct:**
  Popping from pq gives the smallest distance, u, among the not yet finalized nodes. Any other path to u has to reach some unfinilized node w where dist[w] >= u because of the nonnegative edge weights, so finalizing u is correct. 

- **Termination : what the invariant guarantees when the algorithm ends:**
  Every node that is finalized has its shortest path garunteed. Any node at infinity is unreachable. 

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

If a dist in dist_table was wrong, the search would pick a wrong relic and leads to a suboptimal path. 

---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** Greedy chooses the local optimum which is the cheapest path at the current step. This fails because you are stuck with this path and future paths may lead to a less optimal path. 
- **Counter-example setup:** Nodes: S, B, C, T  dist[S,B] = 1, dist[S, C] = 2, dist[B, C] = 100, dist[C, B] = 1, dist[B, T] = 1, dist[C, T] = 1
- **What greedy picks:** S -> B -> C -> T. Greedy starts at S and then picks B because the distance is smaller compared to S to C. Total Cost = 1. Then picks C. Total Cost = 101. Lastly picks T as the exit. Total Cost = 102
- **What optimal picks:** S -> C -> B -> T. Optimal starts at S and then picks C. Total Cost = 2. Then picks B. Total Cost = 1. Lastly picks T as the exit. TOtal Cost = 4
- **Why greedy loses:** Greedy chooses what looks best at its current node and does not account for future node costs. Starting from S, node B is closer so it chooses that one. But then to get to C, it costs 100 which is way more costly going to C from S and then B. 

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- The algorithm must explore every order of relics to account for different costs of different orders. 

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | | | |
| Relics already collected | | | |
| Fuel cost so far | | | |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | |
| Operation: check if relic already collected | Time complexity: |
| Operation: mark a relic as collected | Time complexity: |
| Operation: unmark a relic (backtrack) | Time complexity: |
| Why this structure fits | |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** _Your answer (in terms of k)._
- **Why:** _One-line justification._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- _Your references here._
