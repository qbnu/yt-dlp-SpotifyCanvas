# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: canvas.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x63\x61nvas.proto\"3\n\x06\x41rtist\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06\x61vatar\x18\x03 \x01(\t\"\xb5\x02\n\x14\x45ntityCanvazResponse\x12.\n\x08\x63\x61nvases\x18\x01 \x03(\x0b\x32\x1c.EntityCanvazResponse.Canvaz\x12\x16\n\x0ettl_in_seconds\x18\x02 \x01(\x03\x1a\xd4\x01\n\x06\x43\x61nvaz\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x0f\n\x07\x66ile_id\x18\x03 \x01(\t\x12\x13\n\x04type\x18\x04 \x01(\x0e\x32\x05.Type\x12\x12\n\nentity_uri\x18\x05 \x01(\t\x12\x17\n\x06\x61rtist\x18\x06 \x01(\x0b\x32\x07.Artist\x12\x10\n\x08\x65xplicit\x18\x07 \x01(\x08\x12\x13\n\x0buploaded_by\x18\x08 \x01(\t\x12\x0c\n\x04\x65tag\x18\t \x01(\t\x12\x12\n\ncanvas_uri\x18\x0b \x01(\t\x12\x15\n\rstorylines_id\x18\x0c \x01(\t\"p\n\x13\x45ntityCanvazRequest\x12-\n\x08\x65ntities\x18\x01 \x03(\x0b\x32\x1b.EntityCanvazRequest.Entity\x1a*\n\x06\x45ntity\x12\x12\n\nentity_uri\x18\x01 \x01(\t\x12\x0c\n\x04\x65tag\x18\x02 \x01(\t*R\n\x04Type\x12\t\n\x05IMAGE\x10\x00\x12\t\n\x05VIDEO\x10\x01\x12\x11\n\rVIDEO_LOOPING\x10\x02\x12\x18\n\x14VIDEO_LOOPING_RANDOM\x10\x03\x12\x07\n\x03GIF\x10\x04\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'canvas_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TYPE._serialized_start=495
  _TYPE._serialized_end=577
  _ARTIST._serialized_start=16
  _ARTIST._serialized_end=67
  _ENTITYCANVAZRESPONSE._serialized_start=70
  _ENTITYCANVAZRESPONSE._serialized_end=379
  _ENTITYCANVAZRESPONSE_CANVAZ._serialized_start=167
  _ENTITYCANVAZRESPONSE_CANVAZ._serialized_end=379
  _ENTITYCANVAZREQUEST._serialized_start=381
  _ENTITYCANVAZREQUEST._serialized_end=493
  _ENTITYCANVAZREQUEST_ENTITY._serialized_start=451
  _ENTITYCANVAZREQUEST_ENTITY._serialized_end=493
# @@protoc_insertion_point(module_scope)