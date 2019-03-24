from flask import request,render_template,make_response,jsonify,redirect,url_for
from flask_restplus import Resource
from ..database.models import *
from ..handlers.handlers import *
from flask_restplus import abort
import traceback

from flask_restplus import Api

api = Api(version='1.0', title='ETL MEta',doc='/doc/',description='ETL Meta API')


ns = api.namespace('api', description='Operations: Audit records')

ArtefactRecordRequest = api.model('Artefact Record ', {
    'name': fields.String(required=True, description='Artefact Name'),
    'operational_status': fields.String(required=False, description='Artefact State, Active, INACTIVE, PAUSED etc'),
    'postedOn': fields.DateTime(required=False, description='Artefact Create Date'),
    'updatedOn': fields.DateTime(required=False, description='Artefact Update Date')
})

@ns.route('/artefact')
class Artefact(Resource):
    @api.expect(ArtefactRecordRequest)
    def post(self):
        print request.json
        response = createArtefact(request)
        return response,201

    def get(self):
        response = getAllArtefact()
        return response, 200

@ns.route('/artefact/<string:artefact_id>')
class SingleArtefact(Resource):
    def get(self,artefact_id):
        response = getSingleArtefact(artefact_id)
        return response, 200

    def put(self,artefact_id):
        response = updateSingleArtefact(artefact_id,request)
        return response, 200

    def delete(self,artefact_id):
        response = deleteSingleArtefact(artefact_id)
        return response, 200

@ns.route('/artefact/<string:artefact_id>/artefact_property/multi_create')
class ArtefactDetailsMultiCreate(Resource):
    def post(self,artefact_id):
        print request.json
        response = createArtefactPropertyMultiCreate(artefact_id,request)

@ns.route('/artefact/<string:artefact_id>/artefact_property')
class ArtefactDetails(Resource):
    def post(self,artefact_id):
        print request.json
        response = createArtefactProperty(artefact_id,request)

    def get(self,artefact_id):
        response = getAllArtefactProperty(artefact_id)
        return response, 200

@ns.route('/artefact/<string:artefact_id>/artefact_property/<string:artefact_property_id>')
class SingleArtefactDetail(Resource):
    def get(self,artefact_id,artefact_property_id):
        response = getSingleArtefactProperty(artefact_id,artefact_property_id)
        return response, 200

    def put(self,artefact_id):
        response = updateSingleArtefactProperty(artefact_id,artefact_property_id)
        return response, 200

    def delete(self,artefact_id):
        response = deleteSingleArtefactProperty(artefact_id,artefact_property_id)
        return response, 200

@ns.route('/artefact/<string:artefact_id>/artefact_schema')
class ArtefactSchema(Resource):
    def post(self,artefact_id):
        print request.json
        response = createArtefactSchema(artefact_id,request)
    def get(self,artefact_id):
        print request.json
        response = getArtefactSchema(artefact_id)

@ns.route('/artefact/<string:artefact_id>/artefact_schema/<string:field_id>')
class ArtefactSchemaField(Resource):
    def get(self,artefact_id,field_id):
        response = getSingleArtefactSchemaField(artefact_id,field_id)
        return response, 200

    def put(self,artefact_id,field_id):
        response = updateSingleArtefactSchemaField(artefact_id,field_id)
        return response, 200

    def delete(self,artefact_id,field_id):
        response = deleteSingleArtefactSchemaField(artefact_id,field_id)
        return response, 200

@ns.route('/artefact/<string:artefact_id>/parent')
class ArtefactParent(Resource):
    def post(self,artefact_id):
        print request.json
        response = createArtefactParent(artefact_id,request)

    def get(self,artefact_id):
        response = getAllArtefactParent(artefact_id)
        return response, 200

@ns.route('/artefact/<string:artefact_id>/parent/<string:parent_id>')
class ArtefactSingleParent(Resource):
    def delete(self,artefact_id,parent_id):
        response = deleteSingleArtefactParent(artefact_id,parent_id)
        return response, 200

@ns.route('/artefact/<string:artefact_id>/parent/pending')
class ArtefactParentPending(Resource):
    def get(self,artefact_id):
        response = getAllArtefactParentPending(artefact_id)
        return response, 200

@ns.route('/artefact<string:artefact_id>/schedule_unit')
class ArtefactScheduleUnit(Resource):
    def post(self,artefact_id):
        print request.json
        response = createArtefactScheduleUnit(artefact_id,request)

    def get(self):
        response = getAllArtefactScheduleUnit(artefact_id)
        return response, 200

@ns.route('/artefact<string:artefact_id>/schedule_unit/<string:status>')
class ArtefactScheduleUnitByStatus(Resource):
    def get(self,artefact_id,status):
        response = getArtefactScheduleUnitByStatus(artefact_id,status)
        return response, 200
