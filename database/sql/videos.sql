/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : PostgreSQL
 Source Server Version : 100007
 Source Host           : localhost:5432
 Source Catalog        : stream
 Source Schema         : public

 Target Server Type    : PostgreSQL
 Target Server Version : 100007
 File Encoding         : 65001

 Date: 19/12/2020 10:53:06
*/


-- ----------------------------
-- Table structure for videos
-- ----------------------------
DROP TABLE IF EXISTS "public"."videos";
CREATE TABLE "public"."videos" (
  "id" char(32) COLLATE "pg_catalog"."default" NOT NULL,
  "name" varchar(128) COLLATE "pg_catalog"."default" NOT NULL,
  "live_id" char(32) COLLATE "pg_catalog"."default" NOT NULL,
  "local_video_path" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "duration" int8 NOT NULL,
  "stage" int2 NOT NULL,
  "segment" bool NOT NULL
)
;
COMMENT ON COLUMN "public"."videos"."id" IS ''主键'';
COMMENT ON COLUMN "public"."videos"."name" IS ''名称'';
COMMENT ON COLUMN "public"."videos"."live_id" IS ''直播id'';
COMMENT ON COLUMN "public"."videos"."local_video_path" IS ''本地存储路径'';
COMMENT ON COLUMN "public"."videos"."duration" IS ''时长'';
COMMENT ON COLUMN "public"."videos"."stage" IS ''分段'';
COMMENT ON COLUMN "public"."videos"."segment" IS ''切分标识（0 未切分 1 已切分）'';

-- ----------------------------
-- Primary Key structure for table videos
-- ----------------------------
ALTER TABLE "public"."videos" ADD CONSTRAINT "live_videos_pkey" PRIMARY KEY ("id");
