
SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for resource
-- ----------------------------
DROP TABLE IF EXISTS `resource`;
CREATE TABLE `resource` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` char(255) NOT NULL DEFAULT '' COMMENT '资源的URL',
  `resource_type` enum('image','pdf','text') NOT NULL DEFAULT 'text' COMMENT '资源的类型',
  `has_crawl` tinyint(1) NOT NULL DEFAULT '0' COMMENT '是否已经抓取0否1是',
  `create_date` int(11) NOT NULL DEFAULT '0' COMMENT '添加的时间',
  `crawl_date` int(11) NOT NULL DEFAULT '0' COMMENT '抓取的时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` char(50) NOT NULL COMMENT 'Email',
  `password` char(50) NOT NULL,
  `token` char(50) NOT NULL,
  `regtime` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for user_resource
-- ----------------------------
DROP TABLE IF EXISTS `user_resource`;
CREATE TABLE `user_resource` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL DEFAULT '0' COMMENT '用户的ID',
  `resource_id` int(11) NOT NULL DEFAULT '0' COMMENT '对应的资源ID',
  `resource_type` enum('image','pdf','text') NOT NULL DEFAULT 'text' COMMENT '资源的类型',
  `url` char(255) NOT NULL DEFAULT '' COMMENT 'URL地址，用空间换速度',
  `create_date` int(11) NOT NULL DEFAULT '0' COMMENT '添加的时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
