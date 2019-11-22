# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ChannelDescriptorData.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import SensorChannelData_pb2 as SensorChannelData__pb2
from . import AVChannelData_pb2 as AVChannelData__pb2
from . import InputChannelData_pb2 as InputChannelData__pb2
from . import AVInputChannelData_pb2 as AVInputChannelData__pb2
from . import BluetoothChannelData_pb2 as BluetoothChannelData__pb2
from . import NavigationChannelData_pb2 as NavigationChannelData__pb2
from . import VendorExtensionChannelData_pb2 as VendorExtensionChannelData__pb2
from . import MediaChannelData_pb2 as MediaChannelData__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ChannelDescriptorData.proto',
  package='gb.xxy.trial.proto.data',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x1b\x43hannelDescriptorData.proto\x12\x17gb.xxy.trial.proto.data\x1a\x17SensorChannelData.proto\x1a\x13\x41VChannelData.proto\x1a\x16InputChannelData.proto\x1a\x18\x41VInputChannelData.proto\x1a\x1a\x42luetoothChannelData.proto\x1a\x1bNavigationChannelData.proto\x1a VendorExtensionChannelData.proto\x1a\x16MediaChannelData.proto\"\xc7\x04\n\x11\x43hannelDescriptor\x12\x12\n\nchannel_id\x18\x01 \x02(\r\x12>\n\x0esensor_channel\x18\x02 \x01(\x0b\x32&.gb.xxy.trial.proto.data.SensorChannel\x12\x36\n\nav_channel\x18\x03 \x01(\x0b\x32\".gb.xxy.trial.proto.data.AVChannel\x12<\n\rinput_channel\x18\x04 \x01(\x0b\x32%.gb.xxy.trial.proto.data.InputChannel\x12\x41\n\x10\x61v_input_channel\x18\x05 \x01(\x0b\x32\'.gb.xxy.trial.proto.data.AVInputChannel\x12\x44\n\x11\x62luetooth_channel\x18\x06 \x01(\x0b\x32).gb.xxy.trial.proto.data.BluetoothChannel\x12\x46\n\x12navigation_channel\x18\x08 \x01(\x0b\x32*.gb.xxy.trial.proto.data.NavigationChannel\x12\x44\n\x11media_infoChannel\x18\t \x01(\x0b\x32).gb.xxy.trial.proto.data.MediaInfoChannel\x12Q\n\x18vendor_extension_channel\x18\x0c \x01(\x0b\x32/.gb.xxy.trial.proto.data.VendorExtensionChannel')
  ,
  dependencies=[SensorChannelData__pb2.DESCRIPTOR,AVChannelData__pb2.DESCRIPTOR,InputChannelData__pb2.DESCRIPTOR,AVInputChannelData__pb2.DESCRIPTOR,BluetoothChannelData__pb2.DESCRIPTOR,NavigationChannelData__pb2.DESCRIPTOR,VendorExtensionChannelData__pb2.DESCRIPTOR,MediaChannelData__pb2.DESCRIPTOR,])




_CHANNELDESCRIPTOR = _descriptor.Descriptor(
  name='ChannelDescriptor',
  full_name='gb.xxy.trial.proto.data.ChannelDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel_id', full_name='gb.xxy.trial.proto.data.ChannelDescriptor.channel_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sensor_channel', full_name='gb.xxy.trial.proto.data.ChannelDescriptor.sensor_channel', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='av_channel', full_name='gb.xxy.trial.proto.data.ChannelDescriptor.av_channel', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='input_channel', full_name='gb.xxy.trial.proto.data.ChannelDescriptor.input_channel', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='av_input_channel', full_name='gb.xxy.trial.proto.data.ChannelDescriptor.av_input_channel', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bluetooth_channel', full_name='gb.xxy.trial.proto.data.ChannelDescriptor.bluetooth_channel', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='navigation_channel', full_name='gb.xxy.trial.proto.data.ChannelDescriptor.navigation_channel', index=6,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='media_infoChannel', full_name='gb.xxy.trial.proto.data.ChannelDescriptor.media_infoChannel', index=7,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vendor_extension_channel', full_name='gb.xxy.trial.proto.data.ChannelDescriptor.vendor_extension_channel', index=8,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=268,
  serialized_end=851,
)

_CHANNELDESCRIPTOR.fields_by_name['sensor_channel'].message_type = SensorChannelData__pb2._SENSORCHANNEL
_CHANNELDESCRIPTOR.fields_by_name['av_channel'].message_type = AVChannelData__pb2._AVCHANNEL
_CHANNELDESCRIPTOR.fields_by_name['input_channel'].message_type = InputChannelData__pb2._INPUTCHANNEL
_CHANNELDESCRIPTOR.fields_by_name['av_input_channel'].message_type = AVInputChannelData__pb2._AVINPUTCHANNEL
_CHANNELDESCRIPTOR.fields_by_name['bluetooth_channel'].message_type = BluetoothChannelData__pb2._BLUETOOTHCHANNEL
_CHANNELDESCRIPTOR.fields_by_name['navigation_channel'].message_type = NavigationChannelData__pb2._NAVIGATIONCHANNEL
_CHANNELDESCRIPTOR.fields_by_name['media_infoChannel'].message_type = MediaChannelData__pb2._MEDIAINFOCHANNEL
_CHANNELDESCRIPTOR.fields_by_name['vendor_extension_channel'].message_type = VendorExtensionChannelData__pb2._VENDOREXTENSIONCHANNEL
DESCRIPTOR.message_types_by_name['ChannelDescriptor'] = _CHANNELDESCRIPTOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ChannelDescriptor = _reflection.GeneratedProtocolMessageType('ChannelDescriptor', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELDESCRIPTOR,
  '__module__' : 'ChannelDescriptorData_pb2'
  # @@protoc_insertion_point(class_scope:gb.xxy.trial.proto.data.ChannelDescriptor)
  })
_sym_db.RegisterMessage(ChannelDescriptor)


# @@protoc_insertion_point(module_scope)
