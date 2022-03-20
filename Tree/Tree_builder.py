import Tree
import Tree_node as Tnode

class Tree_builder:

    def __init__(self):
        self.trees = []

    def add_new_tree(self, key=None, values=None):
        try:
            tree = Tree.Tree()
            tree.getRoot().setKey(key)
            tree.getRoot().setValues(values)
            self.trees.append(tree)
        except Exception as e:
            print("Error adding a new tree")
            print(e)

    def add_tree(self, node):
        try:
            tree = Tree.Tree(node)
            self.trees.append(tree)
        except Exception as e:
            print("Error adding a tree")
            print(e)
    
    def getTree(self, index):
        try:
            for (ind, item) in enumerate(self.trees):
                if ind == index:
                    return item
            return None
        except Exception as e:
            print("Error in finding the tree")
            print(e)
            return None

    def getTrees(self):
        return self.trees