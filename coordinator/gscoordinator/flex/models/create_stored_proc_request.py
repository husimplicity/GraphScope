from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from gscoordinator.flex.models.base_model import Model
from gscoordinator.flex import util


class CreateStoredProcRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, description=None, type=None, query=None):  # noqa: E501
        """CreateStoredProcRequest - a model defined in OpenAPI

        :param name: The name of this CreateStoredProcRequest.  # noqa: E501
        :type name: str
        :param description: The description of this CreateStoredProcRequest.  # noqa: E501
        :type description: str
        :param type: The type of this CreateStoredProcRequest.  # noqa: E501
        :type type: str
        :param query: The query of this CreateStoredProcRequest.  # noqa: E501
        :type query: str
        """
        self.openapi_types = {
            'name': str,
            'description': str,
            'type': str,
            'query': str
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'type': 'type',
            'query': 'query'
        }

        self._name = name
        self._description = description
        self._type = type
        self._query = query

    @classmethod
    def from_dict(cls, dikt) -> 'CreateStoredProcRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CreateStoredProcRequest of this CreateStoredProcRequest.  # noqa: E501
        :rtype: CreateStoredProcRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this CreateStoredProcRequest.


        :return: The name of this CreateStoredProcRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this CreateStoredProcRequest.


        :param name: The name of this CreateStoredProcRequest.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self) -> str:
        """Gets the description of this CreateStoredProcRequest.


        :return: The description of this CreateStoredProcRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this CreateStoredProcRequest.


        :param description: The description of this CreateStoredProcRequest.
        :type description: str
        """

        self._description = description

    @property
    def type(self) -> str:
        """Gets the type of this CreateStoredProcRequest.


        :return: The type of this CreateStoredProcRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this CreateStoredProcRequest.


        :param type: The type of this CreateStoredProcRequest.
        :type type: str
        """
        allowed_values = ["cpp", "cypher"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def query(self) -> str:
        """Gets the query of this CreateStoredProcRequest.


        :return: The query of this CreateStoredProcRequest.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query: str):
        """Sets the query of this CreateStoredProcRequest.


        :param query: The query of this CreateStoredProcRequest.
        :type query: str
        """
        if query is None:
            raise ValueError("Invalid value for `query`, must not be `None`")  # noqa: E501

        self._query = query