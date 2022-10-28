# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.2446
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from finbourne_access.configuration import Configuration


class IfIdentityScopeExpression(object):
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
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'scope_name': 'str'
    }

    attribute_map = {
        'scope_name': 'scopeName'
    }

    required_map = {
        'scope_name': 'required'
    }

    def __init__(self, scope_name=None, local_vars_configuration=None):  # noqa: E501
        """IfIdentityScopeExpression - a model defined in OpenAPI"
        
        :param scope_name:  (required)
        :type scope_name: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._scope_name = None
        self.discriminator = None

        self.scope_name = scope_name

    @property
    def scope_name(self):
        """Gets the scope_name of this IfIdentityScopeExpression.  # noqa: E501


        :return: The scope_name of this IfIdentityScopeExpression.  # noqa: E501
        :rtype: str
        """
        return self._scope_name

    @scope_name.setter
    def scope_name(self, scope_name):
        """Sets the scope_name of this IfIdentityScopeExpression.


        :param scope_name: The scope_name of this IfIdentityScopeExpression.  # noqa: E501
        :type scope_name: str
        """
        if self.local_vars_configuration.client_side_validation and scope_name is None:  # noqa: E501
            raise ValueError("Invalid value for `scope_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                scope_name is not None and len(scope_name) < 1):
            raise ValueError("Invalid value for `scope_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._scope_name = scope_name

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IfIdentityScopeExpression):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IfIdentityScopeExpression):
            return True

        return self.to_dict() != other.to_dict()
