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


class ResourceGroups(Base):
    """
    The ResourceGroups class encapsulates a list of resourceGroups resources that are managed by the system.
    A list of resources can be retrieved from the server using the ResourceGroups.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "resourceGroups"
    _SDM_ATT_MAP = {
        "AvailableResourceModes": "availableResourceModes",
        "Card": "card",
        "FrontPanelPorts": "frontPanelPorts",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(ResourceGroups, self).__init__(parent, list_op)

    @property
    def AvailableResourceModes(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[normal | tenGig | fortyGig | singleMode | dualMode | hundredGigNonFanOut | fortyGigFanOut | threeByTenGigFanOut | eightByTenGigFanOut | fourByTwentyFiveGigNonFanOut | twoByTwentyFiveGigNonFanOut | oneByFiftyGigNonFanOut | fortyGigNonFanOut | oneByTenGigFanOut | fourByTenGigFanOut | incompatibleMode | hundredGigCapturePlayback | fortyGigCapturePlayback | novusHundredGigNonFanOut | novusFourByTwentyFiveGigNonFanOut | novusTwoByFiftyGigNonFanOut | novusOneByFortyGigNonFanOut | novusFourByTenGigNonFanOut | krakenOneByFourHundredGigNonFanOut | krakenOneByTwoHundredGigNonFanOut | krakenTwoByOneHundredGigFanOut | krakenFourByFiftyGigFanOut | aresOneOneByFourHundredGigNonFanOut | aresOneTwoByTwoHundredGigFanOut | aresOneFourByOneHundredGigFanOut | aresOneFourByOneHundredGigMacSecFanOut | aresOneEightByFiftyGigFanOut | uhdOneHundredEightByHundredGigNonFanOut | uhdOneHundredEightByFortyGigNonFanOut | uhdOneHundredSixteenByFiftyGigFanOut | uhdOneHundredThirtyTwoByTwentyFiveGigFanOut | uhdOneHundredThirtyTwoByTenGigFanOut | novus5GOneByTenGigNonFanOut | novus5GOneByTwentyFiveGigNonFanOut | novus5GOneByFiftyGigNonFanOut | novus5GOneByHundredGigNonFanOut | starTwoByFourHundredGigNonFannedOutPAM4 | starFourByTwoHundredGigFannedOutPAM4 | starEightByHundredGigFannedOutPAM4 | starFourByHundredGigFannedOutNRZ | starSixteenByFiftyGigFannedOutPAM4 | starEightByFiftyGigFannedOutNRZ | starFourByFortyGigFannedOutNRZ | starSixteenByTwentyFiveGigFannedOutNRZ | starSixteenByTenGigFannedOutNRZ | novusHundredGigNonFanOutHighStream | novusFourByTwentyFiveGigNonFanOutHighStream | novusTwoByFiftyGigNonFanOutHighStream | novusOneByFortyGigNonFanOutHighStream | novusFourByTenGigNonFanOutHighStream]):
        """
        return self._get_attribute(self._SDM_ATT_MAP["AvailableResourceModes"])

    @property
    def Card(self):
        # type: () -> str
        """
        Returns
        -------
        - str:
        """
        return self._get_attribute(self._SDM_ATT_MAP["Card"])

    @property
    def FrontPanelPorts(self):
        # type: () -> List[int]
        """
        Returns
        -------
        - list(number):
        """
        return self._get_attribute(self._SDM_ATT_MAP["FrontPanelPorts"])

    def add(self):
        """Adds a new resourceGroups resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved resourceGroups resources using find and the newly added resourceGroups resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, AvailableResourceModes=None, Card=None, FrontPanelPorts=None):
        # type: (List[str], str, List[int]) -> ResourceGroups
        """Finds and retrieves resourceGroups resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve resourceGroups resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all resourceGroups resources from the server.

        Args
        ----
        - AvailableResourceModes (list(str[normal | tenGig | fortyGig | singleMode | dualMode | hundredGigNonFanOut | fortyGigFanOut | threeByTenGigFanOut | eightByTenGigFanOut | fourByTwentyFiveGigNonFanOut | twoByTwentyFiveGigNonFanOut | oneByFiftyGigNonFanOut | fortyGigNonFanOut | oneByTenGigFanOut | fourByTenGigFanOut | incompatibleMode | hundredGigCapturePlayback | fortyGigCapturePlayback | novusHundredGigNonFanOut | novusFourByTwentyFiveGigNonFanOut | novusTwoByFiftyGigNonFanOut | novusOneByFortyGigNonFanOut | novusFourByTenGigNonFanOut | krakenOneByFourHundredGigNonFanOut | krakenOneByTwoHundredGigNonFanOut | krakenTwoByOneHundredGigFanOut | krakenFourByFiftyGigFanOut | aresOneOneByFourHundredGigNonFanOut | aresOneTwoByTwoHundredGigFanOut | aresOneFourByOneHundredGigFanOut | aresOneFourByOneHundredGigMacSecFanOut | aresOneEightByFiftyGigFanOut | uhdOneHundredEightByHundredGigNonFanOut | uhdOneHundredEightByFortyGigNonFanOut | uhdOneHundredSixteenByFiftyGigFanOut | uhdOneHundredThirtyTwoByTwentyFiveGigFanOut | uhdOneHundredThirtyTwoByTenGigFanOut | novus5GOneByTenGigNonFanOut | novus5GOneByTwentyFiveGigNonFanOut | novus5GOneByFiftyGigNonFanOut | novus5GOneByHundredGigNonFanOut | starTwoByFourHundredGigNonFannedOutPAM4 | starFourByTwoHundredGigFannedOutPAM4 | starEightByHundredGigFannedOutPAM4 | starFourByHundredGigFannedOutNRZ | starSixteenByFiftyGigFannedOutPAM4 | starEightByFiftyGigFannedOutNRZ | starFourByFortyGigFannedOutNRZ | starSixteenByTwentyFiveGigFannedOutNRZ | starSixteenByTenGigFannedOutNRZ | novusHundredGigNonFanOutHighStream | novusFourByTwentyFiveGigNonFanOutHighStream | novusTwoByFiftyGigNonFanOutHighStream | novusOneByFortyGigNonFanOutHighStream | novusFourByTenGigNonFanOutHighStream])):
        - Card (str):
        - FrontPanelPorts (list(number)):

        Returns
        -------
        - self: This instance with matching resourceGroups resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of resourceGroups data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the resourceGroups resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
