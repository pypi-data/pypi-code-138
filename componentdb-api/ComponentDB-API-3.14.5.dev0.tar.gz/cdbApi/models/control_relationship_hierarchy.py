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


class ControlRelationshipHierarchy(object):
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
        'child_item': 'ControlRelationshipHierarchy',
        'machine_item': 'ItemDomainMachineDesign',
        'interface_to_parent': 'str'
    }

    attribute_map = {
        'child_item': 'childItem',
        'machine_item': 'machineItem',
        'interface_to_parent': 'interfaceToParent'
    }

    def __init__(self, child_item=None, machine_item=None, interface_to_parent=None, local_vars_configuration=None):  # noqa: E501
        """ControlRelationshipHierarchy - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._child_item = None
        self._machine_item = None
        self._interface_to_parent = None
        self.discriminator = None

        if child_item is not None:
            self.child_item = child_item
        if machine_item is not None:
            self.machine_item = machine_item
        if interface_to_parent is not None:
            self.interface_to_parent = interface_to_parent

    @property
    def child_item(self):
        """Gets the child_item of this ControlRelationshipHierarchy.  # noqa: E501


        :return: The child_item of this ControlRelationshipHierarchy.  # noqa: E501
        :rtype: ControlRelationshipHierarchy
        """
        return self._child_item

    @child_item.setter
    def child_item(self, child_item):
        """Sets the child_item of this ControlRelationshipHierarchy.


        :param child_item: The child_item of this ControlRelationshipHierarchy.  # noqa: E501
        :type: ControlRelationshipHierarchy
        """

        self._child_item = child_item

    @property
    def machine_item(self):
        """Gets the machine_item of this ControlRelationshipHierarchy.  # noqa: E501


        :return: The machine_item of this ControlRelationshipHierarchy.  # noqa: E501
        :rtype: ItemDomainMachineDesign
        """
        return self._machine_item

    @machine_item.setter
    def machine_item(self, machine_item):
        """Sets the machine_item of this ControlRelationshipHierarchy.


        :param machine_item: The machine_item of this ControlRelationshipHierarchy.  # noqa: E501
        :type: ItemDomainMachineDesign
        """

        self._machine_item = machine_item

    @property
    def interface_to_parent(self):
        """Gets the interface_to_parent of this ControlRelationshipHierarchy.  # noqa: E501


        :return: The interface_to_parent of this ControlRelationshipHierarchy.  # noqa: E501
        :rtype: str
        """
        return self._interface_to_parent

    @interface_to_parent.setter
    def interface_to_parent(self, interface_to_parent):
        """Sets the interface_to_parent of this ControlRelationshipHierarchy.


        :param interface_to_parent: The interface_to_parent of this ControlRelationshipHierarchy.  # noqa: E501
        :type: str
        """

        self._interface_to_parent = interface_to_parent

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
        if not isinstance(other, ControlRelationshipHierarchy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ControlRelationshipHierarchy):
            return True

        return self.to_dict() != other.to_dict()
