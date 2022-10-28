# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

from .. import serializer as jina__pb2


class JinaDataRequestRPCStub(object):
    """*
    jina gRPC service for DataRequests.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.process_data = channel.unary_unary(
                '/jina.JinaDataRequestRPC/process_data',
                request_serializer=jina__pb2.DataRequestListProto.SerializeToString,
                response_deserializer=jina__pb2.DataRequestProto.FromString,
                )


class JinaDataRequestRPCServicer(object):
    """*
    jina gRPC service for DataRequests.
    """

    def process_data(self, request, context):
        """Used for passing DataRequests to the Executors
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_JinaDataRequestRPCServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'process_data': grpc.unary_unary_rpc_method_handler(
                    servicer.process_data,
                    request_deserializer=jina__pb2.DataRequestListProto.FromString,
                    response_serializer=jina__pb2.DataRequestProto.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'jina.JinaDataRequestRPC', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class JinaDataRequestRPC(object):
    """*
    jina gRPC service for DataRequests.
    """

    @staticmethod
    def process_data(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/jina.JinaDataRequestRPC/process_data',
            jina__pb2.DataRequestListProto.SerializeToString,
            jina__pb2.DataRequestProto.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class JinaSingleDataRequestRPCStub(object):
    """*
    jina gRPC service for DataRequests.
    This is used to send requests to Executors when a list of requests is not needed
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.process_single_data = channel.unary_unary(
                '/jina.JinaSingleDataRequestRPC/process_single_data',
                request_serializer=jina__pb2.DataRequestProto.SerializeToString,
                response_deserializer=jina__pb2.DataRequestProto.FromString,
                )


class JinaSingleDataRequestRPCServicer(object):
    """*
    jina gRPC service for DataRequests.
    This is used to send requests to Executors when a list of requests is not needed
    """

    def process_single_data(self, request, context):
        """Used for passing DataRequests to the Executors
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_JinaSingleDataRequestRPCServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'process_single_data': grpc.unary_unary_rpc_method_handler(
                    servicer.process_single_data,
                    request_deserializer=jina__pb2.DataRequestProto.FromString,
                    response_serializer=jina__pb2.DataRequestProto.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'jina.JinaSingleDataRequestRPC', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class JinaSingleDataRequestRPC(object):
    """*
    jina gRPC service for DataRequests.
    This is used to send requests to Executors when a list of requests is not needed
    """

    @staticmethod
    def process_single_data(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/jina.JinaSingleDataRequestRPC/process_single_data',
            jina__pb2.DataRequestProto.SerializeToString,
            jina__pb2.DataRequestProto.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class JinaRPCStub(object):
    """*
    jina Gateway gRPC service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Call = channel.stream_stream(
                '/jina.JinaRPC/Call',
                request_serializer=jina__pb2.DataRequestProto.SerializeToString,
                response_deserializer=jina__pb2.DataRequestProto.FromString,
                )


class JinaRPCServicer(object):
    """*
    jina Gateway gRPC service.
    """

    def Call(self, request_iterator, context):
        """Pass in a Request and a filled Request with matches will be returned.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_JinaRPCServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Call': grpc.stream_stream_rpc_method_handler(
                    servicer.Call,
                    request_deserializer=jina__pb2.DataRequestProto.FromString,
                    response_serializer=jina__pb2.DataRequestProto.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'jina.JinaRPC', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class JinaRPC(object):
    """*
    jina Gateway gRPC service.
    """

    @staticmethod
    def Call(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/jina.JinaRPC/Call',
            jina__pb2.DataRequestProto.SerializeToString,
            jina__pb2.DataRequestProto.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class JinaDiscoverEndpointsRPCStub(object):
    """*
    jina gRPC service to expose Endpoints from Executors.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.endpoint_discovery = channel.unary_unary(
                '/jina.JinaDiscoverEndpointsRPC/endpoint_discovery',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=jina__pb2.EndpointsProto.FromString,
                )


class JinaDiscoverEndpointsRPCServicer(object):
    """*
    jina gRPC service to expose Endpoints from Executors.
    """

    def endpoint_discovery(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_JinaDiscoverEndpointsRPCServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'endpoint_discovery': grpc.unary_unary_rpc_method_handler(
                    servicer.endpoint_discovery,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=jina__pb2.EndpointsProto.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'jina.JinaDiscoverEndpointsRPC', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class JinaDiscoverEndpointsRPC(object):
    """*
    jina gRPC service to expose Endpoints from Executors.
    """

    @staticmethod
    def endpoint_discovery(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/jina.JinaDiscoverEndpointsRPC/endpoint_discovery',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            jina__pb2.EndpointsProto.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class JinaGatewayDryRunRPCStub(object):
    """*
    jina gRPC service to expose Endpoints from Executors.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.dry_run = channel.unary_unary(
                '/jina.JinaGatewayDryRunRPC/dry_run',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=jina__pb2.StatusProto.FromString,
                )


class JinaGatewayDryRunRPCServicer(object):
    """*
    jina gRPC service to expose Endpoints from Executors.
    """

    def dry_run(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_JinaGatewayDryRunRPCServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'dry_run': grpc.unary_unary_rpc_method_handler(
                    servicer.dry_run,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=jina__pb2.StatusProto.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'jina.JinaGatewayDryRunRPC', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class JinaGatewayDryRunRPC(object):
    """*
    jina gRPC service to expose Endpoints from Executors.
    """

    @staticmethod
    def dry_run(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/jina.JinaGatewayDryRunRPC/dry_run',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            jina__pb2.StatusProto.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class JinaInfoRPCStub(object):
    """*
    jina gRPC service to expose information about running jina version and environment.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self._status = channel.unary_unary(
                '/jina.JinaInfoRPC/_status',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=jina__pb2.JinaInfoProto.FromString,
                )


class JinaInfoRPCServicer(object):
    """*
    jina gRPC service to expose information about running jina version and environment.
    """

    def _status(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_JinaInfoRPCServicer_to_server(servicer, server):
    rpc_method_handlers = {
            '_status': grpc.unary_unary_rpc_method_handler(
                    servicer._status,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=jina__pb2.JinaInfoProto.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'jina.JinaInfoRPC', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class JinaInfoRPC(object):
    """*
    jina gRPC service to expose information about running jina version and environment.
    """

    @staticmethod
    def _status(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/jina.JinaInfoRPC/_status',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            jina__pb2.JinaInfoProto.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
