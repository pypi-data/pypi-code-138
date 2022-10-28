from typing import Dict, Mapping, Tuple
from ewoksxrpd.tasks import PyFaiConfig
from ewoksxrpd.gui.trigger_widget import OWTriggerWidget
from ewoksxrpd.gui.forms import input_parameters_pyfai_config
from ewoksxrpd.gui.forms import output_parameters_pyfai_config
from ewoksxrpd.gui.forms import pack_geometry
from ewoksxrpd.gui.forms import unpack_geometry
from ewoksxrpd.gui.forms import unpack_enabled_geometry

__all__ = ["OWPyFaiConfig"]


class OWPyFaiConfig(OWTriggerWidget, ewokstaskclass=PyFaiConfig):
    name = "PyFaiConfig"
    description = "Configuration for pyfai"
    icon = "icons/widget.png"
    want_main_area = True

    def _init_forms(self):
        parameter_info = input_parameters_pyfai_config(self.get_default_input_values())
        self._create_input_form(parameter_info)
        parameter_info = output_parameters_pyfai_config()
        self._create_output_form(parameter_info)

    def _values_from_form(
        self, values: Mapping, checked: Dict[str, bool], output: bool = False
    ) -> Mapping:
        return pack_geometry(values, checked)

    def _values_to_form(
        self, values: Mapping, output: bool = False
    ) -> Tuple[Mapping, Dict[str, bool]]:
        return unpack_geometry(values)

    def _enabled_to_form(
        self, enabled: Dict[str, bool], output: bool = False
    ) -> Dict[str, bool]:
        return unpack_enabled_geometry(enabled)
