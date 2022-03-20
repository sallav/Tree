class Tree_node:

    def __init__(self, key=None, values=[]):
        self.parent = None
        self.children = []
        self.key = key
        self.values = values

    def setKey(self, key):
        self.key = key

    def setValues(self, values):
        self.values = values

    def addValue(self, value):
        try:
            self.values.append(value)
        except Exception as e:
            print("Error adding a value")
            print(e)

    def setParent(self, parent=None):
        self.parent = parent

    def setChild(self, child):
        try:
            self.children.append(child)
        except Exception as e:
            print("Error setting a child node")
            print(e)

    def getParent(self):
        return self.parent

    def getChildren(self):
        return self.children

    def isLeaf(self):
        if len(self.children)==0:
            return True
        else:
            return False

    def getKey(self):
        return self.key 

    def getValues(self):
        return self.values

    def isParentOf(self, child):
        return child in self.children

    def removeChild(self, child): 
        try: 
            for (index, item) in enumerate(self.children):
                if item is child:
                    self.children.pop(index)
                    return True
            return False
        except Exception as e:
            print("Error removing a child node")
            print(e)

    def removeParent(self):
        self.parent = None
    
    def toString(self):
        str = '{}: {}, \nparent: {}, children: {}'.format(self.key, self.values, self.parent, self.children)
        return str