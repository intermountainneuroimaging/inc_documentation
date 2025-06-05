.. _petalibrary_and_blanca:

Get to Know Your Scratch Space
===============================
We encourage all users to utilize the large scratch filesystem mounted on :code:`Blanca` and :code:`Alpine`. Scratch filesystems offer a fast, safe environment for quick development and troubleshooting.

.. warning::
    The scratch filesystem purges files more than 90 days old! This is not a permanent file storage. Any files you wish to retain permanently should be moved to **Petalibrary** or uploaded to **Flywheel**.

Where to find :code:`Scratch` for each Cluster.

+----------+------------------------------------+-------+---------------------------------------------------------------------------+
| Cluster  | Scratch Filesystem                 | Size  | Mounted Locations                                                         |
+==========+====================================+=======+===========================================================================+
| Blanca   | :code:`/scratch/alpine/<user>/`    | 10 TB | Mounted read-write on all BLANCA (login and compute) nodes                |
+----------+------------------------------------+-------+---------------------------------------------------------------------------+
| Alpine   | :code:`/scratch/alpine/<user>/`    | 10 TB | Mounted read-write on all ALPINE nodes (compile, compute)                 |
+----------+------------------------------------+-------+---------------------------------------------------------------------------+


Using my Scratch Space
------------------------
If you are not sure how to log on to CU Boulder Research Computing resources, please go back to read about the :ref:`High Performance Compute Portal`. Be sure to access the scratch filesystem from the appropriate compute or compile nodes (see breakdown above).

Leverage Scratch Space with Flywheel Storage
++++++++++++++++++++++++++++++++++++++++++++++++
Some neuroimaging analyses and workflows are not yet supported as Flywheel gears. For these workflows, the current workaround is to download your Flywheel analyses (or workflow inputs) run the workflow on your local machine (or HPC), then upload the results (workflow outputs) back to flywheel as a new analysis.

Follow our example tutorial using the Flywheel SDK to :ref:`Download and Run Analysis Locally`.

Uploading Scratch Analyses to Flywheel
++++++++++++++++++++++++++++++++++++++++++++++++
Once you generate an analysis you wish to permanently store. Be sure to move the analysis to Petalibrary, or upload the analysis to Flywheel.

Follow our example tutorial using the Flywheel SDK to upload files to Flywheel :ref:`Upload My Analysis to Flywheel`


