# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TouchLocationData.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='TouchLocationData.proto',
  package='gb.xxy.trial.proto.data',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x17TouchLocationData.proto\x12\x17gb.xxy.trial.proto.data\"9\n\rTouchLocation\x12\t\n\x01x\x18\x01 \x02(\r\x12\t\n\x01y\x18\x02 \x02(\r\x12\x12\n\npointer_id\x18\x03 \x02(\r')
)




_TOUCHLOCATION = _descriptor.Descriptor(
  name='TouchLocation',
  full_name='gb.xxy.trial.proto.data.TouchLocation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='gb.xxy.trial.proto.data.TouchLocation.x', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='gb.xxy.trial.proto.data.TouchLocation.y', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pointer_id', full_name='gb.xxy.trial.proto.data.TouchLocation.pointer_id', index=2,
      number=3, type=13, cpp_type=3, label=2,
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
  serialized_start=52,
  serialized_end=109,
)

DESCRIPTOR.message_types_by_name['TouchLocation'] = _TOUCHLOCATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TouchLocation = _reflection.GeneratedProtocolMessageType('TouchLocation', (_message.Message,), {
  'DESCRIPTOR' : _TOUCHLOCATION,
  '__module__' : 'TouchLocationData_pb2'
  # @@protoc_insertion_point(class_scope:gb.xxy.trial.proto.data.TouchLocation)
  })
_sym_db.RegisterMessage(TouchLocation)


# @@protoc_insertion_point(module_scope)
