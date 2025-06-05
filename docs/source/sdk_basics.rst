.. _sdk_basics:

SDK Basics
============

Software Developer Kits (SDKs) are virtual "toolboxes" used to integrate or build applications. SDKs include ready-to-use resources for developers such as pre-made functions to help write, test and fix code, manuals and examples to explain usage, and pre-written code libraries.

    .. image:: imgs/sdk_basics/What-is-SDK-banner.jpg
       :alt: what is sdk

image source: https://www.geeksforgeeks.org/what-is-software-development-kit-sdk/

If you do not yet have experience using Open OnDemand to launch Jupyter Notebooks, please first review the documentation :ref:`High Performance Compute Portal`. Be sure to follow all instructions, including :ref:`Setting Up Conda Environments`

Flywheel's SDK is a set of pre-written functions and documentation allowing users to easily interact with the Flywheel database. Flywheel supports code integration in both :code:`Python` and :code:`Matlab`. Check out Flywheel's useful examples to get started `here <https://flywheel-io.gitlab.io/product/backend/sdk/tags/20.0.0/python/getting_started.html>`_ .

Common Use Cases
------------------
Why use the Flywheel SDK?... Using the Flywheel SDK, users can programmatically interact with Flywheel data and metadata, launch jobs, add or delete files, build and run reports, and more! While many basic functions are also available programmatically using Flywheel.io's CLI, the Python / Matlab SDK gives users greater flexibility and control.

Here are a couple common use cases:

    1. Retrieve, Edit, or Add Metadata

    2. Rename Acquisitions (e.g. to reproin naming convention)

    3. Run Analysis Gears in Batches

    4. Download Analysis Output Files

    5. Read Data Directly to Memory from Flywheel for Computations (e.g. nilearn plotting)


Flywheel Python SDK
---------------------
If you are interested in using the Flywheel Python SDK you need to first set up a conda environment and install the flywheel python package OR access an already built environment on RC nodes using `incenv` or `flywheel` conda environments.

Follow our example tutorial using the Flywheel SDK to :ref:`Flyhweel Software Developer Kit (SDK) Basics and Helpful Hints`.

Once you have a basic understanding of Flywheel's Python SDK, get started on some of the example use cases with our code examples on github `here <https://github.com/intermountainneuroimaging/flywheel_sdk_examples/tree/main>`_.
