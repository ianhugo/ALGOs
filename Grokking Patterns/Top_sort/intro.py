"""
WHEN: 
- linear ordering
- dependencies between elements

Topological Sort
- directed graph
- linear ordering of nodes
- [u, v, w]
- if edge (u, v)
- u comes before v

Concepts:
Source: node with no incoming edge
Sink: node with no outgoing edge
Ordering: start with source, ends with sink
DAG: Directed Acyclic Agraph


Approaches:
1. Simple Top Sort
- there are dependencies
- treat as edges

2. All Top Sort orders
- iterate over all
- call recursively
- reset after

NOTE: depending on question, note stopping early conditions
- unique reconstruction
    - more than one source = more than one way to construct
    - next source or number, differ from original sequence
    - sorted order not size of original sequence
"""