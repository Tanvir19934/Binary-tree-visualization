import graphviz

class Node:
    nodes = []
    def __init__(self, data, parent=None, char='Root'):
        self.data = data
        self.left = None
        self.right = None
        self.char = char
        self.parent = parent
        Node.nodes.append(self)  # Append the node object to the list

    def insert(self, data):
        if self.data is None:
            self.data = data
        elif data <= self.data:
            if self.left is None:
                self.left = Node(data, self, char='L')
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data, self, char='R')
            else:
                self.right.insert(data)

    @classmethod
    def get_nodes(cls):
        return cls.nodes
    
    @staticmethod
    def visualize():
        # Get all node objects
        nodes = Node.get_nodes()
        
        dot = graphviz.Digraph('binary_tree', comment='Binary Tree Visualization',
                            node_attr={'color': 'lightblue', 'style': 'filled'})
        for item in nodes:
            dot.node(f'{item.data}', f'{item.data}\n{item.char}', {'color': 'lightblue', 'style': 'filled'})
            for elem in nodes:
                if item.left==elem:
                    dot.edge(f'{item.data}', f'{item.left.data}')
            for elem in nodes:
                if item.right==elem:
                    dot.edge(f'{item.data}', f'{item.right.data}')
        dot.render(filename='binary_tree', format='png', view=True)

# Example usage:
if __name__ == "__main__":
    # Create the root of the tree
    root = Node(10)

    # Insert nodes
    keys = [20, 11, 9, 30, 5, 15, 25, 35, 3, 1, 13, 31, 27, 7, 4, 24, 17, 8, 49]
    for key in keys:
        root.insert(key)
    root.visualize()


                