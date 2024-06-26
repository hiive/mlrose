""" Classes for defining fitness functions."""

# Author: Genevieve Hayes (Modified by Andrew Rollings)
# License: BSD 3 clause



class MaxKColor:
    """Fitness function for Max-k color optimization problem. Evaluates the
    fitness of an n-dimensional state vector
    :math:`x = [x_{0}, x_{1}, \\ldots, x_{n-1}]`, where :math:`x_{i}`
    represents the color of node i, as the number of pairs of adjacent nodes
    of the same color.

    Parameters
    ----------
    edges: list of pairs
        List of all pairs of connected nodes. Order does not matter, so (a, b)
        and (b, a) are considered to be the same.

    Example
    -------
    .. highlight:: python
    .. code-block:: python

        >>> import mlrose_hiive
        >>> import numpy as np
        >>> edges = [(0, 1), (0, 2), (0, 4), (1, 3), (2, 0), (2, 3), (3, 4)]
        >>> fitness = mlrose_hiive.MaxKColor(edges)
        >>> state = np.array([0, 1, 0, 1, 1])
        >>> fitness.evaluate(state)
        3

    Note
    ----
    The MaxKColor fitness function is suitable for use in discrete-state
    optimization problems *only*.

    If this is a cost minimization problem: lower scores are better than
    higher scores. That is, for a given graph, and a given number of colors,
    the challenge is to assign a color to each node in the graph such that
    the number of pairs of adjacent nodes of the same color is minimized.

    If this is a cost maximization problem: higher scores are better than
    lower scores. That is, for a given graph, and a given number of colors,
    the challenge is to assign a color to each node in the graph such that
    the number of pairs of adjacent nodes of different colors are maximized.
    """

    def __init__(self, edges, maximize=False):

        # Remove any duplicates from list
        edges = list({tuple(sorted(edge)) for edge in edges})

        self.graph_edges = None
        self.edges = edges
        self.prob_type = 'discrete'
        self.maximize = maximize

    def evaluate(self, state):
        """Evaluate the fitness of a state vector.

        Parameters
        ----------
        state: array
            State array for evaluation.

        Returns
        -------
        fitness: float
            Value of fitness function.
        """

        fitness = 0

        # this is the count of neigbor nodes with the same state value.
        # Therefore state value represents color.
        # This is NOT what the docs above say.

        edges = self.edges if self.graph_edges is None else self.graph_edges

        if self.maximize:
            # Maximise the number of adjacent nodes not of the same colour.
            fitness = sum(int(state[n1] != state[n2]) for (n1, n2) in edges)
        else:
            # Minimise the number of adjacent nodes of the same colour.
            fitness = sum(int(state[n1] == state[n2]) for (n1, n2) in edges)
        return fitness

    def get_prob_type(self):
        """ Return the problem type.

        Returns
        -------
        self.prob_type: string
            Specifies problem type as 'discrete', 'continuous', 'tsp'
            or 'either'.
        """
        return self.prob_type

    def set_graph(self, graph):
        self.graph_edges = [e for e in graph.edges()]
