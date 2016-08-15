-- MySQL dump 10.13  Distrib 5.5.50, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: StudyGroupNow
-- ------------------------------------------------------
-- Server version	5.5.50-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add permission',3,'add_permission'),(8,'Can change permission',3,'change_permission'),(9,'Can delete permission',3,'delete_permission'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add study group',7,'add_studygroup'),(20,'Can change study group',7,'change_studygroup'),(21,'Can delete study group',7,'delete_studygroup'),(22,'Can add user info',8,'add_userinfo'),(23,'Can change user info',8,'change_userinfo'),(24,'Can delete user info',8,'delete_userinfo'),(25,'Can add location',9,'add_location'),(26,'Can change location',9,'change_location'),(27,'Can delete location',9,'delete_location');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$30000$MRYxFZrYGbuj$wYDGPpRThFfQkWfO+wiysEwGjsTHCL6MJUoML8SVBcQ=','2016-08-11 09:25:01',1,'admin','','','jhall38@uw.edu',1,1,'2016-08-11 09:22:38'),(2,'pbkdf2_sha256$30000$emlr8D5c71Vp$n5eJDbA51PDsuKSU/7utLwkD3HKN5BN0c1kIuSkbtPA=',NULL,0,'test','','','',0,1,'2016-08-11 09:26:51'),(3,'pbkdf2_sha256$30000$KBEQppUOsjdX$sihPv9YcRNPxo1DvOLBWCrVzsR/9xt5LdF8A6Ck70k8=','2016-08-14 22:46:52',1,'admin2','','','jhall38@uw.edu',1,1,'2016-08-14 02:46:39'),(4,'pbkdf2_sha256$30000$5qMUI6ewanzp$uvFgYg9LwnYOqPuz2GeQcn2h4esgDfN6WNwCtAKq978=',NULL,0,'paulypaul','Pauly','Paul','paulypaul@test.com',0,1,'2016-08-14 02:51:35'),(5,'pbkdf2_sha256$30000$Wn0gsHBFwbKv$KPZtYJnhYa7WcM20U7ogdiJit315A/x+OHk313VyRtk=',NULL,0,'bob','','','bobbybob@test.com',0,1,'2016-08-14 12:07:31'),(6,'pbkdf2_sha256$30000$Efqcjdjb2HnX$U+xaa202djFxDdzxDlRm+s/Wc+R3TdyKuTmwGYM7nRo=',NULL,0,'sam','','','sammysam@test.com',0,1,'2016-08-14 12:07:41'),(7,'pbkdf2_sha256$30000$DO0CZlACyx0c$maq8TFOZRi9ctXfOssMzE2YoMPSURlw7Omtnaeqz9iA=',NULL,0,'jim','','','jimmyjim@test.com',0,1,'2016-08-14 12:07:48'),(8,'pbkdf2_sha256$30000$FyRLv8dlfmCQ$oAUgDblI0TTGiSj0Enj2A0x0gHKgf92/oE95X0J0qww=',NULL,0,'sarah','','','sarahysarah@test.com',0,1,'2016-08-14 12:08:04'),(9,'pbkdf2_sha256$30000$yUCjyG3RwFzJ$S84cd+2jAdrSLiukje6zYm9L4fAFSc2oUt0NNsBp2cQ=','2016-08-14 12:15:19',0,'ben','','','',0,1,'2016-08-14 12:14:38'),(10,'2O692o86oz',NULL,0,'craig','','','craiggycraig@test.com',0,1,'2016-08-14 15:49:36'),(11,'testtest',NULL,0,'josh','','','joshyjosh@test.com',0,1,'2016-08-14 15:50:59'),(12,'pbkdf2_sha256$30000$2bmUdwPCUDWj$Rj+QKTN547Wx6rmGOfaii3W5SnPgrGXhj1yOvROJ5g8=','2016-08-14 17:08:46',0,'dfadsfasd','','','fdasfdasf@dsafdas.com',0,1,'2016-08-14 17:08:46'),(13,'pbkdf2_sha256$30000$fQ5GyDYuEPWH$Ux5NjJboun19vJhL8wyNtWFAiqKMWomE2ibn424Ch5I=','2016-08-14 17:12:39',0,'saxodormat','','','sax@doormat.com',0,1,'2016-08-14 17:12:39'),(14,'pbkdf2_sha256$30000$VHgUvKi3Gc2T$IWj1v41IRnddRt46ZrKdTDWcQ7GGNvEPQIjnfS3kEmI=','2016-08-14 17:30:24',0,'saxosax','','','joshhalljoshhalljoshhall@gmail.com',0,1,'2016-08-14 17:30:24'),(15,'pbkdf2_sha256$30000$TS9IRXYmMoeP$GO/QKJjfEKVc9a4K/tSAklTGp8zNelBoe4L0prPTYnM=','2016-08-14 17:35:16',0,'lolbear','','','lolbear@lol.com',0,1,'2016-08-14 17:35:16'),(16,'pbkdf2_sha256$30000$wXRqvLEDLSDq$4z0Ac4R8/yO5TuuH96KU7RGpElthL8StK9FaLgZEAXc=','2016-08-14 20:53:21',0,'bearybear','','','bearybear@bear.com',0,1,'2016-08-14 18:29:56'),(17,'pbkdf2_sha256$30000$hMUwtTyfJwx3$zNdo5zhh/1nLnoboPf7Qb9iTrkNODvshvY3XeRU/3Sk=',NULL,0,'user1','','','',0,1,'2016-08-14 22:47:08'),(18,'pbkdf2_sha256$30000$kQdqnol2U09G$f8eWkr+iYN9YlwJfehvVySQ1GWdaPLNd86EANacgc/M=',NULL,0,'user2','','','',0,1,'2016-08-14 22:47:34'),(19,'pbkdf2_sha256$30000$crRtO6UDuDgN$Sja/Y1Ipx3ZMda2Zf8ez3eOx6ilIQJb6X0FFatJsumk=',NULL,0,'user3','','','',0,1,'2016-08-14 22:47:57'),(20,'pbkdf2_sha256$30000$D3aV6IEzofrK$RqRIR+lI8P66Yn546XrdOVVsQ9GP4CGaDDfo5/A+PcQ=',NULL,0,'user4','','','',0,1,'2016-08-14 22:48:31'),(21,'pbkdf2_sha256$30000$GdaoWAYYQL02$bwPoFNn4QE610ijX7Wa9g48IXCgn8SWqoaupTyDN4vo=',NULL,0,'user5','','','',0,1,'2016-08-14 22:48:54'),(22,'pbkdf2_sha256$30000$FonSeErjX2rB$wFqSzHDxJO0UYki6pMKTat5qZtJrT6y8sHrBy9SrBwM=',NULL,0,'user6','','','',0,1,'2016-08-14 22:49:04'),(23,'pbkdf2_sha256$30000$H67RuqLnq2iK$dfTHoBI1UkKacT93dtUBLCumrOBkHpuwQ+N/32TN1VI=',NULL,0,'user7','','','',0,1,'2016-08-14 22:49:38'),(24,'pbkdf2_sha256$30000$GDCwX1XOR0Ee$9Qg0RANDSa20mg/jMGJAPnj5z5F4nN/uDJOHYEj1MSM=',NULL,0,'user8','','','',0,1,'2016-08-14 22:49:49'),(25,'pbkdf2_sha256$30000$oO6bMBd7lGjw$fChDGlnbkPEoosRcYEcMWNkk4dls7IkUyB6rT6KMPZY=',NULL,0,'user9','','','',0,1,'2016-08-14 22:50:11'),(26,'pbkdf2_sha256$30000$fbmLyBOX2MMD$FAWV/8o36QSP9+QrZHc3sJgNxvAIVLPPFsVCFQDiyQg=',NULL,0,'user10','','','',0,1,'2016-08-14 22:50:24'),(27,'pbkdf2_sha256$30000$zqojEv3dcLQG$OBHgJDtGnKKoBSx9Q5vRuN+4aGmhPa5Pn0xJlYoXSqc=',NULL,0,'user11','','','',0,1,'2016-08-14 22:50:37'),(28,'pbkdf2_sha256$30000$wYRnKTR4WsaM$0dJB38so37wrHGcjL0nMo8GbXLCNPKkq/YYO8KXGQ+U=',NULL,0,'user12','','','',0,1,'2016-08-14 22:51:11'),(29,'pbkdf2_sha256$30000$dNz0swW6H51j$WA977xfL9lMYyxnfDFY84NhteDUrrXnLGyOYFfcvdCY=','2016-08-14 23:36:44',0,'jeffma','','','jeffma@uw.edu',0,1,'2016-08-14 23:36:44');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2016-08-11 09:26:51','2','test',1,'[{\"added\": {}}]',4,1),(2,'2016-08-14 02:51:35','4','paulypaul',1,'[{\"added\": {}}]',4,3),(3,'2016-08-14 02:52:05','4','paulypaul',2,'[{\"changed\": {\"fields\": [\"first_name\", \"last_name\", \"email\"]}}]',4,3),(4,'2016-08-14 02:52:50','1','UserInfo object',1,'[{\"added\": {}}]',8,3),(5,'2016-08-14 02:54:05','1','StudyGroup object',1,'[{\"added\": {}}]',7,3),(6,'2016-08-14 02:57:06','2','StudyGroup object',1,'[{\"added\": {}}]',7,3),(7,'2016-08-14 02:57:44','3','StudyGroup object',1,'[{\"added\": {}}]',7,3),(8,'2016-08-14 11:55:22','3','StudyGroup object',3,'',7,3),(9,'2016-08-14 11:55:26','2','StudyGroup object',3,'',7,3),(10,'2016-08-14 11:55:30','1','StudyGroup object',3,'',7,3),(11,'2016-08-14 12:04:26','1','Location object',1,'[{\"added\": {}}]',9,3),(12,'2016-08-14 12:05:40','2','Location object',1,'[{\"added\": {}}]',9,3),(13,'2016-08-14 12:06:28','3','Location object',1,'[{\"added\": {}}]',9,3),(14,'2016-08-14 12:07:14','4','Location object',1,'[{\"added\": {}}]',9,3),(15,'2016-08-14 12:07:31','5','bob',1,'[{\"added\": {}}]',4,3),(16,'2016-08-14 12:07:41','6','sam',1,'[{\"added\": {}}]',4,3),(17,'2016-08-14 12:07:48','7','jim',1,'[{\"added\": {}}]',4,3),(18,'2016-08-14 12:08:04','8','sarah',1,'[{\"added\": {}}]',4,3),(19,'2016-08-14 12:08:29','8','sarah',2,'[{\"changed\": {\"fields\": [\"email\"]}}]',4,3),(20,'2016-08-14 12:08:39','5','bob',2,'[{\"changed\": {\"fields\": [\"email\"]}}]',4,3),(21,'2016-08-14 12:08:53','7','jim',2,'[{\"changed\": {\"fields\": [\"email\"]}}]',4,3),(22,'2016-08-14 12:09:04','6','sam',2,'[{\"changed\": {\"fields\": [\"email\"]}}]',4,3),(23,'2016-08-14 12:09:52','2','UserInfo object',1,'[{\"added\": {}}]',8,3),(24,'2016-08-14 12:10:12','3','UserInfo object',1,'[{\"added\": {}}]',8,3),(25,'2016-08-14 12:11:55','4','StudyGroup object',1,'[{\"added\": {}}]',7,3),(26,'2016-08-14 12:12:16','5','StudyGroup object',1,'[{\"added\": {}}]',7,3),(27,'2016-08-14 12:13:07','6','StudyGroup object',1,'[{\"added\": {}}]',7,3),(28,'2016-08-14 12:14:38','9','ben',1,'[{\"added\": {}}]',4,3),(29,'2016-08-14 22:47:08','17','user1',1,'[{\"added\": {}}]',4,3),(30,'2016-08-14 22:47:19','17','user1',2,'[]',4,3),(31,'2016-08-14 22:47:34','18','user2',1,'[{\"added\": {}}]',4,3),(32,'2016-08-14 22:47:38','18','user2',2,'[]',4,3),(33,'2016-08-14 22:47:57','19','user3',1,'[{\"added\": {}}]',4,3),(34,'2016-08-14 22:48:31','20','user4',1,'[{\"added\": {}}]',4,3),(35,'2016-08-14 22:48:36','20','user4',2,'[]',4,3),(36,'2016-08-14 22:48:54','21','user5',1,'[{\"added\": {}}]',4,3),(37,'2016-08-14 22:49:04','22','user6',1,'[{\"added\": {}}]',4,3),(38,'2016-08-14 22:49:38','23','user7',1,'[{\"added\": {}}]',4,3),(39,'2016-08-14 22:49:49','24','user8',1,'[{\"added\": {}}]',4,3),(40,'2016-08-14 22:50:11','25','user9',1,'[{\"added\": {}}]',4,3),(41,'2016-08-14 22:50:24','26','user10',1,'[{\"added\": {}}]',4,3),(42,'2016-08-14 22:50:37','27','user11',1,'[{\"added\": {}}]',4,3),(43,'2016-08-14 22:51:11','28','user12',1,'[{\"added\": {}}]',4,3),(44,'2016-08-14 22:52:12','10','Location object',1,'[{\"added\": {}}]',9,3),(45,'2016-08-14 22:53:02','11','Location object',1,'[{\"added\": {}}]',9,3),(46,'2016-08-14 22:54:15','12','Location object',1,'[{\"added\": {}}]',9,3),(47,'2016-08-14 22:55:09','13','Location object',1,'[{\"added\": {}}]',9,3),(48,'2016-08-14 22:56:19','13','StudyGroup object',1,'[{\"added\": {}}]',7,3),(49,'2016-08-14 22:57:07','14','StudyGroup object',1,'[{\"added\": {}}]',7,3),(50,'2016-08-14 22:57:49','15','StudyGroup object',1,'[{\"added\": {}}]',7,3),(51,'2016-08-14 22:58:19','16','StudyGroup object',1,'[{\"added\": {}}]',7,3),(52,'2016-08-14 22:58:46','17','StudyGroup object',1,'[{\"added\": {}}]',7,3);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(2,'auth','group'),(3,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(9,'studygroups','location'),(7,'studygroups','studygroup'),(8,'studygroups','userinfo');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2016-08-11 09:05:22'),(2,'auth','0001_initial','2016-08-11 09:05:23'),(3,'admin','0001_initial','2016-08-11 09:05:23'),(4,'admin','0002_logentry_remove_auto_add','2016-08-11 09:05:23'),(5,'contenttypes','0002_remove_content_type_name','2016-08-11 09:05:23'),(6,'auth','0002_alter_permission_name_max_length','2016-08-11 09:05:23'),(7,'auth','0003_alter_user_email_max_length','2016-08-11 09:05:23'),(8,'auth','0004_alter_user_username_opts','2016-08-11 09:05:23'),(9,'auth','0005_alter_user_last_login_null','2016-08-11 09:05:23'),(10,'auth','0006_require_contenttypes_0002','2016-08-11 09:05:23'),(11,'auth','0007_alter_validators_add_error_messages','2016-08-11 09:05:23'),(12,'auth','0008_alter_user_username_max_length','2016-08-11 09:05:23'),(13,'sessions','0001_initial','2016-08-11 09:05:23'),(14,'studygroups','0001_initial','2016-08-11 09:19:44'),(15,'studygroups','0002_userinfo','2016-08-11 09:34:03'),(16,'studygroups','0003_studygroup_course_code','2016-08-14 02:37:00'),(17,'studygroups','0004_auto_20160814_0454','2016-08-14 11:58:14'),(18,'studygroups','0005_auto_20160814_0457','2016-08-14 11:58:14'),(19,'studygroups','0006_auto_20160814_0458','2016-08-14 11:59:01'),(20,'studygroups','0002_auto_20160814_1306','2016-08-14 20:06:14'),(21,'studygroups','0003_auto_20160814_1643','2016-08-14 23:43:24');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('gvp5lmsnmrcogxdt8u18xvhl0mqsfkqb','NzYzNTg3MmEwYTg2NGNiYTBiYjJiNzEyMGNhMTA1MjMyY2YwNjhlMjp7Il9hdXRoX3VzZXJfaWQiOiIyOSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZGVlMWRkYWIyMjYwYzViZTliMjUyYTI4M2RiMDY5MzkwOTQ3YWU1ZCJ9','2016-08-28 23:36:44'),('mgpd284ifrq4eq8u8xinmfl8joz2a1o2','NzY1ZWM5YWZiMThiOTExNzdjNTQzYjUyYzM3ZmFmZTQ2Mzc3ZDAwYTp7Il9hdXRoX3VzZXJfaGFzaCI6IjY1ZjViMDc4MDY4ODEzZjc4ZTVhYzhjZDA0MGE1ZGFkNmViMzE5NmQiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2016-08-25 09:25:01');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `studygroups_location`
--

DROP TABLE IF EXISTS `studygroups_location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `studygroups_location` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `address` varchar(500) NOT NULL,
  `lat` double NOT NULL,
  `lon` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `studygroups_location`
--

LOCK TABLES `studygroups_location` WRITE;
/*!40000 ALTER TABLE `studygroups_location` DISABLE KEYS */;
INSERT INTO `studygroups_location` VALUES (1,'Marry Gates Hall','Mary Gates Hall, 1851 NE Grant Ln, Seattle, WA 98105',0,0),(2,'Odegaard Library','Odegaard Undergraduate Library, George Washington Lane Northeast, Seattle, WA',0,0),(3,'Suzzallo Library','Suzzallo Library, Seattle, WA',0,0),(4,'The HUB','Husky Union Bldg (HUB), 4001 E Stevens Way NE, Seattle, WA 98195',0,0),(5,'Location','4040 7th ave ne apt 406',0,0),(6,'Location2','4040 7th ave ne apt 406',0,0),(7,'Location3','4040 7th ave ne apt 406',0,0),(8,'Location4','4040 7th ave ne apt 406',0,0),(9,'Location5','4040 7th ave ne apt 406',0,0),(10,'Smith Hall','Smith Hall, Skagit Lane, Seattle, WA',0,0),(11,'Raitt Hall','Raitt Hall (RAI), Chelan Lane, Seattle, WA',0,0),(12,'Savery Hall','Savery Hall (SAV), Chelan Lane, Seattle, WA',0,0),(13,'Clark Hall','Clark Hall, 2103 Alaskan Way, Seattle, WA 98105',0,0),(14,'Joshua Hall\'s Place','4040 7th ave ne apt 406',0,0);
/*!40000 ALTER TABLE `studygroups_location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `studygroups_studygroup`
--

DROP TABLE IF EXISTS `studygroups_studygroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `studygroups_studygroup` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `location_desc` varchar(500) NOT NULL,
  `stat_time` datetime NOT NULL,
  `end_time` datetime NOT NULL,
  `manager_id` int(11) NOT NULL,
  `course_code` varchar(15) NOT NULL,
  `location_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `studygroups_studygroup_manager_id_e4491886_fk_auth_user_id` (`manager_id`),
  KEY `studygroups_studygroup_e274a5da` (`location_id`),
  CONSTRAINT `studygroups_studygroup_manager_id_e4491886_fk_auth_user_id` FOREIGN KEY (`manager_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `studygroups_studygroup`
--

LOCK TABLES `studygroups_studygroup` WRITE;
/*!40000 ALTER TABLE `studygroups_studygroup` DISABLE KEYS */;
INSERT INTO `studygroups_studygroup` VALUES (4,'afdsafasdfads','2016-08-14 12:11:55','2016-08-14 07:00:00',5,'INFO 200',1),(5,'dfasfasd','2016-08-14 12:12:16','2016-08-14 13:00:00',4,'INFO 360',3),(6,'fdafdsa','2016-08-14 12:13:07','2016-08-14 15:12:58',8,'INFO 200',2),(7,'faddas','2016-08-14 14:07:35','2012-12-12 08:12:00',9,'',1),(12,'fafsadfdasfadsfadsf','2016-08-14 20:53:52','2012-12-12 20:12:00',16,'INFO 360',6),(13,'RM 143 Call me at (206) 457-9658','2016-08-14 22:56:19','2016-08-15 00:05:03',19,'CS 142',7),(14,'RM 234','2016-08-14 22:57:07','2016-09-14 07:00:00',28,'INFO 344',1),(15,'In the study hall','2016-08-14 22:57:49','2016-08-15 01:30:00',18,'MATH 152',13),(16,'dkfdaks','2016-08-14 22:58:19','2016-08-14 22:58:10',7,'INFO 199',5),(17,'fadsfas dsfads','2016-08-14 22:58:46','2016-09-14 07:00:00',5,'INFO 200',10);
/*!40000 ALTER TABLE `studygroups_studygroup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `studygroups_userinfo`
--

DROP TABLE IF EXISTS `studygroups_userinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `studygroups_userinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `phone_number` varchar(20) NOT NULL,
  `facebook_link` varchar(200) NOT NULL,
  `nickname` varchar(50) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `studygroups_userinfo_user_id_6f25eb89_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `studygroups_userinfo`
--

LOCK TABLES `studygroups_userinfo` WRITE;
/*!40000 ALTER TABLE `studygroups_userinfo` DISABLE KEYS */;
INSERT INTO `studygroups_userinfo` VALUES (1,'2064579658','www.facebook.com/joshhalljoshhalljoshhall','pauly',4),(2,'2064579658','','bobby',5),(3,'2064579658','','jimmyjim',7);
/*!40000 ALTER TABLE `studygroups_userinfo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-08-16  0:35:16
