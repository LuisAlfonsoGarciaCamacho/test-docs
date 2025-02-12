# docs/conf.py
import os
import sys

sys.path.insert(
    0, os.path.abspath("../src")
)  # Asegúrate de que Sphinx pueda encontrar los módulos

# -- Project information -----------------------------------------------------

project = "Mi Proyecto"
author = "Tu Nombre"

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",  # Para generar documentación a partir de docstrings
    "sphinx.ext.napoleon",  # Para soportar el formato Google-style docstring
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"

# docs/source/conf.py
import os
import sys

sys.path.insert(0, os.path.abspath("../../src"))  # Ruta a la carpeta 'src'
