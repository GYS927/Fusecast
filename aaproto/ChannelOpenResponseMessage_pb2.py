# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ChannelOpenResponseMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import StatusEnum_pb2 as StatusEnum__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ChannelOpenResponseMessage.proto',
  package='gb.xxy.trial.proto.messages',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n ChannelOpenResponseMessage.proto\x12\x1bgb.xxy.trial.proto.messages\x1a\x10StatusEnum.proto\"L\n\x13\x43hannelOpenResponse\x12\x35\n\x06status\x18\x01 \x02(\x0e\x32%.gb.xxy.trial.proto.enums.Status.Enum')
  ,
  dependencies=[StatusEnum__pb2.DESCRIPTOR,])




_CHANNELOPENRESPONSE = _descriptor.Descriptor(
  name='ChannelOpenResponse',
  full_name='gb.xxy.trial.proto.messages.ChannelOpenResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='gb.xxy.trial.proto.messages.ChannelOpenResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=83,
  serialized_end=159,
)

_CHANNELOPENRESPONSE.fields_by_name['status'].enum_type = StatusEnum__pb2._STATUS_ENUM
DESCRIPTOR.message_types_by_name['ChannelOpenResponse'] = _CHANNELOPENRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ChannelOpenResponse = _reflection.GeneratedProtocolMessageType('ChannelOpenResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELOPENRESPONSE,
  '__module__' : 'ChannelOpenResponseMessage_pb2'
  # @@protoc_insertion_point(class_scope:gb.xxy.trial.proto.messages.ChannelOpenResponse)
  })
_sym_db.RegisterMessage(ChannelOpenResponse)


# @@protoc_insertion_point(module_scope)
