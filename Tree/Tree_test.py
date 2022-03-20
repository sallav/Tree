import re
import Tree_node as Tnode
import Tree
import Tree_func as Func
import Tree_builder as Builder

# Tree_node testing:

node = Tnode.Tree_node()
node.setKey("Key1")
node.setValues(["Val", "Val2"])
node.addValue("Val3")
p = Tnode.Tree_node()
c = Tnode.Tree_node()
node.setParent(p)
node.setChild(c)

str = '{}: {}, \nparent: {}, children: {}'.format(node.getKey(), node.getValues(), node.getParent(), node.getChildren())
print(str)
str2 = node.toString()
print(str2)
print(str == str2)

print(node.isParentOf(c))
node.removeChild(c)
node.removeParent()
str3 = node.toString()
str4 = '{}: {}, \nparent: {}, children: {}'.format(node.getKey(), node.getValues(), None, [])
print(str3)
print(str3 == str4)

# Tree testing

tree = Tree.Tree(node)
tree2 = Tree.Tree()

root = tree.getRoot()
n1 = Tnode.Tree_node("Tervehdys", ["Moi"])
n2 = Tnode.Tree_node("Myöntö", ["Joo"])
n3 = Tnode.Tree_node("Kielto", ["Ei"])
root.setChild(n1)
n1.setParent(root)
n2.setChild(n3)
n3.setParent(n2)
root.setChild(n2)
n2.setParent(root)

tree.printContent()
tree.setHeight()
h=tree.getHeight()
print("Height: {}".format(h))

print(root.isParentOf(n2))

n4 = Tnode.Tree_node("Vastaus", ["Haloo"])
n3.setChild(n4)
n4.setParent(n3)
tree.setHeight()
h = tree.getHeight()
print("New height: {}".format(h))

# Tree_func testing

n5 = Tnode.Tree_node("Moikkaus", ["Moro"])
f = Func.Tree_func()
f.addNode(n4, n5)
h = tree.getHeight()
print("Height before: {}".format(h))

a = f.search(root, "Vastaus")
print(a.toString())

f.removeNode(a)
h2 = tree.getHeight()
print("Height after: {}".format(h2))
print(h2<h)

# Tree_builder testing

tb = Builder.Tree_builder()

tb.add_tree(tree)
tb.add_new_tree("Tervehdys", "Moi")
tree1 = tb.getTree(0)
print(tree.getRoot()==tree1.getRoot().getRoot())

