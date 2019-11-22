# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SensorStartRequestMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import SensorTypeEnum_pb2 as SensorTypeEnum__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='SensorStartRequestMessage.proto',
  package='gb.xxy.trial.proto.messages',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x1fSensorStartRequestMessage.proto\x12\x1bgb.xxy.trial.proto.messages\x1a\x14SensorTypeEnum.proto\"u\n\x19SensorStartRequestMessage\x12>\n\x0bsensor_type\x18\x01 \x02(\x0e\x32).gb.xxy.trial.proto.enums.SensorType.Enum\x12\x18\n\x10refresh_interval\x18\x02 \x02(\x03')
  ,
  dependencies=[SensorTypeEnum__pb2.DESCRIPTOR,])




_SENSORSTARTREQUESTMESSAGE = _descriptor.Descriptor(
  name='SensorStartRequestMessage',
  full_name='gb.xxy.trial.proto.messages.SensorStartRequestMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sensor_type', full_name='gb.xxy.trial.proto.messages.SensorStartRequestMessage.sensor_type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='refresh_interval', full_name='gb.xxy.trial.proto.messages.SensorStartRequestMessage.refresh_interval', index=1,
      number=2, type=3, cpp_type=2, label=2,
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
  serialized_start=86,
  serialized_end=203,
)

_SENSORSTARTREQUESTMESSAGE.fields_by_name['sensor_type'].enum_type = SensorTypeEnum__pb2._SENSORTYPE_ENUM
DESCRIPTOR.message_types_by_name['SensorStartRequestMessage'] = _SENSORSTARTREQUESTMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SensorStartRequestMessage = _reflection.GeneratedProtocolMessageType('SensorStartRequestMessage', (_message.Message,), {
  'DESCRIPTOR' : _SENSORSTARTREQUESTMESSAGE,
  '__module__' : 'SensorStartRequestMessage_pb2'
  # @@protoc_insertion_point(class_scope:gb.xxy.trial.proto.messages.SensorStartRequestMessage)
  })
_sym_db.RegisterMessage(SensorStartRequestMessage)


# @@protoc_insertion_point(module_scope)