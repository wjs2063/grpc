# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0emessages.proto\x12\x07\x65xample\"\"\n\x0b\x43hatMessage\x12\x13\n\x0b\x63hatmessage\x18\x01 \x01(\t2K\n\x0b\x43hatService\x12<\n\nChatStream\x12\x14.example.ChatMessage\x1a\x14.example.ChatMessage\"\x00\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'messages_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CHATMESSAGE']._serialized_start=27
  _globals['_CHATMESSAGE']._serialized_end=61
  _globals['_CHATSERVICE']._serialized_start=63
  _globals['_CHATSERVICE']._serialized_end=138
# @@protoc_insertion_point(module_scope)
