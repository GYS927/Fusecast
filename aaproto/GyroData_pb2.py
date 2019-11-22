# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GyroData.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='GyroData.proto',
  package='gb.xxy.trial.proto.data',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x0eGyroData.proto\x12\x17gb.xxy.trial.proto.data\"T\n\x04Gyro\x12\x18\n\x10rotation_speed_x\x18\x01 \x02(\x05\x12\x18\n\x10rotation_speed_y\x18\x02 \x02(\x05\x12\x18\n\x10rotation_speed_z\x18\x03 \x02(\x05')
)




_GYRO = _descriptor.Descriptor(
  name='Gyro',
  full_name='gb.xxy.trial.proto.data.Gyro',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rotation_speed_x', full_name='gb.xxy.trial.proto.data.Gyro.rotation_speed_x', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rotation_speed_y', full_name='gb.xxy.trial.proto.data.Gyro.rotation_speed_y', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rotation_speed_z', full_name='gb.xxy.trial.proto.data.Gyro.rotation_speed_z', index=2,
      number=3, type=5, cpp_type=1, label=2,
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
  serialized_start=43,
  serialized_end=127,
)

DESCRIPTOR.message_types_by_name['Gyro'] = _GYRO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Gyro = _reflection.GeneratedProtocolMessageType('Gyro', (_message.Message,), {
  'DESCRIPTOR' : _GYRO,
  '__module__' : 'GyroData_pb2'
  # @@protoc_insertion_point(class_scope:gb.xxy.trial.proto.data.Gyro)
  })
_sym_db.RegisterMessage(Gyro)


# @@protoc_insertion_point(module_scope)
