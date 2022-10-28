"""
    Alvin

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from alvin_api_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from alvin_api_client.exceptions import ApiAttributeError


def lazy_import():
    from alvin_api_client.model.data_entity_job_step import DataEntityJobStep
    from alvin_api_client.model.job_entity_usage_stats_report import JobEntityUsageStatsReport
    globals()['DataEntityJobStep'] = DataEntityJobStep
    globals()['JobEntityUsageStatsReport'] = JobEntityUsageStatsReport


class IAJobData(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('source_entities',): {
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'org_id': (str,),  # noqa: E501
            'comparison_key': (str,),  # noqa: E501
            'depth': (int,),  # noqa: E501
            'display_name': (str,),  # noqa: E501
            'job_data': (DataEntityJobStep,),  # noqa: E501
            'impact_status': ({str: (int,)},),  # noqa: E501
            'impacted_users': ([bool, date, datetime, dict, float, int, list, str, none_type],),  # noqa: E501
            'usage_stats': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'user_usage_stats': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'last_used': (datetime,),  # noqa: E501
            'source_entities': ([str],),  # noqa: E501
            'row_type': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'job_stats': (JobEntityUsageStatsReport,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'org_id': 'orgId',  # noqa: E501
        'comparison_key': 'comparisonKey',  # noqa: E501
        'depth': 'depth',  # noqa: E501
        'display_name': 'displayName',  # noqa: E501
        'job_data': 'jobData',  # noqa: E501
        'impact_status': 'impactStatus',  # noqa: E501
        'impacted_users': 'impactedUsers',  # noqa: E501
        'usage_stats': 'usageStats',  # noqa: E501
        'user_usage_stats': 'userUsageStats',  # noqa: E501
        'last_used': 'lastUsed',  # noqa: E501
        'source_entities': 'sourceEntities',  # noqa: E501
        'row_type': 'rowType',  # noqa: E501
        'job_stats': 'jobStats',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, org_id, comparison_key, depth, display_name, job_data, *args, **kwargs):  # noqa: E501
        """IAJobData - a model defined in OpenAPI

        Args:
            org_id (str):
            comparison_key (str):
            depth (int):
            display_name (str):
            job_data (DataEntityJobStep):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            impact_status ({str: (int,)}): [optional] if omitted the server will use the default value of {}  # noqa: E501
            impacted_users ([bool, date, datetime, dict, float, int, list, str, none_type]): [optional] if omitted the server will use the default value of []  # noqa: E501
            usage_stats (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            user_usage_stats (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            last_used (datetime): [optional]  # noqa: E501
            source_entities ([str]): [optional] if omitted the server will use the default value of []  # noqa: E501
            row_type (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            job_stats (JobEntityUsageStatsReport): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.org_id = org_id
        self.comparison_key = comparison_key
        self.depth = depth
        self.display_name = display_name
        self.job_data = job_data
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, org_id, comparison_key, depth, display_name, job_data, *args, **kwargs):  # noqa: E501
        """IAJobData - a model defined in OpenAPI

        Args:
            org_id (str):
            comparison_key (str):
            depth (int):
            display_name (str):
            job_data (DataEntityJobStep):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            impact_status ({str: (int,)}): [optional] if omitted the server will use the default value of {}  # noqa: E501
            impacted_users ([bool, date, datetime, dict, float, int, list, str, none_type]): [optional] if omitted the server will use the default value of []  # noqa: E501
            usage_stats (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            user_usage_stats (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            last_used (datetime): [optional]  # noqa: E501
            source_entities ([str]): [optional] if omitted the server will use the default value of []  # noqa: E501
            row_type (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            job_stats (JobEntityUsageStatsReport): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.org_id = org_id
        self.comparison_key = comparison_key
        self.depth = depth
        self.display_name = display_name
        self.job_data = job_data
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
