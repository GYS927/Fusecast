# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TouchConfigData.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='TouchConfigData.proto',
  package='gb.xxy.trial.proto.data',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x15TouchConfigData.proto\x12\x17gb.xxy.trial.proto.data\",\n\x0bTouchConfig\x12\r\n\x05width\x18\x01 \x02(\r\x12\x0e\n\x06height\x18\x02 \x02(\r')
)




_TOUCHCONFIG = _descriptor.Descriptor(
  name='TouchConfig',
  full_name='gb.xxy.trial.proto.data.TouchConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='width', full_name='gb.xxy.trial.proto.data.TouchConfig.width', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='gb.xxy.trial.proto.data.TouchConfig.height', index=1,
      number=2, type=13, cpp_type=3, label=2,
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
  serialized_start=50,
  serialized_end=94,
)

DESCRIPTOR.message_types_by_name['TouchConfig'] = _TOUCHCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TouchConfig = _reflection.GeneratedProtocolMessageType('TouchConfig', (_message.Message,), {
  'DESCRIPTOR' : _TOUCHCONFIG,
  '__module__' : 'TouchConfigData_pb2'
  # @@protoc_insertion_point(class_scope:gb.xxy.trial.proto.data.TouchConfig)
  })
_sym_db.RegisterMessage(TouchConfig)


# @@protoc_insertion_point(module_scope)
