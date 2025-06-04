.. _cli_basics:

CLI Basics
============
Flywheel's Command Line Interface (CLI) permits users to easily ingest and export data from Flywheel as well as interact with data including running gears and listing file contents.

CLI From Local Computer
************************

Follow the instruction here to install the Flywheel CLI and log-in (`Flywheel CLI Guide <https://docs.flywheel.io/hc/en-us/articles/360008162214-Installing-the-Flywheel-Command-Line-Interface-CLI->`_).

Test your installation...

    :code:`fw status`

Common Use Cases
*****************

1. **Ingesting a BIDS dataset as a Flywheel Project.** Follow the `Flywheel BIDS Ingestion Guide <https://docs.flywheel.io/hc/en-us/articles/360008162174>`_. For example, the command to ingest a single BIDS session (for subject 101, session S1) for a project called TEST, which is in group **sample** is:

    :code:`fw ingest bids -p TEST --subject 101 --session S1 <path_to_your_BIDS_folder> sample`

2. **Ingest DICOM files.** If you'd like to ingest raw dicom data from your local machine into Flywheel, follow the `Flywheel Dicom Ingestion Guide <https://docs.flywheel.io/hc/en-us/articles/4536060470035>`_. For example, the command to ingest the raw dicoms for a single session (for subject 101, session S1) for a project called TEST, which is in group **sample** is:

    :code:`fw ingest dicom <path_to_your_dicom_folder> sample TEST --subject 101 --session S1`

3. **Export BIDS Formatted Dataset**. For post-processing outside of Flywheel, exporting data to a public repository, and for other use cases its helpful to export data as BIDS formatted project.

    :code:`fw export bids <path_to_your_dicom_folder> sample TEST --subject 101 --session S1`


4. **Export Analysis Derivatives**. In many cases, users may elect to export analysis output files to a local server.

    :code:`fw download <flywheel_lookup_path_to_file>`
  Example...
    :code:`fw download "ics/flanker/01/S1/analyses/(lower run-01) bids-feat 11/13/24 13:56:15/files/feat_6735126f5911e143e4ce26d6.zip"`

  Most *.zip analysis outputs are stored in the format <analysis-id>/<gear-name>/...contents... Users who wish to learn more about handling this directory convention should visit our Flywheel SDK Examples repository `here <https://github.com/intermountainneuroimaging/flywheel_sdk_examples/tree/main/3_tables_and_downloads>`_

:IMPORTANT: Notice that the example commands above use the flywheel client "fw", the "fw-beta" command does not have the same functionality.

For a full list of other Flywheel command line features (including checking login status, managing server jobs, exporting and downloading data, and much more), review the `Flywheel CLI Overview <https://docs.flywheel.io/hc/en-us/articles/4536067900435-Command-Line-Interface-Overview>`_

CLI From Blanca Compute Node
****************************

For your convenience, the Flywheel CLI is already installed in a Conda environment on PetaLibrary. To use the Flywheel CLI from a compute node, follow the steps below:

1. Log in to a login or compute node on RC resources (e.g. `Open OnDemand <https://ondemand.rc.colorado.edu/pun/sys/dashboard>`_ Core Desktop or Jupyter Session).

2. Load the latest Anaconda3 module:

     :code:`module load anaconda`

3. Activate the *flywheel* conda environment:

     :code:`conda activate flywheel`

4. Check the flywheel status to ensure you are logged in as the correct user:

     :code:`fw status`

5. If you are not logged with yourself as the user, log in to the Flywheel API with your Flywheel API key:

     :code:`fw login <your_api_key>`

6. Now you are ready to run any FW API command (refer to the section above for specific commands)

.. note:: **Special Instructions for Large Uploads**: Even though the Flywheel CLI lives on PetaLibrary in the conda environment called *flywheel*, the cache for all temporary data is hard coded to go to your *home* directory on PetaLibrary. However, because your *home* directory is so small, this cache can quickly fill up resulting in the upload failing and your *home* directory full. To avoid this issue, you should create a soft link between your *home* cache directory and your *projects* cache directory, which is much large, ie:

         :code:`/home/<identiKey>/.cache/flywheel -> /projects/<identiKey>/.cache/flywheel`
