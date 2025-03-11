.. _nda_uploads:

NDA Upload
========================

Most data collected through an NIH funded grant mechanism are required to share complete study data with the National Data Archive (NDA).

Please confirm with your program officer if your grant is required to submit data to the NDA. If so, please review requirements **before** data collection on the NDA website.

Once study personnel have generated GUID (global participant identifiers) for each study participant, you may proceed with neuroimaging data upload. Follow the guidance below to get started. We also highly recommend consulting with an INC staff member for guidance on the most up to date methods and standards.

Step 1: Download BIDS formatted project data.
    :code:`fw export bids <path_to_your_dicom_folder> [group-id] [project] --subject [subjects] --session [sessions]`

 - Be sure to include your event timing data! The event timing data may automatically be exported in the BIDS export or you may need to manually export depending on the project settings. If you have questions or concerns, contact INC staff

**Step 2:** Generate image03.csv file.

Consult the NDA official documentation on the best practices of uploading neuroimaging and BIDS formatted data. Current recommendations are to upload data as image03 format. Select your primary acquisition to extract the sequence parameters for image03 formatting.

**Step 3:**  Create json files for each BIDS formatted session. We recommend using the following github resource to generate subject json files

**Step 4:** Upload data files to NDA.

To batch upload files, you will need to use the NDA upload scripts. INC generally maintains a error free version of the upload code. Please contact INC staff for instructions to access the shared code environment.

.. IMPORTANT:: Users should start the process of uploading NDA data at least 6 weeks before any upload deadlines! The upload process is time consuming!
