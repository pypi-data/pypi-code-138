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
    from . import _itkVkRealToHalfHermitianForwardFFTImageFilterPython
else:
    import _itkVkRealToHalfHermitianForwardFFTImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkVkRealToHalfHermitianForwardFFTImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkVkRealToHalfHermitianForwardFFTImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkRealToHalfHermitianForwardFFTImageFilterPython
import itk.itkImageToImageFilterBPython
import itk.itkImageRegionPython
import itk.itkIndexPython
import itk.itkSizePython
import itk.pyBasePython
import itk.itkOffsetPython
import itk.ITKCommonBasePython
import itk.itkMatrixPython
import itk.itkPointPython
import itk.vnl_vector_refPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.itkFixedArrayPython
import itk.itkVectorPython
import itk.itkCovariantVectorPython
import itk.vnl_matrix_fixedPython
import itk.itkVectorImagePython
import itk.itkVariableLengthVectorPython
import itk.itkImagePython
import itk.itkRGBAPixelPython
import itk.itkRGBPixelPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkImageSourcePython
import itk.itkImageSourceCommonPython
import itk.itkImageToImageFilterCommonPython
import itk.itkSimpleDataObjectDecoratorPython
import itk.itkArrayPython

def itkVkRealToHalfHermitianForwardFFTImageFilterID2_New():
    return itkVkRealToHalfHermitianForwardFFTImageFilterID2.New()

class itkVkRealToHalfHermitianForwardFFTImageFilterID2(itk.itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterID2ICD2):
    r"""Proxy of C++ itkVkRealToHalfHermitianForwardFFTImageFilterID2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVkRealToHalfHermitianForwardFFTImageFilterPython.itkVkRealToHalfHermitianForwardFFTImageFilterID2___New_orig__)
    Clone = _swig_new_instance_method(_itkVkRealToHalfHermitianForwardFFTImageFilterPython.itkVkRealToHalfHermitianForwardFFTImageFilterID2_Clone)
    SetUseVkGlobalConfiguration = _swig_new_instance_method(_itkVkRealToHalfHermitianForwardFFTImageFilterPython.itkVkRealToHalfHermitianForwardFFTImageFilterID2_SetUseVkGlobalConfiguration)
    GetUseVkGlobalConfiguration = _swig_new_instance_method(_itkVkRealToHalfHermitianForwardFFTImageFilterPython.itkVkRealToHalfHermitianForwardFFTImageFilterID2_GetUseVkGlobalConfiguration)
    SetDeviceID = _swig_new_instance_method(_itkVkRealToHalfHermitianForwardFFTImageFilterPython.itkVkRealToHalfHermitianForwardFFTImageFilterID2_SetDeviceID)
    GetDeviceID = _swig_new_instance_method(_itkVkRealToHalfHermitianForwardFFTImageFilterPython.itkVkRealToHalfHermitianForwardFFTImageFilterID2_GetDeviceID)
    __swig_destroy__ = _itkVkRealToHalfHermitianForwardFFTImageFilterPython.delete_itkVkRealToHalfHermitianForwardFFTImageFilterID2
    cast = _swig_new_static_method(_itkVkRealToHalfHermitianForwardFFTImageFilterPython.itkVkRealToHalfHermitianForwardFFTImageFilterID2_cast)

    def New(*args, **kargs):
        """New() -> itkVkRealToHalfHermitianForwardFFTImageFilterID2

        Create a new object of the class itkVkRealToHalfHermitianForwardFFTImageFilterID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVkRealToHalfHermitianForwardFFTImageFilterID2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVkRealToHalfHermitianForwardFFTImageFilterID2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVkRealToHalfHermitianForwardFFTImageFilterID2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVkRealToHalfHermitianForwardFFTImageFilterID2 in _itkVkRealToHalfHermitianForwardFFTImageFilterPython:
_itkVkRealToHalfHermitianForwardFFTImageFilterPython.itkVkRealToHalfHermitianForwardFFTImageFilterID2_swigregister(itkVkRealToHalfHermitianForwardFFTImageFilterID2)
itkVkRealToHalfHermitianForwardFFTImageFilterID2___New_orig__ = _itkVkRealToHalfHermitianForwardFFTImageFilterPython.itkVkRealToHalfHermitianForwardFFTImageFilterID2___New_orig__
itkVkRealToHalfHermitianForwardFFTImageFilterID2_cast = _itkVkRealToHalfHermitianForwardFFTImageFilterPython.itkVkRealToHalfHermitianForwardFFTImageFilterID2_cast


def itkVkRealToHalfHermitianForwardFFTImageFilterID3_New():
    return itkVkRealToHalfHermitianForwardFFTImageFilterID3.New()

