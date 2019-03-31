from ..database import db
from ..database.models import *
from sqlalchemy.orm.exc import NoResultFound
from flask_restplus import fields

from flask_restplus import reqparse
from datetime import datetime

def safeCommit():
    try:
        db.session.commit()
    except:
        print "Rolling Back"
        db.session.rollback()
        raise

def safeFlush():
    try:
        db.session.flush()
    except:
        print "Rolling Back"
        db.session.rollback()
        raise

def modelExists(db,model):
    try:
        r = db.session.query(model).one()
        return True
    except:
        return False

def createAllModels(db):
    db.create_all()


def createArtefact(request):
    createAllModels(db)
    payload = {}
    payload['name'] = request.json.get('name')
    r = Artefact(payload)
    db.session.add(r)
    db.session.commit()
    return { "artedact_id" : r.artefact_id}


def getAllArtefact():
    createAllModels(db)
    qryRes = Artefact\
                  .query\
                  .all()
    print qryRes
    if qryRes:
        return qryRes  #[i.serialize for i in qryRes]
    else:
        pass


def createArtefactProperty(artefact_id,payload):
    r = ArtefactProperty(artefact_id,payload)
    db.session.add(r)
    db.session.commit()
    return { "artefact_property_id" : r.artefact_property_id}

def createArtefactPropertyMultiCreate(artefact_id,payload_list):
    l = []
    print payload_list
    for p in payload_list:
        apid = createArtefactProperty(artefact_id,p)
        l.append(apid)
    return l

def getAllArtefactProperty(artefact_id):
    qryRes = ArtefactProperty\
                  .query\
                  .filter_by(artefact_id=artefact_id)\
                  .all()

    if qryRes:
        return qryRes  
    else:
        pass
