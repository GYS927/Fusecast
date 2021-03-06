# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: VideoConfigData.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import VideoResolutionEnum_pb2 as VideoResolutionEnum__pb2
from . import VideoFPSEnum_pb2 as VideoFPSEnum__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='VideoConfigData.proto',
  package='gb.xxy.trial.proto.data',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x15VideoConfigData.proto\x12\x17gb.xxy.trial.proto.data\x1a\x19VideoResolutionEnum.proto\x1a\x12VideoFPSEnum.proto\"\xe7\x01\n\x0bVideoConfig\x12H\n\x10video_resolution\x18\x01 \x02(\x0e\x32..gb.xxy.trial.proto.enums.VideoResolution.Enum\x12:\n\tvideo_fps\x18\x02 \x02(\x0e\x32\'.gb.xxy.trial.proto.enums.VideoFPS.Enum\x12\x14\n\x0cmargin_width\x18\x03 \x02(\r\x12\x15\n\rmargin_height\x18\x04 \x02(\r\x12\x0b\n\x03\x64pi\x18\x05 \x02(\r\x12\x18\n\x10\x61\x64\x64itional_depth\x18\x06 \x01(\r')
  ,
  dependencies=[VideoResolutionEnum__pb2.DESCRIPTOR,VideoFPSEnum__pb2.DESCRIPTOR,])




_VIDEOCONFIG = _descriptor.Descriptor(
  name='VideoConfig',
  full_name='gb.xxy.trial.proto.data.VideoConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='video_resolution', full_name='gb.xxy.trial.proto.data.VideoConfig.video_resolution', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='video_fps', full_name='gb.xxy.trial.proto.data.VideoConfig.video_fps', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='margin_width', full_name='gb.xxy.trial.proto.data.VideoConfig.margin_width', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='margin_height', full_name='gb.xxy.trial.proto.data.VideoConfig.margin_height', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dpi', full_name='gb.xxy.trial.proto.data.VideoConfig.dpi', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='additional_depth', full_name='gb.xxy.trial.proto.data.VideoConfig.additional_depth', index=5,
      number=6, type=13, cpp_type=3, label=1,
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
  serialized_start=98,
  serialized_end=329,
)

_VIDEOCONFIG.fields_by_name['video_resolution'].enum_type = VideoResolutionEnum__pb2._VIDEORESOLUTION_ENUM
_VIDEOCONFIG.fields_by_name['video_fps'].enum_type = VideoFPSEnum__pb2._VIDEOFPS_ENUM
DESCRIPTOR.message_types_by_name['VideoConfig'] = _VIDEOCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VideoConfig = _reflection.GeneratedProtocolMessageType('VideoConfig', (_message.Message,), {
  'DESCRIPTOR' : _VIDEOCONFIG,
  '__module__' : 'VideoConfigData_pb2'
  # @@protoc_insertion_point(class_scope:gb.xxy.trial.proto.data.VideoConfig)
  })
_sym_db.RegisterMessage(VideoConfig)


# @@protoc_insertion_point(module_scope)
