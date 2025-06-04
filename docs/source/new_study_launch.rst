.. _new_study:

Starting A New Study?
========================

Starting a new study in Flywheel is quick and easy! The infrastructure in place streamlines study concept to final analysis results faster than ever!

INC staff will set up your project in Flywheel. Be sure to contact INC staff to setup time to Pilot your study protocol on the MRI scanner. Piloting data can be found in the newly created Flywheel project. Here are the steps to take once your project is created:

**Step 1:** Permissions: Add all study personnel who needs access to study data within Flywheel. Check out `User Permissions` for more information.

**Step 2:** Acquisition naming - if you plan to use BIDS formatting, ensure all acquisitions comply with Reproin naming conventions.

**Step 3:** Add or enable gear rules for basic data processing (classifier, dcm2niix, brain souvenirs)

**Step 4:** Upload generic and commonly used files to the project:

    (1) .bidsignore

    .. code-block::

        *.txt
        gear*.json
        *.pdf
        *.fsf
        *.zip
        *ignore-BIDS.json


    (2) license.txt (freesurfer license file) `generate here <https://surfer.nmr.mgh.harvard.edu/fswiki/License>`_

    (3) scanner protocol (INC staff will provide)

**Step 5:** Setup completeness worksheet.

We highly recommend documenting your full protocol using completeness.csv and use the hierarchy curator in Flywheel to check each data collection session against the expected template. It helps catch errors in data collection or transfer quickly! For more information on how to create and use completeness worksheets visit our github `repo. <https://github.com/intermountainneuroimaging/flywheel_sdk_examples/tree/main/1_metadata_and_curator>`_

You can also set up a session template in Flywheel, which provides a limited check of session completeness.

**Step 6:** Setup you gear auto-workflow.

Here is where you can define the full analysis pipeline to run for complete sessions in Flywheel. Visit our github `repo <https://github.com/intermountainneuroimaging/flywheel_sdk_examples/tree/main/2_gear_autoworkflow>`_ for more information.

Feel free to contact INC staff for support to complete any of the steps above.

<video link>
