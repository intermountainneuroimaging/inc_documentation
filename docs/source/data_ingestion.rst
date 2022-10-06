.. _data_ingestion:

Working With Your Data Outside Flywheel
==========================================

Some workflows are not currently supported in Flywheel, and need to be implemented on a local compute environment. Please check out out python SDK tutorials `here <notebooks/download-and-run-locally.ipynb>` to learn more.


CONN Functional Connectivity Toolbox
***************************************

`CONN Functional Connectivity Toolbox <https://web.conn-toolbox.org/home>`_. is an open-source Matlab/SPM-based cross-platform software for the computation, display, and analysis of functional connectivity Magnetic Resonance Imaging (fcMRI).

CONN Analyses can generate *very* large output directories and therefore special care must be taken whenever generating analyses in the platform to ensure responsible data stewardship. Below we have outlined our recommendation for best practices for developing CONN analyses as well as archiving these analyses after publication.

Setting Up Your Analysis
++++++++++++++++++++++++++++++++++++
CONN analyses require extensive computational and disk size resources. To ensure responsible use of computational resources, it is best practice to:

1. Test your CONN analysis design with 3-5 subjects
2. Start simple, build out the complexity of the model design one step at a time
3. Once you are satisfied with the model design run the final full model design only once
4. All CONN *development* models should be stored on a scratch filesystem and removed when complete
5. When possible generate a single preprocessed dataset for all CONN analyses
6. Current CONN limitations limit single file import size < 1GB. For input file sizes greater than 1GB, downgrading the datatype can reduce nifti file sizes for conn import.

Archiving Analysis When Complete
++++++++++++++++++++++++++++++++++++
Once a CONN analysis is completed, we recommend users archive their conn analysis. Removing intermediate data files can help manage the size of the archived analysis.

1. Intermediate preprocessing files can be removed. Before removing any preprocessing files, check which dataset files are loaded in CONN. This includes checking the file paths defined in the "Primary Dataset", "Unsmoothed Dataset", ...

.. important::
    Do not remove any input files that are referenced in the "Setup" panel of CONN. Removing these files may result in irreversible errors in the conn menu.

2. Approximately 60%-80% of the data storage requirements of the CONN outputs directory are contained in the "results" subdirectory. These *.mat and *.matc files contain information generated from the denoising, first-level, and second-level modeling steps of the CONN analysis.

    Users **can** remove the contents of "results/preprocessing" and "results/firstlevel" without disrupting ability to recover the second level model results already generated for the project. To generate new second level model results, the denoising and first-level modelling step would need to be regenerated.

Zipping Archived Outputs
++++++++++++++++++++++++++++++++++++
Once users have removed all intermediate result files, the conn analysis can be archived by first zipping the conn outputs directory and mat file, then uploading the analysis to the flywheel platform. Here is an example below:

.. code-block::

    # zip outputs directory and mat file
    !zip -R conn_analysis conn_analysis/ conn_analysis.mat

    # zip preprocessed inputs **only if not already stored on platform
    !zip -R conn_inputs conn_inputs/

    # upload zips to flywheel
    fw = flywheel.Client()

    project = fw.lookup('<group>/<project>')

    # create new project level analysis
    analysis = project.add_analysis(label='CONN Analysis: ' + datetime.now(" %x %X"))

    # upload output zipped directories
    analysis.upload_output('conn_analysis.zip')
