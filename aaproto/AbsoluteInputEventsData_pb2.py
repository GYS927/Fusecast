# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: AbsoluteInputEventsData.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import AbsoluteInputEventData_pb2 as AbsoluteInputEventData__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='AbsoluteInputEventsData.proto',
  package='gb.xxy.trial.proto.data',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x1d\x41\x62soluteInputEventsData.proto\x12\x17gb.xxy.trial.proto.data\x1a\x1c\x41\x62soluteInputEventData.proto\"a\n\x13\x41\x62soluteInputEvents\x12J\n\x15\x61\x62solute_input_events\x18\x01 \x03(\x0b\x32+.gb.xxy.trial.proto.data.AbsoluteInputEvent')
  ,
  dependencies=[AbsoluteInputEventData__pb2.DESCRIPTOR,])




_ABSOLUTEINPUTEVENTS = _descriptor.Descriptor(
  name='AbsoluteInputEvents',
  full_name='gb.xxy.trial.proto.data.AbsoluteInputEvents',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='absolute_input_events', full_name='gb.xxy.trial.proto.data.AbsoluteInputEvents.absolute_input_events', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=88,
  serialized_end=185,
)

_ABSOLUTEINPUTEVENTS.fields_by_name['absolute_input_events'].message_type = AbsoluteInputEventData__pb2._ABSOLUTEINPUTEVENT
DESCRIPTOR.message_types_by_name['AbsoluteInputEvents'] = _ABSOLUTEINPUTEVENTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AbsoluteInputEvents = _reflection.GeneratedProtocolMessageType('AbsoluteInputEvents', (_message.Message,), {
  'DESCRIPTOR' : _ABSOLUTEINPUTEVENTS,
  '__module__' : 'AbsoluteInputEventsData_pb2'
  # @@protoc_insertion_point(class_scope:gb.xxy.trial.proto.data.AbsoluteInputEvents)
  })
_sym_db.RegisterMessage(AbsoluteInputEvents)


# @@protoc_insertion_point(module_scope)
