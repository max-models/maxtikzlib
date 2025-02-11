import maxtikzlib.logo

fig = maxtikzlib.logo.generate_logo()
fig.compile_pdf(filename="output/mtl_logo.pdf")