.. _auto_analysis:

Automated Analysis Workflow
===============================

Studies wishing to use the Flywheel Analysis Gears for data processing should review this section. At INC, we implement an **Automated Analysis Workflow** option where studies can define a custom analysis workflow. The custom analysis workflow is automatically applied to new data collection sessions using a custom job scheduling script (see more on our github page: `here <https://github.com/intermountainneuroimaging/fw-gear-rules>`_.

Why use automated analyses? Using INC's custom **Automated Analysis Workflow** ensures that every session collected in the project is processed in an identical fashion, and immediately following data collection ensuring data are available to users more quickly.

INC has created a custom **Automated Analysis Workflow** wherein the user need only define a "workflow template" where each analysis stage is documented including prerequisite stages and all gear configurations, tags and labels. When conditions are met for the recent data collection session, the custom "job scheduler" will launch a new analysis jobs. This is currently the best "work around" for session level gear rules in flywheel. The automated process runs overnight, 7 days a week.

Please set up a consultation time with INC staff to discuss your study's specific needs. Follow the steps below to create a new Workflow template file.

Template File
----------------
"Gear conditions" and run configurations are set using a `JSON` file. The optional and required json dictionary keys are described in detail below.

The json file must contain an `analysis` dictionary, where all workflow steps are detailed. Here, each analysis should be it's own `JSON` object and are ordered in a list as shown below.::

    "__comment__": "example template",
    "analysis":
        [
            {
              <gear template descriptors>
            }
        ]

Each "workflow stage" should contain instructions to run a single analysis, include the gear name, version, inputs, config, tags, label and conditions.

-------------------------------------------------

Gear Template Descriptors
++++++++++++++++++++++++++++++

:code:`comment`

    __(optional)__ add description of workflow stage or any other relevant comments::

        "__comment__": "step 1: curate session using bids reproin naming convention"


:code:`gear-name`

    __(required)__ flywheel gear name used to run analysis::

        "gear-name": "curate-bids"


:code:`gear-version`

    __(optional)__ flywheel gear version used in current analysis, if this key is excluded, the most recent version of the gear is used.::

        "gear-version":"2.1.3_1.0.7"

:code:`inputs`

    __(optional)__ if input files are required in the current analysis, each input file should be detailed here. The inputs should be formated as a `JSON` object. Each key must exactly match the input name for the flywheel gear. If you are not sure the input name for the flywheel gear, you can find the placeholder in the gear info. In the example below we are passing two input files, one that will be passed as "template" and a second that will be passed as "freesurfer-license". For each input file, there are additional dictionary settings that can be passed to point to the correct file in flywheel.

    Two options can be used to point to a file name: (1) :code:`regex` uses python's regular expression syntax to return matching files by regular expression. If more than one file is found, an error will be logged and the current analysis will not run; (2) :code:`value` which will look for an exact filename match in flywheel. It is also required to identify `parent-container` where the particular file should be located (:code:`project` | :code:`subject` | :code:`session` | :code:`analysis`).

    Additional flag, :code:`optional` is used to either log and error and exit if no file match is found, or proceed without a file match. This can be useful for 'generic' files such as :code:`.bidsignore` which may only be present in some projects.::

        "inputs": {
                    "template": {
                        "regex": "-reproin-template.json$",
                        "parent-container": "project",
                        "optional": true
                    },
                    "freesurfer-license": {
                      "value": "license.txt"
                      "parent-container": "project",
                      "optional": false
                    }
                },

:code:`config`

    __(optional)__ if configuration settings differ from the gear defaults, the configuration for the current analysis is detailed here. The configurations should be written exactly as they appear in the gear info, and must be formated as a `JSON` object.::

        "config": {
                    "reset": true,
                    "intendedfor_regexes": ".*fmap.* nii",
                    "use_or_save_config": "Ignore Config File"
                },



:code:`tags`

    __(optional)__ if any tags should be added to the analysis, enter them as a list of strings here::

        "tags": ["hpc"]


:code:`custom-label`

    __(optional)__ add a custom label for the current analysis. Default label is the gear name followed by current date and time.::

        "custom-label": "completeness-curator"


Other Options - Setting :code:`RUN` conditions
+++++++++++++++++++++++++++++++++++++++++++++++++

:code:`prerequisites`
    __(optional)__ list of prerequisite gears that must have completed successfully before current analysis will run (e.g. curate-bids should always be run *before* bids-mriqc). Prerequisite conditions should be structured as one `JSON` object prerequisite analysis and stored in a list.

    Each Prerequisite :code:`JSON` object should contain the following: (1) :code:`prereq-gear` containing the gear name or gear/version information for requisite analysis; (2) :code:`prereq-complete-analysis` indicating if all analyses should be checked or find first matching requisite analysis (:code:`any`|:code:`all`), (3) :code:`prereq-analysis-label` (optional) if passed will look for a gear with specific analysis label (useful for repeated gears such as **hierarchy-curator**.::

        "prerequisites":  [
                {
                    "prereq-gear": "hierarchy-curator",
                    "prereq-analysis-label": "events-curator",
                    "prereq-complete-analysis":"any"
                },
                {
                    "prereq-gear": "bids-fmriprep",
                    "prereq-complete-analysis":"any"
                }
            ],


:code:`count-failures`

    __(optional)__ by default, the worflow will not re-run gears that are currently running or have completed sucessfully. In the case, were a prior analysis failed, you can automatically re-try the analysis up to the number defined here (e.g. count-failures: 2 ... would re-try the gear once resulting in 2 total attempts).::

        "count-failures": 2


:code:`sleep_seconds`

    __(optional)__ for some light weight gears, it can be nice to hold the program open for a period of time to check if the gear finishes before proceeding. This is recommended only for light weight gears where downstream analyses are held due to prerequisite conditions.::

        "sleep_seconds": 30


:code:`completeness-tags`

    __(optional)__ CU Boulder specific metadata tag produced during the completeness curator which details if the session meets a predefined template. For more information on the completeness curator, contact the INC data and analysis team. Boolean metadata tags will be checked for all those passed in a list of strings.::

        "completeness-tags": ["Run Downstream Analyses"]


**NEW!** Other Options - Setting :code:`DOWNLOAD` conditions
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

We have recently added the option in the auto analysis workflow to include data downloads to a local server. Identify analysis stages which should be automatically downloaded using the following template descriptors.

:code:`download-locally`

    __(optional)__ Boolean flag (true | false) to indicate weather analysis stage should be donwloaded locally. If this template descriptor is not include, assumed :code:`false`. ::

        "download-locally": true

:code:`download-path`

    __(linked)__ The descriptor must be included if the :code:`download-locally == true`. The is a writable file-path where data should be downloaded. Important to note, the auto_workflow.py jobs are typically run on CURC's compute resources permitting access to CURC's :code:`/scratch/alpine/` and :code:`/pl/active/` directory paths. Other directory paths (such as a user's local computer) can ONLY be used if the user creates a unique "workflow template" and runs the auto_workflow.py script on their local machine. For users desiring this setting, contact INC Staff to ensure correct implementation. ::

        "download-path": "/pl/active/ics/flanker/analysis",

:code:`custom-download-script`

    __(optional)__ For workflows requiring data manipulation after download (e.g. file renaming, resampling to new datatype, etc), users can include a single shell script stored in the :code:`Project` files in Flywheel. Users wishing to use this option should contact INC Staff for consultation.::

            "custom-download-script": "custom_download_script-fmriprep.txt"




Looking for sample workflow template, check out our github repository `here <https://github.com/intermountainneuroimaging/fw-gear-rules>`_.

