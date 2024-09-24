# Created by: Ian McCourt
from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


root = Node("Start")
node1 = Node("1")
node2 = Node("2")
node3 = Node("3")
node4 = Node("4")
node5 = Node("5")
node6 = Node("6")
node7 = Node("7")
node8 = Node("8")
node9 = Node("9")
node10 = Node("10")
node11 = Node("11")
node12 = Node("Goal")

root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
node4.left = node5
node4.right = node6
node5.left = node7
node5.right = node8
node8.left = node9
node8.right = node10
node10.left = node11
node10.right = node12


def DFS(root, target):
    def dfs_path(node, target, path):
        if node is None:
            return None

        path.append(node.value)
        print(f"DFS current path: {path}")

        if node.value == target:
            return path

        left_path = dfs_path(node.left, target, path)
        right_path = dfs_path(node.right, target, path)

        if left_path is not None:
            return left_path
        if right_path is not None:
            return right_path

        path.pop()
        return None

    return dfs_path(root, target, [])

def BFS(root, target):
    def bfs_path(node, target):
        queue = deque([(node, [])])

        while queue:
            current, path = queue.popleft()

            if current is None:
                continue

            path.append(current.value)
            print(f"BFS current path: {path}")

            if current.value == target:
                return path

            queue.append((current.left, path.copy()))
            queue.append((current.right, path.copy()))

        return None

    return bfs_path(root, target)


path = DFS(root, "Goal")

print(f"Path to Goal with DFS: {path}")

path = BFS(root, "Goal")

print(f"Path to Goal with BFS: {path}")

