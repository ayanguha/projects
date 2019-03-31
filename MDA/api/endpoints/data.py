from flask import request,render_template,make_response,jsonify,redirect,url_for
from flask_restplus import Resource
from ..database.models import *
from ..handlers.handlers import *
from flask_restplus import abort
import traceback

from flask_restplus import Api

api = Api(version='1.0', title='ETL MEta',doc='/doc/',description='ETL Meta API')


ns = api.namespace('api/artefact', description='Operations: Audit records')

ArtefactRecordRequest = api.model('Artefact Record ', {
    'name': fields.String(required=True, description='Artefact Name'),
    'operational_status': fields.String(required=False, description='Artefact State, Active, INACTIVE, PAUSED etc'),
    'postedOn': fields.DateTime(required=False, description='Artefact Create Date'),
    'updatedOn': fields.DateTime(required=False, description='Artefact Update Date')
})

ArtefactRecord = api.model('Artefact Record With Id', {
    'artefact_id': fields.String(),
    'name': fields.String(),
    'operational_status': fields.String(),
    'postedOn': fields.DateTime(),
    'updatedOn': fields.DateTime()
})

ArtefactPropertyRecordRequest = api.model('Artefact Property Record ', {
    'property_name': fields.String(required=True),
    'property_value': fields.String(required=False),
    'postedOn': fields.DateTime(required=False),
    'updatedOn': fields.DateTime(required=False)
})

ArtefactPropertyListRecordRequest = api.model('Artefact Property List Record ', {
    'propert_list': fields.List(fields.Nested(ArtefactPropertyRecordRequest))
})

ArtefactPropertyRecord = api.model('Artefact Property Record With Id', {
    'artefact_id': fields.String(required=True),
    'artefact_property_id': fields.String(required=True),
    'property_name': fields.String(required=True),
    'property_value': fields.String(required=False),
    'postedOn': fields.DateTime(required=False),
    'updatedOn': fields.DateTime(required=False)
})

@ns.route('/')
class Artefact(Resource):
    @api.expect(ArtefactRecordRequest)
    def post(self):
        response = createArtefact(request)
        return response,201
    @api.marshal_with(ArtefactRecord, as_list=True)
    def get(self):
        response = getAllArtefact()
        return response, 200

@ns.route('/<string:artefact_id>')
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

@ns.route('/<string:artefact_id>/artefact_property/multi_create')
class ArtefactPropertyMultiCreate(Resource):
    @api.expect(ArtefactPropertyListRecordRequest)
    def post(self,artefact_id):
        response = createArtefactPropertyMultiCreate(artefact_id,request.json.get('property_list'))

@ns.route('/<string:artefact_id>/artefact_property')
class ArtefactProperty(Resource):
    @api.expect(ArtefactPropertyRecordRequest)
    def post(self,artefact_id):
        payload = {}
        payload['property_name'] = request.json.get('property_name')
        payload['property_value'] = request.json.get('property_value')
        response = createArtefactProperty(artefact_id,payload)
        return response,201

    @api.marshal_with(ArtefactPropertyRecord, as_list=True)
    def get(self,artefact_id):
        response = getAllArtefactProperty(artefact_id)
        return response, 200

@ns.route('/<string:artefact_id>/artefact_property/<string:artefact_property_id>')
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

@ns.route('/<string:artefact_id>/artefact_schema')
class ArtefactSchema(Resource):
    def post(self,artefact_id):
        print request.json
        response = createArtefactSchema(artefact_id,request)
    def get(self,artefact_id):
        print request.json
        response = getArtefactSchema(artefact_id)

@ns.route('/<string:artefact_id>/artefact_schema/<string:field_id>')
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

@ns.route('/<string:artefact_id>/parent')
class ArtefactParent(Resource):
    def post(self,artefact_id):
        print request.json
        response = createArtefactParent(artefact_id,request)

    def get(self,artefact_id):
        response = getAllArtefactParent(artefact_id)
        return response, 200

@ns.route('/<string:artefact_id>/parent/<string:parent_id>')
class ArtefactSingleParent(Resource):
    def delete(self,artefact_id,parent_id):
        response = deleteSingleArtefactParent(artefact_id,parent_id)
        return response, 200

@ns.route('/<string:artefact_id>/schedule_unit')
class ArtefactScheduleUnit(Resource):
    def post(self,artefact_id):
        print request.json
        response = createArtefactScheduleUnit(artefact_id,request)

    def get(self):
        response = getAllArtefactScheduleUnit(artefact_id)
        return response, 200

@ns.route('/<string:artefact_id>/schedule_unit/<string:status>')
class ArtefactScheduleUnitByStatus(Resource):
    def get(self,artefact_id,status):
        response = getArtefactScheduleUnitByStatus(artefact_id,status)
        return response, 200

@ns.route('/<string:artefact_id>/schedule_unit/<string:schedule_unit_id>/parent')
class ArtefactScheduleUnitParent(Resource):
    def post(self,artefact_id,schedule_unit_id):
        print request.json
        response = createArtefactScheduleUnitParent(artefact_id,schedule_unit_id,request)

    def get(self):
        response = getAllArtefactScheduleUnitParent(artefact_id,schedule_unit_id)
        return response, 200
