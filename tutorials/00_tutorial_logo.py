import maxtikzlib.logo

fig = maxtikzlib.logo.generate_logo()
fig.compile_pdf(filename="mtl_logo.pdf")
