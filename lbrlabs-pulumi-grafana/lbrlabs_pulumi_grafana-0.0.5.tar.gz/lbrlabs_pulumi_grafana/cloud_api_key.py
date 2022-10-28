# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['CloudApiKeyArgs', 'CloudApiKey']

@pulumi.input_type
class CloudApiKeyArgs:
    def __init__(__self__, *,
                 cloud_org_slug: pulumi.Input[str],
                 role: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CloudApiKey resource.
        :param pulumi.Input[str] cloud_org_slug: The slug of the organization to create the API key in. This is the same slug as the organization name in the URL.
        :param pulumi.Input[str] role: Role of the API key. Should be one of [Viewer Editor Admin MetricsPublisher PluginPublisher]. See https://grafana.com/docs/grafana-cloud/api/#create-api-key for details.
        :param pulumi.Input[str] name: Name of the API key.
        """
        pulumi.set(__self__, "cloud_org_slug", cloud_org_slug)
        pulumi.set(__self__, "role", role)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="cloudOrgSlug")
    def cloud_org_slug(self) -> pulumi.Input[str]:
        """
        The slug of the organization to create the API key in. This is the same slug as the organization name in the URL.
        """
        return pulumi.get(self, "cloud_org_slug")

    @cloud_org_slug.setter
    def cloud_org_slug(self, value: pulumi.Input[str]):
        pulumi.set(self, "cloud_org_slug", value)

    @property
    @pulumi.getter
    def role(self) -> pulumi.Input[str]:
        """
        Role of the API key. Should be one of [Viewer Editor Admin MetricsPublisher PluginPublisher]. See https://grafana.com/docs/grafana-cloud/api/#create-api-key for details.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: pulumi.Input[str]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the API key.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _CloudApiKeyState:
    def __init__(__self__, *,
                 cloud_org_slug: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering CloudApiKey resources.
        :param pulumi.Input[str] cloud_org_slug: The slug of the organization to create the API key in. This is the same slug as the organization name in the URL.
        :param pulumi.Input[str] key: The generated API key.
        :param pulumi.Input[str] name: Name of the API key.
        :param pulumi.Input[str] role: Role of the API key. Should be one of [Viewer Editor Admin MetricsPublisher PluginPublisher]. See https://grafana.com/docs/grafana-cloud/api/#create-api-key for details.
        """
        if cloud_org_slug is not None:
            pulumi.set(__self__, "cloud_org_slug", cloud_org_slug)
        if key is not None:
            pulumi.set(__self__, "key", key)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if role is not None:
            pulumi.set(__self__, "role", role)

    @property
    @pulumi.getter(name="cloudOrgSlug")
    def cloud_org_slug(self) -> Optional[pulumi.Input[str]]:
        """
        The slug of the organization to create the API key in. This is the same slug as the organization name in the URL.
        """
        return pulumi.get(self, "cloud_org_slug")

    @cloud_org_slug.setter
    def cloud_org_slug(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cloud_org_slug", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        """
        The generated API key.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the API key.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[str]]:
        """
        Role of the API key. Should be one of [Viewer Editor Admin MetricsPublisher PluginPublisher]. See https://grafana.com/docs/grafana-cloud/api/#create-api-key for details.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role", value)


class CloudApiKey(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cloud_org_slug: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a single API key on the Grafana Cloud portal (on the organization level)
        * [API documentation](https://grafana.com/docs/grafana-cloud/reference/cloud-api/#api-keys)

        ## Example Usage

        ```python
        import pulumi
        import lbrlabs_pulumi_grafana as grafana

        test = grafana.CloudApiKey("test",
            cloud_org_slug="myorg",
            role="Admin")
        ```

        ## Import

        ```sh
         $ pulumi import grafana:index/cloudApiKey:CloudApiKey resource_name "{{org-name}}-{{api_key_name}}"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cloud_org_slug: The slug of the organization to create the API key in. This is the same slug as the organization name in the URL.
        :param pulumi.Input[str] name: Name of the API key.
        :param pulumi.Input[str] role: Role of the API key. Should be one of [Viewer Editor Admin MetricsPublisher PluginPublisher]. See https://grafana.com/docs/grafana-cloud/api/#create-api-key for details.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CloudApiKeyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a single API key on the Grafana Cloud portal (on the organization level)
        * [API documentation](https://grafana.com/docs/grafana-cloud/reference/cloud-api/#api-keys)

        ## Example Usage

        ```python
        import pulumi
        import lbrlabs_pulumi_grafana as grafana

        test = grafana.CloudApiKey("test",
            cloud_org_slug="myorg",
            role="Admin")
        ```

        ## Import

        ```sh
         $ pulumi import grafana:index/cloudApiKey:CloudApiKey resource_name "{{org-name}}-{{api_key_name}}"
        ```

        :param str resource_name: The name of the resource.
        :param CloudApiKeyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CloudApiKeyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cloud_org_slug: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CloudApiKeyArgs.__new__(CloudApiKeyArgs)

            if cloud_org_slug is None and not opts.urn:
                raise TypeError("Missing required property 'cloud_org_slug'")
            __props__.__dict__["cloud_org_slug"] = cloud_org_slug
            __props__.__dict__["name"] = name
            if role is None and not opts.urn:
                raise TypeError("Missing required property 'role'")
            __props__.__dict__["role"] = role
            __props__.__dict__["key"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["key"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(CloudApiKey, __self__).__init__(
            'grafana:index/cloudApiKey:CloudApiKey',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cloud_org_slug: Optional[pulumi.Input[str]] = None,
            key: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            role: Optional[pulumi.Input[str]] = None) -> 'CloudApiKey':
        """
        Get an existing CloudApiKey resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cloud_org_slug: The slug of the organization to create the API key in. This is the same slug as the organization name in the URL.
        :param pulumi.Input[str] key: The generated API key.
        :param pulumi.Input[str] name: Name of the API key.
        :param pulumi.Input[str] role: Role of the API key. Should be one of [Viewer Editor Admin MetricsPublisher PluginPublisher]. See https://grafana.com/docs/grafana-cloud/api/#create-api-key for details.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CloudApiKeyState.__new__(_CloudApiKeyState)

        __props__.__dict__["cloud_org_slug"] = cloud_org_slug
        __props__.__dict__["key"] = key
        __props__.__dict__["name"] = name
        __props__.__dict__["role"] = role
        return CloudApiKey(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="cloudOrgSlug")
    def cloud_org_slug(self) -> pulumi.Output[str]:
        """
        The slug of the organization to create the API key in. This is the same slug as the organization name in the URL.
        """
        return pulumi.get(self, "cloud_org_slug")

    @property
    @pulumi.getter
    def key(self) -> pulumi.Output[str]:
        """
        The generated API key.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the API key.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def role(self) -> pulumi.Output[str]:
        """
        Role of the API key. Should be one of [Viewer Editor Admin MetricsPublisher PluginPublisher]. See https://grafana.com/docs/grafana-cloud/api/#create-api-key for details.
        """
        return pulumi.get(self, "role")

