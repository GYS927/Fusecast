# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: AVChannelStopIndicationMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='AVChannelStopIndicationMessage.proto',
  package='gb.xxy.trial.proto.messages',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n$AVChannelStopIndicationMessage.proto\x12\x1bgb.xxy.trial.proto.messages\"\x19\n\x17\x41VChannelStopIndication')
)




_AVCHANNELSTOPINDICATION = _descriptor.Descriptor(
  name='AVChannelStopIndication',
  full_name='gb.xxy.trial.proto.messages.AVChannelStopIndication',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=69,
  serialized_end=94,
)

DESCRIPTOR.message_types_by_name['AVChannelStopIndication'] = _AVCHANNELSTOPINDICATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AVChannelStopIndication = _reflection.GeneratedProtocolMessageType('AVChannelStopIndication', (_message.Message,), {
  'DESCRIPTOR' : _AVCHANNELSTOPINDICATION,
  '__module__' : 'AVChannelStopIndicationMessage_pb2'
  # @@protoc_insertion_point(class_scope:gb.xxy.trial.proto.messages.AVChannelStopIndication)
  })
_sym_db.RegisterMessage(AVChannelStopIndication)


# @@protoc_insertion_point(module_scope)
