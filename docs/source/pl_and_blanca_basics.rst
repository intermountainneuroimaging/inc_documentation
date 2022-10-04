.. _petalibrary_and_blanca:

The Basics
===============
Placeholder...

Placeholder `here <https://curc.readthedocs.io/en/latest/gateways/OnDemand.html>`_!


High Performance Compute Portal
================================

CU Boulder Reserach Computing (CURC) supports a browser based HPC Portal, **Open OnDemand** `here <https://curc.readthedocs.io/en/latest/gateways/OnDemand.html>`_. This browser based portal allows users to navigate and interact with CURC's HPC from any anywhere with an internet connection! Its fast and easy one stop shop for your HPC needs.

Please visit CURC documentation on `Open OnDemand <https://curc.readthedocs.io/en/latest/gateways/OnDemand.html>`_ for a step by step guide.

In the document below we will talk through the methods you need to access the HPC environment and get started with your own neuroimaging analyses. First, lets consider your "use case." How will you be using HPC? Once you have that answer in mind, let us work through the following questions.

Do you need a Desktop?
-----------------------
In your *use case* will you need to interact with a graphical user interface (GUI)? Some examples where you may need a desktop include using `CONN: Functional Connectivity Toolbox <https://web.conn-toolbox.org/>`_, viewing spreadsheets, or html reports, viewing data or images such as nifti images or surface meshes. Most other cases (such as moving/copying/deleting files, running bash or python code, etc.) can be achieved without a User Desktop.

  :If you answer "Yes":
    You will use Open OnDemand to start a new "Core Desktop" Interactive session. Follow the instructions in :ref:`Using Core Desktop` to get started.


  :If you answer "No":
    Without a desktop, we recommend you use an interactive "Jupyter Notebook" session. Follow the instructions in :ref:`Using Jupyter Notebook (New)` to get started.


Using Core Desktop
+++++++++++++++++++++
Core Desktop is used to open a "Desktop" view into the HPC. The desktop is run on CURC's **viz nodes** which are special GPU accelerated login nodes designed to support running desktop viewers for multiple users.

To get started, go to `open ondemand <https://ondemand.rc.colorado.edu>`_.

1. From the dropdown list of "Interactive Sessions", Select **Core Desktop**

.. image:: imgs/pl_and_blanca_basics/open-ondemand-coredesktop.png
   :alt: Selecting Core Desktop from Interactive Sessions on Open OnDemand
   :width: 200pt

2. Set the compute options for your **Core Desktop** session.

.. image:: imgs/pl_and_blanca_basics/open-ondemand-coredesktop-options.png
   :alt: Selecting Core Desktop from Interactive Sessions on Open OnDemand
   :width: 200pt

3. Launch the new Desktop. Here you can start a terminal, or another application.
.. image:: imgs/pl_and_blanca_basics/open-ondenmand-coredesktop-terminal.png
   :alt: Selecting Core Desktop from Interactive Sessions on Open OnDemand
   :width: 200pt

.. Note::
    the Desktop is running on a **viz node**. To access filesystems and compute nodes exclusive to Blanca, you must first start a secure shell (SSH) to blanca login nodes.

Scratch and Blanca Compute From Desktop
********************************************
At present, some CURC resources are not accessible directly from the viz nodes used to house Core Desktop sessions. Therefore, we must first move to either a :code:`Blanca head node` or :code:`Alpine compile node` to access scratch filesystem and run compute jobs.

The easiest way to do this is using secure shell (SSH)

.. code-block::

    # to log into Blanca head nodes
    ssh -X blogin01

    # to log into Alpine compile nodes
    module load slurm/alpine
    acompile

Using Jupyter Notebook (New)
++++++++++++++++++++++++++++++
In most cases, actions you need to take on the HPC can be done using a terminal or within python using a Jupyter Notebook or Console. Want to learn more about Jupyter Notebooks? read up `here <https://curc.readthedocs.io/en/latest/gateways/jupyterhub.html>`_.

To get started, go to `open ondemand <https://ondemand.rc.colorado.edu>`_.

1. From the dropdown list of "Interactive Sessions", Select **Jupyter Notebook (New)**

.. image:: imgs/pl_and_blanca_basics/open-ondemand-interactivesessions.png
   :alt: Selecting Jupyter Notebook from Interactive Sessions on Open OnDemand
   :width: 200pt

2. Set the compute options for your **Jupyter Notebook** session. Be careful to correctly set both the partition and QOS section, to match the desired cluster. Here are examples of correct partition/QOS settings:

:Blanca Cluster:
   | Partition:  :code:`blanca-ics`
   | QOS:        :code:`blanca-ics`

:Alpine Cluster:
   | Partition:  :code:`amilan`
   | QOS:        <leave blank>

.. image:: imgs/pl_and_blanca_basics/open-ondemand-blanca-jupyterhub.png
   :alt: Setting compute options for jupyter notebook session.
   :width: 200pt

.. Note::
    The new jupyter notebook session will be launched from a :code:`Blanca` or :code:`Alpine` compute node depending on your preference.

3. You can use the **Terminal** feature to run any shell scripts, as well as the Python **Console** and Python **Jupyter Notebook** for any python based scripts.

Keep Reading to learn more about about leveraging the large :code:`Scratch` filesystem with Flywheel for local analyses.


