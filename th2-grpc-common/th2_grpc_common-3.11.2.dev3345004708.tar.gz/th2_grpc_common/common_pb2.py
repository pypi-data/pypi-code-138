# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: th2_grpc_common/common.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cth2_grpc_common/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1egoogle/protobuf/wrappers.proto\"<\n\x0c\x43onnectionID\x12\x15\n\rsession_alias\x18\x01 \x01(\t\x12\x15\n\rsession_group\x18\x02 \x01(\t\"w\n\tMessageID\x12$\n\rconnection_id\x18\x01 \x01(\x0b\x32\r.ConnectionID\x12\x1d\n\tdirection\x18\x02 \x01(\x0e\x32\n.Direction\x12\x10\n\x08sequence\x18\x03 \x01(\x03\x12\x13\n\x0bsubsequence\x18\x04 \x03(\r\"\xe9\x01\n\x0fMessageMetadata\x12\x16\n\x02id\x18\x01 \x01(\x0b\x32\n.MessageID\x12-\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x14\n\x0cmessage_type\x18\x03 \x01(\t\x12\x34\n\nproperties\x18\x04 \x03(\x0b\x32 .MessageMetadata.PropertiesEntry\x12\x10\n\x08protocol\x18\x05 \x01(\t\x1a\x31\n\x0fPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xd9\x01\n\x12RawMessageMetadata\x12\x16\n\x02id\x18\x01 \x01(\x0b\x32\n.MessageID\x12-\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x37\n\nproperties\x18\x03 \x03(\x0b\x32#.RawMessageMetadata.PropertiesEntry\x12\x10\n\x08protocol\x18\x04 \x01(\t\x1a\x31\n\x0fPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x8e\x01\n\x05Value\x12 \n\nnull_value\x18\x01 \x01(\x0e\x32\n.NullValueH\x00\x12\x16\n\x0csimple_value\x18\x02 \x01(\tH\x00\x12!\n\rmessage_value\x18\x03 \x01(\x0b\x32\x08.MessageH\x00\x12 \n\nlist_value\x18\x04 \x01(\x0b\x32\n.ListValueH\x00\x42\x06\n\x04kind\"#\n\tListValue\x12\x16\n\x06values\x18\x01 \x03(\x0b\x32\x06.Value\"\xad\x01\n\x07Message\x12!\n\x0fparent_event_id\x18\x03 \x01(\x0b\x32\x08.EventID\x12\"\n\x08metadata\x18\x01 \x01(\x0b\x32\x10.MessageMetadata\x12$\n\x06\x66ields\x18\x02 \x03(\x0b\x32\x14.Message.FieldsEntry\x1a\x35\n\x0b\x46ieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x15\n\x05value\x18\x02 \x01(\x0b\x32\x06.Value:\x02\x38\x01\"d\n\nRawMessage\x12!\n\x0fparent_event_id\x18\x03 \x01(\x0b\x32\x08.EventID\x12%\n\x08metadata\x18\x01 \x01(\x0b\x32\x13.RawMessageMetadata\x12\x0c\n\x04\x62ody\x18\x02 \x01(\x0c\"U\n\nAnyMessage\x12\x1b\n\x07message\x18\x01 \x01(\x0b\x32\x08.MessageH\x00\x12\"\n\x0braw_message\x18\x02 \x01(\x0b\x32\x0b.RawMessageH\x00\x42\x06\n\x04kind\"-\n\x0cMessageGroup\x12\x1d\n\x08messages\x18\x01 \x03(\x0b\x32\x0b.AnyMessage\"*\n\x0cMessageBatch\x12\x1a\n\x08messages\x18\x01 \x03(\x0b\x32\x08.Message\"0\n\x0fRawMessageBatch\x12\x1d\n\x08messages\x18\x01 \x03(\x0b\x32\x0b.RawMessage\"2\n\x11MessageGroupBatch\x12\x1d\n\x06groups\x18\x01 \x03(\x0b\x32\r.MessageGroup\"i\n\rRequestStatus\x12%\n\x06status\x18\x01 \x01(\x0e\x32\x15.RequestStatus.Status\x12\x0f\n\x07message\x18\x02 \x01(\t\" \n\x06Status\x12\x0b\n\x07SUCCESS\x10\x00\x12\t\n\x05\x45RROR\x10\x01\"Y\n\x12\x43omparisonSettings\x12\x19\n\rignore_fields\x18\x01 \x03(\tB\x02\x18\x01\x12(\n\x0f\x66\x61il_unexpected\x18\x02 \x01(\x0e\x32\x0f.FailUnexpected\"\xa2\x01\n\x16RootComparisonSettings\x12\x15\n\rignore_fields\x18\x01 \x03(\t\x12#\n\x1b\x63heck_repeating_group_order\x18\x02 \x01(\x08\x12\x31\n\x0etime_precision\x18\x03 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x19\n\x11\x64\x65\x63imal_precision\x18\x04 \x01(\t\"\xf9\x01\n\x0bValueFilter\x12#\n\toperation\x18\x01 \x01(\x0e\x32\x10.FilterOperation\x12\x0b\n\x03key\x18\x02 \x01(\x08\x12\x17\n\rsimple_filter\x18\x03 \x01(\tH\x00\x12(\n\x0emessage_filter\x18\x04 \x01(\x0b\x32\x0e.MessageFilterH\x00\x12\'\n\x0blist_filter\x18\x05 \x01(\x0b\x32\x10.ListValueFilterH\x00\x12\"\n\x0bsimple_list\x18\x06 \x01(\x0b\x32\x0b.SimpleListH\x00\x12 \n\nnull_value\x18\x07 \x01(\x0e\x32\n.NullValueH\x00\x42\x06\n\x04kind\"/\n\x0fListValueFilter\x12\x1c\n\x06values\x18\x01 \x03(\x0b\x32\x0c.ValueFilter\"#\n\nSimpleList\x12\x15\n\rsimple_values\x18\x01 \x03(\t\"\xda\x01\n\rMessageFilter\x12\x17\n\x0bmessageType\x18\x01 \x01(\tB\x02\x18\x01\x12\x15\n\tdirection\x18\x02 \x01(\tB\x02\x18\x01\x12*\n\x06\x66ields\x18\x03 \x03(\x0b\x32\x1a.MessageFilter.FieldsEntry\x12\x30\n\x13\x63omparison_settings\x18\x04 \x01(\x0b\x32\x13.ComparisonSettings\x1a;\n\x0b\x46ieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1b\n\x05value\x18\x02 \x01(\x0b\x32\x0c.ValueFilter:\x02\x38\x01\"\xae\x02\n\x0eMetadataFilter\x12>\n\x10property_filters\x18\x01 \x03(\x0b\x32$.MetadataFilter.PropertyFiltersEntry\x1a\x85\x01\n\x0cSimpleFilter\x12#\n\toperation\x18\x01 \x01(\x0e\x32\x10.FilterOperation\x12\x0b\n\x03key\x18\x02 \x01(\x08\x12\x0f\n\x05value\x18\x03 \x01(\tH\x00\x12\"\n\x0bsimple_list\x18\x04 \x01(\x0b\x32\x0b.SimpleListH\x00\x42\x0e\n\x0c\x66ilter_value\x1aT\n\x14PropertyFiltersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.MetadataFilter.SimpleFilter:\x02\x38\x01\"\xe3\x01\n\x11RootMessageFilter\x12\x13\n\x0bmessageType\x18\x01 \x01(\t\x12&\n\x0emessage_filter\x18\x02 \x01(\x0b\x32\x0e.MessageFilter\x12(\n\x0fmetadata_filter\x18\x03 \x01(\x0b\x32\x0f.MetadataFilter\x12\x34\n\x13\x63omparison_settings\x18\x04 \x01(\x0b\x32\x17.RootComparisonSettings\x12\x31\n\x0b\x64\x65scription\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\xae\x05\n\nCheckpoint\x12\n\n\x02id\x18\x01 \x01(\t\x12\x61\n%session_alias_to_direction_checkpoint\x18\x02 \x03(\x0b\x32\x32.Checkpoint.SessionAliasToDirectionCheckpointEntry\x1ai\n&SessionAliasToDirectionCheckpointEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.Checkpoint.DirectionCheckpoint:\x02\x38\x01\x1aQ\n\x0e\x43heckpointData\x12\x10\n\x08sequence\x18\x01 \x01(\x03\x12-\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x1a\xf2\x02\n\x13\x44irectionCheckpoint\x12[\n\x15\x64irection_to_sequence\x18\x01 \x03(\x0b\x32\x38.Checkpoint.DirectionCheckpoint.DirectionToSequenceEntryB\x02\x18\x01\x12\x64\n\x1c\x64irection_to_checkpoint_data\x18\x02 \x03(\x0b\x32>.Checkpoint.DirectionCheckpoint.DirectionToCheckpointDataEntry\x1a:\n\x18\x44irectionToSequenceEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x1a\\\n\x1e\x44irectionToCheckpointDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x1a.Checkpoint.CheckpointData:\x02\x38\x01\"\x15\n\x07\x45ventID\x12\n\n\x02id\x18\x01 \x01(\t\"\x94\x02\n\x05\x45vent\x12\x14\n\x02id\x18\x01 \x01(\x0b\x32\x08.EventID\x12\x1b\n\tparent_id\x18\x02 \x01(\x0b\x32\x08.EventID\x12\x33\n\x0fstart_timestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\rend_timestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1c\n\x06status\x18\x05 \x01(\x0e\x32\x0c.EventStatus\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x0c\n\x04type\x18\x07 \x01(\t\x12\x0c\n\x04\x62ody\x18\x08 \x01(\x0c\x12(\n\x14\x61ttached_message_ids\x18\t \x03(\x0b\x32\n.MessageID\"G\n\nEventBatch\x12!\n\x0fparent_event_id\x18\x01 \x01(\x0b\x32\x08.EventID\x12\x16\n\x06\x65vents\x18\x02 \x03(\x0b\x32\x06.Event*\"\n\tDirection\x12\t\n\x05\x46IRST\x10\x00\x12\n\n\x06SECOND\x10\x01*\x1b\n\tNullValue\x12\x0e\n\nNULL_VALUE\x10\x00*=\n\x0e\x46\x61ilUnexpected\x12\x06\n\x02NO\x10\x00\x12\n\n\x06\x46IELDS\x10\x01\x12\x17\n\x13\x46IELDS_AND_MESSAGES\x10\x02*\xf2\x01\n\x0f\x46ilterOperation\x12\t\n\x05\x45QUAL\x10\x00\x12\r\n\tNOT_EQUAL\x10\x01\x12\t\n\x05\x45MPTY\x10\x02\x12\r\n\tNOT_EMPTY\x10\x03\x12\x06\n\x02IN\x10\x04\x12\n\n\x06NOT_IN\x10\x05\x12\x08\n\x04LIKE\x10\x06\x12\x0c\n\x08NOT_LIKE\x10\x07\x12\x08\n\x04MORE\x10\x08\x12\x0c\n\x08NOT_MORE\x10\t\x12\x08\n\x04LESS\x10\n\x12\x0c\n\x08NOT_LESS\x10\x0b\x12\x0c\n\x08WILDCARD\x10\x0c\x12\x10\n\x0cNOT_WILDCARD\x10\r\x12\x15\n\x11\x45Q_TIME_PRECISION\x10\x0e\x12\x18\n\x14\x45Q_DECIMAL_PRECISION\x10\x0f*&\n\x0b\x45ventStatus\x12\x0b\n\x07SUCCESS\x10\x00\x12\n\n\x06\x46\x41ILED\x10\x01\x42 \n\x1c\x63om.exactpro.th2.common.grpcP\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'th2_grpc_common.common_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034com.exactpro.th2.common.grpcP\001'
  _MESSAGEMETADATA_PROPERTIESENTRY._options = None
  _MESSAGEMETADATA_PROPERTIESENTRY._serialized_options = b'8\001'
  _RAWMESSAGEMETADATA_PROPERTIESENTRY._options = None
  _RAWMESSAGEMETADATA_PROPERTIESENTRY._serialized_options = b'8\001'
  _MESSAGE_FIELDSENTRY._options = None
  _MESSAGE_FIELDSENTRY._serialized_options = b'8\001'
  _COMPARISONSETTINGS.fields_by_name['ignore_fields']._options = None
  _COMPARISONSETTINGS.fields_by_name['ignore_fields']._serialized_options = b'\030\001'
  _MESSAGEFILTER_FIELDSENTRY._options = None
  _MESSAGEFILTER_FIELDSENTRY._serialized_options = b'8\001'
  _MESSAGEFILTER.fields_by_name['messageType']._options = None
  _MESSAGEFILTER.fields_by_name['messageType']._serialized_options = b'\030\001'
  _MESSAGEFILTER.fields_by_name['direction']._options = None
  _MESSAGEFILTER.fields_by_name['direction']._serialized_options = b'\030\001'
  _METADATAFILTER_PROPERTYFILTERSENTRY._options = None
  _METADATAFILTER_PROPERTYFILTERSENTRY._serialized_options = b'8\001'
  _CHECKPOINT_SESSIONALIASTODIRECTIONCHECKPOINTENTRY._options = None
  _CHECKPOINT_SESSIONALIASTODIRECTIONCHECKPOINTENTRY._serialized_options = b'8\001'
  _CHECKPOINT_DIRECTIONCHECKPOINT_DIRECTIONTOSEQUENCEENTRY._options = None
  _CHECKPOINT_DIRECTIONCHECKPOINT_DIRECTIONTOSEQUENCEENTRY._serialized_options = b'8\001'
  _CHECKPOINT_DIRECTIONCHECKPOINT_DIRECTIONTOCHECKPOINTDATAENTRY._options = None
  _CHECKPOINT_DIRECTIONCHECKPOINT_DIRECTIONTOCHECKPOINTDATAENTRY._serialized_options = b'8\001'
  _CHECKPOINT_DIRECTIONCHECKPOINT.fields_by_name['direction_to_sequence']._options = None
  _CHECKPOINT_DIRECTIONCHECKPOINT.fields_by_name['direction_to_sequence']._serialized_options = b'\030\001'
  _DIRECTION._serialized_start=4029
  _DIRECTION._serialized_end=4063
  _NULLVALUE._serialized_start=4065
  _NULLVALUE._serialized_end=4092
  _FAILUNEXPECTED._serialized_start=4094
  _FAILUNEXPECTED._serialized_end=4155
  _FILTEROPERATION._serialized_start=4158
  _FILTEROPERATION._serialized_end=4400
  _EVENTSTATUS._serialized_start=4402
  _EVENTSTATUS._serialized_end=4440
  _CONNECTIONID._serialized_start=129
  _CONNECTIONID._serialized_end=189
  _MESSAGEID._serialized_start=191
  _MESSAGEID._serialized_end=310
  _MESSAGEMETADATA._serialized_start=313
  _MESSAGEMETADATA._serialized_end=546
  _MESSAGEMETADATA_PROPERTIESENTRY._serialized_start=497
  _MESSAGEMETADATA_PROPERTIESENTRY._serialized_end=546
  _RAWMESSAGEMETADATA._serialized_start=549
  _RAWMESSAGEMETADATA._serialized_end=766
  _RAWMESSAGEMETADATA_PROPERTIESENTRY._serialized_start=497
  _RAWMESSAGEMETADATA_PROPERTIESENTRY._serialized_end=546
  _VALUE._serialized_start=769
  _VALUE._serialized_end=911
  _LISTVALUE._serialized_start=913
  _LISTVALUE._serialized_end=948
  _MESSAGE._serialized_start=951
  _MESSAGE._serialized_end=1124
  _MESSAGE_FIELDSENTRY._serialized_start=1071
  _MESSAGE_FIELDSENTRY._serialized_end=1124
  _RAWMESSAGE._serialized_start=1126
  _RAWMESSAGE._serialized_end=1226
  _ANYMESSAGE._serialized_start=1228
  _ANYMESSAGE._serialized_end=1313
  _MESSAGEGROUP._serialized_start=1315
  _MESSAGEGROUP._serialized_end=1360
  _MESSAGEBATCH._serialized_start=1362
  _MESSAGEBATCH._serialized_end=1404
  _RAWMESSAGEBATCH._serialized_start=1406
  _RAWMESSAGEBATCH._serialized_end=1454
  _MESSAGEGROUPBATCH._serialized_start=1456
  _MESSAGEGROUPBATCH._serialized_end=1506
  _REQUESTSTATUS._serialized_start=1508
  _REQUESTSTATUS._serialized_end=1613
  _REQUESTSTATUS_STATUS._serialized_start=1581
  _REQUESTSTATUS_STATUS._serialized_end=1613
  _COMPARISONSETTINGS._serialized_start=1615
  _COMPARISONSETTINGS._serialized_end=1704
  _ROOTCOMPARISONSETTINGS._serialized_start=1707
  _ROOTCOMPARISONSETTINGS._serialized_end=1869
  _VALUEFILTER._serialized_start=1872
  _VALUEFILTER._serialized_end=2121
  _LISTVALUEFILTER._serialized_start=2123
  _LISTVALUEFILTER._serialized_end=2170
  _SIMPLELIST._serialized_start=2172
  _SIMPLELIST._serialized_end=2207
  _MESSAGEFILTER._serialized_start=2210
  _MESSAGEFILTER._serialized_end=2428
  _MESSAGEFILTER_FIELDSENTRY._serialized_start=2369
  _MESSAGEFILTER_FIELDSENTRY._serialized_end=2428
  _METADATAFILTER._serialized_start=2431
  _METADATAFILTER._serialized_end=2733
  _METADATAFILTER_SIMPLEFILTER._serialized_start=2514
  _METADATAFILTER_SIMPLEFILTER._serialized_end=2647
  _METADATAFILTER_PROPERTYFILTERSENTRY._serialized_start=2649
  _METADATAFILTER_PROPERTYFILTERSENTRY._serialized_end=2733
  _ROOTMESSAGEFILTER._serialized_start=2736
  _ROOTMESSAGEFILTER._serialized_end=2963
  _CHECKPOINT._serialized_start=2966
  _CHECKPOINT._serialized_end=3652
  _CHECKPOINT_SESSIONALIASTODIRECTIONCHECKPOINTENTRY._serialized_start=3091
  _CHECKPOINT_SESSIONALIASTODIRECTIONCHECKPOINTENTRY._serialized_end=3196
  _CHECKPOINT_CHECKPOINTDATA._serialized_start=3198
  _CHECKPOINT_CHECKPOINTDATA._serialized_end=3279
  _CHECKPOINT_DIRECTIONCHECKPOINT._serialized_start=3282
  _CHECKPOINT_DIRECTIONCHECKPOINT._serialized_end=3652
  _CHECKPOINT_DIRECTIONCHECKPOINT_DIRECTIONTOSEQUENCEENTRY._serialized_start=3500
  _CHECKPOINT_DIRECTIONCHECKPOINT_DIRECTIONTOSEQUENCEENTRY._serialized_end=3558
  _CHECKPOINT_DIRECTIONCHECKPOINT_DIRECTIONTOCHECKPOINTDATAENTRY._serialized_start=3560
  _CHECKPOINT_DIRECTIONCHECKPOINT_DIRECTIONTOCHECKPOINTDATAENTRY._serialized_end=3652
  _EVENTID._serialized_start=3654
  _EVENTID._serialized_end=3675
  _EVENT._serialized_start=3678
  _EVENT._serialized_end=3954
  _EVENTBATCH._serialized_start=3956
  _EVENTBATCH._serialized_end=4027
# @@protoc_insertion_point(module_scope)
