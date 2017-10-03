#####################################################################################
# Program name: servicenow.py
# Program Desc: Endpoints for servicenow wrapper API's which will be consumed by Client Portal
# Project Name: API-Repository > ServiceNow > SNAPI-DEV
# TFS Location: $/CloudEngineering/API-Repository/ServiceNow/
# Initial Date: September 2016
# Modified Dt.: 10/10/2016
# Author: Ravikant Khond and Rohit Srivastava
# Last Modified: Ravikant Khond
#####################################################################################
# Change Log
# 10/10/2016 - RAK The initial draft was modified to accept change in cases API filter. Added more filters to cases API.
# 11/02/2016 - RAK Updated to bring all SN API URLs at one place.
# 11/03/2016 - RAK Developed wrapper APIs for insert and update client portal APIs
# 11/08/2016 - RAK Modified create case and update case API to use scripted ServiceNow APIs
# 11/18/2016 - DL  Modified servicenow wrapper API program to use snconfig file for list of SN API's
# 12/29/2016 - DL  Added catalog endpoint to create a catalog request in service now
# 12/29/2016 - RAK Modified servicenowapi.conf to change SN API link from JSONv2 to scripted API for updating CP user in SN 
# 01/03/2017 - DL  Modified servicenowapi.conf to store servicenow user information and log file
# 01/12/2017 - DL  Added cancel and add comments for catalog item requests
# 01/13/2017 - DL  Added to get the list of catalog request items
# 02/10/2017 - RAK Modified API for case details API. watch list users has been replaced with emails. Change in SN API. Table SN API replaced with scripted API.
# 02/22/2017 - RAK Modified to add update request API
# 03/01/2017 - RAK Modified to use sys_id instead of number in get case details API.
# 03/10/2017 - DL  Created notification group API.
# 04/11/2017 - RAK Modified GET API for case details and request details to add mcCode parameter to corresponding SN API
# 05/08/2017 - RAK Modified users put and delete methods to include account parameter in URL of SN API Call
#####################################################################################

from flask import Flask, jsonify, abort, request, Response, make_response, after_this_request,send_file,send_from_directory
from pprint import pprint, pformat
import os , os.path
import requests
from requests.auth import HTTPDigestAuth
import sys
import time
import logging
import decorators
from werkzeug import secure_filename
from flask.ext.restful import reqparse, abort, Api, Resource, fields,\
    marshal_with
from flask_restful_swagger import swagger
import base64
from time import gmtime, strftime
import json
from multiprocessing import Pool
from flask_restful_swagger import swagger
from snWrapperSwaggerDocs import docDict 

#from eagle_status import getEagleCEApiStatusObj
#app = Flask(__name__)
app = Flask(__name__, static_folder='../static')

###################################
# This is important:
api = swagger.docs(Api(app), apiVersion='0.1',
                   basePath='http://localhost:5000',
                   resourcePath='/',
                   produces=["application/json", "text/html"],
                   api_spec_url='/api/spec',
                   description='A Basic API')
###################################


UPLOAD_FOLDER = '/tmp/'
ALLOWED_EXTENSIONS = set(['txt','png','jpeg','jpg','doc','docx','xls','xlsx','ppt','pptx','csv'])




class Cases(Resource):
	@swagger.operation(
	notes="Get Cases  the client",
	nickname="get cases",
	parameters= docDict['Cases']['get'])
	def get(self,mcCode):
		print(docDict["Cases"]["get"])
		return jsonify({"msg":"its ok"})
		
api.add_resource(Cases, "/clients/<mcCode>/cases")

# -----------------------------------------------------------------------------------------------------------------------------
# Main Routine
# -----------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	app.run(threaded=True)
