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
    from . import _itkVkForward1DFFTImageFilterPython
else:
    import _itkVkForward1DFFTImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkVkForward1DFFTImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkVkForward1DFFTImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkForward1DFFTImageFilterPython
import itk.itkImageToImageFilterBPython
import itk.itkImagePython
import itk.itkSizePython
import itk.pyBasePython
import itk.itkRGBAPixelPython
import itk.itkFixedArrayPython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkMatrixPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.vnl_vectorPython
import itk.vnl_matrix_fixedPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.itkCovariantVectorPython
import itk.itkPointPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkRGBPixelPython
import itk.itkImageRegionPython
import itk.ITKCommonBasePython
import itk.itkVectorImagePython
import itk.itkVariableLengthVectorPython
import itk.itkImageToImageFilterCommonPython
import itk.itkImageSourcePython
import itk.itkImageSourceCommonPython

def itkVkForward1DFFTImageFilterID2_New():
    return itkVkForward1DFFTImageFilterID2.New()

class itkVkForward1DFFTImageFilterID2(itk.itkForward1DFFTImageFilterPython.itkForward1DFFTImageFilterID2):
    r"""Proxy of C++ itkVkForward1DFFTImageFilterID2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVkForward1DFFTImageFilterPython.itkVkForward1DFFTImageFilterID2___New_orig__)
    Clone = _swig_new_instance_method(_itkVkForward1DFFTImageFilterPython.itkVkForward1DFFTImageFilterID2_Clone)
    SetUseVkGlobalConfiguration = _swig_new_instance_method(_itkVkForward1DFFTImageFilterPython.itkVkForward1DFFTImageFilterID2_SetUseVkGlobalConfiguration)
    GetUseVkGlobalConfiguration = _swig_new_instance_method(_itkVkForward1DFFTImageFilterPython.itkVkForward1DFFTImageFilterID2_GetUseVkGlobalConfiguration)
    SetDeviceID = _swig_new_instance_method(_itkVkForward1DFFTImageFilterPython.itkVkForward1DFFTImageFilterID2_SetDeviceID)
    GetDeviceID = _swig_new_instance_method(_itkVkForward1DFFTImageFilterPython.itkVkForward1DFFTImageFilterID2_GetDeviceID)
    __swig_destroy__ = _itkVkForward1DFFTImageFilterPython.delete_itkVkForward1DFFTImageFilterID2
    cast = _swig_new_static_method(_itkVkForward1DFFTImageFilterPython.itkVkForward1DFFTImageFilterID2_cast)

    def New(*args, **kargs):
        """New() -> itkVkForward1DFFTImageFilterID2

        Create a new object of the class itkVkForward1DFFTImageFilterID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVkForward1DFFTImageFilterID2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVkForward1DFFTImageFilterID2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVkForward1DFFTImageFilterID2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVkForward1DFFTImageFilterID2 in _itkVkForward1DFFTImageFilterPython:
_itkVkForward1DFFTImageFilterPython.itkVkForward1DFFTImageFilterID2_swigregister(itkVkForward1DFFTImageFilterID2)
itkVkForward1DFFTImageFilterID2___New_orig__ = _itkVkForward1DFFTImageFilterPython.itkVkForward1DFFTImageFilterID2___New_orig__
itkVkForward1DFFTImageFilterID2_cast = _itkVkForward1DFFTImageFilterPython.itkVkForward1DFFTImageFilterID2_cast


def itkVkForward1DFFTImageFilterID3_New():
    return itkVkForward1DFFTImageFilterID3.New()

