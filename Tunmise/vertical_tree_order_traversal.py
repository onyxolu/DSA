class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        '''
        I can visit the tree layer by layer to get each node's coordinates
        and then put them in a dictionary whose keys are X while values are 
        node.val.
        2 things to note:
        1, when handling the same layer, for nodes in same position, I need to
        put smaller value one ahead of larger one
        2, when the visit finishes, I need to sort keys so that reported results
        are from left to right
        '''
        if not root:
            return []
        d = {}
        nodesInCurrentLayer = [(root, 0)] #each node in layer is represented by a tuple of (node, X value)
        nodesInNextLayer    = []
        while(len(nodesInCurrentLayer) > 0): #use BFS to navigate layer by layer
            tempDict = {}
            while(len(nodesInCurrentLayer) > 0):
                nodeWithX = nodesInCurrentLayer.pop(0)
                #add childrens of next layer
                if nodeWithX[0].left:
                    nodesInNextLayer.append((nodeWithX[0].left, nodeWithX[1] - 1))
                if nodeWithX[0].right:
                    nodesInNextLayer.append((nodeWithX[0].right, nodeWithX[1] + 1))
                #add node's value and X to a temp list
                if tempDict.get(nodeWithX[1]) == None:
                    tempDict[nodeWithX[1]] = []
                tempDict[nodeWithX[1]].append(nodeWithX[0].val)
                
            #now tempDict looks like {'x1':[val1, val2],'x2':[val3, val4]} 
            #need to sort each [val1, val2]., [val3, val4]
            for key in tempDict:       
                if d.get(key) == None:
                    d[key] = []
                d[key] += sorted(tempDict[key]) 
            
            nodesInCurrentLayer = nodesInNextLayer
            nodesInNextLayer    = [] #remember to do this!
            #end of the first while

        res = []
        for x in sorted(d.keys()): #don't forget to sort keys
            res.append(d[x])
        
        return res
    
            