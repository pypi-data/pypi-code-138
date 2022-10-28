# coding: utf-8

"""
    Component Database API

    The API that provides access to Component Database data.  # noqa: E501

    The version of the OpenAPI document: 3.14.4
    Contact: djarosz@anl.gov
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from cdbApi.configuration import Configuration


class UpdateMachineAssignedItemInformation(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'md_item_id': 'int',
        'assigned_item_id': 'int',
        'is_installed': 'bool'
    }

    attribute_map = {
        'md_item_id': 'mdItemId',
        'assigned_item_id': 'assignedItemId',
        'is_installed': 'isInstalled'
    }

    def __init__(self, md_item_id=None, assigned_item_id=None, is_installed=None, local_vars_configuration=None):  # noqa: E501
        """UpdateMachineAssignedItemInformation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._md_item_id = None
        self._assigned_item_id = None
        self._is_installed = None
        self.discriminator = None

        if md_item_id is not None:
            self.md_item_id = md_item_id
        if assigned_item_id is not None:
            self.assigned_item_id = assigned_item_id
        if is_installed is not None:
            self.is_installed = is_installed

    @property
    def md_item_id(self):
        """Gets the md_item_id of this UpdateMachineAssignedItemInformation.  # noqa: E501


        :return: The md_item_id of this UpdateMachineAssignedItemInformation.  # noqa: E501
        :rtype: int
        """
        return self._md_item_id

    @md_item_id.setter
    def md_item_id(self, md_item_id):
        """Sets the md_item_id of this UpdateMachineAssignedItemInformation.


        :param md_item_id: The md_item_id of this UpdateMachineAssignedItemInformation.  # noqa: E501
        :type: int
        """

        self._md_item_id = md_item_id

    @property
    def assigned_item_id(self):
        """Gets the assigned_item_id of this UpdateMachineAssignedItemInformation.  # noqa: E501


        :return: The assigned_item_id of this UpdateMachineAssignedItemInformation.  # noqa: E501
        :rtype: int
        """
        return self._assigned_item_id

    @assigned_item_id.setter
    def assigned_item_id(self, assigned_item_id):
        """Sets the assigned_item_id of this UpdateMachineAssignedItemInformation.


        :param assigned_item_id: The assigned_item_id of this UpdateMachineAssignedItemInformation.  # noqa: E501
        :type: int
        """

        self._assigned_item_id = assigned_item_id

    @property
    def is_installed(self):
        """Gets the is_installed of this UpdateMachineAssignedItemInformation.  # noqa: E501


        :return: The is_installed of this UpdateMachineAssignedItemInformation.  # noqa: E501
        :rtype: bool
        """
        return self._is_installed

    @is_installed.setter
    def is_installed(self, is_installed):
        """Sets the is_installed of this UpdateMachineAssignedItemInformation.


        :param is_installed: The is_installed of this UpdateMachineAssignedItemInformation.  # noqa: E501
        :type: bool
        """

        self._is_installed = is_installed

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateMachineAssignedItemInformation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateMachineAssignedItemInformation):
            return True

        return self.to_dict() != other.to_dict()
