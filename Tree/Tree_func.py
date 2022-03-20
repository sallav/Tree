import Tree_node as tnode

class Tree_func:


    def search(self, root, key):
        try:
            if root.getKey() is not key:
                chn = root.getChildren()
                if chn:
                    for child in chn:   
                        found = self.search(child, key)  # search tree recursively
                        if found is None:
                            continue    # If not found continue to next branch
                        else:
                            return found
                else: 
                    return None         # Hitted leaf
            else: 
                return root
        except Exception as e:
            print("Error searching a tree")
            print(e)
            return None

    @staticmethod 
    def addNode(parent, child):
        try:
            parent.setChild(child)
            child.setParent(parent)
        except Exception as e:
            print("Error adding a node")
            print(e)

    @staticmethod
    def removeNode(node):
        try:
            parent = node.getParent()
            parent.removeChild(node)
            node.removeParent()
        except Exception as e:
            print("Error removing a node")
            print(e)

