# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'INC Flywheel Documentation'
copyright = '2022, Internmountain Imaging Consortium'
author = 'Lena & Amy'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser',
    'sphinx.ext.autosectionlabel',
    'nbsphinx',
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown'
}

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# npsphinx setting
nbsphinx_allow_errors = True