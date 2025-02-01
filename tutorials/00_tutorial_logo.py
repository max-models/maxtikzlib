from maxtikzlib.figure import TikzFigure
import numpy as np

fig = TikzFigure()

path_actions = ["draw", "rounded corners=8pt", "line width=6"]
colors = ["purple", "blue", "purple"]

# M with thick tracing
nodes_M = [
    [0, 0],
    [0, 3.5],
    [1, 3.5],
    [1.25, 2.75],
    [1.5, 3.5],
    [2.5, 3.5],
    [2.5, 0],
    [2, 0],
    [2, 2.75],
    [1.25, 2.0],
    [0.5, 2.75],
    [0.5, 0],
]
for i, node_data in enumerate(nodes_M):
    fig.add_node(node_data[0], node_data[1], f"M{i}", layer=0, color=colors[0])
fig.add_path(
    [f"M{i}" for i in range(len(nodes_M))],
    path_actions=path_actions,
    layer=2,
    cycle=True,
    color=colors[0],
    fill=f"{colors[0]}!50!white",
)

# T with thick tracing
nodes_T = [
    [3.125, 0],
    [3.125, 4],
    [0, 4],
    [0, 4.75],
    [7, 4.75],
    [7, 4],
    [3.875, 4],
    [3.875, 0],
]
for i, node_data in enumerate(nodes_T):
    fig.add_node(node_data[0], node_data[1], f"T{i}", layer=0, color=colors[1])
fig.add_path(
    [f"T{i}" for i in range(len(nodes_T))],
    path_actions=path_actions,
    layer=0,
    cycle=True,
    color=colors[1],
    fill=f"{colors[1]}!50!white",
)

# L with thick tracing
nodes_L = [[4.5, 0], [4.5, 3.5], [5.25, 3.5], [5.25, 0.75], [7, 0.75], [7, 0]]
for i, node_data in enumerate(nodes_L):
    fig.add_node(node_data[0], node_data[1], f"L{i}", layer=0, color=colors[2])
fig.add_path(
    [f"L{i}" for i in range(len(nodes_L))],
    path_actions=path_actions,
    layer=2,
    cycle=True,
    color=colors[2],
    fill=f"{colors[2]}!50!white",
)

xvec = np.arange(0, 7, 0.1)
yvec = np.sin(xvec) * 0.25 + 1.25
# print(x)
nodes_line = []
for x, y in zip(xvec, yvec):
    nodes_line.append([x, y])
for i, node_data in enumerate(nodes_line):
    fig.add_node(node_data[0], node_data[1], f"Line{i}", layer=0)
fig.add_path(
    [f"Line{i}" for i in range(len(nodes_line))],
    path_actions=path_actions,
    layer=1,
    color="black",
)


# print(fig.generate_tikz())

fig.compile_pdf(filename="mtl_logo.pdf")
