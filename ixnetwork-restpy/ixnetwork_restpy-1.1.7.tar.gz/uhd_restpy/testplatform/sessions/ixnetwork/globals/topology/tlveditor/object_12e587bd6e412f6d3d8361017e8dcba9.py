# MIT LICENSE
#
# Copyright 1997 - 2020 by IXIA Keysight
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE. 
import sys
from uhd_restpy.base import Base
from uhd_restpy.files import Files
if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class Object(Base):
    """Tlv object container which can contain one of a field, sub tlv or container
    The Object class encapsulates a list of object resources that are managed by the user.
    A list of resources can be retrieved from the server using the Object.find() method.
    The list can be managed by using the Object.add() and Object.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'object'
    _SDM_ATT_MAP = {
        'Name': 'name',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(Object, self).__init__(parent, list_op)

    @property
    def Container(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.tlveditor.container_1a12044c5aa69dabfe18a51e622cd1b5.Container): An instance of the Container class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.tlveditor.container_1a12044c5aa69dabfe18a51e622cd1b5 import Container
        if len(self._object_properties) > 0:
            if self._properties.get('Container', None) is not None:
                return self._properties.get('Container')
        return Container(self)

    @property
    def Field(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.tlveditor.field_01f1f7f093248c40b24c4bf69cffe573.Field): An instance of the Field class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.tlveditor.field_01f1f7f093248c40b24c4bf69cffe573 import Field
        if len(self._object_properties) > 0:
            if self._properties.get('Field', None) is not None:
                return self._properties.get('Field')
        return Field(self)

    @property
    def SubTlv(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.tlveditor.subtlv_60e12b7ebaca7628a30e30506e5025bc.SubTlv): An instance of the SubTlv class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.tlveditor.subtlv_60e12b7ebaca7628a30e30506e5025bc import SubTlv
        if len(self._object_properties) > 0:
            if self._properties.get('SubTlv', None) is not None:
                return self._properties.get('SubTlv')
        return SubTlv(self)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The name of the object
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    def update(self, Name=None):
        # type: (str) -> Object
        """Updates object resource on the server.

        Args
        ----
        - Name (str): The name of the object

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Name=None):
        # type: (str) -> Object
        """Adds a new object resource on the server and adds it to the container.

        Args
        ----
        - Name (str): The name of the object

        Returns
        -------
        - self: This instance with all currently retrieved object resources using find and the newly added object resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained object resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Name=None):
        # type: (str) -> Object
        """Finds and retrieves object resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve object resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all object resources from the server.

        Args
        ----
        - Name (str): The name of the object

        Returns
        -------
        - self: This instance with matching object resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of object data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the object resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
