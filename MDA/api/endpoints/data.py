from flask import request,render_template,make_response,jsonify,redirect,url_for
from flask_restplus import Resource
from ..handlers.handlers import *
from models import *
from ..endpoints import api



artefact_ns = api.namespace('api/artefact', description='Stages')

foundation_ns = api.namespace('api/foundation', description='Foundation')

audit_ns = api.namespace('api/audit', description='Audit')

########################################
@audit_ns.route('/master')
@api.doc(params={'Purpose': 'Audit Master'})
class AuditMaster(Resource):
    def post(self):
        pass
    def get(self):
        pass

@audit_ns.route('/detail')
@api.doc(params={'Purpose': 'Audit Detail'})
class AuditDetail(Resource):
    def post(self):
        pass
    def get(self):
        pass

@audit_ns.route('/error')
@api.doc(params={'Purpose': 'Audit Error'})
class AuditError(Resource):
    def post(self):
        pass
    def get(self):
        pass

########################################
@foundation_ns.route('/process')
@api.doc(params={'Purpose': 'Name of each supported processes'})
class Process(Resource):
    def post(self):
        pass
    def get(self):
        pass

@foundation_ns.route('/process/<string:process_id>')
class SingleProcess(Resource):
    def put(self,process_id):
        pass
    def get(self,process_id):
        pass
    def delete(self,process_id):
        pass
########################################
@foundation_ns.route('/process_group')
class ProcessGroup(Resource):
    def post(self):
        pass
    def get(self):
        pass

@foundation_ns.route('/process_group/<string:process_group_id>')
class SingleProcessGroup(Resource):
    def put(self,process_group_id):
        pass
    def get(self,process_group_id):
        pass
    def delete(self,process_group_id):
        pass
########################################
@foundation_ns.route('/attribute_data_type')
class AttributeDataType(Resource):
    def post(self):
        pass
    def get(self):
        pass

@foundation_ns.route('/attribute_data_type/<string:attribute_data_type_id>')
class SingleAttributeDataType(Resource):
    def put(self,attribute_data_type_id):
        pass
    def get(self,attribute_data_type_id):
        pass
    def delete(self,attribute_data_type_id):
        pass

########################################
@foundation_ns.route('/execution_frequency')
class ExecutionFrequency(Resource):
    def post(self):
        pass
    def get(self):
        pass

@foundation_ns.route('/execution_frequency/<string:execution_frequency_id>')
# Daily, Weekly Etc
class SingleExecutionFrequency(Resource):
    def put(self,execution_frequency_id):
        pass
    def get(self,execution_frequency_id):
        pass
    def delete(self,execution_frequency_id):
        pass

########################################
@foundation_ns.route('/execution_interval')
# For Each Frequency, Master list of Slices (Start time, end time)
class ExecutionInterval(Resource):
    def post(self):
        pass
    def get(self):
        pass

@foundation_ns.route('/execution_interval/<string:execution_interval_id>')
class SingleExecutionInterval(Resource):
    def put(self,execution_interval_id):
        pass
    def get(self,execution_interval_id):
        pass
    def delete(self,execution_interval_id):
        pass

########################################
@foundation_ns.route('/dependency_type')
# Parent, Child, Sibling etc
class DependencyType(Resource):
    def post(self):
        pass
    def get(self):
        pass

@foundation_ns.route('/dependency_type/<string:dependency_type_id>')
class SingleDependencyType(Resource):
    def put(self,dependency_type_id):
        pass
    def get(self,dependency_type_id):
        pass
    def delete(self,dependency_type_id):
        pass
########################################
@artefact_ns.route('/')
class Artefact(Resource):
    @api.expect(ArtefactRecordRequest)
    def post(self):
        response = createArtefact(request)
        return response,201
    @api.marshal_with(ArtefactRecordSerializer, as_list=True)
    def get(self):
        response = getAllArtefact()
        return response, 200

@artefact_ns.route('/<string:artefact_id>')
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
########################################

