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
    from . import _itkVkComplexToComplexFFTImageFilterPython
else:
    import _itkVkComplexToComplexFFTImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkVkComplexToComplexFFTImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkVkComplexToComplexFFTImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkComplexToComplexFFTImageFilterPython
import itk.itkImageToImageFilterBPython
import itk.itkImagePython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.pyBasePython
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.vnl_matrixPython
import itk.vnl_vector_refPython
import itk.itkCovariantVectorPython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkPointPython
import itk.itkRGBAPixelPython
import itk.ITKCommonBasePython
import itk.itkRGBPixelPython
import itk.itkImageRegionPython
import itk.itkImageToImageFilterCommonPython
import itk.itkVectorImagePython
import itk.itkVariableLengthVectorPython
import itk.itkImageSourcePython
import itk.itkImageSourceCommonPython

def itkVkComplexToComplexFFTImageFilterICD2_New():
    return itkVkComplexToComplexFFTImageFilterICD2.New()

class itkVkComplexToComplexFFTImageFilterICD2(itk.itkComplexToComplexFFTImageFilterPython.itkComplexToComplexFFTImageFilterICD2):
    r"""Proxy of C++ itkVkComplexToComplexFFTImageFilterICD2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICD2___New_orig__)
    Clone = _swig_new_instance_method(_itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICD2_Clone)
    SetUseVkGlobalConfiguration = _swig_new_instance_method(_itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICD2_SetUseVkGlobalConfiguration)
    GetUseVkGlobalConfiguration = _swig_new_instance_method(_itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICD2_GetUseVkGlobalConfiguration)
    SetDeviceID = _swig_new_instance_method(_itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICD2_SetDeviceID)
    GetDeviceID = _swig_new_instance_method(_itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICD2_GetDeviceID)
    GetSizeGreatestPrimeFactor = _swig_new_instance_method(_itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICD2_GetSizeGreatestPrimeFactor)
    __swig_destroy__ = _itkVkComplexToComplexFFTImageFilterPython.delete_itkVkComplexToComplexFFTImageFilterICD2
    cast = _swig_new_static_method(_itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICD2_cast)

    def New(*args, **kargs):
        """New() -> itkVkComplexToComplexFFTImageFilterICD2

        Create a new object of the class itkVkComplexToComplexFFTImageFilterICD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVkComplexToComplexFFTImageFilterICD2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVkComplexToComplexFFTImageFilterICD2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVkComplexToComplexFFTImageFilterICD2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVkComplexToComplexFFTImageFilterICD2 in _itkVkComplexToComplexFFTImageFilterPython:
_itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICD2_swigregister(itkVkComplexToComplexFFTImageFilterICD2)
itkVkComplexToComplexFFTImageFilterICD2___New_orig__ = _itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICD2___New_orig__
itkVkComplexToComplexFFTImageFilterICD2_cast = _itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICD2_cast


def itkVkComplexToComplexFFTImageFilterICD3_New():
    return itkVkComplexToComplexFFTImageFilterICD3.New()

class itkVkComplexToComplexFFTImageFilterICD3(itk.itkComplexToComplexFFTImageFilterPython.itkComplexToComplexFFTImageFilterICD3):
    r"""Proxy of C++ itkVkComplexToComplexFFTImageFilterICD3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICD3___New_orig__)
    Clone = _swig_new_instance_method(_itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICD3_Clone)
    SetUseVkGlobalConfiguration = _swig_new_instance_method(_itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICD3_SetUseVkGlobalConfiguration)
    GetUseVkGlobalConfiguration = _swig_new_instance_method(_itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICD3_GetUseVkGlobalConfiguration)
    SetDeviceID = _swig_new_instance_method(_itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICD3_SetDeviceID)
    GetDeviceID = _swig_new_instance_method(_itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICD3_GetDeviceID)
    GetSizeGreatestPrimeFactor = _swig_new_instance_method(_itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICD3_GetSizeGreatestPrimeFactor)
    __swig_destroy__ = _itkVkComplexToComplexFFTImageFilterPython.delete_itkVkComplexToComplexFFTImageFilterICD3
    cast = _swig_new_static_method(_itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICD3_cast)

    def New(*args, **kargs):
        """New() -> itkVkComplexToComplexFFTImageFilterICD3

        Create a new object of the class itkVkComplexToComplexFFTImageFilterICD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVkComplexToComplexFFTImageFilterICD3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVkComplexToComplexFFTImageFilterICD3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVkComplexToComplexFFTImageFilterICD3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVkComplexToComplexFFTImageFilterICD3 in _itkVkComplexToComplexFFTImageFilterPython:
_itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICD3_swigregister(itkVkComplexToComplexFFTImageFilterICD3)
itkVkComplexToComplexFFTImageFilterICD3___New_orig__ = _itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICD3___New_orig__
itkVkComplexToComplexFFTImageFilterICD3_cast = _itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICD3_cast


