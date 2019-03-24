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
    print r.id
    db.session.add(r)
    db.session.commit()
    return { "artedact_id" : r.id}


def getAllArtefact():
    qryRes = Artefact\
                  .query\
                  .all()

    if qryRes:
        return [i.serialize for i in qryRes]
    else:
        raise NoResultFound
