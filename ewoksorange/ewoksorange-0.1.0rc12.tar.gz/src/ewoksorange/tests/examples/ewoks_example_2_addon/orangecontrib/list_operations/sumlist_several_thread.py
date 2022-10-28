from ewoksorange.bindings import OWEwoksWidgetOneThreadPerRun
from ewoksorange.tests.listoperations import SumList2
from ewoks_example_2_addon.widgets import WidgetMixin


class SumListSeveralThread(
    WidgetMixin, OWEwoksWidgetOneThreadPerRun, ewokstaskclass=SumList2
):
    """
    Simple demo class that create a new thread each time an execution of
    SumList2 is required
    """

    name = "SumList on several thread"
    description = "Sum all elements of a list using a new thread for each summation"
    icon = "icons/mywidget.svg"
    want_main_area = True