class itkVkForward1DFFTImageFilterID3(itk.itkForward1DFFTImageFilterPython.itkForward1DFFTImageFilterID3):
    r"""Proxy of C++ itkVkForward1DFFTImageFilterID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVkForward1DFFTImageFilterPython.itkVkForward1DFFTImageFilterID3___New_orig__)
    Clone = _swig_new_instance_method(_itkVkForward1DFFTImageFilterPython.itkVkForward1DFFTImageFilterID3_Clone)
    SetUseVkGlobalConfiguration = _swig_new_instance_method(_itkVkForward1DFFTImageFilterPython.itkVkForward1DFFTImageFilterID3_SetUseVkGlobalConfiguration)
    GetUseVkGlobalConfiguration = _swig_new_instance_method(_itkVkForward1DFFTImageFilterPython.itkVkForward1DFFTImageFilterID3_GetUseVkGlobalConfiguration)
    SetDeviceID = _swig_new_instance_method(_itkVkForward1DFFTImageFilterPython.itkVkForward1DFFTImageFilterID3_SetDeviceID)
    GetDeviceID = _swig_new_instance_method(_itkVkForward1DFFTImageFilterPython.itkVkForward1DFFTImageFilterID3_GetDeviceID)
    __swig_destroy__ = _itkVkForward1DFFTImageFilterPython.delete_itkVkForward1DFFTImageFilterID3
    cast = _swig_new_static_method(_itkVkForward1DFFTImageFilterPython.itkVkForward1DFFTImageFilterID3_cast)

    def New(*args, **kargs):
        """New() -> itkVkForward1DFFTImageFilterID3

        Create a new object of the class itkVkForward1DFFTImageFilterID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVkForward1DFFTImageFilterID3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVkForward1DFFTImageFilterID3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVkForward1DFFTImageFilterID3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVkForward1DFFTImageFilterID3 in _itkVkForward1DFFTImageFilterPython:
_itkVkForward1DFFTImageFilterPython.itkVkForward1DFFTImageFilterID3_swigregister(itkVkForward1DFFTImageFilterID3)
itkVkForward1DFFTImageFilterID3___New_orig__ = _itkVkForward1DFFTImageFilterPython.itkVkForward1DFFTImageFilterID3___New_orig__
itkVkForward1DFFTImageFilterID3_cast = _itkVkForward1DFFTImageFilterPython.itkVkForward1DFFTImageFilterID3_cast


def itkVkForward1DFFTImageFilterIF2_New():
    return itkVkForward1DFFTImageFilterIF2.New()

class itkVkForward1DFFTImageFilterIF2(itk.itkForward1DFFTImageFilterPython.itkForward1DFFTImageFilterIF2):
    r"""Proxy of C++ itkVkForward1DFFTImageFilterIF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVkForward1DFFTImageFilterPython.itkVkForward1DFFTImageFilterIF2___New_orig__)
    Clone = _swig_new_instance_method(_itkVkForward1DFFTImageFilterPython.itkVkForward1DFFTImageFilterIF2_Clone)
    SetUseVkGlobalConfiguration = _swig_new_instance_method(_itkVkForward1DFFTImageFilterPython.itkVkForward1DFFTImageFilterIF2_SetUseVkGlobalConfiguration)
    GetUseVkGlobalConfiguration = _swig_new_instance_method(_itkVkForward1DFFTImageFilterPython.itkVkForward1DFFTImageFilterIF2_GetUseVkGlobalConfiguration)
    SetDeviceID = _swig_new_instance_method(_itkVkForward1DFFTImageFilterPython.itkVkForward1DFFTImageFilterIF2_SetDeviceID)
    GetDeviceID = _swig_new_instance_method(_itkVkForward1DFFTImageFilterPython.itkVkForward1DFFTImageFilterIF2_GetDeviceID)
    __swig_destroy__ = _itkVkForward1DFFTImageFilterPython.delete_itkVkForward1DFFTImageFilterIF2
    cast = _swig_new_static_method(_itkVkForward1DFFTImageFilterPython.itkVkForward1DFFTImageFilterIF2_cast)

    def New(*args, **kargs):
        """New() -> itkVkForward1DFFTImageFilterIF2

        Create a new object of the class itkVkForward1DFFTImageFilterIF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVkForward1DFFTImageFilterIF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVkForward1DFFTImageFilterIF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVkForward1DFFTImageFilterIF2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVkForward1DFFTImageFilterIF2 in _itkVkForward1DFFTImageFilterPython:
