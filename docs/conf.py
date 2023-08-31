# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'difPy Guide'
copyright = '2023, Elise Landman'
author = 'Elise Landman'

release = 'v4.0.0'
version = 'v4.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_rtd_theme',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for output
formats:
  - epub
  - pdf


def setup(app):
   app.add_css_file('static/css/custom.css')