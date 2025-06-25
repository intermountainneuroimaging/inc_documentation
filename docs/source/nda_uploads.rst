.. _nda_uploads:

NDA Data Submissions
========================

Most data collected through an NIH funded grant mechanisms are required to share complete study data with the National Data Archive (NDA).

Please confirm with your program officer if your grant is required to submit data to the NDA. If so, please review requirements **before** data collection on the NDA website.

Once study personnel have generated GUID (global participant identifiers) for each study participant, you may proceed with neuroimaging data upload. Follow the guidance below to get started. We also highly recommend consulting with an INC staff member for guidance on the most up to date methods and standards.

We recommend working within CURC's compute and data storage resources for NDA data submissions. INC manages a communal code repository with up-to-date NDAR tools for data submission. If users elect to use a local compute envrionment, you will need to be sure to install the prerequisite code environments before getting started.

Using CURC resources (OpenOndemand)?
++++++++++++++++++++++++++++++++++++++++++

   Great! Skip over the next section. Quickly refresh yourself on how to access CURC's resources in our early documentation :ref:`Using Core Desktop` and :ref:`Setting Up Conda Environments`.

   .. code-block:: bash

      module load anaconda
      conda activate nda-tools-2025

(Extra Steps) Prerequisite software packages
++++++++++++++++++++++++++++++++++++++++++++++++++++

   1. `install Flywheel.io command line tool <https://docs.flywheel.io/CLI/start/install/>`_.
   2. `set up NDAR nda-tools environment <https://github.com/NDAR/nda-tools/blob/main/README.md#how-to-set-up-nda-tools>`_.
   3. `download NDAR manifest-data repository <https://github.com/NDAR/manifest-data/tree/master>`_

BIDS formatted files
++++++++++++++++++++++++++++++++++++++++++++++

Easily export all of your unprocessed nifti imaging files (and event timing, dicom files) from Flywheel.io using the command line interface.

    :code:`fw export bids <target_path_for_bids> --project PROJECT --group GROUPID --subject [subjects] --session [sessions]`

 - Be sure to include your event timing data! The event timing data may automatically be exported in the BIDS export or you may need to manually export depending on the project settings. If you have questions or concerns, contact INC staff


Generate image03.csv file
++++++++++++++++++++++++++++++++

Consult the NDA official documentation on the best practices of uploading neuroimaging and BIDS formatted data. Current recommendations are to upload data as :code:`image03` or :code:`fmriresults01` format. :code:`image03` data submission spreadsheets require addtional dicom related metadata to be associated with each file/manifest entry. We recommend using the dicom metadata from the main fMRI acquisition.

Sample image03 table. Notice, using the manifest requires an entry for the :code:`manifest` column and requires :code:`image_file` column to be left empty.

====  ================  ==================  ==================  =================  =======  ===================  ==============  ========================  =========================================  =====================  =====================  ==================  ===========================  ===================  ================================  ===========================  ==========================  ==============  ======================  ========================  ====================  ======================  ================  =================  ============================  =======================  =================  ========================  =================  =================  =================  =================  ================  =================  ================  ===============  ===============  ===============  ===============  ===============  =====================  =====================  =====================  =====================  =====================  =========================  =====================  ==============  ==================  ========================  ===============  ==============  ====================  =============================  ===================  ====================  ==================  ==============  ===================  =============  =====================  ====================  =============  =================  ===============  ===================  =====================  =========  ========  ==========================  =====================  ================  ============  ============  ===================  ======================  ============  ==========  ====================
..     SUBJECTKEY        SRC_SUBJECT_ID      INTERVIEW_DATE        INTERVIEW_AGE    SEX      COMMENTS_MISC        IMAGE_FILE      IMAGE_THUMBNAIL_FILE      MANIFEST                                   IMAGE_DESCRIPTION      IMAGE_FILE_FORMAT      IMAGE_MODALITY      SCANNER_MANUFACTURER_PD      SCANNER_TYPE_PD      SCANNER_SOFTWARE_VERSIONS_PD        MAGNETIC_FIELD_STRENGTH      MRI_REPETITION_TIME_PD      FLIP_ANGLE    ACQUISITION_MATRIX      MRI_FIELD_OF_VIEW_PD      PATIENT_POSITION      PHOTOMET_INTERPRET      RECEIVE_COIL      TRANSMIT_COIL      TRANSFORMATION_PERFORMED      TRANSFORMATION_TYPE      IMAGE_HISTORY      IMAGE_NUM_DIMENSIONS      IMAGE_EXTENT1      IMAGE_EXTENT2      IMAGE_EXTENT3      IMAGE_EXTENT4      EXTENT4_TYPE      IMAGE_EXTENT5      EXTENT5_TYPE      IMAGE_UNIT1      IMAGE_UNIT2      IMAGE_UNIT3      IMAGE_UNIT4      IMAGE_UNIT5        IMAGE_RESOLUTION1    IMAGE_RESOLUTION2      IMAGE_RESOLUTION3      IMAGE_RESOLUTION4      IMAGE_RESOLUTION5        IMAGE_SLICE_THICKNESS    IMAGE_ORIENTATION      QC_OUTCOME      QC_DESCRIPTION      QC_FAIL_QUEST_REASON      PET_ISOTOPE      PET_TRACER      DECAY_CORRECTION      TIME_DIFF_INJECT_TO_IMAGE      TIME_DIFF_UNITS      FRAME_START_UNIT      FRAME_END_UNIT      DATA_FILE2      DATA_FILE2_TYPE      SCAN_TYPE      SLICE_ACQUISITION      SOFTWARE_PREPROC      PULSE_SEQ      EXPERIMENT_ID      SCAN_OBJECT      FRAME_END_TIMES      FRAME_START_TIMES      STUDY      WEEK      EXPERIMENT_DESCRIPTION      VISIT                  SLICE_TIMING      BVECFILE      BVALFILE      BVEK_BVAL_FILES      DEVICESERIALNUMBER      PROCDATE      VISNUM        MRI_ECHO_TIME_PD
====  ================  ==================  ==================  =================  =======  ===================  ==============  ========================  =========================================  =====================  =====================  ==================  ===========================  ===================  ================================  ===========================  ==========================  ==============  ======================  ========================  ====================  ======================  ================  =================  ============================  =======================  =================  ========================  =================  =================  =================  =================  ================  =================  ================  ===============  ===============  ===============  ===============  ===============  =====================  =====================  =====================  =====================  =====================  =========================  =====================  ==============  ==================  ========================  ===============  ==============  ====================  =============================  ===================  ====================  ==================  ==============  ===================  =============  =====================  ====================  =============  =================  ===============  ===================  =====================  =========  ========  ==========================  =====================  ================  ============  ============  ===================  ======================  ============  ==========  ====================
   0  NDAR_INV25KAJM0U  NDAR_INV25KAJM0U    6/4/17                            109  M        MB2 fMRI Fieldmap P                                            100206_3T_Diffusion_preproc_manifest.json  ABCD-fMRI-FM-PA        fMRI                   MRI                 Philips Medical Systems      Achieva dStream      ["5.3.0", "5.3.0.0"]                                        3                           7              52  [92, 0, 0, 89]                                    HFS                   MONOCHROME2             MULTI COIL                           No                                                                                                                                                                                                                                                                                                                                              0                                                                                                                    2.4                                                             NA                                                                                                                                                                                                                  Field Map                                                                                     Live                                                                                                          baseline_year_1_arm_1                                                                     anonb2d4                                                          0.07
