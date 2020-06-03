""" Render SVG files with Jinja2 templating engine
"""

import os

from jinja2 import Environment, FileSystemLoader

def svgjinja(app, config):
    """

    Sources
    -------
    https://github.com/adafruit/circuitpython/blob/master/docs/rstjinja.py
    https://stackoverflow.com/questions/11857530/how-do-i-render-jinja2-output-to-a-file-in-python-instead-of-a-browser
    https://stackoverflow.com/questions/31190537/recursive-search-of-file-with-specific-extension
    https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python
    https://stackoverflow.com/questions/4444923/get-filename-without-extension-in-python/4444952

    """

    for root, dirs, files in os.walk(app.confdir):
        env = None
        for f in files:
            if f.endswith('.svg.j2') and f not in config.exclude_templates:
                if not env:
                    env = Environment(loader=FileSystemLoader(root))
                template = env.get_template(f)
                output = template.render()

                filepath = os.path.join(
                        root, os.path.splitext(f)[0])

                with open(filepath, "w") as f:
                    f.write(output)

def setup(app):
    app.connect("config-inited", svgjinja)
