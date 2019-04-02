from ..endpoints import api
from flask_restplus import fields

ProcessRecordRequest = api.model('Process Record ', {
    'name': fields.String(required=True, description='Process Name')
})

ProcessRecordSerializer = api.model('Process Record ', {
    'ProcessId': fields.String(),
    'name': fields.String(),
    'IsActive': fields.String(),
    'postedOn': fields.DateTime(),
    'updatedOn': fields.DateTime()
})

ArtefactRecordRequest = api.model('Artefact Record ', {
    'name': fields.String(required=True, description='Artefact Name')
})

ArtefactRecordSerializer = api.model('Artefact Record With Id', {
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
