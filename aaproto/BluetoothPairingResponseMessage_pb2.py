# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: BluetoothPairingResponseMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import BluetoothPairingStatusEnum_pb2 as BluetoothPairingStatusEnum__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='BluetoothPairingResponseMessage.proto',
  package='gb.xxy.trial.proto.messages',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n%BluetoothPairingResponseMessage.proto\x12\x1bgb.xxy.trial.proto.messages\x1a BluetoothPairingStatusEnum.proto\"y\n\x18\x42luetoothPairingResponse\x12\x16\n\x0e\x61lready_paired\x18\x01 \x02(\x08\x12\x45\n\x06status\x18\x02 \x02(\x0e\x32\x35.gb.xxy.trial.proto.enums.BluetoothPairingStatus.Enum')
  ,
  dependencies=[BluetoothPairingStatusEnum__pb2.DESCRIPTOR,])




_BLUETOOTHPAIRINGRESPONSE = _descriptor.Descriptor(
  name='BluetoothPairingResponse',
  full_name='gb.xxy.trial.proto.messages.BluetoothPairingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='already_paired', full_name='gb.xxy.trial.proto.messages.BluetoothPairingResponse.already_paired', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='gb.xxy.trial.proto.messages.BluetoothPairingResponse.status', index=1,
      number=2, type=14, cpp_type=8, label=2,
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
  serialized_start=104,
  serialized_end=225,
)

_BLUETOOTHPAIRINGRESPONSE.fields_by_name['status'].enum_type = BluetoothPairingStatusEnum__pb2._BLUETOOTHPAIRINGSTATUS_ENUM
DESCRIPTOR.message_types_by_name['BluetoothPairingResponse'] = _BLUETOOTHPAIRINGRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BluetoothPairingResponse = _reflection.GeneratedProtocolMessageType('BluetoothPairingResponse', (_message.Message,), {
  'DESCRIPTOR' : _BLUETOOTHPAIRINGRESPONSE,
  '__module__' : 'BluetoothPairingResponseMessage_pb2'
  # @@protoc_insertion_point(class_scope:gb.xxy.trial.proto.messages.BluetoothPairingResponse)
  })
_sym_db.RegisterMessage(BluetoothPairingResponse)


# @@protoc_insertion_point(module_scope)
