// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: BlogService.proto

package com.dipper.proto.rpc;

public final class BlogProto {
  private BlogProto() {}
  public static void registerAllExtensions(
      com.google.protobuf.ExtensionRegistryLite registry) {
  }

  public static void registerAllExtensions(
      com.google.protobuf.ExtensionRegistry registry) {
    registerAllExtensions(
        (com.google.protobuf.ExtensionRegistryLite) registry);
  }
  static final com.google.protobuf.Descriptors.Descriptor
    internal_static_com_dipper_proto_rpc_BlogPro_descriptor;
  static final 
    com.google.protobuf.GeneratedMessageV3.FieldAccessorTable
      internal_static_com_dipper_proto_rpc_BlogPro_fieldAccessorTable;

  public static com.google.protobuf.Descriptors.FileDescriptor
      getDescriptor() {
    return descriptor;
  }
  private static  com.google.protobuf.Descriptors.FileDescriptor
      descriptor;
  static {
    java.lang.String[] descriptorData = {
      "\n\021BlogService.proto\022\024com.dipper.proto.rp" +
      "c\"[\n\007BlogPro\022\n\n\002id\030\001 \001(\005\022\017\n\007user_id\030\002 \001(" +
      "\005\022\016\n\006header\030\003 \001(\t\022\017\n\007content\030\004 \001(\t\022\022\n\nbu" +
      "ild_time\030\005 \001(\t2\r\n\013BlogServiceB#\n\024com.dip" +
      "per.proto.rpcB\tBlogProtoP\001b\006proto3"
    };
    descriptor = com.google.protobuf.Descriptors.FileDescriptor
      .internalBuildGeneratedFileFrom(descriptorData,
        new com.google.protobuf.Descriptors.FileDescriptor[] {
        });
    internal_static_com_dipper_proto_rpc_BlogPro_descriptor =
      getDescriptor().getMessageTypes().get(0);
    internal_static_com_dipper_proto_rpc_BlogPro_fieldAccessorTable = new
      com.google.protobuf.GeneratedMessageV3.FieldAccessorTable(
        internal_static_com_dipper_proto_rpc_BlogPro_descriptor,
        new java.lang.String[] { "Id", "UserId", "Header", "Content", "BuildTime", });
  }

  // @@protoc_insertion_point(outer_class_scope)
}