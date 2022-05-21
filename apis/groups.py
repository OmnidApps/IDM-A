from flask_restx import Resource
from flask import request

from apis.APIModels.Group import GroupFields, GroupCreateFields, GroupUpdateFields, GroupMemberModifyFields
from apis.namespaces import group_api
from core.logic.Groups import GroupController
from core.logic.Users import UserController
from core.ViewSchemas.Group import *

gcon = GroupController()


@group_api.route('/all')
class Groups(Resource):
    @group_api.doc('list_groups')
    @group_api.marshal_list_with(GroupFields)
    def get(self):
        '''List all groups.'''
        groups = gcon.get_all()
        if groups is None:
            return 'No groups found.', 404

        return groups_schema.dump(groups)

@group_api.route('/create')
class Group(Resource):
    @group_api.doc('create_group')
    @group_api.expect(GroupCreateFields)
    @group_api.response( 201, 'Group created.' )
    @group_api.response( 400, 'Failed to create group.' )
    def post( self ):
        '''Create a group.'''
        new_group = gcon.create(
            name=request.json['name']
        )

        if new_group is None:
            return 'Failed to create group.', 400

        return group_schema.dump(new_group), 201

@group_api.route('/uuid/<uuid>')
@group_api.param('uuid', 'The group UUID.')
@group_api.response( 404, 'Group not found.' )
class Group(Resource):
    @group_api.doc('get_group_uuid')
    def get(self, group_uuid ):
        '''Get group details by group UUID.'''
        group = gcon.get_uuid( uuid=group_uuid )
        if group is None:
            return 'Group not found.', 404
        return group_schema.dump(group)

    def put( self, group_uuid ):
        '''Rename a group.'''
        group = gcon.get_uuid( uuid=group_uuid )
        if group is None:
            return 'Group not found.', 404

        result = gcon.update( group, request.json['name'] )
        if result is None:
            return 'Failed to update group.', 400

        return group_schema.dump( result )


@group_api.route('/name/<name>')
@group_api.param('name', 'The group name.')
@group_api.response( 404, 'Group not found.' )
class Group(Resource):
    @group_api.doc('get_group_byname')
    def get(self, group_name ):
        '''Get group details by group name.'''
        group = gcon.get_name( name=group_name )
        if group is None:
            return 'Group not found.', 404
        return group_schema.dump(group)

    @group_api.doc( 'delete_group_uuid' )
    def delete(self, group_uuid ):
        '''Delete an empty group.'''
        pass


@group_api.route('/uuid/<uuid>/members')
@group_api.param('uuid', 'The group UUID.')
@group_api.response( 404, 'Group not found.' )
class Group(Resource):
    @group_api.doc('add_user_to_group')
    @group_api.expect(GroupMemberModifyFields)
    def put(self, uuid ):
        '''Add a user to a group.'''
        group = gcon.get_uuid( uuid=uuid )
        if group is None:
            return 'Group not found.', 404

        ucon = UserController()
        user = ucon.get_uuid( uuid=request.json['uuid'] )

        if user is None:
            return 'User not found.', 401

        result = gcon.add_member( group=group, user=user )
        if result is None:
            return 'Failed to append group.', 400
        return group_schema.dump(result), 201

    @group_api.doc('remove_user_from_group')
    def delete( self, uuid ):
        '''Remove a user from a group.'''
        pass