@artefact_ns.route('/<string:artefact_id>/artefact_property/multi_create')
class ArtefactPropertyMultiCreate(Resource):
    @api.expect(ArtefactPropertyListRecordRequest)
    def post(self,artefact_id):
        response = createArtefactPropertyMultiCreate(artefact_id,request.json.get('property_list'))

@artefact_ns.route('/<string:artefact_id>/artefact_property')
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

@artefact_ns.route('/<string:artefact_id>/artefact_property/<string:artefact_property_id>')
class SingleArtefactProperty(Resource):
    def get(self,artefact_id,artefact_property_id):
        response = getSingleArtefactProperty(artefact_id,artefact_property_id)
        return response, 200

    def put(self,artefact_id,artefact_property_id):
        response = updateSingleArtefactProperty(artefact_id,artefact_property_id)
        return response, 200

    def delete(self,artefact_id,artefact_property_id):
        response = deleteSingleArtefactProperty(artefact_id,artefact_property_id)
        return response, 200

########################################

@artefact_ns.route('/<string:artefact_id>/artefact_process_property/multi_create')
class ArtefactProcessPropertyMultiCreate(Resource):
    def post(self,artefact_id):
        pass

@artefact_ns.route('/<string:artefact_id>/artefact_process_property')
class ArtefactProcessProperty(Resource):
    def post(self,artefact_id):
        return response,201

    def get(self,artefact_id):
        return response, 200

@artefact_ns.route('/<string:artefact_id>/artefact_process_property/<string:artefact_process_property_id>')
class SingleArtefactProcessProperty(Resource):
    def get(self,artefact_id,artefact_process_property_id):
        pass

    def put(self,artefact_id,artefact_process_property_id):
        pass

    def delete(self,artefact_id,artefact_process_property_id):
        pass

########################################

@artefact_ns.route('/<string:artefact_id>/artefact_schema')
class ArtefactSchema(Resource):
    def post(self,artefact_id):
        print request.json
        response = createArtefactSchema(artefact_id,request)
    def get(self,artefact_id):
        print request.json
        response = getArtefactSchema(artefact_id)

@artefact_ns.route('/<string:artefact_id>/artefact_schema/<string:field_id>')
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

########################################

@artefact_ns.route('/<string:artefact_id>/dependency')
class ArtefactParent(Resource):
    def post(self,artefact_id):
        print request.json
        response = createArtefactDependency(artefact_id,request)

    def get(self,artefact_id):
        response = getAllArtefactDependency(artefact_id)
        return response, 200

########################################

@artefact_ns.route('/<string:artefact_id>/execution_interval')
class ArtefactExecutionInterval(Resource):
    def post(self,artefact_id):
        print request.json
        response = createArtefactExecutionInterval(artefact_id,request)

    def get(self):
        response = getAllArtefactExecutionInterval(artefact_id)
        return response, 200

@artefact_ns.route('/<string:artefact_id>/execution_interval/status/<string:status>')
class ArtefactExecutionIntervalByStatus(Resource):
    def get(self):
        response = getAllArtefactExecutionIntervalByStatus(artefact_id,status)
        return response, 200

@artefact_ns.route('/<string:artefact_id>/execution_interval/<string:execution_interval_id>/')
class SingleArtefactExecutionInterval(Resource):
    def put(self,artefact_id,execution_interval_id):
        print request.json
        response = createSingleArtefactExecutionInterval(artefact_id,execution_interval_id,request)

    def get(self):
        response = getArtefactExecutionIntervalByStatus(artefact_id,execution_interval_id)
        return response, 200

    def delete(self):
        response = deleteArtefactExecutionIntervalByStatus(artefact_id,execution_interval_id)
        return response, 200

@artefact_ns.route('/<string:artefact_id>/execution_interval/<string:execution_interval_id>/parent_status')
class SingleArtefactExecutionIntervalParentStatus(Resource):
    def get(self,artefact_id,execution_interval_id):
        response = getSingleArtefactExecutionIntervalParentStatus(artefact_id,execution_interval_id,request)
