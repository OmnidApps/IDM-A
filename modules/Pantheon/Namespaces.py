from flask_restx import Namespace


class NamespaceWrapper(Namespace):
    """Wrap `flask_restx.Namespace` to provide helper utilities."""

    def expect_header(self, name, desc):
        """
        Add required header to API specification for the decorated endpoint

        :param str name: The name of the header
        :param str desc: Human readable description of the header
        """
        return self.doc(params={name: {"in": "header", "description": desc}})

    def input_schema(self, schema):
        """
        Define model for input data for the decorated endpoint

        :param str schema: Model for input data
        """

        return self.expect(schema)

    def expect_url_var(self, variable, desc):
        """
        Add required URL variable

        :param str variable: Name of variable to expect in URL
        :param str desc: Human readable description of variable
        """
        return self.param(variable, desc)

    def output_schema(self, schema):
        """
        Define model for output data for the decorated endpoint

        :param str schema: Model for output data
        """

        return self.marshal_list_with(schema, mask='')


user_api = NamespaceWrapper('user', description='User Management API')
group_api = NamespaceWrapper('group', description='Group Management API')
session_api = NamespaceWrapper('session', description='Session Management API')
