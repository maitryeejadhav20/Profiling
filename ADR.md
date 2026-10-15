# SLE-4: Final Viva & Architecture Decision Record (ADR)
**Course:** 02AML204 – Introduction to Artificial Intelligence  
**PRN:** 25UAM052  
**Name:** Maitryee Dilip Jadhav (Maitryee Jadhav)  
**Division:** A  

---

## PART A: Architecture Decision Record (ADR)
**Title:** Use of A* Search with Manhattan Distance Heuristic over Uninformed Search (BFS)  
**Status:** Accepted  
**Date:** October 2026  

### 1. Context
While developing the Grid-Based Maze Solver & Pathfinding System, the application needed to efficiently compute optimal paths across an 800×800 grid matrix containing dynamic obstacle walls. Because grid-based pathfinding can suffer from state-space explosion, choosing the right traversal mechanism was critical to ensure low latency and minimal resource overhead. The system required a reliable algorithm capable of navigating complex user-defined maze configurations without excessive CPU bottlenecks[cite: 1].

### 2. Decision
We decided to implement A* Search utilizing the Manhattan distance heuristic as the primary pathfinding algorithm within the Search Engine container, supported by a Priority Queue (Open List) and a Hash-Set (Closed List)[cite: 1].

### 3. Alternatives Considered
* **Alternative 1: Breadth-First Search (BFS)** – An uninformed layer-order search strategy using a standard queue[cite: 1].
* **Alternative 2: Depth-First Search (DFS)** – An uninformed graph traversal strategy using a stack (rejected due to non-optimality and risk of infinite loops in open grids)[cite: 1].
* **Alternative 3: Greedy Best-First Search** – Uses only heuristic values without path cost ($g(n)$), leading to suboptimal paths[cite: 1].

### 4. Rationale / Justification
The selection of A* Search is strongly backed by both empirical profiling data from SLE-2 and modular architecture principles from SLE-3[cite: 1]: 
* **Profiling Evidence (SLE-2):** Benchmarking across 20 iterations on an 800×800 grid proved that BFS consumed an average of ~450 ms per run while expanding ~280,000 nodes, with `get_neighbors()` choking 58% of total CPU runtime due to blind expansion[cite: 1]. In contrast, A* Search reduced average execution time to ~210 ms and compressed node expansion down to ~95,000 nodes[cite: 1].
* **Architectural Synergy (SLE-3):** By decoupling the Heuristic Module from the core Search Engine, A* cleanly computes $f(n) = g(n) + h(n)$ via Manhattan distance calculations[cite: 1]. Furthermore, utilizing an explicit Explored Set (Closed List) mapped to a hash-set lookup structure guarantees $O(1)$ node checks, preventing redundant evaluations[cite: 1].

### 5. Consequences
* **Positive:** Significantly faster execution speeds (~210 ms vs ~450 ms) and lower memory overhead; highly targeted node exploration, cutting down unnecessary expansions by nearly 66%[cite: 1].
* **Negative / Trade-offs:** Slightly higher implementation complexity due to priority queue management (`heapq`) and heuristic function overhead compared to standard queues[cite: 1].

---

## PART B: Short Summary of My SLE Journey
My software journey began in SLE-1 with the creation of the core agent search code, AI contribution tracking, and initial README setup[cite: 1]. In SLE-2, I benchmarked the system on an 800×800 grid using `py-spy`, proving quantitatively that A* outperforms BFS by reducing execution time from ~450 ms to ~210 ms[cite: 1]. Moving into SLE-3, I structured the system into a modular C4 architecture—separating the Input Module, Search Engine, Heuristic Module, and Output Module—while defining precise data structures like Priority Queues and Closed Lists[cite: 1]. Finally, in SLE-4, I consolidated these findings into this Architecture Decision Record (ADR) to formally justify why A* Search is the optimal choice for our pathfinding system[cite: 1].

---

## PART C: AI Contribution Note
* **AI tools used:** Gemini / ChatGPT[cite: 1]
* **What AI helped with:** Generating structural templates, assisting with C4 diagram syntax formatting, and providing command-line guidance for running `py-spy` profiling metrics[cite: 1].
* **What I did myself:** Configured the custom Python codebase, executed benchmark tests across 20 iterations, analyzed flame graphs, mapped out modular component interactions, and wrote the final analytical justifications[cite: 1].

---

## PART D: Viva Preparation Notes (Quick Key Points)
* **Core Decision:** Chose A* Search with Manhattan distance over BFS because informed search directs traversal toward the goal, avoiding blind expansion[cite: 1].
* **Profiling Proof (SLE-2):** A* ran in ~210 ms (expanding ~95,000 nodes) compared to BFS at ~450 ms (expanding ~280,000 nodes)[cite: 1].
* **Architecture (SLE-3):** The decoupled Heuristic Module feeds $h(n)$ into the Search Engine's priority queue, while the closed hash-set ensures $O(1)$ lookup times[cite: 1].
* **C4 Container Overview:** User inputs configuration $\rightarrow$ Input Module parses data $\rightarrow$ Search Engine executes A* using the Heuristic Module $\rightarrow$ Output Module renders final metrics[cite: 1].
