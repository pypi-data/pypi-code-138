# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 7, 0):
    raise RuntimeError("Python 3.7 or later required")

from . import _ITKCommonPython


from . import _VkFFTBackendPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkVkGlobalConfigurationPython
else:
    import _itkVkGlobalConfigurationPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkVkGlobalConfigurationPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkVkGlobalConfigurationPython.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import collections.abc
import itk.ITKCommonBasePython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.vnl_vectorPython
import itk.itkCovariantVectorPython
import itk.itkFixedArrayPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.itkPointPython
class itkVkGlobalConfiguration(itk.ITKCommonBasePython.itkLightObject):
    r"""Proxy of C++ itkVkGlobalConfiguration class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetDeviceID = _swig_new_static_method(_itkVkGlobalConfigurationPython.itkVkGlobalConfiguration_SetDeviceID)
    GetDeviceID = _swig_new_static_method(_itkVkGlobalConfigurationPython.itkVkGlobalConfiguration_GetDeviceID)
    __swig_destroy__ = _itkVkGlobalConfigurationPython.delete_itkVkGlobalConfiguration
    cast = _swig_new_static_method(_itkVkGlobalConfigurationPython.itkVkGlobalConfiguration_cast)

# Register itkVkGlobalConfiguration in _itkVkGlobalConfigurationPython:
_itkVkGlobalConfigurationPython.itkVkGlobalConfiguration_swigregister(itkVkGlobalConfiguration)
itkVkGlobalConfiguration_SetDeviceID = _itkVkGlobalConfigurationPython.itkVkGlobalConfiguration_SetDeviceID
itkVkGlobalConfiguration_GetDeviceID = _itkVkGlobalConfigurationPython.itkVkGlobalConfiguration_GetDeviceID
itkVkGlobalConfiguration_cast = _itkVkGlobalConfigurationPython.itkVkGlobalConfiguration_cast



