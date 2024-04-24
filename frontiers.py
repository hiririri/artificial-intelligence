import heapq
from collections import deque 

"""
This module contains the different Frontier classes to run the search algorithms in an observable environment. 

@author: Hugo Gilbert
"""
class Frontier:
    """ Class to represent the frontier in the AStar algorithm.
    
    Attributes
    ----------
    frontier : list
        A list representing the frontier. It contains pairs where the first element is an AStar score and the second element is a node.    
    frontierDict : dict
        A dictionary to know which nodes are in the frontier and at   representing the frontier. It contains pairs where the first element is an AStar score and the second element is a node.

    Methods
    -------
    push(score, node)
        Pushes a new node in the fontier 
    pop()
        Pops the search node with smallest AStar score
    isEmpty()
        Checks if the frontier is empty
    """

    def __init__(self):
        self.frontier = []
    
    def __str__(self):
        return " ".join((str(x) + str(y)) for (x,y) in self.frontier)

    def push(self, score, node):
        """ Pushes a new node in the fontier. 
        If the node is already present, the method checks the current Astar score of the node to decide which one to keep.

        Parameters
        ----------
        score : int
            The AStar score of the node to be stored.
        node : Node
            The search node to be stored.

        """
        found = False
        for i in range(len(self.frontier)):
            (s,n) = self.frontier[i]
            if node.state == n.state:
                found = True
                if s > score:
                    self.frontier.pop(i)
                    heapq.heappush(self.frontier, (score, node))
                break
        if(found is False):
            heapq.heappush(self.frontier, (score, node))
        
    def pop(self):
        """ Pops the search node with smallest AStar score. 

        Returns
        -------
        (int, Node)
            A pair with the search node with smallest AStar score (in second position), and the smallest AStar score (in first position).
        """
        return heapq.heappop(self.frontier)
        
    def isEmpty(self):
        """ Checks if the frontier is empty.

        Returns
        -------
        bool
            True if the frontier is empty else False.
        """
        return len(self.frontier) == 0   


class FrontierFIFO:
    """ Class to represent the frontier in the breadth first search algorithm.
    
    Attributes
    ----------
    frontier : deque
        A doubly ended queu representing the frontier.     
    
    Methods
    -------
    push(node)
        Pushes a new node in the fontier 
    pop()
        Pops the next search node following FIFO order
    isEmpty()
        Checks if the frontier is empty
    """

    def __init__(self):
        self.frontier = deque()
        self.elements = set()
    
    def __str__(self):
        return " ".join(str(x) for x in self.frontier)

    def push(self, node):
        """ Pushes a new node in the fontier. 
        If the node is already present, the push is not realized.

        Parameters
        ----------
        node : Node
            The search node to be stored.

        """
        if(node.state in self.elements):
            return
        self.elements.add(node.state)
        self.frontier.appendleft(node)
        
    def pop(self):
        """ Pops the search node following the FIFO order. 

        Returns
        -------
        Node
            the next search node following the FIFO order.
        """
        res = self.frontier.pop()
        self.elements.discard(res.state)
        return res 
        
    def isEmpty(self):
        """ Checks if the frontier is empty.

        Returns
        -------
        bool
            True if the frontier is empty else False.
        """
        return len(self.frontier) == 0

class FrontierLIFO:
    """ Class to represent the frontier in the depth-first search algorithm.
    
    Attributes
    ----------
    frontier : list
        A list representing the frontier.     
    
    Methods
    -------
    push(node)
        Pushes a new node in the fontier 
    pop()
        Pops the next search node following the LIFO order.
    isEmpty()
        Checks if the frontier is empty
    """

    def __init__(self):
        self.frontier = []
    
    def __str__(self):
        return " ".join(str(x) for x in self.frontier)

    def push(self, node):
        """ Pushes a new node in the fontier. 

        Parameters
        ----------
        node : Node
            The search node to be stored.

        """
        self.frontier.append(node)
        
    def pop(self):
        """ Pops the next search node following the LIFO order. 

        Returns
        -------
        Node
            The next search node following the LIFO order. 
        """
        return self.frontier.pop()
        
    def isEmpty(self):
        """ Checks if the frontier is empty.

        Returns
        -------
        bool
            True if the frontier is empty else False.
        """
        return len(self.frontier)==0  

     
