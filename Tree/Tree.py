import Tree_node as Tnode
import Tree_func as Func

class Tree:

    def __init__(self, root=Tnode.Tree_node()):
        self.root = root
        self.height = 0

    def getRoot(self):
        return self.root

    def getHeight(self):
        self.setHeight()
        return self.height

    def setHeight(self):
        try:
            self.height = self.calculateHeight(self.root, 0)
        except Exception as e:
            print("Error setting trees height")
            print(e)

    def calculateHeight(self, root, level):
        try: 
            if root.isLeaf():
                return level
            else:
                chn = root.getChildren()
                heighest = 0
                for child in chn:
                    if not child or child is None:
                        break
                    else:
                        nl = level + 1
                        nheight = self.calculateHeight(child, nl)
                        if nheight is None or nheight<heighest:
                            continue
                        else:
                            heighest = nheight
                return heighest
        except Exception as e:
            print("Error calculating tree height")
            print(e)
            return None

    def printContent(self):
        print("Tree content: ")
        self.printNode(self.root)

    def printNode(self, root):
        print(root.toString())
        if not root.isLeaf():
            chn = root.getChildren()
            for child in chn:
                self.printNode(child)