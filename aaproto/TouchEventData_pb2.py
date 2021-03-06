# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TouchEventData.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import TouchLocationData_pb2 as TouchLocationData__pb2
from . import TouchActionEnum_pb2 as TouchActionEnum__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='TouchEventData.proto',
  package='gb.xxy.trial.proto.data',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x14TouchEventData.proto\x12\x17gb.xxy.trial.proto.data\x1a\x17TouchLocationData.proto\x1a\x15TouchActionEnum.proto\"\xa4\x01\n\nTouchEvent\x12>\n\x0etouch_location\x18\x01 \x03(\x0b\x32&.gb.xxy.trial.proto.data.TouchLocation\x12\x14\n\x0c\x61\x63tion_index\x18\x02 \x02(\r\x12@\n\x0ctouch_action\x18\x03 \x02(\x0e\x32*.gb.xxy.trial.proto.enums.TouchAction.Enum')
  ,
  dependencies=[TouchLocationData__pb2.DESCRIPTOR,TouchActionEnum__pb2.DESCRIPTOR,])




_TOUCHEVENT = _descriptor.Descriptor(
  name='TouchEvent',
  full_name='gb.xxy.trial.proto.data.TouchEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='touch_location', full_name='gb.xxy.trial.proto.data.TouchEvent.touch_location', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action_index', full_name='gb.xxy.trial.proto.data.TouchEvent.action_index', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='touch_action', full_name='gb.xxy.trial.proto.data.TouchEvent.touch_action', index=2,
      number=3, type=14, cpp_type=8, label=2,
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
  serialized_end=262,
)

_TOUCHEVENT.fields_by_name['touch_location'].message_type = TouchLocationData__pb2._TOUCHLOCATION
_TOUCHEVENT.fields_by_name['touch_action'].enum_type = TouchActionEnum__pb2._TOUCHACTION_ENUM
DESCRIPTOR.message_types_by_name['TouchEvent'] = _TOUCHEVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TouchEvent = _reflection.GeneratedProtocolMessageType('TouchEvent', (_message.Message,), {
  'DESCRIPTOR' : _TOUCHEVENT,
  '__module__' : 'TouchEventData_pb2'
  # @@protoc_insertion_point(class_scope:gb.xxy.trial.proto.data.TouchEvent)
  })
_sym_db.RegisterMessage(TouchEvent)


# @@protoc_insertion_point(module_scope)
