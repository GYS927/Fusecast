# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: NavigationFocusRequestMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='NavigationFocusRequestMessage.proto',
  package='gb.xxy.trial.proto.messages',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n#NavigationFocusRequestMessage.proto\x12\x1bgb.xxy.trial.proto.messages\"&\n\x16NavigationFocusRequest\x12\x0c\n\x04type\x18\x01 \x02(\r')
)




_NAVIGATIONFOCUSREQUEST = _descriptor.Descriptor(
  name='NavigationFocusRequest',
  full_name='gb.xxy.trial.proto.messages.NavigationFocusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='gb.xxy.trial.proto.messages.NavigationFocusRequest.type', index=0,
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
  serialized_start=68,
  serialized_end=106,
)

DESCRIPTOR.message_types_by_name['NavigationFocusRequest'] = _NAVIGATIONFOCUSREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NavigationFocusRequest = _reflection.GeneratedProtocolMessageType('NavigationFocusRequest', (_message.Message,), {
  'DESCRIPTOR' : _NAVIGATIONFOCUSREQUEST,
  '__module__' : 'NavigationFocusRequestMessage_pb2'
  # @@protoc_insertion_point(class_scope:gb.xxy.trial.proto.messages.NavigationFocusRequest)
  })
_sym_db.RegisterMessage(NavigationFocusRequest)


# @@protoc_insertion_point(module_scope)
