# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mcenter_server_api.models.base_model_ import Model
from mcenter_server_api import util


class PipelinePattern(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, created=None, created_by=None, default_model_id=None, engine_type=None, id=None, is_profile=None, is_user_defined=None, is_visible=None, name=None, pipeline=None):  # noqa: E501
        """PipelinePattern - a model defined in OpenAPI

        :param created: The created of this PipelinePattern.  # noqa: E501
        :type created: int
        :param created_by: The created_by of this PipelinePattern.  # noqa: E501
        :type created_by: str
        :param default_model_id: The default_model_id of this PipelinePattern.  # noqa: E501
        :type default_model_id: str
        :param engine_type: The engine_type of this PipelinePattern.  # noqa: E501
        :type engine_type: str
        :param id: The id of this PipelinePattern.  # noqa: E501
        :type id: str
        :param is_profile: The is_profile of this PipelinePattern.  # noqa: E501
        :type is_profile: bool
        :param is_user_defined: The is_user_defined of this PipelinePattern.  # noqa: E501
        :type is_user_defined: bool
        :param is_visible: The is_visible of this PipelinePattern.  # noqa: E501
        :type is_visible: bool
        :param name: The name of this PipelinePattern.  # noqa: E501
        :type name: str
        :param pipeline: The pipeline of this PipelinePattern.  # noqa: E501
        :type pipeline: str
        """
        self.openapi_types = {
            'created': 'int',
            'created_by': 'str',
            'default_model_id': 'str',
            'engine_type': 'str',
            'id': 'str',
            'is_profile': 'bool',
            'is_user_defined': 'bool',
            'is_visible': 'bool',
            'name': 'str',
            'pipeline': 'str'
        }

        self.attribute_map = {
            'created': 'created',
            'created_by': 'createdBy',
            'default_model_id': 'defaultModelId',
            'engine_type': 'engineType',
            'id': 'id',
            'is_profile': 'isProfile',
            'is_user_defined': 'isUserDefined',
            'is_visible': 'isVisible',
            'name': 'name',
            'pipeline': 'pipeline'
        }

        self._created = created
        self._created_by = created_by
        self._default_model_id = default_model_id
        self._engine_type = engine_type
        self._id = id
        self._is_profile = is_profile
        self._is_user_defined = is_user_defined
        self._is_visible = is_visible
        self._name = name
        self._pipeline = pipeline

    @classmethod
    def from_dict(cls, dikt) -> 'PipelinePattern':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PipelinePattern of this PipelinePattern.  # noqa: E501
        :rtype: PipelinePattern
        """
        return util.deserialize_model(dikt, cls)

    @property
    def created(self):
        """Gets the created of this PipelinePattern.


        :return: The created of this PipelinePattern.
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this PipelinePattern.


        :param created: The created of this PipelinePattern.
        :type created: int
        """
        if created is not None and created < 0:  # noqa: E501
            raise ValueError("Invalid value for `created`, must be a value greater than or equal to `0`")  # noqa: E501

        self._created = created

    @property
    def created_by(self):
        """Gets the created_by of this PipelinePattern.


        :return: The created_by of this PipelinePattern.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this PipelinePattern.


        :param created_by: The created_by of this PipelinePattern.
        :type created_by: str
        """

        self._created_by = created_by

    @property
    def default_model_id(self):
        """Gets the default_model_id of this PipelinePattern.


        :return: The default_model_id of this PipelinePattern.
        :rtype: str
        """
        return self._default_model_id

    @default_model_id.setter
    def default_model_id(self, default_model_id):
        """Sets the default_model_id of this PipelinePattern.


        :param default_model_id: The default_model_id of this PipelinePattern.
        :type default_model_id: str
        """

        self._default_model_id = default_model_id

    @property
    def engine_type(self):
        """Gets the engine_type of this PipelinePattern.


        :return: The engine_type of this PipelinePattern.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        """Sets the engine_type of this PipelinePattern.


        :param engine_type: The engine_type of this PipelinePattern.
        :type engine_type: str
        """

        self._engine_type = engine_type

    @property
    def id(self):
        """Gets the id of this PipelinePattern.


        :return: The id of this PipelinePattern.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PipelinePattern.


        :param id: The id of this PipelinePattern.
        :type id: str
        """

        self._id = id

    @property
    def is_profile(self):
        """Gets the is_profile of this PipelinePattern.


        :return: The is_profile of this PipelinePattern.
        :rtype: bool
        """
        return self._is_profile

    @is_profile.setter
    def is_profile(self, is_profile):
        """Sets the is_profile of this PipelinePattern.


        :param is_profile: The is_profile of this PipelinePattern.
        :type is_profile: bool
        """

        self._is_profile = is_profile

    @property
    def is_user_defined(self):
        """Gets the is_user_defined of this PipelinePattern.


        :return: The is_user_defined of this PipelinePattern.
        :rtype: bool
        """
        return self._is_user_defined

    @is_user_defined.setter
    def is_user_defined(self, is_user_defined):
        """Sets the is_user_defined of this PipelinePattern.


        :param is_user_defined: The is_user_defined of this PipelinePattern.
        :type is_user_defined: bool
        """

        self._is_user_defined = is_user_defined

    @property
    def is_visible(self):
        """Gets the is_visible of this PipelinePattern.


        :return: The is_visible of this PipelinePattern.
        :rtype: bool
        """
        return self._is_visible

    @is_visible.setter
    def is_visible(self, is_visible):
        """Sets the is_visible of this PipelinePattern.


        :param is_visible: The is_visible of this PipelinePattern.
        :type is_visible: bool
        """

        self._is_visible = is_visible

    @property
    def name(self):
        """Gets the name of this PipelinePattern.


        :return: The name of this PipelinePattern.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PipelinePattern.


        :param name: The name of this PipelinePattern.
        :type name: str
        """

        self._name = name

    @property
    def pipeline(self):
        """Gets the pipeline of this PipelinePattern.


        :return: The pipeline of this PipelinePattern.
        :rtype: str
        """
        return self._pipeline

    @pipeline.setter
    def pipeline(self, pipeline):
        """Sets the pipeline of this PipelinePattern.


        :param pipeline: The pipeline of this PipelinePattern.
        :type pipeline: str
        """

        self._pipeline = pipeline
