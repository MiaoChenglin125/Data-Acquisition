# Host: 127.0.0.1  (Version 5.7.16-log)
# Date: 2021-10-28 16:24:48
# Generator: MySQL-Front 5.4  (Build 3.52)
# Internet: http://www.mysqlfront.de/

/*!40101 SET NAMES utf8 */;

#
# Structure for table "admit_data"
#

DROP TABLE IF EXISTS `admit_data`;
CREATE TABLE `admit_data` (
  `Id` int(11) AUTO_INCREMENT,
  `graduate_school` varchar(255) DEFAULT NULL,
  `graduate_major` varchar(255) DEFAULT NULL,
  `undergraduate_school` varchar(255) DEFAULT NULL,
  `undergraduate_major` varchar(255) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  `background` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=414 DEFAULT CHARSET=utf8;

#
# Data for table "admit_data"
#

INSERT INTO `admit_data` VALUES (1,"熊本大学2022秋季政府奖学金硕博项目申请信息（接受方大学推荐途径） ","同济大学外事办公室","2021-12-31","申请领域：理工类，计算机科学与电信工学","https://fao.tongji.edu.cn/a6/ed/c4111a239341/page.htm","熊本,大学,2022,");
