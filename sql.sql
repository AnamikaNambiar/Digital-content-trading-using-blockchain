/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 8.0.31 : Database - dctb
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`dctb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `dctb`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add complaint',7,'add_complaint'),(20,'Can change complaint',7,'change_complaint'),(21,'Can delete complaint',7,'delete_complaint'),(22,'Can add feedback',8,'add_feedback'),(23,'Can change feedback',8,'change_feedback'),(24,'Can delete feedback',8,'delete_feedback'),(25,'Can add image',9,'add_image'),(26,'Can change image',9,'change_image'),(27,'Can delete image',9,'delete_image'),(28,'Can add login',10,'add_login'),(29,'Can change login',10,'change_login'),(30,'Can delete login',10,'delete_login'),(31,'Can add request',11,'add_request'),(32,'Can change request',11,'change_request'),(33,'Can delete request',11,'delete_request'),(34,'Can add user',12,'add_user'),(35,'Can change user',12,'change_user'),(36,'Can delete user',12,'delete_user'),(37,'Can add file',13,'add_file'),(38,'Can change file',13,'change_file'),(39,'Can delete file',13,'delete_file');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `dctbapp_complaint` */

DROP TABLE IF EXISTS `dctbapp_complaint`;

CREATE TABLE `dctbapp_complaint` (
  `id` int NOT NULL AUTO_INCREMENT,
  `complaint` varchar(200) NOT NULL,
  `c_date` varchar(200) NOT NULL,
  `reply` varchar(200) NOT NULL,
  `r_date` varchar(200) NOT NULL,
  `USER_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `dctbapp_complaint_USER_id_b23573e2` (`USER_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `dctbapp_complaint` */

insert  into `dctbapp_complaint`(`id`,`complaint`,`c_date`,`reply`,`r_date`,`USER_id`) values (1,'dggf','dfg','dffg','sdf',1),(2,'asdfghjkiuytrewq','31/01/2024-15:44:14','pending','',4);

/*Table structure for table `dctbapp_feedback` */

DROP TABLE IF EXISTS `dctbapp_feedback`;

CREATE TABLE `dctbapp_feedback` (
  `id` int NOT NULL AUTO_INCREMENT,
  `feedback` varchar(200) NOT NULL,
  `date` varchar(200) NOT NULL,
  `USER_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `dctbapp_feedback_USER_id_e4fbe625` (`USER_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `dctbapp_feedback` */

insert  into `dctbapp_feedback`(`id`,`feedback`,`date`,`USER_id`) values (1,'sdfg','sdfg',1),(2,'dnbvdk','31/01/2024-15:50:59',4);

/*Table structure for table `dctbapp_file` */

DROP TABLE IF EXISTS `dctbapp_file`;

CREATE TABLE `dctbapp_file` (
  `id` int NOT NULL AUTO_INCREMENT,
  `image` varchar(200) NOT NULL,
  `date` varchar(200) NOT NULL,
  `type` varchar(200) NOT NULL,
  `USER_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `dctbapp_file_USER_id_3c895cbb` (`USER_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `dctbapp_file` */

insert  into `dctbapp_file`(`id`,`image`,`date`,`type`,`USER_id`) values (1,'/static/img/20240131-112130post.jpg','31/01/2024-11:21:30','img',3),(2,'/static/img/20240131-121741post.jpg','31/01/2024-12:17:41','img',1),(3,'/static/img/20240131-121919post.jpg','31/01/2024-12:19:19','img',1),(4,'/static/img/20240131-122558post.jpg','31/01/2024-12:25:58','img',1),(5,'/static/img/20240131-124127post.jpg','31/01/2024-12:41:27','img',4),(6,'/static/img/20240131-124135post.jpg','31/01/2024-12:41:35','img',4);

/*Table structure for table `dctbapp_login` */

DROP TABLE IF EXISTS `dctbapp_login`;

CREATE TABLE `dctbapp_login` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  `usertype` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `dctbapp_login` */

insert  into `dctbapp_login`(`id`,`username`,`password`,`usertype`) values (1,'admin','123','admin'),(2,'usr','111','user'),(3,'assd','123','user'),(4,'asd','321','user'),(5,'aks','222','user');

/*Table structure for table `dctbapp_request` */

DROP TABLE IF EXISTS `dctbapp_request`;

CREATE TABLE `dctbapp_request` (
  `id` int NOT NULL AUTO_INCREMENT,
  `status` varchar(200) NOT NULL,
  `date` varchar(200) NOT NULL,
  `USER_id` int NOT NULL,
  `FILE_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `dctbapp_request_USER_id_f907e6f5` (`USER_id`),
  KEY `dctbapp_request_FILE_id_369070db` (`FILE_id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `dctbapp_request` */

insert  into `dctbapp_request`(`id`,`status`,`date`,`USER_id`,`FILE_id`) values (1,'pending','20240131-132216',4,3),(2,'approved','20240131-132545',4,5),(3,'pending','20240131-132555',4,1),(4,'pending','20240131-140954',4,1),(5,'pending','20240131-141001',4,2),(6,'approved','20240131-141005',4,5),(7,'pending','20240131-142503',4,1),(8,'pending','31/01/2024-14:38:04',4,1),(9,'pending','31/01/2024-14:38:29',4,3),(10,'rejected','31/01/2024-14:39:13',1,5);

/*Table structure for table `dctbapp_user` */

DROP TABLE IF EXISTS `dctbapp_user`;

CREATE TABLE `dctbapp_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(200) NOT NULL,
  `photo` varchar(500) NOT NULL,
  `contacts` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `LOGIN_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `dctbapp_user_LOGIN_id_f227b819` (`LOGIN_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `dctbapp_user` */

insert  into `dctbapp_user`(`id`,`username`,`photo`,`contacts`,`email`,`LOGIN_id`) values (1,'ffvefv','htmjm','tyhtyj','ryjuj6u',2),(2,'assd','/static/img/20240127-143244.jpg','e234','sdfg',3),(3,'asd','/static/img/20240131-103759.jpg','12345678','ahs@gmail.com',4),(4,'aks','/static/img/20240131-124058.jpg','345678','asdfgh@gmail.com',5);

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values (1,'admin','logentry'),(2,'auth','permission'),(3,'auth','group'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(7,'dctbapp','complaint'),(8,'dctbapp','feedback'),(9,'dctbapp','image'),(10,'dctbapp','login'),(11,'dctbapp','request'),(12,'dctbapp','user'),(13,'dctbapp','file');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (1,'contenttypes','0001_initial','2023-12-01 07:28:48.841507'),(2,'auth','0001_initial','2023-12-01 07:28:49.404203'),(3,'admin','0001_initial','2023-12-01 07:28:49.557698'),(4,'admin','0002_logentry_remove_auto_add','2023-12-01 07:28:49.567836'),(5,'contenttypes','0002_remove_content_type_name','2023-12-01 07:28:49.642859'),(6,'auth','0002_alter_permission_name_max_length','2023-12-01 07:28:49.676365'),(7,'auth','0003_alter_user_email_max_length','2023-12-01 07:28:49.728443'),(8,'auth','0004_alter_user_username_opts','2023-12-01 07:28:49.738206'),(9,'auth','0005_alter_user_last_login_null','2023-12-01 07:28:49.777711'),(10,'auth','0006_require_contenttypes_0002','2023-12-01 07:28:49.779860'),(11,'auth','0007_alter_validators_add_error_messages','2023-12-01 07:28:49.788260'),(12,'auth','0008_alter_user_username_max_length','2023-12-01 07:28:49.827961'),(13,'auth','0009_alter_user_last_name_max_length','2023-12-01 07:28:49.867579'),(14,'dctbapp','0001_initial','2023-12-01 07:28:50.421358'),(15,'sessions','0001_initial','2023-12-01 07:28:50.468830'),(16,'dctbapp','0002_auto_20240131_1045','2024-01-31 05:15:39.889418');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values ('6uvgzjghspkcfy46xni8lxixoc1p3sw6','YzkwNDU3YzMyZWZjNmYzOWY2MDc4ZTIwMDBmMWFiYWI5MTAyNmI1Yzp7ImxpZCI6MX0=','2023-12-25 05:50:17.312614'),('zgrv3359jja9hha40b0duyl8viofxgtc','MmZkMzA5YTVlODg4YzU3ZWMzYTNlZTUzN2UyYWE2MGE5OTU2MWMzYjp7ImxpZCI6M30=','2024-02-10 09:07:09.899793'),('3auimj55cfy2sp01ji3to2poitbneixr','YmFhNGI2ZTMyNDQyMzNmNGZiYWFhMjM5MGNlYzZmMDgyYTNkNmY3ZTp7ImxpZCI6NX0=','2024-02-14 10:33:53.474582');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
