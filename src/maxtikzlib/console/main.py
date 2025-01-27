from maxtikzlib.figure import TikzFigure


def main():

    tikz = TikzFigure()

    path_actions = ["draw", "rounded corners", "line width=3"]

    # M
    nodes = [[0, 0], [0, 3], [1, 2], [2, 3], [2, 0]]
    for i, node_data in enumerate(nodes):
        tikz.add_node(
            node_data[0],
            node_data[1],
            f"M{i}",
            layer=0,
            color="red",
            content=f"Node {i}",
        )
    tikz.add_path(
        [f"M{i}" for i in range(len(nodes))], path_actions=path_actions, layer=1
    )

    print(tikz.generate_tikz())

    tikz_2 = TikzFigure(tikz_code=tikz.generate_tikz())

    print(tikz_2.generate_tikz())
    # with open('_standalone.tex','w') as f:
    #     f.write(tikz_2.generate_standalone())


if __name__ == "__main__":
    main()
