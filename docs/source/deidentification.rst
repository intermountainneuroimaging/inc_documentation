.. _deidentification:

Deidentification
================

Deidentification Overview
*************************
There are many instances in which you would want to de-identify your data before ingesting it into Flywheel. The main reason is if your acquired data from the scanner is not already de-identified (ie, if you don't scan at INC). Below is a brief summary of several ways to de-identify your data before it enters Flywheel, or once it's already in Flywheel.

.. warning::
    The UCB instance of Flywheel relies on storage (PetaLibrary) that can have **no personal identifying information** on it. Therefore, it is crucial to de-identify your data if it was collected somewhere outside of INC.

Deidentification on Edge
************************
De-identification on edge refers to wiping out any identifying information in dicom headers at the source (before those dicoms are ever uploaded to Flywheel). That source can be your institution's data storage cluster, or your institution's scanner. In either case, Flywheel will have no record of any personal identifying information (PII) in your dicom headers if de-identification happens on edge.

Fortunately, through the Flywheel command line interface tool (CLI), Flywheel can assist in the de-identification process without "knowing" about your data or registering it in the Flywheel database.

Pre-requisites
++++++++++++++
To get started, you'll need to download the Flywheel CLI on the machine where your data resides, or on a machine that has mounted access to where your data resides: visit the :ref:`cli_basics` page.

Before getting started, you'll also need some way to read the existing header information in your dicom files (for example, `DCMTK's dcmdump tool <https://dicom.offis.de/dcmtk.php.en>`_). Alternatively, if you already know the header codes and header information, you can forgo looking it up with the dicom header reader.

Once the Flywheel CLI is downloaded (and your personal API key generated), you are ready to start ingesting de-identified data into Flywheel.

Simple De-identification
++++++++++++++++++++++++
If the only identifiable information in your dicoms exists in the Patient ID, Patient Name, and Patient Birthdate, Flywheel has a pre-built flag that simply removes those dicom header fields from every dicom file that is uploaded.

Suppose we want to upload a dicom acquisition from our local computer onto Flywheel. We first inspect the header information in that acquisition (just checking one dicom in the acquisition is enough). All of the following commands are run in a Terminal or DOS prompt (aka command line interface):

.. code-block:: bash

    dcmdump <path_to_single_dicom>

For example:

.. code-block:: bash

    dcmdump just_t1_dummy_ids/ics/deid/deid02/inc01/anat-T1w_acq-mpr08_run-01/1.3.12.2.1107.5.2.43.67087.2022101911212761306002309.0.0.0.dicom/1.3.12.2.1107.5.2.43.67087.2022101911284077703103114.MR.dcm

The returned output below (a partial dump of the dicom header) makes it clear that there is indeed identifying information:

+---------------------+-----------------------------+--------------------------------+
| Dicom Code          | Field Name                  | Value                          |
+=====================+=============================+================================+
| (0010,0010)         | Patient's Name              | John                           |
+---------------------+-----------------------------+--------------------------------+
| (0010,0020)         | Patient ID                  | Doe                            |
+---------------------+-----------------------------+--------------------------------+
| (0010,0030)         | Patient's Birth Date        | 19010101                       |
+---------------------+-----------------------------+--------------------------------+
| (0010,0040)         | Patient's Sex               | F                              |
+---------------------+-----------------------------+--------------------------------+
| (0010,1010)         | Patient's Age               | 121Y                           |
+---------------------+-----------------------------+--------------------------------+

To upload this acquisition but *without* the Patient's Name, Patient ID, or Patient's Birth Date, the Flywheel command is simply to add the :code:`--de-identify` flag onto the :code:`fw ingest dicom` command.

.. code-block:: bash

    fw ingest dicom --de-identify --subject <subject_ID> --session <session_ID> <path_to_dicom_directory> <Flywheel Group> <Flywheel Project>

For example:

.. code-block:: bash

    fw ingest dicom --de-identify --subject deid01 --session inc01 just_t1_dummy_ids/ics/deid/deid02/inc01/anat-T1w_acq-mpr08_run-01/1.3.12.2.1107.5.2.43.67087.2022101911212761306002309.0.0.0.dicom ics deid

More details about the :code:`fw ingest dicom` command are given on our :ref:`cli_basics` page.

If you now check your upload in Flywheel by clicking on the information button next to the dicom, you'll see that the Patient's Name, Patient ID, and Patient Birth Date simply don't exist as metadata.

.. note::
    While the Patient's Name, Patient ID, and Patient's Birthdate have been de-identified, if you had any other identifying information in your dicom header, it is now in Flywheel. Not good. For scrubbing other identifying metadata from the dicom header, read on.

De-identification Profile
+++++++++++++++++++++++++
Creating a de-identification profile allows you to have maximum control over how *each and every* piece of metadata in your dicom header is handled. Creating a de-identification profile can be a daunting task at first - not because it's difficult - but because of how many different options you have at every decision. Some of the basic options include: do nothing, increment all age-related numbers by some given amount, delete the data entirely, replace the data with something different, jitter the data if it's a number, and hash the data.

Flywheel has extensive information about how to create a de-identification profile on their `de-id documentation website. <https://docs.flywheel.io/hc/en-us/articles/1500003050521>`_

In short, this de-identification profile is nothing more than a YAML file. The example below shows a de-identification profile that does the following:

    * Sets up a place to store the de-id log (a csv file that allows you to re-identify your data, should you need to)

    * Increments each date field by subtracting 17 days

    * Sets the patient's age to use Year units

    * Calculates the Patient's Age from the Patient Birth Date dicom tag

    * Removes the PatientID dicom tag

    * Replaces the dicom tag StationName with XXXXX

    * Hashes the AccessionNumber and ConcatenationUID dicom tags

.. code-block:: yaml

    # the de-id updates before uploading
    # The option is ignored in ingest, you can use --save-deid-logs PATH to save the log.

    deid-log: ./deid_log.csv

    # Sets the filetype to DICOM

    dicom:

      # Date-increment controls how many days to offset each date field
      # where the increment-date (shown below) is configured.
      #Positive values will result in later dates, negative
      # values will result in earlier dates.

      date-increment: -17

      # patient-age-from-birthdate sets the DICOM header as a 3-digit value with a suffix
      # be 091D, and that same age in months would be 003M. By default, if
      # the age fits in days, then days will be used,
      # otherwise if it fits in months, then months
      # will be used, otherwise years will be used

      patient-age-from-birthdate: true

      # Set patient age units as Years. Other options include months (M) and days (D)

      patient-age-units: Y

      # The following are field transformations.
      # Remove, replace-with, increment-date, hash, and hashuid can be used with any DICOM
      # field. Replace name with the DICOM field "keyword" by the DICOM standard
      fields:

        # Use remove Remove a dicom field Removes the field from the DICOM entirely.
        # If removal is not supported then this field will be blank.
        # This example removes PatientID.

        - name: PatientID
          remove: true

        # Replace a dicom field with the value provided.
        # This example replaces “StationName” with "XXXX" in Flywheel

        - name: StationName
          replace-with: XXXX

        # Offsets the date by the number of days defined in
        # the date-increment setting above, preserving the time
        # and timezone. In this example, StudyDate appears as 17 days earlier

        - name: StudyDate
          increment-date: true

        # One-Way hash a dicom field to a unique string

        - name: AccessionNumber
          hash: true

         # Replaces a UID field with a hashed version of that
         # field. The first four nodes (prefix) and last node
         # (suffix) will be preserved, with the middle being
         # replaced by the hashed value

        - name: ConcatenationUID
          hashuid: true

Testing the De-identification Profile
+++++++++++++++++++++++++++++++++++++
Once you've created your de-identification profile, Flywheel also has a command line interface tool that allows you to test your profile on sample data before using it more broadly for the final dicom upload.

Extensive documentation on testing your de-id profile exists on the `Flywheel site <https://docs.flywheel.io/hc/en-us/articles/1500010369681#UUID-474d115b-d8d5-11e4-ff51-f9e22b5359bd>`_ as well as a brief summary below.

In the previous section, we created a de-identification profile that we called :code:`deid_profile.yaml`. Suppose we now want to test how this profile transforms one of our example dicom directories, and store the results of this transformation in a directory we call *deid_test_dir*. Below is the Flywheel command line call that performs the aforementioned steps:

.. code-block:: bash

    fw deid test <path_to_dicom_directory_to_deid> <path_to_deid_yaml_profile> <path_to_directory_for_test_results> --session <session_ID> --subject <subject_ID>

For example:

.. code-block:: bash

    fw deid test just_t1_dummy_ids/1.3.12.2.1107.5.2.43.67087.2022101911212761306002309.0.0.0.dicom deid_profile.yaml deid_test_dir --session inc01 --subject deid02

The result of this call from the terminal creates a csv file called :code:`deid_log.csv` in the directory *deid_test_dir*. The CSV file shows a before and after (what each dicom header field was before the transformation, and what it became after the transformation).  When you first build a de-id profile, it'll be an iterative process of testing the profile to make sure you have captured all the desired transformations and haven't left any identifying information in the dicom header.

Uploading the De-ID Profile To You Flywheel Project
+++++++++++++++++++++++++++++++++++++++++++++++++++

Once you have created and tested your de-identification profile, you can ask the INC team to upload your profile to the relevant Flywheel Project. Once the profile exists as an attachment in your Project settings, any upload you perform (via the GUI, SDK, or CLI) for that Project will first be de-identified based on the rules you laid out in your profile.

Alternatively, if you'd rather keep your de-id profile secret, want to apply different de-id profiles for different subjects, etc, it's best to continue to the next section which describes how to upload data while the de-id profile remains local to your personal computer (not in Flywheel).

The Ingest Config Template
++++++++++++++++++++++++++

Now that you've put in the hard work into making the perfect de-id profile, you'd like to use it for an actual data upload. However, if you opted not to upload the de-id profile to Flywheel, there's one more step: the Ingest Config Template.

The ingest config template is a broad topic in and of itself (best described in the `Flywheel template documentation <https://docs.flywheel.io/hc/en-us/articles/4413200627987>`_).

Briefly, the ingest template is a configuration YAML file that allows you to control every part of the Flywheel upload process. For example, the ingest template defines the relationship between your local folder structure (where the data exists) and how you want that data to be labelled and mapped onto the Flywheel data hierarchy. Critically, the ingest config template also defines the de-identification profile(s) for the given Project.

The ingest template is its own topic and won't be covered in this section; however, to apply the de-id profile you created and tested, you simply need to paste it into the ingest config template. Below is an example of an ingest config template titled :code:`config.yaml`. Notice the copied and pasted de-identification profile we worked on in previous sections.

.. code-block:: yaml

        ####
        # Template and Group/Project Settings
        #####

        template:
          - pattern: "{group}"
          - pattern: "{project}"
          - pattern: "{subject}"
          - pattern: "{session}"
          - pattern: "{acquisition}"
            packfile_type: dicom

        #####
        # Optional includes/excludes for directories and files
        #####

        # Patterns of directories to include
        # include-dirs:
        # - "*.dicom"

        # Patterns of filenames to exclude
        # exclude:
        # - "*.txt"
        # - "*.xml"

        #####
        # De-identification Settings
        #####
        deid-profiles:
        - name: Anschutz

          # Indicates where you want to place the de-id log. You will use this log file to preview
          # the de-id updates before uploading
          # The option is ignored in ingest, you can use --save-deid-logs PATH to save the log.

          deid-log: ./deid_log.csv

          # Sets the filetype to DICOM

          dicom:

            # Date-increment controls how many days to offset each date field
            # where the increment-date (shown below) is configured.
            #Positive values will result in later dates, negative
            # values will result in earlier dates.

            date-increment: -17

            # patient-age-from-birthdate sets the DICOM header as a 3-digit value with a suffix
            # be 091D, and that same age in months would be 003M. By default, if
            # the age fits in days, then days will be used,
            # otherwise if it fits in months, then months
            # will be used, otherwise years will be used

            patient-age-from-birthdate: true

            # Set patient age units as Years. Other options include months (M) and days (D)

            patient-age-units: Y

            # The following are field transformations.
            # Remove, replace-with, increment-date, hash, and hashuid can be used with any DICOM
            # field. Replace name with the DICOM field "keyword" by the DICOM standard
            fields:
              # Use remove Remove a dicom field Removes the field from the DICOM entirely.
              # If removal is not supported then this field will be blank.
              # This example removes PatientID.

              - name: PatientID
                remove: true

              # Replace a dicom field with the value provided.
              # This example replaces “StationName” with "XXXX" in Flywheel

              - name: StationName
                replace-with: XXXX

              # Offsets the date by the number of days defined in
              # the date-increment setting above, preserving the time
              # and timezone. In this example, StudyDate appears as 17 days earlier

              - name: StudyDate
                increment-date: true

              # One-Way hash a dicom field to a unique string

              - name: AccessionNumber
                hash: true

               # Replaces a UID field with a hashed version of that
               # field. The first four nodes (prefix) and last node
               # (suffix) will be preserved, with the middle being
               # replaced by the hashed value

              - name: ConcatenationUID
                hashuid: true


Putting it All Together
+++++++++++++++++++++++
The last step once the de-id profile and the template config YAML are ready, is to make the actual call to Flywheel to upload your dicoms. This is done either with a call to :code:`fw ingest dicom` or with :code:`fw ingest template`.

To use :code:`fw ingest dicom` to upload the example data to Flywheel Group ics, Flywheel Project deid, Flywheel Subject deid03, and Flywheel Session inc01, using our created config file :code:`config.yaml` which includes the de-ide profile named :code:`Anschutz`, we use the following command line call:

.. code-block:: bash

    fw ingest dicom --config-file config.yaml --de-identify --deid-profile Anschutz --subject deid03 --session inc01 ./just_t1_dummy_ids/ics/deid/deid02/inc01/anat-T1w_acq-mpr08_run-01/1.3.12.2.1107.5.2.43.67087.2022101911212761306002309.0.0.0.dicom ics deid

More options are available with :code:`fw ingest template`, but to accomplish the same upload as above, the command line argument is:

.. code-block:: bash

    fw ingest template -C config.yaml ./just_t1_dummy_ids --group ics --project deid --de-identify --deid-profile Anschutz

Deidentification From the Scanner
*********************************
It is also possible to create a profile that applies to data coming directly from the scanner. If this is of interest, please contact Lena or Amy.

Deidentification Gear in Flywheel
*********************************
Lastly, there's an additional option to de-identify the data once it's already in Flywheel by running the de-id gear. However, Flywheel has version control on files (including DICOM files), so a copy of your "identifiable" data before the de-id gear was run will exist somewhere in Flywheel (even if it is not accessible to all users). Since the CUB instance of Flywheel can't have any identifiable information at any time, running the de-id gear is not an option we advertise on our site.

