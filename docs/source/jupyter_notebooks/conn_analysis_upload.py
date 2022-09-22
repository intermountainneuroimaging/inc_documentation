#!/bin/python

from pathlib import Path
import sys, os, logging

sys.path.append('/projects/ics/software/flywheel-python/bids-client/')
sys.path.append('/projects/ics/software/flywheel-python/')
import flywheel, flywheel_gear_toolkit
from datetime import datetime

# Only execute if file is run as main, not when imported by another module
if __name__ == "__main__":
    # Instantiate a logger
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
    log = logging.getLogger('root')

    # Create client, using CLI credentials
    fw = flywheel.Client()

    # who am I logged in as?
    log.info('You are now logged in as %s to %s', fw.get_current_user()['email'], fw.get_config()['site']['api_url'])

    project = fw.lookup('<group>/<project>')

    # create new project level analysis
    analysis = project.add_analysis(label='CONN Analysis: ' + datetime.now(" %x %X"))

    # zip outputs...
    os.system('zip -R conn_analysis conn_analysis/ conn_analysis.mat')

    # upload output zipped directories
    analysis.upload_output('conn_analysis.zip')

    if os.path.exists('conn_inputs.zip'):
        os.system('zip -R conn_inputs conn_inputs/ ')
        analysis.upload_output('conn_inputs.zip')



