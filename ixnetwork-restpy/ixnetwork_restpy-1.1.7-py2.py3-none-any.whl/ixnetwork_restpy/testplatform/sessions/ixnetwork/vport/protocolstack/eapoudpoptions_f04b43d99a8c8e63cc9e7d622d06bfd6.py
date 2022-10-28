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
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files

if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class EapoUdpOptions(Base):
    """
    The EapoUdpOptions class encapsulates a list of eapoUdpOptions resources that are managed by the user.
    A list of resources can be retrieved from the server using the EapoUdpOptions.find() method.
    The list can be managed by using the EapoUdpOptions.add() and EapoUdpOptions.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "eapoUdpOptions"
    _SDM_ATT_MAP = {
        "DutMac": "dutMac",
        "IcmpTriggerTargetAddress": "icmpTriggerTargetAddress",
        "MaxClientsPerSecond": "maxClientsPerSecond",
        "MaxOutstandingRequests": "maxOutstandingRequests",
        "ObjectId": "objectId",
        "OverrideGlobalSetupRate": "overrideGlobalSetupRate",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(EapoUdpOptions, self).__init__(parent, list_op)

    @property
    def DutMac(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The MAC address of a DUT port to which the PCPU is connected. This is needed when using ICMP, DHCP_ICMP internal triggers.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DutMac"])

    @DutMac.setter
    def DutMac(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DutMac"], value)

    @property
    def IcmpTriggerTargetAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The target address where ICMP messages are sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IcmpTriggerTargetAddress"])

    @IcmpTriggerTargetAddress.setter
    def IcmpTriggerTargetAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IcmpTriggerTargetAddress"], value)

    @property
    def MaxClientsPerSecond(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number interfaces to setup per second.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxClientsPerSecond"])

    @MaxClientsPerSecond.setter
    def MaxClientsPerSecond(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxClientsPerSecond"], value)

    @property
    def MaxOutstandingRequests(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The maximum number of sessions that can be negotiated at one moment.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxOutstandingRequests"])

    @MaxOutstandingRequests.setter
    def MaxOutstandingRequests(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxOutstandingRequests"], value)

    @property
    def ObjectId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP["ObjectId"])

    @property
    def OverrideGlobalSetupRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true then all the rate settings defined at Session level will be overriden by rate settings defined on this PortGroup.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OverrideGlobalSetupRate"])

    @OverrideGlobalSetupRate.setter
    def OverrideGlobalSetupRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OverrideGlobalSetupRate"], value)

    def update(
        self,
        DutMac=None,
        IcmpTriggerTargetAddress=None,
        MaxClientsPerSecond=None,
        MaxOutstandingRequests=None,
        OverrideGlobalSetupRate=None,
    ):
        # type: (str, str, int, int, bool) -> EapoUdpOptions
        """Updates eapoUdpOptions resource on the server.

        Args
        ----
        - DutMac (str): The MAC address of a DUT port to which the PCPU is connected. This is needed when using ICMP, DHCP_ICMP internal triggers.
        - IcmpTriggerTargetAddress (str): The target address where ICMP messages are sent.
        - MaxClientsPerSecond (number): The number interfaces to setup per second.
        - MaxOutstandingRequests (number): The maximum number of sessions that can be negotiated at one moment.
        - OverrideGlobalSetupRate (bool): If true then all the rate settings defined at Session level will be overriden by rate settings defined on this PortGroup.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        DutMac=None,
        IcmpTriggerTargetAddress=None,
        MaxClientsPerSecond=None,
        MaxOutstandingRequests=None,
        OverrideGlobalSetupRate=None,
    ):
        # type: (str, str, int, int, bool) -> EapoUdpOptions
        """Adds a new eapoUdpOptions resource on the server and adds it to the container.

        Args
        ----
        - DutMac (str): The MAC address of a DUT port to which the PCPU is connected. This is needed when using ICMP, DHCP_ICMP internal triggers.
        - IcmpTriggerTargetAddress (str): The target address where ICMP messages are sent.
        - MaxClientsPerSecond (number): The number interfaces to setup per second.
        - MaxOutstandingRequests (number): The maximum number of sessions that can be negotiated at one moment.
        - OverrideGlobalSetupRate (bool): If true then all the rate settings defined at Session level will be overriden by rate settings defined on this PortGroup.

        Returns
        -------
        - self: This instance with all currently retrieved eapoUdpOptions resources using find and the newly added eapoUdpOptions resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained eapoUdpOptions resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        DutMac=None,
        IcmpTriggerTargetAddress=None,
        MaxClientsPerSecond=None,
        MaxOutstandingRequests=None,
        ObjectId=None,
        OverrideGlobalSetupRate=None,
    ):
        # type: (str, str, int, int, str, bool) -> EapoUdpOptions
        """Finds and retrieves eapoUdpOptions resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve eapoUdpOptions resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all eapoUdpOptions resources from the server.

        Args
        ----
        - DutMac (str): The MAC address of a DUT port to which the PCPU is connected. This is needed when using ICMP, DHCP_ICMP internal triggers.
        - IcmpTriggerTargetAddress (str): The target address where ICMP messages are sent.
        - MaxClientsPerSecond (number): The number interfaces to setup per second.
        - MaxOutstandingRequests (number): The maximum number of sessions that can be negotiated at one moment.
        - ObjectId (str): Unique identifier for this object
        - OverrideGlobalSetupRate (bool): If true then all the rate settings defined at Session level will be overriden by rate settings defined on this PortGroup.

        Returns
        -------
        - self: This instance with matching eapoUdpOptions resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of eapoUdpOptions data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the eapoUdpOptions resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def CustomProtocolStack(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the customProtocolStack operation on the server.

        Create custom protocol stack under /vport/protocolStack

        customProtocolStack(Arg2=list, Arg3=enum, async_operation=bool)
        ---------------------------------------------------------------
        - Arg2 (list(str)): List of plugin types to be added in the new custom stack
        - Arg3 (str(kAppend | kMerge | kOverwrite)): Append, merge or overwrite existing protocol stack
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "customProtocolStack", payload=payload, response_object=None
        )

    def DisableProtocolStack(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the disableProtocolStack operation on the server.

        Disable a protocol under protocolStack using the class name

        disableProtocolStack(Arg2=string, async_operation=bool)string
        -------------------------------------------------------------
        - Arg2 (str): Protocol class name to disable
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "disableProtocolStack", payload=payload, response_object=None
        )

    def EnableProtocolStack(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the enableProtocolStack operation on the server.

        Enable a protocol under protocolStack using the class name

        enableProtocolStack(Arg2=string, async_operation=bool)string
        ------------------------------------------------------------
        - Arg2 (str): Protocol class name to enable
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "enableProtocolStack", payload=payload, response_object=None
        )