def itkVkComplexToComplexFFTImageFilterICF2_New():
    return itkVkComplexToComplexFFTImageFilterICF2.New()

class itkVkComplexToComplexFFTImageFilterICF2(itk.itkComplexToComplexFFTImageFilterPython.itkComplexToComplexFFTImageFilterICF2):
    r"""Proxy of C++ itkVkComplexToComplexFFTImageFilterICF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICF2___New_orig__)
    Clone = _swig_new_instance_method(_itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICF2_Clone)
    SetUseVkGlobalConfiguration = _swig_new_instance_method(_itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICF2_SetUseVkGlobalConfiguration)
    GetUseVkGlobalConfiguration = _swig_new_instance_method(_itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICF2_GetUseVkGlobalConfiguration)
    SetDeviceID = _swig_new_instance_method(_itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICF2_SetDeviceID)
    GetDeviceID = _swig_new_instance_method(_itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICF2_GetDeviceID)
    GetSizeGreatestPrimeFactor = _swig_new_instance_method(_itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICF2_GetSizeGreatestPrimeFactor)
    __swig_destroy__ = _itkVkComplexToComplexFFTImageFilterPython.delete_itkVkComplexToComplexFFTImageFilterICF2
    cast = _swig_new_static_method(_itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICF2_cast)

    def New(*args, **kargs):
        """New() -> itkVkComplexToComplexFFTImageFilterICF2

        Create a new object of the class itkVkComplexToComplexFFTImageFilterICF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVkComplexToComplexFFTImageFilterICF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVkComplexToComplexFFTImageFilterICF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVkComplexToComplexFFTImageFilterICF2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVkComplexToComplexFFTImageFilterICF2 in _itkVkComplexToComplexFFTImageFilterPython:
_itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICF2_swigregister(itkVkComplexToComplexFFTImageFilterICF2)
itkVkComplexToComplexFFTImageFilterICF2___New_orig__ = _itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICF2___New_orig__
itkVkComplexToComplexFFTImageFilterICF2_cast = _itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICF2_cast


def itkVkComplexToComplexFFTImageFilterICF3_New():
    return itkVkComplexToComplexFFTImageFilterICF3.New()

class itkVkComplexToComplexFFTImageFilterICF3(itk.itkComplexToComplexFFTImageFilterPython.itkComplexToComplexFFTImageFilterICF3):
    r"""Proxy of C++ itkVkComplexToComplexFFTImageFilterICF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICF3___New_orig__)
    Clone = _swig_new_instance_method(_itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICF3_Clone)
    SetUseVkGlobalConfiguration = _swig_new_instance_method(_itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICF3_SetUseVkGlobalConfiguration)
    GetUseVkGlobalConfiguration = _swig_new_instance_method(_itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICF3_GetUseVkGlobalConfiguration)
    SetDeviceID = _swig_new_instance_method(_itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICF3_SetDeviceID)
    GetDeviceID = _swig_new_instance_method(_itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICF3_GetDeviceID)
    GetSizeGreatestPrimeFactor = _swig_new_instance_method(_itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICF3_GetSizeGreatestPrimeFactor)
    __swig_destroy__ = _itkVkComplexToComplexFFTImageFilterPython.delete_itkVkComplexToComplexFFTImageFilterICF3
    cast = _swig_new_static_method(_itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICF3_cast)

    def New(*args, **kargs):
        """New() -> itkVkComplexToComplexFFTImageFilterICF3

        Create a new object of the class itkVkComplexToComplexFFTImageFilterICF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVkComplexToComplexFFTImageFilterICF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVkComplexToComplexFFTImageFilterICF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVkComplexToComplexFFTImageFilterICF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVkComplexToComplexFFTImageFilterICF3 in _itkVkComplexToComplexFFTImageFilterPython:
_itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICF3_swigregister(itkVkComplexToComplexFFTImageFilterICF3)
itkVkComplexToComplexFFTImageFilterICF3___New_orig__ = _itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICF3___New_orig__
itkVkComplexToComplexFFTImageFilterICF3_cast = _itkVkComplexToComplexFFTImageFilterPython.itkVkComplexToComplexFFTImageFilterICF3_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def vk_complex_to_complex_fft_image_filter(*args: itkt.ImageLike,  use_vk_global_configuration: bool=..., device_id: int=..., transform_direction=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for VkComplexToComplexFFTImageFilter"""
    import itk

    kwarg_typehints = { 'use_vk_global_configuration':use_vk_global_configuration,'device_id':device_id,'transform_direction':transform_direction }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.VkComplexToComplexFFTImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def vk_complex_to_complex_fft_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.VkFFTBackend.VkComplexToComplexFFTImageFilter
    vk_complex_to_complex_fft_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    vk_complex_to_complex_fft_image_filter.__doc__ = filter_object.__doc__




