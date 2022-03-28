from tree import TreeNode
from bfs import bfs

sample_root_node = TreeNode("1")
docs = TreeNode("1.1")
photos = TreeNode("1.2")
sample_root_node.children = [docs, photos]
my_wish = TreeNode("2.1.1.txt")
my_todo = TreeNode("2.1.2.txt")
my_cat = TreeNode("2.2.1.jpg")
my_dog = TreeNode("2.2.2.jpg")
docs.children = [my_wish, my_todo]
photos.children = [my_cat, my_dog]

print(sample_root_node)
# Change the 2nd argument below
goal_path = bfs(sample_root_node, "2.2.2.jpg")
if goal_path is None:
  print("No path found")
else:
  print("Path found")
  for node in goal_path:
    print(node.value)
