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


class ItemConnector(object):
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
        'id': 'int',
        'label': 'str',
        'quantity': 'int',
        'property_value_list': 'list[PropertyValue]',
        'item': 'Item',
        'connector': 'Connector',
        'item_element_relationship_history_list': 'list[ItemElementRelationshipHistory]',
        'item_element_relationship_history_list1': 'list[ItemElementRelationshipHistory]',
        'item_resource_list': 'list[ItemResource]',
        'item_element_relationship_list': 'list[ItemElementRelationship]',
        'item_element_relationship_list1': 'list[ItemElementRelationship]',
        'item_connector_of_item_connected_to': 'ItemConnector',
        'item_connected_via': 'Item',
        'connectors_to_update': 'list[Connector]',
        'connectors_to_remove': 'list[Connector]',
        'connected': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'label': 'label',
        'quantity': 'quantity',
        'property_value_list': 'propertyValueList',
        'item': 'item',
        'connector': 'connector',
        'item_element_relationship_history_list': 'itemElementRelationshipHistoryList',
        'item_element_relationship_history_list1': 'itemElementRelationshipHistoryList1',
        'item_resource_list': 'itemResourceList',
        'item_element_relationship_list': 'itemElementRelationshipList',
        'item_element_relationship_list1': 'itemElementRelationshipList1',
        'item_connector_of_item_connected_to': 'itemConnectorOfItemConnectedTo',
        'item_connected_via': 'itemConnectedVia',
        'connectors_to_update': 'connectorsToUpdate',
        'connectors_to_remove': 'connectorsToRemove',
        'connected': 'connected'
    }

    def __init__(self, id=None, label=None, quantity=None, property_value_list=None, item=None, connector=None, item_element_relationship_history_list=None, item_element_relationship_history_list1=None, item_resource_list=None, item_element_relationship_list=None, item_element_relationship_list1=None, item_connector_of_item_connected_to=None, item_connected_via=None, connectors_to_update=None, connectors_to_remove=None, connected=None, local_vars_configuration=None):  # noqa: E501
        """ItemConnector - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._label = None
        self._quantity = None
        self._property_value_list = None
        self._item = None
        self._connector = None
        self._item_element_relationship_history_list = None
        self._item_element_relationship_history_list1 = None
        self._item_resource_list = None
        self._item_element_relationship_list = None
        self._item_element_relationship_list1 = None
        self._item_connector_of_item_connected_to = None
        self._item_connected_via = None
        self._connectors_to_update = None
        self._connectors_to_remove = None
        self._connected = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if label is not None:
            self.label = label
        if quantity is not None:
            self.quantity = quantity
        if property_value_list is not None:
            self.property_value_list = property_value_list
        if item is not None:
            self.item = item
        if connector is not None:
            self.connector = connector
        if item_element_relationship_history_list is not None:
            self.item_element_relationship_history_list = item_element_relationship_history_list
        if item_element_relationship_history_list1 is not None:
            self.item_element_relationship_history_list1 = item_element_relationship_history_list1
        if item_resource_list is not None:
            self.item_resource_list = item_resource_list
        if item_element_relationship_list is not None:
            self.item_element_relationship_list = item_element_relationship_list
        if item_element_relationship_list1 is not None:
            self.item_element_relationship_list1 = item_element_relationship_list1
        if item_connector_of_item_connected_to is not None:
            self.item_connector_of_item_connected_to = item_connector_of_item_connected_to
        if item_connected_via is not None:
            self.item_connected_via = item_connected_via
        if connectors_to_update is not None:
            self.connectors_to_update = connectors_to_update
        if connectors_to_remove is not None:
            self.connectors_to_remove = connectors_to_remove
        if connected is not None:
            self.connected = connected

    @property
    def id(self):
        """Gets the id of this ItemConnector.  # noqa: E501


        :return: The id of this ItemConnector.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ItemConnector.


        :param id: The id of this ItemConnector.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this ItemConnector.  # noqa: E501


        :return: The label of this ItemConnector.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ItemConnector.


        :param label: The label of this ItemConnector.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                label is not None and len(label) > 64):
            raise ValueError("Invalid value for `label`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                label is not None and len(label) < 0):
            raise ValueError("Invalid value for `label`, length must be greater than or equal to `0`")  # noqa: E501

        self._label = label

    @property
    def quantity(self):
        """Gets the quantity of this ItemConnector.  # noqa: E501


        :return: The quantity of this ItemConnector.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this ItemConnector.


        :param quantity: The quantity of this ItemConnector.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

    @property
    def property_value_list(self):
        """Gets the property_value_list of this ItemConnector.  # noqa: E501


        :return: The property_value_list of this ItemConnector.  # noqa: E501
        :rtype: list[PropertyValue]
        """
        return self._property_value_list

    @property_value_list.setter
    def property_value_list(self, property_value_list):
        """Sets the property_value_list of this ItemConnector.


        :param property_value_list: The property_value_list of this ItemConnector.  # noqa: E501
        :type: list[PropertyValue]
        """

        self._property_value_list = property_value_list

    @property
    def item(self):
        """Gets the item of this ItemConnector.  # noqa: E501


        :return: The item of this ItemConnector.  # noqa: E501
        :rtype: Item
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this ItemConnector.


        :param item: The item of this ItemConnector.  # noqa: E501
        :type: Item
        """

        self._item = item

    @property
    def connector(self):
        """Gets the connector of this ItemConnector.  # noqa: E501


        :return: The connector of this ItemConnector.  # noqa: E501
        :rtype: Connector
        """
        return self._connector

    @connector.setter
    def connector(self, connector):
        """Sets the connector of this ItemConnector.


        :param connector: The connector of this ItemConnector.  # noqa: E501
        :type: Connector
        """

        self._connector = connector

    @property
    def item_element_relationship_history_list(self):
        """Gets the item_element_relationship_history_list of this ItemConnector.  # noqa: E501


        :return: The item_element_relationship_history_list of this ItemConnector.  # noqa: E501
        :rtype: list[ItemElementRelationshipHistory]
        """
        return self._item_element_relationship_history_list

    @item_element_relationship_history_list.setter
    def item_element_relationship_history_list(self, item_element_relationship_history_list):
        """Sets the item_element_relationship_history_list of this ItemConnector.


        :param item_element_relationship_history_list: The item_element_relationship_history_list of this ItemConnector.  # noqa: E501
        :type: list[ItemElementRelationshipHistory]
        """

        self._item_element_relationship_history_list = item_element_relationship_history_list

    @property
    def item_element_relationship_history_list1(self):
        """Gets the item_element_relationship_history_list1 of this ItemConnector.  # noqa: E501


        :return: The item_element_relationship_history_list1 of this ItemConnector.  # noqa: E501
        :rtype: list[ItemElementRelationshipHistory]
        """
        return self._item_element_relationship_history_list1

    @item_element_relationship_history_list1.setter
    def item_element_relationship_history_list1(self, item_element_relationship_history_list1):
        """Sets the item_element_relationship_history_list1 of this ItemConnector.


        :param item_element_relationship_history_list1: The item_element_relationship_history_list1 of this ItemConnector.  # noqa: E501
        :type: list[ItemElementRelationshipHistory]
        """

        self._item_element_relationship_history_list1 = item_element_relationship_history_list1

    @property
    def item_resource_list(self):
        """Gets the item_resource_list of this ItemConnector.  # noqa: E501


        :return: The item_resource_list of this ItemConnector.  # noqa: E501
        :rtype: list[ItemResource]
        """
        return self._item_resource_list

    @item_resource_list.setter
    def item_resource_list(self, item_resource_list):
        """Sets the item_resource_list of this ItemConnector.


        :param item_resource_list: The item_resource_list of this ItemConnector.  # noqa: E501
        :type: list[ItemResource]
        """

        self._item_resource_list = item_resource_list

    @property
    def item_element_relationship_list(self):
        """Gets the item_element_relationship_list of this ItemConnector.  # noqa: E501


        :return: The item_element_relationship_list of this ItemConnector.  # noqa: E501
        :rtype: list[ItemElementRelationship]
        """
        return self._item_element_relationship_list

    @item_element_relationship_list.setter
    def item_element_relationship_list(self, item_element_relationship_list):
        """Sets the item_element_relationship_list of this ItemConnector.


        :param item_element_relationship_list: The item_element_relationship_list of this ItemConnector.  # noqa: E501
        :type: list[ItemElementRelationship]
        """

        self._item_element_relationship_list = item_element_relationship_list

    @property
    def item_element_relationship_list1(self):
        """Gets the item_element_relationship_list1 of this ItemConnector.  # noqa: E501


        :return: The item_element_relationship_list1 of this ItemConnector.  # noqa: E501
        :rtype: list[ItemElementRelationship]
        """
        return self._item_element_relationship_list1

    @item_element_relationship_list1.setter
    def item_element_relationship_list1(self, item_element_relationship_list1):
        """Sets the item_element_relationship_list1 of this ItemConnector.


        :param item_element_relationship_list1: The item_element_relationship_list1 of this ItemConnector.  # noqa: E501
        :type: list[ItemElementRelationship]
        """

        self._item_element_relationship_list1 = item_element_relationship_list1

    @property
    def item_connector_of_item_connected_to(self):
        """Gets the item_connector_of_item_connected_to of this ItemConnector.  # noqa: E501


        :return: The item_connector_of_item_connected_to of this ItemConnector.  # noqa: E501
        :rtype: ItemConnector
        """
        return self._item_connector_of_item_connected_to

    @item_connector_of_item_connected_to.setter
    def item_connector_of_item_connected_to(self, item_connector_of_item_connected_to):
        """Sets the item_connector_of_item_connected_to of this ItemConnector.


        :param item_connector_of_item_connected_to: The item_connector_of_item_connected_to of this ItemConnector.  # noqa: E501
        :type: ItemConnector
        """

        self._item_connector_of_item_connected_to = item_connector_of_item_connected_to

    @property
    def item_connected_via(self):
        """Gets the item_connected_via of this ItemConnector.  # noqa: E501


        :return: The item_connected_via of this ItemConnector.  # noqa: E501
        :rtype: Item
        """
        return self._item_connected_via

    @item_connected_via.setter
    def item_connected_via(self, item_connected_via):
        """Sets the item_connected_via of this ItemConnector.


        :param item_connected_via: The item_connected_via of this ItemConnector.  # noqa: E501
        :type: Item
        """

        self._item_connected_via = item_connected_via

    @property
    def connectors_to_update(self):
        """Gets the connectors_to_update of this ItemConnector.  # noqa: E501


        :return: The connectors_to_update of this ItemConnector.  # noqa: E501
        :rtype: list[Connector]
        """
        return self._connectors_to_update

    @connectors_to_update.setter
    def connectors_to_update(self, connectors_to_update):
        """Sets the connectors_to_update of this ItemConnector.


        :param connectors_to_update: The connectors_to_update of this ItemConnector.  # noqa: E501
        :type: list[Connector]
        """

        self._connectors_to_update = connectors_to_update

    @property
    def connectors_to_remove(self):
        """Gets the connectors_to_remove of this ItemConnector.  # noqa: E501


        :return: The connectors_to_remove of this ItemConnector.  # noqa: E501
        :rtype: list[Connector]
        """
        return self._connectors_to_remove

    @connectors_to_remove.setter
    def connectors_to_remove(self, connectors_to_remove):
        """Sets the connectors_to_remove of this ItemConnector.


        :param connectors_to_remove: The connectors_to_remove of this ItemConnector.  # noqa: E501
        :type: list[Connector]
        """

        self._connectors_to_remove = connectors_to_remove

    @property
    def connected(self):
        """Gets the connected of this ItemConnector.  # noqa: E501


        :return: The connected of this ItemConnector.  # noqa: E501
        :rtype: bool
        """
        return self._connected

    @connected.setter
    def connected(self, connected):
        """Sets the connected of this ItemConnector.


        :param connected: The connected of this ItemConnector.  # noqa: E501
        :type: bool
        """

        self._connected = connected

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
        if not isinstance(other, ItemConnector):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ItemConnector):
            return True

        return self.to_dict() != other.to_dict()
