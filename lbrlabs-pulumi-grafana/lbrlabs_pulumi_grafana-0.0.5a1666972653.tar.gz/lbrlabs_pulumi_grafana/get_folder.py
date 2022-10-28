# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetFolderResult',
    'AwaitableGetFolderResult',
    'get_folder',
    'get_folder_output',
]

@pulumi.output_type
class GetFolderResult:
    """
    A collection of values returned by getFolder.
    """
    def __init__(__self__, id=None, title=None, uid=None, url=None):
        if id and not isinstance(id, int):
            raise TypeError("Expected argument 'id' to be a int")
        pulumi.set(__self__, "id", id)
        if title and not isinstance(title, str):
            raise TypeError("Expected argument 'title' to be a str")
        pulumi.set(__self__, "title", title)
        if uid and not isinstance(uid, str):
            raise TypeError("Expected argument 'uid' to be a str")
        pulumi.set(__self__, "uid", uid)
        if url and not isinstance(url, str):
            raise TypeError("Expected argument 'url' to be a str")
        pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter
    def id(self) -> int:
        """
        The numerical ID of the Grafana folder.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def title(self) -> str:
        """
        The name of the Grafana folder.
        """
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def uid(self) -> str:
        """
        The uid of the Grafana folder.
        """
        return pulumi.get(self, "uid")

    @property
    @pulumi.getter
    def url(self) -> str:
        """
        The full URL of the folder.
        """
        return pulumi.get(self, "url")


class AwaitableGetFolderResult(GetFolderResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFolderResult(
            id=self.id,
            title=self.title,
            uid=self.uid,
            url=self.url)


def get_folder(title: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFolderResult:
    """
    * [Official documentation](https://grafana.com/docs/grafana/latest/dashboards/dashboard-folders/)
    * [HTTP API](https://grafana.com/docs/grafana/latest/http_api/folder/)

    ## Example Usage

    ```python
    import pulumi
    import lbrlabs_pulumi_grafana as grafana
    import pulumi_grafana as grafana

    test = grafana.Folder("test",
        title="test-folder",
        uid="test-ds-folder-uid")
    from_title = grafana.get_folder_output(title=test.title)
    ```


    :param str title: The name of the Grafana folder.
    """
    __args__ = dict()
    __args__['title'] = title
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('grafana:index/getFolder:getFolder', __args__, opts=opts, typ=GetFolderResult).value

    return AwaitableGetFolderResult(
        id=__ret__.id,
        title=__ret__.title,
        uid=__ret__.uid,
        url=__ret__.url)


@_utilities.lift_output_func(get_folder)
def get_folder_output(title: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFolderResult]:
    """
    * [Official documentation](https://grafana.com/docs/grafana/latest/dashboards/dashboard-folders/)
    * [HTTP API](https://grafana.com/docs/grafana/latest/http_api/folder/)

    ## Example Usage

    ```python
    import pulumi
    import lbrlabs_pulumi_grafana as grafana
    import pulumi_grafana as grafana

    test = grafana.Folder("test",
        title="test-folder",
        uid="test-ds-folder-uid")
    from_title = grafana.get_folder_output(title=test.title)
    ```


    :param str title: The name of the Grafana folder.
    """
    ...
