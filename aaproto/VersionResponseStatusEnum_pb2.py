# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: VersionResponseStatusEnum.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='VersionResponseStatusEnum.proto',
  package='gb.xxy.trial.proto.enums',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x1fVersionResponseStatusEnum.proto\x12\x18gb.xxy.trial.proto.enums\":\n\x15VersionResponseStatus\"!\n\x04\x45num\x12\t\n\x05MATCH\x10\x00\x12\x0e\n\x08MISMATCH\x10\xff\xff\x03')
)



_VERSIONRESPONSESTATUS_ENUM = _descriptor.EnumDescriptor(
  name='Enum',
  full_name='gb.xxy.trial.proto.enums.VersionResponseStatus.Enum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MATCH', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISMATCH', index=1, number=65535,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=86,
  serialized_end=119,
)
_sym_db.RegisterEnumDescriptor(_VERSIONRESPONSESTATUS_ENUM)


_VERSIONRESPONSESTATUS = _descriptor.Descriptor(
  name='VersionResponseStatus',
  full_name='gb.xxy.trial.proto.enums.VersionResponseStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _VERSIONRESPONSESTATUS_ENUM,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=61,
  serialized_end=119,
)

_VERSIONRESPONSESTATUS_ENUM.containing_type = _VERSIONRESPONSESTATUS
DESCRIPTOR.message_types_by_name['VersionResponseStatus'] = _VERSIONRESPONSESTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VersionResponseStatus = _reflection.GeneratedProtocolMessageType('VersionResponseStatus', (_message.Message,), {
  'DESCRIPTOR' : _VERSIONRESPONSESTATUS,
  '__module__' : 'VersionResponseStatusEnum_pb2'
  # @@protoc_insertion_point(class_scope:gb.xxy.trial.proto.enums.VersionResponseStatus)
  })
_sym_db.RegisterMessage(VersionResponseStatus)


# @@protoc_insertion_point(module_scope)