class itkVkRealToHalfHermitianForwardFFTImageFilterID3(itk.itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterID3ICD3):
    r"""Proxy of C++ itkVkRealToHalfHermitianForwardFFTImageFilterID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVkRealToHalfHermitianForwardFFTImageFilterPython.itkVkRealToHalfHermitianForwardFFTImageFilterID3___New_orig__)
    Clone = _swig_new_instance_method(_itkVkRealToHalfHermitianForwardFFTImageFilterPython.itkVkRealToHalfHermitianForwardFFTImageFilterID3_Clone)
    SetUseVkGlobalConfiguration = _swig_new_instance_method(_itkVkRealToHalfHermitianForwardFFTImageFilterPython.itkVkRealToHalfHermitianForwardFFTImageFilterID3_SetUseVkGlobalConfiguration)
    GetUseVkGlobalConfiguration = _swig_new_instance_method(_itkVkRealToHalfHermitianForwardFFTImageFilterPython.itkVkRealToHalfHermitianForwardFFTImageFilterID3_GetUseVkGlobalConfiguration)
    SetDeviceID = _swig_new_instance_method(_itkVkRealToHalfHermitianForwardFFTImageFilterPython.itkVkRealToHalfHermitianForwardFFTImageFilterID3_SetDeviceID)
    GetDeviceID = _swig_new_instance_method(_itkVkRealToHalfHermitianForwardFFTImageFilterPython.itkVkRealToHalfHermitianForwardFFTImageFilterID3_GetDeviceID)
    __swig_destroy__ = _itkVkRealToHalfHermitianForwardFFTImageFilterPython.delete_itkVkRealToHalfHermitianForwardFFTImageFilterID3
    cast = _swig_new_static_method(_itkVkRealToHalfHermitianForwardFFTImageFilterPython.itkVkRealToHalfHermitianForwardFFTImageFilterID3_cast)

    def New(*args, **kargs):
        """New() -> itkVkRealToHalfHermitianForwardFFTImageFilterID3

        Create a new object of the class itkVkRealToHalfHermitianForwardFFTImageFilterID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVkRealToHalfHermitianForwardFFTImageFilterID3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVkRealToHalfHermitianForwardFFTImageFilterID3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVkRealToHalfHermitianForwardFFTImageFilterID3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVkRealToHalfHermitianForwardFFTImageFilterID3 in _itkVkRealToHalfHermitianForwardFFTImageFilterPython:
_itkVkRealToHalfHermitianForwardFFTImageFilterPython.itkVkRealToHalfHermitianForwardFFTImageFilterID3_swigregister(itkVkRealToHalfHermitianForwardFFTImageFilterID3)
itkVkRealToHalfHermitianForwardFFTImageFilterID3___New_orig__ = _itkVkRealToHalfHermitianForwardFFTImageFilterPython.itkVkRealToHalfHermitianForwardFFTImageFilterID3___New_orig__
itkVkRealToHalfHermitianForwardFFTImageFilterID3_cast = _itkVkRealToHalfHermitianForwardFFTImageFilterPython.itkVkRealToHalfHermitianForwardFFTImageFilterID3_cast


def itkVkRealToHalfHermitianForwardFFTImageFilterIF2_New():
    return itkVkRealToHalfHermitianForwardFFTImageFilterIF2.New()

class itkVkRealToHalfHermitianForwardFFTImageFilterIF2(itk.itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2):
    r"""Proxy of C++ itkVkRealToHalfHermitianForwardFFTImageFilterIF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVkRealToHalfHermitianForwardFFTImageFilterPython.itkVkRealToHalfHermitianForwardFFTImageFilterIF2___New_orig__)
    Clone = _swig_new_instance_method(_itkVkRealToHalfHermitianForwardFFTImageFilterPython.itkVkRealToHalfHermitianForwardFFTImageFilterIF2_Clone)
    SetUseVkGlobalConfiguration = _swig_new_instance_method(_itkVkRealToHalfHermitianForwardFFTImageFilterPython.itkVkRealToHalfHermitianForwardFFTImageFilterIF2_SetUseVkGlobalConfiguration)
    GetUseVkGlobalConfiguration = _swig_new_instance_method(_itkVkRealToHalfHermitianForwardFFTImageFilterPython.itkVkRealToHalfHermitianForwardFFTImageFilterIF2_GetUseVkGlobalConfiguration)
    SetDeviceID = _swig_new_instance_method(_itkVkRealToHalfHermitianForwardFFTImageFilterPython.itkVkRealToHalfHermitianForwardFFTImageFilterIF2_SetDeviceID)
    GetDeviceID = _swig_new_instance_method(_itkVkRealToHalfHermitianForwardFFTImageFilterPython.itkVkRealToHalfHermitianForwardFFTImageFilterIF2_GetDeviceID)
    __swig_destroy__ = _itkVkRealToHalfHermitianForwardFFTImageFilterPython.delete_itkVkRealToHalfHermitianForwardFFTImageFilterIF2
    cast = _swig_new_static_method(_itkVkRealToHalfHermitianForwardFFTImageFilterPython.itkVkRealToHalfHermitianForwardFFTImageFilterIF2_cast)

    def New(*args, **kargs):
        """New() -> itkVkRealToHalfHermitianForwardFFTImageFilterIF2

        Create a new object of the class itkVkRealToHalfHermitianForwardFFTImageFilterIF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVkRealToHalfHermitianForwardFFTImageFilterIF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVkRealToHalfHermitianForwardFFTImageFilterIF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVkRealToHalfHermitianForwardFFTImageFilterIF2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVkRealToHalfHermitianForwardFFTImageFilterIF2 in _itkVkRealToHalfHermitianForwardFFTImageFilterPython:
