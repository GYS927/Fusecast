# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: AudioTypeEnum.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='AudioTypeEnum.proto',
  package='gb.xxy.trial.proto.enums',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x13\x41udioTypeEnum.proto\x12\x18gb.xxy.trial.proto.enums\"K\n\tAudioType\">\n\x04\x45num\x12\x08\n\x04NONE\x10\x00\x12\n\n\x06SPEECH\x10\x01\x12\n\n\x06SYSTEM\x10\x02\x12\t\n\x05MEDIA\x10\x03\x12\t\n\x05\x41LARM\x10\x04')
)



_AUDIOTYPE_ENUM = _descriptor.EnumDescriptor(
  name='Enum',
  full_name='gb.xxy.trial.proto.enums.AudioType.Enum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPEECH', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYSTEM', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MEDIA', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALARM', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=62,
  serialized_end=124,
)
_sym_db.RegisterEnumDescriptor(_AUDIOTYPE_ENUM)


_AUDIOTYPE = _descriptor.Descriptor(
  name='AudioType',
  full_name='gb.xxy.trial.proto.enums.AudioType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _AUDIOTYPE_ENUM,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=49,
  serialized_end=124,
)

_AUDIOTYPE_ENUM.containing_type = _AUDIOTYPE
DESCRIPTOR.message_types_by_name['AudioType'] = _AUDIOTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AudioType = _reflection.GeneratedProtocolMessageType('AudioType', (_message.Message,), {
  'DESCRIPTOR' : _AUDIOTYPE,
  '__module__' : 'AudioTypeEnum_pb2'
  # @@protoc_insertion_point(class_scope:gb.xxy.trial.proto.enums.AudioType)
  })
_sym_db.RegisterMessage(AudioType)


# @@protoc_insertion_point(module_scope)
