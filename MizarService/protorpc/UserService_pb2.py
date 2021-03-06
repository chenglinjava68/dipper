# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: UserService.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='UserService.proto',
  package='com.dipper.proto.rpc',
  syntax='proto3',
  serialized_options=b'\n\024com.dipper.proto.rpcB\tUserProtoP\001',
  serialized_pb=b'\n\x11UserService.proto\x12\x14\x63om.dipper.proto.rpc\"\xbd\x01\n\x07UserPro\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x11\n\tuser_name\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\x12\x11\n\tnick_name\x18\x04 \x01(\t\x12\x0e\n\x06gender\x18\x05 \x01(\x05\x12\x0e\n\x06\x61vatar\x18\x06 \x01(\t\x12\r\n\x05\x65mail\x18\x07 \x01(\t\x12\r\n\x05phone\x18\x08 \x01(\t\x12\x11\n\trole_code\x18\t \x01(\t\x12\x0f\n\x07version\x18\n \x01(\t\x12\x0c\n\x04sign\x18\x0b \x01(\t2\r\n\x0bUserServiceB#\n\x14\x63om.dipper.proto.rpcB\tUserProtoP\x01\x62\x06proto3'
)




_USERPRO = _descriptor.Descriptor(
  name='UserPro',
  full_name='com.dipper.proto.rpc.UserPro',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='com.dipper.proto.rpc.UserPro.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='com.dipper.proto.rpc.UserPro.user_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='com.dipper.proto.rpc.UserPro.password', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nick_name', full_name='com.dipper.proto.rpc.UserPro.nick_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gender', full_name='com.dipper.proto.rpc.UserPro.gender', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='avatar', full_name='com.dipper.proto.rpc.UserPro.avatar', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='com.dipper.proto.rpc.UserPro.email', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='phone', full_name='com.dipper.proto.rpc.UserPro.phone', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='role_code', full_name='com.dipper.proto.rpc.UserPro.role_code', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='com.dipper.proto.rpc.UserPro.version', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sign', full_name='com.dipper.proto.rpc.UserPro.sign', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=44,
  serialized_end=233,
)

DESCRIPTOR.message_types_by_name['UserPro'] = _USERPRO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserPro = _reflection.GeneratedProtocolMessageType('UserPro', (_message.Message,), {
  'DESCRIPTOR' : _USERPRO,
  '__module__' : 'UserService_pb2'
  # @@protoc_insertion_point(class_scope:com.dipper.proto.rpc.UserPro)
  })
_sym_db.RegisterMessage(UserPro)


DESCRIPTOR._options = None

_USERSERVICE = _descriptor.ServiceDescriptor(
  name='UserService',
  full_name='com.dipper.proto.rpc.UserService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=235,
  serialized_end=248,
  methods=[
])
_sym_db.RegisterServiceDescriptor(_USERSERVICE)

DESCRIPTOR.services_by_name['UserService'] = _USERSERVICE

# @@protoc_insertion_point(module_scope)