====  ================  ==================  ==================  =================  =======  ===================  ==============  ========================  =========================================  =====================  =====================  ==================  ===========================  ===================  ================================  ===========================  ==========================  ==============  ======================  ========================  ====================  ======================  ================  =================  ============================  =======================  =================  ========================  =================  =================  =================  =================  ================  =================  ================  ===============  ===============  ===============  ===============  ===============  =====================  =====================  =====================  =====================  =====================  =========================  =====================  ==============  ==================  ========================  ===============  ==============  ====================  =============================  ===================  ====================  ==================  ==============  ===================  =============  =====================  ====================  =============  =================  ===============  ===================  =====================  =========  ========  ==========================  =====================  ================  ============  ============  ===================  ======================  ============  ==========  ====================

Generate :code:`manifest.json`
++++++++++++++++++++++++++++++++++++++++++++++

After downloading necessary fMRI data and organizing entries in the image03 format, you will need to generate a unique :code:`manifest.json` for each image03.csv file entry (generally on data collection *session*). Uploading fMRI data using :code:`manifest.json` instead of a single zipped archive has a few advantages. It improves visibility within NDA's registry and affords users wishing to download the dataset flexibility to select a subset of the full imaging protocol. To learn more about generate the :code:`manifest.json` files, check out NDAR's repo `manifest-data. <https://github.com/NDAR/manifest-data/tree/master>`_

   :code:`python /projects/ics/software/NDA/manifest-data/nda_manifests.py -id sub-[ID] -of manifest_[ID].json`


Check out this example to pull BIDS data from Flywheel.io and generate manifest files using some BASH scripting.

   .. code-block:: bash
      :linenos:

      # Example putting it all together... with a subject id list
      FILE="subject_list.txt"

      #setup file paths
      BIDSDIR=/scratch/alpine/$USER/nda_submission_data/bids
      #make bids and manifest directories if missing
      mkdir –p $BIDSDIR
      mkdir –p $BIDSDIR/manifests

      # Loop through file list, subject by subject
      while IFS= read -r SUBJECT; do
         echo "Processing subject: ${SUBJECT}"
         # download BIDS formatted fmri data from Flywheel.io
         fw  bids $BIDSDIR --project PROJECT --group GROUP --subject ${SUBJECT}"

         # generate a manifest files containing all bids formated data for subject XX
         python /projects/ics/software/NDA/manifest-data/nda_manifests.py -id sub-${SUBJECT} -of manifest_${SUBJECT}.json

      done < "$FILE"



Validate and Upload
++++++++++++++++++++++

NIMH Data Archive (NDAR) retains a set of python packages which can be used to batch upload fMRI neuroimaging data. The nda-tools code base can come with software bugs. Feel free to reach out to INC staff for support troubleshooting any nda-tools error or warning messages.

 - Start by ensuring your credentials are stored in your working environment (`looking for help? <https://github.com/NDAR/nda-tools/blob/main/README.md#step-4-authenticate-with-nda-tools>`_)
 - You are ready for the data submission! Have your :code:`image03.csv` submission file handy, directory with all :code:`manifest.json` files, and of course access to path with the fMRI data.

   :code:`vtcmd sample_image03.csv  -m <path/to/manifests>`

INC generally maintains a error free version of the nda-tools software package. Please contact INC staff for instructions to access the shared code environment.

.. IMPORTANT:: Users should start the process of uploading NDA data at least 6 weeks before any upload deadlines! The upload process is time consuming!
