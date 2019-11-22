# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GearData.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import GearEnum_pb2 as GearEnum__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='GearData.proto',
  package='gb.xxy.trial.proto.data',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x0eGearData.proto\x12\x17gb.xxy.trial.proto.data\x1a\x0eGearEnum.proto\"9\n\x04Gear\x12\x31\n\x04gear\x18\x01 \x02(\x0e\x32#.gb.xxy.trial.proto.enums.Gear.Enum')
  ,
  dependencies=[GearEnum__pb2.DESCRIPTOR,])




_GEAR = _descriptor.Descriptor(
  name='Gear',
  full_name='gb.xxy.trial.proto.data.Gear',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gear', full_name='gb.xxy.trial.proto.data.Gear.gear', index=0,
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
  serialized_start=59,
  serialized_end=116,
)

_GEAR.fields_by_name['gear'].enum_type = GearEnum__pb2._GEAR_ENUM
DESCRIPTOR.message_types_by_name['Gear'] = _GEAR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Gear = _reflection.GeneratedProtocolMessageType('Gear', (_message.Message,), {
  'DESCRIPTOR' : _GEAR,
  '__module__' : 'GearData_pb2'
  # @@protoc_insertion_point(class_scope:gb.xxy.trial.proto.data.Gear)
  })
_sym_db.RegisterMessage(Gear)


# @@protoc_insertion_point(module_scope)
