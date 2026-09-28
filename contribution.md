AI Tools Used:
	Gemini (Interactive AI Assistant) 
Contribution by AI:
	Generated the initial standalone Python script for BFS and A* search operating on an 800×800 obstacle grid matrix.
	Tailored the workload duration (grid size and loop iterations) to ensure execution lasted long enough for statistical accuracy during py-spy profiling sessions.
	Provided exact command-line syntax for executing py-spy (py-spy record, py-spy top, SVG Flame Graph generation) across different operating systems.
	Assisted in formatting the quantitative results and analysis into the required SLE-2 report structure.
Contribution by Me (Maitryee Jadhav):
	Selected the specific pair of algorithms (BFS vs. A* Search) and defined the problem scope. 
	Installed and configured py-spy in the terminal environment.
	Executed the Python profiling scripts and monitored live CPU usage via py-spy top.
	Analyzed the generated flamegraph.svg output to inspect stack traces and function call timings (get_neighbors, heapq, bfs, a_star).
	Collected, verified, and benchmarked the numerical performance data (average execution times and node expansion counts) across multiple test runs. 
	Wrote the justifications and analytical conclusions based on empirical observation rather than pure theoretical assumptions. 