_itkVkRealToHalfHermitianForwardFFTImageFilterPython.itkVkRealToHalfHermitianForwardFFTImageFilterIF2_swigregister(itkVkRealToHalfHermitianForwardFFTImageFilterIF2)
itkVkRealToHalfHermitianForwardFFTImageFilterIF2___New_orig__ = _itkVkRealToHalfHermitianForwardFFTImageFilterPython.itkVkRealToHalfHermitianForwardFFTImageFilterIF2___New_orig__
itkVkRealToHalfHermitianForwardFFTImageFilterIF2_cast = _itkVkRealToHalfHermitianForwardFFTImageFilterPython.itkVkRealToHalfHermitianForwardFFTImageFilterIF2_cast


def itkVkRealToHalfHermitianForwardFFTImageFilterIF3_New():
    return itkVkRealToHalfHermitianForwardFFTImageFilterIF3.New()

class itkVkRealToHalfHermitianForwardFFTImageFilterIF3(itk.itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3):
    r"""Proxy of C++ itkVkRealToHalfHermitianForwardFFTImageFilterIF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVkRealToHalfHermitianForwardFFTImageFilterPython.itkVkRealToHalfHermitianForwardFFTImageFilterIF3___New_orig__)
    Clone = _swig_new_instance_method(_itkVkRealToHalfHermitianForwardFFTImageFilterPython.itkVkRealToHalfHermitianForwardFFTImageFilterIF3_Clone)
    SetUseVkGlobalConfiguration = _swig_new_instance_method(_itkVkRealToHalfHermitianForwardFFTImageFilterPython.itkVkRealToHalfHermitianForwardFFTImageFilterIF3_SetUseVkGlobalConfiguration)
    GetUseVkGlobalConfiguration = _swig_new_instance_method(_itkVkRealToHalfHermitianForwardFFTImageFilterPython.itkVkRealToHalfHermitianForwardFFTImageFilterIF3_GetUseVkGlobalConfiguration)
    SetDeviceID = _swig_new_instance_method(_itkVkRealToHalfHermitianForwardFFTImageFilterPython.itkVkRealToHalfHermitianForwardFFTImageFilterIF3_SetDeviceID)
    GetDeviceID = _swig_new_instance_method(_itkVkRealToHalfHermitianForwardFFTImageFilterPython.itkVkRealToHalfHermitianForwardFFTImageFilterIF3_GetDeviceID)
    __swig_destroy__ = _itkVkRealToHalfHermitianForwardFFTImageFilterPython.delete_itkVkRealToHalfHermitianForwardFFTImageFilterIF3
    cast = _swig_new_static_method(_itkVkRealToHalfHermitianForwardFFTImageFilterPython.itkVkRealToHalfHermitianForwardFFTImageFilterIF3_cast)

    def New(*args, **kargs):
        """New() -> itkVkRealToHalfHermitianForwardFFTImageFilterIF3

        Create a new object of the class itkVkRealToHalfHermitianForwardFFTImageFilterIF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVkRealToHalfHermitianForwardFFTImageFilterIF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVkRealToHalfHermitianForwardFFTImageFilterIF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVkRealToHalfHermitianForwardFFTImageFilterIF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVkRealToHalfHermitianForwardFFTImageFilterIF3 in _itkVkRealToHalfHermitianForwardFFTImageFilterPython:
_itkVkRealToHalfHermitianForwardFFTImageFilterPython.itkVkRealToHalfHermitianForwardFFTImageFilterIF3_swigregister(itkVkRealToHalfHermitianForwardFFTImageFilterIF3)
itkVkRealToHalfHermitianForwardFFTImageFilterIF3___New_orig__ = _itkVkRealToHalfHermitianForwardFFTImageFilterPython.itkVkRealToHalfHermitianForwardFFTImageFilterIF3___New_orig__
itkVkRealToHalfHermitianForwardFFTImageFilterIF3_cast = _itkVkRealToHalfHermitianForwardFFTImageFilterPython.itkVkRealToHalfHermitianForwardFFTImageFilterIF3_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def vk_real_to_half_hermitian_forward_fft_image_filter(*args: itkt.ImageLike,  use_vk_global_configuration: bool=..., device_id: int=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for VkRealToHalfHermitianForwardFFTImageFilter"""
    import itk

    kwarg_typehints = { 'use_vk_global_configuration':use_vk_global_configuration,'device_id':device_id }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.VkRealToHalfHermitianForwardFFTImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def vk_real_to_half_hermitian_forward_fft_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.VkFFTBackend.VkRealToHalfHermitianForwardFFTImageFilter
    vk_real_to_half_hermitian_forward_fft_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    vk_real_to_half_hermitian_forward_fft_image_filter.__doc__ = filter_object.__doc__




