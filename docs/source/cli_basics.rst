.. _cli_basics:

CLI Basics
============

CLI From Local Computer
************************

Follow the steps below to interact with Flywheel from the command line interface on your own personal computer.
    1. Install the CLI on the machine from which you'd like to transfer data to/from Flywheel using the `Flywheel CLI Guide <https://docs.flywheel.io/hc/en-us/articles/360008162214-Installing-the-Flywheel-Command-Line-Interface-CLI->`_

    2. Now that the CLI is installed, if you'd like to ingest BIDS data from your local machine into Flywheel, follow the `Flywheel BIDS Ingestion Guide <https://docs.flywheel.io/hc/en-us/articles/360008162174>`_. For example, the command to ingest a single BIDS session (for subject 101, session S1) for a project called TEST, which is in group **sample** is:

         :code:`fw ingest bids -p TEST --subject 101 --session S1 <path_to_your_BIDS_folder> sample`

    3. If you'd like to ingest raw dicom data from your local machine into Flywheel, follow the `Flywheel Dicom Ingestion Guide <https://docs.flywheel.io/hc/en-us/articles/4536060470035>`_. For example, the command to ingest the raw dicoms for a single session (for subject 101, session S1) for a project called TEST, which is in group **sample** is:

         :code:`fw ingest dicom <path_to_your_dicom_folder> sample TEST --subject 101 --session S1`

    4. For a full list of other Flywheel command line features (including checking login status, managing server jobs, exporting and downloading data, and much more), review the `Flywheel CLI Overview <https://docs.flywheel.io/hc/en-us/articles/4536067900435-Command-Line-Interface-Overview>`_

CLI From Blanca Compute Node
****************************

For your convenience, the Flywheel CLI is already installed in a Conda environment on PetaLibrary. To use the Flywheel CLI from a compute node, follow the steps below:

    1. Log in to a Blanca compute node (interactive session, JupyterHub, or even a Summit compute node will work)

    2. Load the latest Anaconda3 module:

         :code:`source /curc/sw/anaconda3/latest`

    3. Activate the *flywheel* conda environment:

         :code:`conda activate flywheel`

    4. Check the flywheel status to ensure you are logged in as the correct user:

         :code:`fw status`

    5. If you are not logged with yourself as the user, log in to the Flywheel API with your Flywheel API key:

         :code:`fw login <your_api_key>`

    6. Now you are ready to run any FW API command (refer to the section above for specific commands)

.. note:: **Special Instructions for Large Uploads**: Even though the Flywheel CLI lives on PetaLibrary in the conda environment called *flywheel*, the cache for all temporary data is hard coded to go to your *home* directory on PetaLibrary. However, because your *home* directory is so small, this cache can quickly fill up resulting in the upload failing and your *home* directory full. To avoid this issue, you should create a soft link between your *home* cache directory and your *projects* cache directory, which is much large, ie:

         :code:`/home/<identiKey>/.cache/flywheel -> /projects/<identiKey>/.cache/flywheel`
