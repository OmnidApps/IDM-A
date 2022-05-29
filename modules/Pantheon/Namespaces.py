from flask_restx import Namespace


class NamespaceWrapper(Namespace):
    def expect_header(self, name, desc):
        return self.doc(params={name: {"in": "header", "description": desc}})

    def input_schema(self, schema):
        return self.expect(schema)

    def expect_url_var(self, variable, desc):
        return self.param(variable, desc)

    def output_schema(self, schema):
        return self.marshal_list_with(schema, mask='')


user_api = NamespaceWrapper('user', description='User Management API')
group_api = NamespaceWrapper('group', description='Group Management API')
session_api = NamespaceWrapper('session', description='Session Management API')