_itkVkForward1DFFTImageFilterPython.itkVkForward1DFFTImageFilterIF2_swigregister(itkVkForward1DFFTImageFilterIF2)
itkVkForward1DFFTImageFilterIF2___New_orig__ = _itkVkForward1DFFTImageFilterPython.itkVkForward1DFFTImageFilterIF2___New_orig__
itkVkForward1DFFTImageFilterIF2_cast = _itkVkForward1DFFTImageFilterPython.itkVkForward1DFFTImageFilterIF2_cast


def itkVkForward1DFFTImageFilterIF3_New():
    return itkVkForward1DFFTImageFilterIF3.New()

class itkVkForward1DFFTImageFilterIF3(itk.itkForward1DFFTImageFilterPython.itkForward1DFFTImageFilterIF3):
    r"""Proxy of C++ itkVkForward1DFFTImageFilterIF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVkForward1DFFTImageFilterPython.itkVkForward1DFFTImageFilterIF3___New_orig__)
    Clone = _swig_new_instance_method(_itkVkForward1DFFTImageFilterPython.itkVkForward1DFFTImageFilterIF3_Clone)
    SetUseVkGlobalConfiguration = _swig_new_instance_method(_itkVkForward1DFFTImageFilterPython.itkVkForward1DFFTImageFilterIF3_SetUseVkGlobalConfiguration)
    GetUseVkGlobalConfiguration = _swig_new_instance_method(_itkVkForward1DFFTImageFilterPython.itkVkForward1DFFTImageFilterIF3_GetUseVkGlobalConfiguration)
    SetDeviceID = _swig_new_instance_method(_itkVkForward1DFFTImageFilterPython.itkVkForward1DFFTImageFilterIF3_SetDeviceID)
    GetDeviceID = _swig_new_instance_method(_itkVkForward1DFFTImageFilterPython.itkVkForward1DFFTImageFilterIF3_GetDeviceID)
    __swig_destroy__ = _itkVkForward1DFFTImageFilterPython.delete_itkVkForward1DFFTImageFilterIF3
    cast = _swig_new_static_method(_itkVkForward1DFFTImageFilterPython.itkVkForward1DFFTImageFilterIF3_cast)

    def New(*args, **kargs):
        """New() -> itkVkForward1DFFTImageFilterIF3

        Create a new object of the class itkVkForward1DFFTImageFilterIF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVkForward1DFFTImageFilterIF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVkForward1DFFTImageFilterIF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVkForward1DFFTImageFilterIF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVkForward1DFFTImageFilterIF3 in _itkVkForward1DFFTImageFilterPython:
_itkVkForward1DFFTImageFilterPython.itkVkForward1DFFTImageFilterIF3_swigregister(itkVkForward1DFFTImageFilterIF3)
itkVkForward1DFFTImageFilterIF3___New_orig__ = _itkVkForward1DFFTImageFilterPython.itkVkForward1DFFTImageFilterIF3___New_orig__
itkVkForward1DFFTImageFilterIF3_cast = _itkVkForward1DFFTImageFilterPython.itkVkForward1DFFTImageFilterIF3_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def vk_forward1_dfft_image_filter(*args: itkt.ImageLike,  use_vk_global_configuration: bool=..., device_id: int=..., direction: int=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for VkForward1DFFTImageFilter"""
    import itk

    kwarg_typehints = { 'use_vk_global_configuration':use_vk_global_configuration,'device_id':device_id,'direction':direction }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.VkForward1DFFTImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def vk_forward1_dfft_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.VkFFTBackend.VkForward1DFFTImageFilter
    vk_forward1_dfft_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    vk_forward1_dfft_image_filter.__doc__ = filter_object.__doc__




