# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: svc.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tsvc.proto\x12\x07\x65xample\"\xa4\x01\n\x13MsgDeliveryResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12:\n\x04recv\x18\x02 \x03(\x0b\x32,.example.MsgDeliveryResponse.OperationResult\x1a\x45\n\x0fOperationResult\x12\x11\n\tinterface\x18\x01 \x01(\t\x12\x0e\n\x06result\x18\x02 \x01(\t\x12\x0f\n\x07\x62\x61lance\x18\x03 \x01(\x01\"B\n\x12MsgDeliveryRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x11\n\tinterface\x18\x02 \x01(\t\x12\r\n\x05money\x18\x03 \x01(\x05\"#\n\x0cQueryRequest\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\x05\"1\n\rQueryResponse\x12\x0f\n\x07\x62\x61lance\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\"6\n\x0fWithdrawRequest\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\x05\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x05\"5\n\x0e\x44\x65positRequest\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\x05\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x05\"\x1b\n\x08Response\x12\x0f\n\x07message\x18\x01 \x01(\t\"=\n\x18PropagateWithdrawRequest\x12\x11\n\tbranch_id\x18\x01 \x01(\x05\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x05\"<\n\x17PropagateDepositRequest\x12\x11\n\tbranch_id\x18\x01 \x01(\x05\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x05\"\x1d\n\x07Request\x12\x12\n\nevent_type\x18\x01 \x01(\t2\x90\x03\n\x06\x42ranch\x12\x36\n\x05Query\x12\x15.example.QueryRequest\x1a\x16.example.QueryResponse\x12\x37\n\x08Withdraw\x12\x18.example.WithdrawRequest\x1a\x11.example.Response\x12\x35\n\x07\x44\x65posit\x12\x17.example.DepositRequest\x1a\x11.example.Response\x12H\n\x0bMsgDelivery\x12\x1b.example.MsgDeliveryRequest\x1a\x1c.example.MsgDeliveryResponse\x12J\n\x12Propagate_Withdraw\x12!.example.PropagateWithdrawRequest\x1a\x11.example.Response\x12H\n\x11Propagate_Deposit\x12 .example.PropagateDepositRequest\x1a\x11.example.Responseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'svc_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_MSGDELIVERYRESPONSE']._serialized_start=23
  _globals['_MSGDELIVERYRESPONSE']._serialized_end=187
  _globals['_MSGDELIVERYRESPONSE_OPERATIONRESULT']._serialized_start=118
  _globals['_MSGDELIVERYRESPONSE_OPERATIONRESULT']._serialized_end=187
  _globals['_MSGDELIVERYREQUEST']._serialized_start=189
  _globals['_MSGDELIVERYREQUEST']._serialized_end=255
  _globals['_QUERYREQUEST']._serialized_start=257
  _globals['_QUERYREQUEST']._serialized_end=292
  _globals['_QUERYRESPONSE']._serialized_start=294
  _globals['_QUERYRESPONSE']._serialized_end=343
  _globals['_WITHDRAWREQUEST']._serialized_start=345
  _globals['_WITHDRAWREQUEST']._serialized_end=399
  _globals['_DEPOSITREQUEST']._serialized_start=401
  _globals['_DEPOSITREQUEST']._serialized_end=454
  _globals['_RESPONSE']._serialized_start=456
  _globals['_RESPONSE']._serialized_end=483
  _globals['_PROPAGATEWITHDRAWREQUEST']._serialized_start=485
  _globals['_PROPAGATEWITHDRAWREQUEST']._serialized_end=546
  _globals['_PROPAGATEDEPOSITREQUEST']._serialized_start=548
  _globals['_PROPAGATEDEPOSITREQUEST']._serialized_end=608
  _globals['_REQUEST']._serialized_start=610
  _globals['_REQUEST']._serialized_end=639
  _globals['_BRANCH']._serialized_start=642
  _globals['_BRANCH']._serialized_end=1042
# @@protoc_insertion_point(module_scope)