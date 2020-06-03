# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'mathdoc'
copyright = '2019, open_MODEX'
author = 'open_MODEX'

master_doc = 'index'

# -- svgjinja configuration ----------------------------------------------------

# jinja templates with file extension `.svg.j2` that should not be rendered
exclude_templates = ['base.svg.j2']

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.ifconfig',
    'fluiddoc.mathmacro',
    'svgjinja'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

#Necessary for some latex preamble things:
latex_elements = {
    'passoptionstopackages': r'\PassOptionsToPackage{svgnames}{xcolor}',
}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Mathjax options.
# See
#
#    https://www.sphinx-doc.org/en/master/usage/extensions/math.html#confval-mathjax_config
#
# for more information.
# This one in particular prevents mathematical equations from being centered,
# which would make the different equation blocks harder to compare.
mathjax_config = {
    "displayAlign": "left",
}

# https://www.sphinx-doc.org/en/master/usage/extensions/ifconfig.html
def setup(app):
    app.add_config_value('exclude_templates', exclude_templates, 'env')
