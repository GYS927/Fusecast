# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: AVStreamTypeEnum.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='AVStreamTypeEnum.proto',
  package='gb.xxy.trial.proto.enums',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x16\x41VStreamTypeEnum.proto\x12\x18gb.xxy.trial.proto.enums\"6\n\x0c\x41VStreamType\"&\n\x04\x45num\x12\x08\n\x04NONE\x10\x00\x12\t\n\x05\x41UDIO\x10\x01\x12\t\n\x05VIDEO\x10\x03')
)



_AVSTREAMTYPE_ENUM = _descriptor.EnumDescriptor(
  name='Enum',
  full_name='gb.xxy.trial.proto.enums.AVStreamType.Enum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUDIO', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VIDEO', index=2, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=68,
  serialized_end=106,
)
_sym_db.RegisterEnumDescriptor(_AVSTREAMTYPE_ENUM)


_AVSTREAMTYPE = _descriptor.Descriptor(
  name='AVStreamType',
  full_name='gb.xxy.trial.proto.enums.AVStreamType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _AVSTREAMTYPE_ENUM,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=52,
  serialized_end=106,
)

_AVSTREAMTYPE_ENUM.containing_type = _AVSTREAMTYPE
DESCRIPTOR.message_types_by_name['AVStreamType'] = _AVSTREAMTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AVStreamType = _reflection.GeneratedProtocolMessageType('AVStreamType', (_message.Message,), {
  'DESCRIPTOR' : _AVSTREAMTYPE,
  '__module__' : 'AVStreamTypeEnum_pb2'
  # @@protoc_insertion_point(class_scope:gb.xxy.trial.proto.enums.AVStreamType)
  })
_sym_db.RegisterMessage(AVStreamType)


# @@protoc_insertion_point(module_scope)