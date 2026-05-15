# Development Log – The Torchbearer

**Student Name:** Michelle Nguyen  
**Student ID:** 130389867


---

## Entry 1 – May 13: Initial Plan


We are given a weighted, directed graph. The problem is to find the cheapest route from S to T. I will be implementing dijkstra to find the shortest path from the start to all other relics and exit. A part that I expect will be difficult is the pruning. 

---

## Entry 2 – May 13: [Short description]



A wrong assumption I had was that I could just use dijkstra to cheapest path, but upon reading the assignment again, I realized that that implementation does not work as it does not account for visiting all relics. We need to consider all paths since different orders have different costs. 

---

## Entry 3 – May 14: Part 3

Worked on Part 3. For initialization, you start at S which gives a distance of 0. There is no where else to go. For maintanence, the priority queue/min heap pops the smallest distance from the unfinalized node. Due to the nonnegative weights, this is correct. At termination, when the heap is empty, finalized nodes have their shortest distance. 

---

## Entry 4– May 14: Part 4

Worked on why greedy cannot work for this problem. While coming up with a counter example, I was going to use the one in ASSIGNMENT.md but when I tried applying greedy to it by taking the cheapest path each time, I ended up with an optimal solution. So I took out node D and from there greedy ended up failing, which is what I wanted. Greedy chose the local optimal path which resulted in its failure because the distance from B to C was 100 and the distance from C to B was only 1. If it took the path S to C first, then it wouldn't have had to take the path that cost 100. 

---
## Entry 4– May 14: Part 5+6

While working on part 5+6, in _explore(), I noticed that it wasn't trying different paths. I used a print statement to print the sets for relics_remaining, relics_visited_order, and cost_so_far. It only tried one path which wasn't the solution I wanted. To fix this, I added backtracking. ALso added pruning which wasn't as difficult as I thought it would be as it was just comparing the cost so far to the best we had. 

---
## Entry 5 – May 14: Post-Implementation Reflection


Given more time, or if I had started it more earlier, I would probably work on edge cases more. I was mainly focusing on working through the problems. I would also maybe work on the readibility of my code since there were a lot of variables to deal with. 

---

## Final Entry – May 14: Time Estimate


| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | 0.5 |
| Part 2: Precomputation Design | 1|
| Part 3: Algorithm Correctness | 1.5|
| Part 4: Search Design | 1|
| Part 5: State and Search Space | 2|
| Part 6: Pruning | 1|
| Part 7: Implementation | 3|
| README and DEVLOG writing | 2|
| **Total** | 12 |
