# Host: 127.0.0.1  (Version 5.7.16-log)
# Date: 2021-10-28 16:24:48
# Generator: MySQL-Front 5.4  (Build 3.52)
# Internet: http://www.mysqlfront.de/

/*!40101 SET NAMES utf8 */;

#
# Structure for table "guanchazhe"
#

DROP TABLE IF EXISTS `guanchazhe`;
CREATE TABLE `guanchazhe` (
  `Id` int(11) AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `author` varchar(255) DEFAULT NULL,
  `publish_time` varchar(255) DEFAULT NULL,
  `content` longtext,
  `url` varchar(255) DEFAULT NULL,
  `key_word` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=414 DEFAULT CHARSET=utf8;

#
# Data for table "guanchazhe"
#

INSERT INTO `guanchazhe` VALUES (1,"熊本大学2022秋季政府奖学金硕博项目申请信息（接受方大学推荐途径） ","同济大学外事办公室","2021-12-31","申请领域：理工类，计算机科学与电信工学申请期限：2022年1月6日-1月28日注意事项：1）如申请材料无法在2022年1月28日16:00前寄到熊本大学，先发送电子版到指定邮箱2）提交申请前须自行联系熊本大学指导老师并获得接收认可详细及申请：-University Recommendation (in the field of Science and Technology)https://prsf.kumamoto-u.ac.jp/public/osHkgALGUI-A19UBP299Ldn-HB6_puBN887jRrQ5i7SH-Special Allocation in the field of Computer Science and Electrical Engineeringhttps://prsf.kumamoto-u.ac.jp/public/fsrwgArGEc-AGtIB5N19MaH-fsO-Pxe0gUhmyOEF6W1aPW：Mext2022以下网站将于2022年1月6日更新：https://www.fast.kumamoto-u.ac.jp/gsst-en/admissions/- MEXT Scholarship Application for Admission in October 20221. University Recommendation (in the field of Science and Technology)2. Special Allocation in the field of Computer Science and Electrical Engineering","https://fao.tongji.edu.cn/a6/ed/c4111a239341/page.htm","熊本,大学,2022,");
