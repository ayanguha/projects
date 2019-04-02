import uuid
from flask import jsonify
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def __str2datetime__(s):
    try:
        return datetime.strptime(s,'%Y-%m-%dT%H:%M:%S.%fZ')
    except:
        return datetime.strptime(s + 'T00:00:00.000Z','%Y-%m-%dT%H:%M:%S.%fZ')

def __datetime2str__(d):
    return datetime.strftime(d,'%Y-%m-%dT%H:%M:%S.%fZ').decode('utf-8', 'ignore')
def __stringifyArray__(arr):
    return ",".join(arr)
def __stringifyArrayStruct__(arr):
    return "|".join([",".join([i+'#'+str(k[i]) for i in k.keys()]) for k in arr])
def __DestringifyArray__(s):
    return s.split(',')
def __DestringifyArrayStruct__(s):
    try:
        arr = [dict([i.split('#') for i in k.split(",")]) for k in s.split('|')]
    except:
        arr = []
    return arr

class Artefact(db.Model):
    artefact_id = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    operational_status = db.Column(db.String(255), unique=False, nullable=False)
    postedOn = db.Column(db.DateTime(), unique=False, nullable=False)
    updatedOn = db.Column(db.DateTime(), unique=False, nullable=False)


    def __init__(self,payload):
        self.artefact_id = str(uuid.uuid4())
        self.name = payload['name']
        self.operational_status = 'CREATED'
        self.postedOn = datetime.now()
        self.updatedOn = datetime.now()




class ArtefactProperty(db.Model):
    artefact_property_id = db.Column(db.String(255), primary_key=True)
    artefact_id = db.Column(db.String(255), nullable=False)
    property_name = db.Column(db.String(255), unique=False, nullable=False)
    property_value = db.Column(db.String(255), unique=False, nullable=False)
    postedOn = db.Column(db.DateTime(), unique=False, nullable=False)
    updatedOn = db.Column(db.DateTime(), unique=False, nullable=False)


    def __init__(self,artefact_id,payload):
        self.artefact_property_id = str(uuid.uuid4())
        self.artefact_id = artefact_id
        self.property_name = payload['property_name']
        self.property_value = payload['property_value']
        self.postedOn = datetime.now()
        self.updatedOn = datetime.now()
