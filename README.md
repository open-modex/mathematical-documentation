# Mathematical documentation of open_MODEX frameworks

[![Documentation](https://readthedocs.org/projects/open-modex-mathdoc/badge/?version=latest)](https://open-modex-mathdoc.readthedocs.io/en/latest/?badge=latest)

Click on the badge to get to the compiled version of the mathematical documentation.

To write the documentation, use an editor of your choice and add your formulas in the respective rst file in `doc/source/frameworks`.

Graph descriptions written in the DOT language are rendered with a sphinx extension, that requires Graphviz, a cross-platform open source graph visualization software, that can be downloaded from [here](https://graphviz.org/).

Compiling is done by sphinx, therefore you need a python environment.
If you use conda, you can install the necessary packages doing the following steps:

1. Download the [environment file](https://github.com/open-modex/mathematical-documentation/blob/master/mathdoc.yml).
2. Launch a new command prompt (Windows: Win+R, type "cmd", Enter)
3. Install it via conda by `conda env create -f mathdoc.yml`.
4. Each time you open a new terminal for compiling, you can activate the environment by `conda activate mathdoc`.

You can build the html pages with the following command while you are in the `doc` folder (ensure that you have a subfolder in `doc` named `build` and a subfolder named `_static` in `doc/source`). Make sure to update the `graphviz_dot` argument to point to the correct location of the `dot` executable on your system:

    sphinx-build -b html -D graphviz_dot=C:\path\to\dot.exe source build
