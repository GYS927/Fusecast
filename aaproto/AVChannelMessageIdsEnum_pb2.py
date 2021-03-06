# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: AVChannelMessageIdsEnum.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='AVChannelMessageIdsEnum.proto',
  package='gb.xxy.trial.proto.ids',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x1d\x41VChannelMessageIdsEnum.proto\x12\x16gb.xxy.trial.proto.ids\"\xc9\x02\n\x10\x41VChannelMessage\"\xb4\x02\n\x04\x45num\x12&\n\"AV_MEDIA_WITH_TIMESTAMP_INDICATION\x10\x00\x12\x17\n\x13\x41V_MEDIA_INDICATION\x10\x01\x12\x13\n\rSETUP_REQUEST\x10\x80\x80\x02\x12\x16\n\x10START_INDICATION\x10\x81\x80\x02\x12\x15\n\x0fSTOP_INDICATION\x10\x82\x80\x02\x12\x14\n\x0eSETUP_RESPONSE\x10\x83\x80\x02\x12\x1d\n\x17\x41V_MEDIA_ACK_INDICATION\x10\x84\x80\x02\x12\x1b\n\x15\x41V_INPUT_OPEN_REQUEST\x10\x85\x80\x02\x12\x1c\n\x16\x41V_INPUT_OPEN_RESPONSE\x10\x86\x80\x02\x12\x19\n\x13VIDEO_FOCUS_REQUEST\x10\x87\x80\x02\x12\x1c\n\x16VIDEO_FOCUS_INDICATION\x10\x88\x80\x02')
)



_AVCHANNELMESSAGE_ENUM = _descriptor.EnumDescriptor(
  name='Enum',
  full_name='gb.xxy.trial.proto.ids.AVChannelMessage.Enum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='AV_MEDIA_WITH_TIMESTAMP_INDICATION', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AV_MEDIA_INDICATION', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SETUP_REQUEST', index=2, number=32768,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='START_INDICATION', index=3, number=32769,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOP_INDICATION', index=4, number=32770,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SETUP_RESPONSE', index=5, number=32771,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AV_MEDIA_ACK_INDICATION', index=6, number=32772,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AV_INPUT_OPEN_REQUEST', index=7, number=32773,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AV_INPUT_OPEN_RESPONSE', index=8, number=32774,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VIDEO_FOCUS_REQUEST', index=9, number=32775,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VIDEO_FOCUS_INDICATION', index=10, number=32776,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=79,
  serialized_end=387,
)
_sym_db.RegisterEnumDescriptor(_AVCHANNELMESSAGE_ENUM)


_AVCHANNELMESSAGE = _descriptor.Descriptor(
  name='AVChannelMessage',
  full_name='gb.xxy.trial.proto.ids.AVChannelMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _AVCHANNELMESSAGE_ENUM,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=387,
)

_AVCHANNELMESSAGE_ENUM.containing_type = _AVCHANNELMESSAGE
DESCRIPTOR.message_types_by_name['AVChannelMessage'] = _AVCHANNELMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AVChannelMessage = _reflection.GeneratedProtocolMessageType('AVChannelMessage', (_message.Message,), {
  'DESCRIPTOR' : _AVCHANNELMESSAGE,
  '__module__' : 'AVChannelMessageIdsEnum_pb2'
  # @@protoc_insertion_point(class_scope:gb.xxy.trial.proto.ids.AVChannelMessage)
  })
_sym_db.RegisterMessage(AVChannelMessage)


# @@protoc_insertion_point(module_scope)
