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


class ItemPermissions(object):
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
        'item_id': 'int',
        'owner_user': 'UserInfo',
        'owner_group': 'UserGroup',
        'group_writeable': 'bool'
    }

    attribute_map = {
        'item_id': 'itemId',
        'owner_user': 'ownerUser',
        'owner_group': 'ownerGroup',
        'group_writeable': 'groupWriteable'
    }

    def __init__(self, item_id=None, owner_user=None, owner_group=None, group_writeable=None, local_vars_configuration=None):  # noqa: E501
        """ItemPermissions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._item_id = None
        self._owner_user = None
        self._owner_group = None
        self._group_writeable = None
        self.discriminator = None

        if item_id is not None:
            self.item_id = item_id
        if owner_user is not None:
            self.owner_user = owner_user
        if owner_group is not None:
            self.owner_group = owner_group
        if group_writeable is not None:
            self.group_writeable = group_writeable

    @property
    def item_id(self):
        """Gets the item_id of this ItemPermissions.  # noqa: E501


        :return: The item_id of this ItemPermissions.  # noqa: E501
        :rtype: int
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this ItemPermissions.


        :param item_id: The item_id of this ItemPermissions.  # noqa: E501
        :type: int
        """

        self._item_id = item_id

    @property
    def owner_user(self):
        """Gets the owner_user of this ItemPermissions.  # noqa: E501


        :return: The owner_user of this ItemPermissions.  # noqa: E501
        :rtype: UserInfo
        """
        return self._owner_user

    @owner_user.setter
    def owner_user(self, owner_user):
        """Sets the owner_user of this ItemPermissions.


        :param owner_user: The owner_user of this ItemPermissions.  # noqa: E501
        :type: UserInfo
        """

        self._owner_user = owner_user

    @property
    def owner_group(self):
        """Gets the owner_group of this ItemPermissions.  # noqa: E501


        :return: The owner_group of this ItemPermissions.  # noqa: E501
        :rtype: UserGroup
        """
        return self._owner_group

    @owner_group.setter
    def owner_group(self, owner_group):
        """Sets the owner_group of this ItemPermissions.


        :param owner_group: The owner_group of this ItemPermissions.  # noqa: E501
        :type: UserGroup
        """

        self._owner_group = owner_group

    @property
    def group_writeable(self):
        """Gets the group_writeable of this ItemPermissions.  # noqa: E501


        :return: The group_writeable of this ItemPermissions.  # noqa: E501
        :rtype: bool
        """
        return self._group_writeable

    @group_writeable.setter
    def group_writeable(self, group_writeable):
        """Sets the group_writeable of this ItemPermissions.


        :param group_writeable: The group_writeable of this ItemPermissions.  # noqa: E501
        :type: bool
        """

        self._group_writeable = group_writeable

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
        if not isinstance(other, ItemPermissions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ItemPermissions):
            return True

        return self.to_dict() != other.to_dict()
