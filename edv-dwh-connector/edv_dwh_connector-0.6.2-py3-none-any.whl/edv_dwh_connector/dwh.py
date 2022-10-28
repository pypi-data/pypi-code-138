"""
This module helps to represent a data warehouse.
.. since: 0.1
"""

# -*- coding: utf-8 -*-
# Copyright (c) 2022 Endeavour Mining
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to read
# the Software only. Permissions is hereby NOT GRANTED to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from abc import ABC, abstractmethod
from datetime import date, time
from sqlalchemy.engine.base import Connection  # type: ignore


# pylint: disable=too-few-public-methods
class Dwh(ABC):
    """
    Abstract Data warehouse.
    .. since: 0.1
    """

    @abstractmethod
    def connection(self) -> Connection:
        """
        Gets connection to DWH.
        :return: Connection
        """


class DatePK:
    """
    Date primary key.
    .. since: 0.5
    """

    def __init__(self, dte: date) -> None:
        """
        Ctor.
        :param dte: Date
        """
        self.__date = dte

    def value(self) -> int:
        """
        Gets key value.
        :return: Key value
        """
        return int(self.__date.strftime("%Y%m%d"))


class TimePK:
    """
    Time primary key.
    .. since: 0.5
    """

    def __init__(self, tme: time) -> None:
        """
        Ctor.
        :param tme: Time
        """
        self.__time = tme

    def value(self) -> int:
        """
        Gets key value.
        :return: UID
        """
        return int(self.__time.strftime("%H%M%S"))
