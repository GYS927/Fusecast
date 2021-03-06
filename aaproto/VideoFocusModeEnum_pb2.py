# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: VideoFocusModeEnum.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='VideoFocusModeEnum.proto',
  package='gb.xxy.trial.proto.enums',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x18VideoFocusModeEnum.proto\x12\x18gb.xxy.trial.proto.enums\">\n\x0eVideoFocusMode\",\n\x04\x45num\x12\x08\n\x04NONE\x10\x00\x12\x0b\n\x07\x46OCUSED\x10\x01\x12\r\n\tUNFOCUSED\x10\x02')
)



_VIDEOFOCUSMODE_ENUM = _descriptor.EnumDescriptor(
  name='Enum',
  full_name='gb.xxy.trial.proto.enums.VideoFocusMode.Enum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FOCUSED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNFOCUSED', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=72,
  serialized_end=116,
)
_sym_db.RegisterEnumDescriptor(_VIDEOFOCUSMODE_ENUM)


_VIDEOFOCUSMODE = _descriptor.Descriptor(
  name='VideoFocusMode',
  full_name='gb.xxy.trial.proto.enums.VideoFocusMode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _VIDEOFOCUSMODE_ENUM,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=116,
)

_VIDEOFOCUSMODE_ENUM.containing_type = _VIDEOFOCUSMODE
DESCRIPTOR.message_types_by_name['VideoFocusMode'] = _VIDEOFOCUSMODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VideoFocusMode = _reflection.GeneratedProtocolMessageType('VideoFocusMode', (_message.Message,), {
  'DESCRIPTOR' : _VIDEOFOCUSMODE,
  '__module__' : 'VideoFocusModeEnum_pb2'
  # @@protoc_insertion_point(class_scope:gb.xxy.trial.proto.enums.VideoFocusMode)
  })
_sym_db.RegisterMessage(VideoFocusMode)


# @@protoc_insertion_point(module_scope)
