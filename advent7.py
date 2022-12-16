"""
Advent of Code 2022, Day 7
solution by Maja Sellmer
"""

class TreeNode:
    """
    standard tree implementation from codecademy
    added method get_size to calculate size of directories
    """
    def __init__(self, node_name, node_size=0):
        self.name = node_name
        self.children = []
        self.size = node_size

    def add_child(self, child_node):
        """
        adds child_node (type TreeNode) to children
        """
        self.children.append(child_node)

    def traverse(self):
        """
        traverses the tree from this node, printing all names
        """
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.name)
            nodes_to_visit += current_node.children

    def get_size(self):
        """
        retrieves the file size or calculates the directory size
        """
        if self.children == []:
            return self.size
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            self.size += current_node.size
            nodes_to_visit += current_node.children

with open('advent7.txt') as commands:
    commands_list = [command.rstrip("\n") for command in commands.readlines()]
    # first recreate the filesystem as a tree
    root = TreeNode("/")
    current_path = [root]
    all_nodes = [root]
    for command in commands_list:
        current_dir = current_path[-1]
        current_dir_children_names = [child.name for child in current_dir.children]
        # list command can be ignored
        if command == "$ ls":
            continue
        # change directory
        if command[:5] == "$ cd ":
            # go to root
            if command[5] == "/":
                current_path = [root]
            # move out one level
            elif command[5:7] == "..":
                current_path = current_path[:-1]
            # move in one level
            else:
                dir_name = command[5:]
                # search for the new directory among current children
                if dir_name in current_dir_children_names:
                    for child in current_dir.children:
                        if child.name == dir_name:
                            current_path.append(child)
                # if it doesn't exist yet, create new node
                else:
                    new_node = TreeNode(dir_name)
                    current_dir.add_child(new_node)
                    current_path.append(new_node)
                    all_nodes.append(new_node)
        else:
            this_line = command.split(" ")
            name = this_line[1]
            # check if a node for this file/directory already exists
            if name in current_dir_children_names:
                continue
            # otherwise create it
            if this_line[0] == "dir":
                new_node = TreeNode(name)
                current_dir.add_child(new_node)
                all_nodes.append(new_node)
            else:
                new_node = TreeNode(name, int(this_line[0]))
                current_dir.add_child(new_node)
                all_nodes.append(new_node)
    # calculate size of all directories
    for node in all_nodes:
        node.get_size()
    # small_directories_sum = 0
    # calculate how much space needs to be freed
    free_space = 70000000 - root.size
    space_to_be_freed = 30000000 - free_space
    print("There is {} free space, {} needs to be freed.".format(free_space, space_to_be_freed))
    # find smallest directory bigger than that amount
    smallest_candidate = root
    for node in all_nodes:
        # if node.size > 100000 or node.children == []:
        #     continue
        # small_directories_sum += node.size
        if node.size < space_to_be_freed or node.children == []:
            continue
        if node.size >= smallest_candidate.size:
            continue
        smallest_candidate = node
    # print(small_directories_sum)
    print(smallest_candidate.size)
