# Week 0 - Search

Status: In progress
Date started: 2026-07-21
Official module: https://cs50.harvard.edu/ai/weeks/0/

## Search Problems

- Agent: entity that perceives its environment and act upon that environment
- State: a config of the agent and its environment
- Initial state: the state where the agent begins, we begin with it and start to reason about it
- Actions: choices that can be made in a state. Function ACTIONS(s) returns the set of actions that can be made in the state 's'
- Transition model: a description of what state results from performing any aplicable action in any state. Function RESULT(s,a) returns the state resulting from action 'a' in state 's'
- state space: the set of all states reachable from the initial state by any sequence of actions
- Goal test: way to determine wheter a give state is a goal state
- Path cost: numerical cost associated with a given path

## Notes

1. **node**
    - a data structure that keeps track of:
     * a state;
     * a parent (node that generated this node)
     * an action (action apllied to parent to get node)
     * a path cost (from initial state to node)

2. **Approach**
    - Start with a frontier that contains the initial state
    - Repeat:
        * if the frontier is empty, then no solution
        * Remove a node from the frontier
        * if node contains goal state, return solution -> Done
        * Expand node, add resulting nodes to the frontier

3. **Revised Approach** (infinite loop safe)
    - Start with a frontier that contains the initial state
    - Start with an empty explored set
    - Repeat:
        * if the frontier is empty, then no solution
        * Remove a node from the frontier
        * if node contains goal state, return solution
        * Add the node to the explored set
        * Expand node, add resulting nodes to the frontier if they aren't already in the frontier of the explored set

5. **Depth-first search (DFS)**
    - search algobrithm that always expands the deepest node in the frontier
    - **stack**
       * last-in first-out data type
       * We should treat the frontier like a **stack**
    - Code example:
        # **Define the function that removes a node from the frontier and returns it.**
        def remove(self):
            # **Terminate the search if the frontier is empty, because this means that there is no solution.**
            if self.empty():
                raise Exception("empty frontier")
            else:
                # **Save the last item in the list (which is the newest node added)**
                node = self.frontier[-1]
                # **Save all the items on the list besides the last node (i.e. removing the last node)**
                self.frontier = self.frontier[:-1]
                return node

6. **Breadth-first search (BFS)**
    - search algorithm that always expands the shallowest node in the frontier
    - **queue**
        * first-in first-out data type
    - Code example:
    # **Define the function that removes a node from the frontier and returns it.**
    def remove(self):
        # **Terminate the search if the frontier is empty, because this means that there is no solution.**
        if self.empty():
            raise Exception("empty frontier")
        else:
            # **Save the oldest item on the list (which was the first one to be added)**
            node = self.frontier[0]
            # **Save all the items on the list besides the first one (i.e. removing the first node)**
            self.frontier = self.frontier[1:]
            return node

7. **Informed strategy**
    - search strategy that uses problem-specific knowledge to find solutions more efficiently

8. **Greedy Best-First Search**
    - search algorithm that expands the node that is closest to the goal, as estimated by a heuristic function (manhattan distances)
     * **manhattan distance** - how far is it from the goal

9. **A* search**
    - search algorithm that expands node with lowest value g(n) + h(n)
        * g(n) = cost to reach node
        * h(n) = estimated cost to goal

10. **Minimax**
    - Given a state s:
        * **MAX** picks action a in ACTIONS(s) that produces highest value of MIN-VALUE(RESULT(s,a))
        * **MIN** picks action a in ACTIONS(s) that produces smallest value of MAX-VALUE(RESULT(s,a))
