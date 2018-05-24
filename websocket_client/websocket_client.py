#!/usr/bin/python

#-------------------------------------------------------------------------------

#import logging
#logging.getLogger('requests').setLevel(logging.WARNING)
#logging.basicConfig(level=logging.DEBUG)

import json, time

from socketIO_client import SocketIO, BaseNamespace
from flask import jsonify, json as flask_json
from pprint import pprint

connected = 0

#-------------------------------------------------------------------------------

datastream_js = {'text': "- CCU: Datastream activated"}
connected_js = {'text': "- CCU: Connection Accomplised"}

#-------------------------------------------------------------------------------

# Define Namespace for basic communication with ccu
class StatusNamespace(BaseNamespace):
    # function handler for connect event from iotcloud
    def on_connect(*args):
        # Print feedback from iotcloud about connection
        print(args[1]['text'])
        # Tell iotcloud about activation of datastream
        socketIO.emit('message', connected_js, namespace='/status')
        # When connected to ccu, connect data channel
        socketIO.define(DataNamespace, '/data')
        # Print feedback from iotcloud
        print(args[1]['text'])

# Define Namespace for datastrom between ccu and iotcloud
class DataNamespace(BaseNamespace):
    def on_connect(*args):
        # Tell iotcloud about activation of datastream
        socketIO.emit('message', datastream_js)
        # Print feedback from iotcloud about connection
        print(args[1]['text'])

    def on_response(*args):
            # Print streamed data from iotcloud
            print(args[1][1]['status'])

print('CCU: Starting connection to IoTCloud...')

socketIO = SocketIO('ccurestapi.ddns.net', 8000, StatusNamespace)

socketIO.define(StatusNamespace, '/status')

#-------------------------------------------------------------------------------
