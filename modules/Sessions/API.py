from flask_restx import Resource
from flask import request, g
from functools import wraps
from modules.Pantheon.Factory import app
from modules.Sessions.APIModels import SessionFields, SessionCreateFields, InsecureSessionFields
from modules.Pantheon.Namespaces import session_api
from modules.Sessions.Controller import session_controller
from modules.Sessions.ViewSchemas import session_schema, sessions_schema




@session_api.route('/all')
class Sessions(Resource):
    @session_api.doc('list_sessions')
    @session_api.marshal_list_with(InsecureSessionFields)
    def get(self):
        '''List all Sessions.'''
        sessions = session_controller.get_all()
        if sessions is None:
            return 'No sessions found.', 404

        return sessions_schema.dump(sessions)


@session_api.route('/create')
class Sessions(Resource):
    @session_api.doc('create_session')
    @session_api.expect(SessionCreateFields)
    @session_api.response(201, 'Session created.')
    @session_api.response(400, 'Failed to create session.')
    def post(self):
        '''Create a session.'''
        session = session_controller.create( uuid=request.json['uuid'], password=request.json['password'] )
        if session is None:
            return 'No session could be created.', 401

        return session_schema.dump(session), 201
