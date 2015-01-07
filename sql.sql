CREATE TABLE `user` (
  `id`       INT(11)  NOT NULL,
  `email`    CHAR(50) NOT NULL
  COMMENT 'Email',
  `password` CHAR(50) NOT NULL,
  `token`    CHAR(50) NOT NULL,
  `regtime`  INT(11)  NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
)
  ENGINE =InnoDB
  DEFAULT CHARSET =utf8