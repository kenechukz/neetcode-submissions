"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        """
        R:
        given node

        return deep copy of graph

        E: 
        null node -> return None

        no neighbours -> return


        A:

        for each node in neighbours of node 

        create a new node and add that node to list for startNode
        """

        if node == None:
            return None


        adjList = {}
        startNode = Node(node.val)

        def dfs(nodeRef):
            
            newNode = Node(nodeRef.val)
            adjList[nodeRef.val] = newNode

            for n in nodeRef.neighbors:
                if n.val not in adjList:
                    newNode.neighbors.append(dfs(n))
                else:
                    newNode.neighbors.append(adjList[n.val])

            return newNode

        return dfs(node)

        