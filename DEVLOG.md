# Development Log – The Torchbearer

**Student Name:** Michelle Nguyen  
**Student ID:** 130389867

> Instructions: Write at least four dated entries. Required entry types are marked below.
> Two to five sentences per entry is sufficient. Write entries as you go, not all in one
> sitting. Graders check that entries reflect genuine work across multiple sessions.
> Delete all blockquotes before submitting.

---

## Entry 1 – May 13: Initial Plan

> Required. Write this before writing any code. Describe your plan: what you will
> implement first, what parts you expect to be difficult, and how you plan to test.

We are given a weighted, directed graph. The problem is to find the cheapest route from S to T. I will be implementing dijkstra to find the shortest path from the start to all other relics and exit. A part that I expect will be difficult is the pruning. 

---

## Entry 2 – May 13: [Short description]

> Required. At least one entry must describe a bug, wrong assumption, or design change
> you encountered. Describe what went wrong and how you resolved it.

A wrong assumption I had was that I could just use dijkstra to cheapest path, but upon reading the assignment again, I realized that that implementation does not work as it does not account for visiting all relics. 

---

## Entry 3 – May 14: Part 3

Worked on Part 3. For initialization, you start at S which gives a distance of 0. There is no where else to go. For maintanence, the priority queue/min heap pops the smallest distance from the unfinalized node. Due to the nonnegative weights, this is correct. At termination, when the heap is empty, finalized nodes have their shortest distance. 

---

## Entry 4– May 14: Part 4

Worked on why greedy cannot work for this problem. While coming up with a counter example, I was going to use the one in ASSIGNMENT.md but when I tried applying greedy to it by taking the cheapest path each time, I ended up with an optimal solution. So I took out node D and from there greedy ended up failing, which is what I wanted. Greedy chose the local optimal path which resulted in its failure because the distance from B to C was 100 and the distance from C to B was only 1. If it took the path S to C first, then it wouldn't have had to take the path that cost 100. 

---

## Entry 5 – [Date]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

_Your entry here._

---

## Final Entry – [Date]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | 0.5 |
| Part 2: Precomputation Design | |
| Part 3: Algorithm Correctness | |
| Part 4: Search Design | |
| Part 5: State and Search Space | |
| Part 6: Pruning | |
| Part 7: Implementation | |
| README and DEVLOG writing | |
| **Total** | |
