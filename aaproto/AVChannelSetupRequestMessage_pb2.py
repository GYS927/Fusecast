# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: AVChannelSetupRequestMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='AVChannelSetupRequestMessage.proto',
  package='gb.xxy.trial.proto.messages',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\"AVChannelSetupRequestMessage.proto\x12\x1bgb.xxy.trial.proto.messages\"-\n\x15\x41VChannelSetupRequest\x12\x14\n\x0c\x63onfig_index\x18\x01 \x02(\r')
)




_AVCHANNELSETUPREQUEST = _descriptor.Descriptor(
  name='AVChannelSetupRequest',
  full_name='gb.xxy.trial.proto.messages.AVChannelSetupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='config_index', full_name='gb.xxy.trial.proto.messages.AVChannelSetupRequest.config_index', index=0,
      number=1, type=13, cpp_type=3, label=2,
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
  serialized_start=67,
  serialized_end=112,
)

DESCRIPTOR.message_types_by_name['AVChannelSetupRequest'] = _AVCHANNELSETUPREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AVChannelSetupRequest = _reflection.GeneratedProtocolMessageType('AVChannelSetupRequest', (_message.Message,), {
  'DESCRIPTOR' : _AVCHANNELSETUPREQUEST,
  '__module__' : 'AVChannelSetupRequestMessage_pb2'
  # @@protoc_insertion_point(class_scope:gb.xxy.trial.proto.messages.AVChannelSetupRequest)
  })
_sym_db.RegisterMessage(AVChannelSetupRequest)


# @@protoc_insertion_point(module_scope)
