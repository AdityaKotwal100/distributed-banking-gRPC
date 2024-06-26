# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import svc_pb2 as svc__pb2


class BranchStub(object):
    """Define the Branch service
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Query = channel.unary_unary(
                '/example.Branch/Query',
                request_serializer=svc__pb2.QueryRequest.SerializeToString,
                response_deserializer=svc__pb2.QueryResponse.FromString,
                )
        self.Withdraw = channel.unary_unary(
                '/example.Branch/Withdraw',
                request_serializer=svc__pb2.WithdrawRequest.SerializeToString,
                response_deserializer=svc__pb2.Response.FromString,
                )
        self.Deposit = channel.unary_unary(
                '/example.Branch/Deposit',
                request_serializer=svc__pb2.DepositRequest.SerializeToString,
                response_deserializer=svc__pb2.Response.FromString,
                )
        self.MsgDelivery = channel.unary_unary(
                '/example.Branch/MsgDelivery',
                request_serializer=svc__pb2.MsgDeliveryRequest.SerializeToString,
                response_deserializer=svc__pb2.MsgDeliveryResponse.FromString,
                )
        self.Propagate_Withdraw = channel.unary_unary(
                '/example.Branch/Propagate_Withdraw',
                request_serializer=svc__pb2.PropagateWithdrawRequest.SerializeToString,
                response_deserializer=svc__pb2.Response.FromString,
                )
        self.Propagate_Deposit = channel.unary_unary(
                '/example.Branch/Propagate_Deposit',
                request_serializer=svc__pb2.PropagateDepositRequest.SerializeToString,
                response_deserializer=svc__pb2.Response.FromString,
                )


class BranchServicer(object):
    """Define the Branch service
    """

    def Query(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Withdraw(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Deposit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MsgDelivery(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Propagate_Withdraw(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Propagate_Deposit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BranchServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Query': grpc.unary_unary_rpc_method_handler(
                    servicer.Query,
                    request_deserializer=svc__pb2.QueryRequest.FromString,
                    response_serializer=svc__pb2.QueryResponse.SerializeToString,
            ),
            'Withdraw': grpc.unary_unary_rpc_method_handler(
                    servicer.Withdraw,
                    request_deserializer=svc__pb2.WithdrawRequest.FromString,
                    response_serializer=svc__pb2.Response.SerializeToString,
            ),
            'Deposit': grpc.unary_unary_rpc_method_handler(
                    servicer.Deposit,
                    request_deserializer=svc__pb2.DepositRequest.FromString,
                    response_serializer=svc__pb2.Response.SerializeToString,
            ),
            'MsgDelivery': grpc.unary_unary_rpc_method_handler(
                    servicer.MsgDelivery,
                    request_deserializer=svc__pb2.MsgDeliveryRequest.FromString,
                    response_serializer=svc__pb2.MsgDeliveryResponse.SerializeToString,
            ),
            'Propagate_Withdraw': grpc.unary_unary_rpc_method_handler(
                    servicer.Propagate_Withdraw,
                    request_deserializer=svc__pb2.PropagateWithdrawRequest.FromString,
                    response_serializer=svc__pb2.Response.SerializeToString,
            ),
            'Propagate_Deposit': grpc.unary_unary_rpc_method_handler(
                    servicer.Propagate_Deposit,
                    request_deserializer=svc__pb2.PropagateDepositRequest.FromString,
                    response_serializer=svc__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'example.Branch', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Branch(object):
    """Define the Branch service
    """

    @staticmethod
    def Query(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/example.Branch/Query',
            svc__pb2.QueryRequest.SerializeToString,
            svc__pb2.QueryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Withdraw(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/example.Branch/Withdraw',
            svc__pb2.WithdrawRequest.SerializeToString,
            svc__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Deposit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/example.Branch/Deposit',
            svc__pb2.DepositRequest.SerializeToString,
            svc__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MsgDelivery(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/example.Branch/MsgDelivery',
            svc__pb2.MsgDeliveryRequest.SerializeToString,
            svc__pb2.MsgDeliveryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Propagate_Withdraw(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/example.Branch/Propagate_Withdraw',
            svc__pb2.PropagateWithdrawRequest.SerializeToString,
            svc__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Propagate_Deposit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/example.Branch/Propagate_Deposit',
            svc__pb2.PropagateDepositRequest.SerializeToString,
            svc__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
