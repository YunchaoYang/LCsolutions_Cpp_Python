## 3.1.1 Graphs: Introduction
Examples: 
1. Internet connection
2. Constellation
3. Course scheduling of final exam.

## 3.1.2 Graphs: Vocabulary
- __G(V, E)__ - Graph is composed of vertices and edges.
- |V| = n;
- |E| = m;
- Incident edges: |l(v)| = {(x,v) in E};
- __Degree__ of a Node, how many edges is has;
- __Adjacent vertices__
- __Path(G2)__ - Sequence of vertices connected by edges;
- __Cycle(G1)__ - Path with same begin and end vertices;
- __Simple graph__, 1) no self-loop, 2) no multi-edge;

- SubGraph

- minimum number of edges: 
  - Not connected: 0
  - Connected: n - 1  
- maximum number of edges: 
  - Simple: n(n-1)/2 = O(n^2)
  - No simple: infinity ( multi-edges)

Sum of all degree of all vertices = 2m

## 3.1.3 Graphs: Edge List Implementation

- Graph ADT
