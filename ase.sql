-- MySQL dump 10.13  Distrib 5.7.24, for Linux (x86_64)
--
-- Host: localhost    Database: ase
-- ------------------------------------------------------
-- Server version	5.7.24-0ubuntu0.18.04.1

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
-- Table structure for table `Department`
--

DROP TABLE IF EXISTS `Department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Department` (
  `Department_Id` int(11) NOT NULL,
  `Department_Name` varchar(45) NOT NULL,
  `Department_Head_Position` varchar(45) NOT NULL,
  `Department_Head_Emp_Id` int(11) NOT NULL,
  `Department_IsFaculty` binary(1) DEFAULT NULL,
  PRIMARY KEY (`Department_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Department`
--

LOCK TABLES `Department` WRITE;
/*!40000 ALTER TABLE `Department` DISABLE KEYS */;
INSERT INTO `Department` VALUES (1,'Computer Science Engineering','faculty advisor',12345,_binary '1'),(2,'Electronics and Communication Engineering','faculty advisor',12344,_binary '1');
/*!40000 ALTER TABLE `Department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `academic_batch`
--

DROP TABLE IF EXISTS `academic_batch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `academic_batch` (
  `Academic_Batch_Id` int(11) NOT NULL,
  `Academic_Batch_Number` int(11) NOT NULL,
  `Academic_Batch_Degree` int(11) NOT NULL,
  `Academic_Batch_Start_Year` varchar(4) NOT NULL,
  `Academic_Batch_End_Year` varchar(4) NOT NULL,
  PRIMARY KEY (`Academic_Batch_Id`),
  KEY `Academic_Batch_Degree` (`Academic_Batch_Degree`),
  CONSTRAINT `academic_batch_ibfk_1` FOREIGN KEY (`Academic_Batch_Degree`) REFERENCES `academic_degree` (`Academic_Degree_Id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `academic_batch`
--

LOCK TABLES `academic_batch` WRITE;
/*!40000 ALTER TABLE `academic_batch` DISABLE KEYS */;
INSERT INTO `academic_batch` VALUES (1,1,1,'2013','2017'),(2,2,1,'2014','2018'),(3,3,1,'2015','2019'),(4,4,1,'2016','2020'),(5,5,1,'2017','2021'),(6,1,2,'2013','2015');
/*!40000 ALTER TABLE `academic_batch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `academic_course`
--

DROP TABLE IF EXISTS `academic_course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `academic_course` (
  `Academic_Course_Id` int(11) NOT NULL,
  `Academic_Course_Name` varchar(45) NOT NULL,
  `Academic_Course_Rigour` varchar(2) NOT NULL,
  `Academic_Course_Level` int(11) NOT NULL,
  `Academic_Course_Pre_Req` binary(1) NOT NULL,
  `Academic_Course_Delivery_Mode` int(11) NOT NULL,
  `Academic_Course_Description` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`Academic_Course_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `academic_course`
--

LOCK TABLES `academic_course` WRITE;
/*!40000 ALTER TABLE `academic_course` DISABLE KEYS */;
INSERT INTO `academic_course` VALUES (1,'ASE2','NO',1,_binary '0',1,NULL),(2,'TOC','NO',2,_binary '0',2,NULL),(3,'DIGICOMM','NO',3,_binary '0',3,NULL),(4,'EMT','NO',4,_binary '0',4,NULL),(5,'IR','NO',5,_binary '0',5,NULL),(6,'DM','NO',6,_binary '1',6,NULL),(7,'DIP','NO',7,_binary '1',7,NULL),(8,'IOT','NO',8,_binary '0',8,NULL),(9,'CSD','NO',9,_binary '1',9,NULL),(10,'VLSI','NO',10,_binary '1',10,NULL),(11,'PC','NO',0,_binary '0',11,NULL),(12,'DMPT','NO',0,_binary '0',12,NULL),(13,'OC','NO',0,_binary '0',13,NULL),(14,'DEC','NO',0,_binary '0',14,NULL),(15,'Comm Skills-1','NO',1,_binary '0',15,NULL),(16,'OS','NO',0,_binary '0',16,NULL),(17,'ASE','NO',1,_binary '0',17,NULL),(18,'maths-3','NO',3,_binary '0',18,NULL),(19,'Comm skills-3','NO',2,_binary '0',19,NULL),(20,'Algo','NO',0,_binary '0',20,NULL),(21,'DSAA','NO',0,_binary '0',21,NULL),(22,'LS','NO',0,_binary '0',22,NULL),(23,'GE','NO',0,_binary '0',23,NULL),(24,'APS','NO',0,_binary '0',24,NULL),(25,'SDS','NO',0,_binary '0',25,NULL),(26,'DE','NO',0,_binary '0',26,NULL),(27,'YW','NO',0,_binary '0',27,NULL),(28,'EIS','NO',4,_binary '0',28,NULL),(29,'ASE1','NO',4,_binary '0',29,NULL),(30,'DS','NO',4,_binary '0',30,NULL),(31,'CO','NO',4,_binary '0',31,NULL),(32,'BEC','NO',4,_binary '0',32,NULL),(33,'FCOMM','NO',4,_binary '0',33,NULL),(34,'AI','NO',4,_binary '0',34,NULL),(35,'DBMS','NO',4,_binary '0',35,NULL),(36,'LEC','NO',4,_binary '0',36,NULL),(37,'DSP','NO',4,_binary '0',37,NULL),(38,'CV','NO',4,_binary '0',38,NULL),(39,'BTP','NO',4,_binary '0',39,NULL),(40,'HONORS','NO',4,_binary '0',40,NULL);
/*!40000 ALTER TABLE `academic_course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `academic_degree`
--

DROP TABLE IF EXISTS `academic_degree`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `academic_degree` (
  `Academic_Degree_Id` int(11) NOT NULL,
  `Academic_Degree_Name` varchar(45) DEFAULT NULL,
  `Academic_Degree_Start_Year` varchar(4) DEFAULT NULL,
  `Academic_Degree_Duration` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`Academic_Degree_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `academic_degree`
--

LOCK TABLES `academic_degree` WRITE;
/*!40000 ALTER TABLE `academic_degree` DISABLE KEYS */;
INSERT INTO `academic_degree` VALUES (1,'Btech','2016','4'),(2,'Ms','2013','2'),(3,'Honours','2014','4'),(4,'Phd','2015','2');
/*!40000 ALTER TABLE `academic_degree` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `academic_prog_batch_sem_course`
--

DROP TABLE IF EXISTS `academic_prog_batch_sem_course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `academic_prog_batch_sem_course` (
  `Academic_Prog_Batch_Sem_Course_Id` int(11) NOT NULL,
  `Academic_Prog_Batch_Sem_Course_Batch_Id` int(11) NOT NULL,
  `Academic_Prog_Batch_Sem_Course_Sem_Num` int(11) NOT NULL,
  `Academic_Prog_Batch_Sem_Course` int(11) NOT NULL,
  `Academic_Prog_Batch_Sem_Course_Credits` int(11) DEFAULT NULL,
  `Academic_Prog_Batch_Sem_Course_Curr_Year` varchar(4) DEFAULT NULL,
  `Academic_Prog_Batch_Sem_Course_Eval_Code` varchar(20) DEFAULT NULL,
  `Academic_Prog_Batch_Sem_Course_Status` varchar(45) DEFAULT NULL,
  `Academic_Prog_Batch_Sem_Course_Type` int(11) DEFAULT NULL,
  `Academic_Prog_Batch_Sem_Course_Faculty` int(11) DEFAULT NULL,
  `Academic_Prog_Batch_Sem_Course_Max` int(11) DEFAULT NULL,
  PRIMARY KEY (`Academic_Prog_Batch_Sem_Course_Id`),
  KEY `Academic_Prog_Batch_Sem_Course_Batch_Id` (`Academic_Prog_Batch_Sem_Course_Batch_Id`),
  KEY `Academic_Prog_Batch_Sem_Course` (`Academic_Prog_Batch_Sem_Course`),
  KEY `Academic_Prog_Batch_Sem_Course_Type` (`Academic_Prog_Batch_Sem_Course_Type`),
  KEY `Academic_Prog_Batch_Sem_Course_Faculty` (`Academic_Prog_Batch_Sem_Course_Faculty`),
  CONSTRAINT `academic_prog_batch_sem_course_ibfk_1` FOREIGN KEY (`Academic_Prog_Batch_Sem_Course_Batch_Id`) REFERENCES `academic_batch` (`Academic_Batch_Id`),
  CONSTRAINT `academic_prog_batch_sem_course_ibfk_2` FOREIGN KEY (`Academic_Prog_Batch_Sem_Course`) REFERENCES `academic_course` (`Academic_Course_Id`),
  CONSTRAINT `academic_prog_batch_sem_course_ibfk_3` FOREIGN KEY (`Academic_Prog_Batch_Sem_Course_Type`) REFERENCES `dept_type` (`id`),
  CONSTRAINT `academic_prog_batch_sem_course_ibfk_4` FOREIGN KEY (`Academic_Prog_Batch_Sem_Course_Faculty`) REFERENCES `employee` (`Employee_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `academic_prog_batch_sem_course`
--

LOCK TABLES `academic_prog_batch_sem_course` WRITE;
/*!40000 ALTER TABLE `academic_prog_batch_sem_course` DISABLE KEYS */;
INSERT INTO `academic_prog_batch_sem_course` VALUES (1,2,5,1,4,'2018',NULL,NULL,7,9,5),(2,2,5,2,4,'2018',NULL,NULL,5,10,5),(3,2,5,3,4,'2018',NULL,NULL,6,11,30),(4,4,5,4,4,'2018',NULL,NULL,2,14,60),(5,4,5,5,4,'2018',NULL,NULL,1,1,60),(6,4,5,7,4,'2018',NULL,NULL,4,8,100),(7,4,5,22,2,'2018',NULL,NULL,10,9,100),(8,4,5,25,4,'2018',NULL,NULL,8,2,100),(9,4,5,23,2,'2018',NULL,NULL,10,9,50),(10,4,2,12,4,'2018',NULL,NULL,8,8,100);
/*!40000 ALTER TABLE `academic_prog_batch_sem_course` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session');
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$120000$mzKX3JLWiq0J$QJnzx3KR+jYr1+1xpYKwUrXLymSJCehEow3NxrmZGOc=','2018-10-18 02:51:41.956148',1,'admin','','','',1,1,'2018-10-18 02:40:57.920985');
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
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `course_acad_perf_eval`
--

DROP TABLE IF EXISTS `course_acad_perf_eval`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `course_acad_perf_eval` (
  `Course_Acad_Perf_Eval_Id` int(11) NOT NULL,
  `Course_Acad_Perf_Eval_Std_Sem_Cou_ID` int(11) NOT NULL,
  `Course_Academic_Performance_Weightage` int(11) NOT NULL,
  PRIMARY KEY (`Course_Acad_Perf_Eval_Id`),
  KEY `Course_Acad_Perf_Eval_Std_Sem_Cou_ID` (`Course_Acad_Perf_Eval_Std_Sem_Cou_ID`),
  CONSTRAINT `course_acad_perf_eval_ibfk_1` FOREIGN KEY (`Course_Acad_Perf_Eval_Std_Sem_Cou_ID`) REFERENCES `student_sem_course_reg` (`Student_Sem_Course_Reg_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course_acad_perf_eval`
--

LOCK TABLES `course_acad_perf_eval` WRITE;
/*!40000 ALTER TABLE `course_acad_perf_eval` DISABLE KEYS */;
/*!40000 ALTER TABLE `course_acad_perf_eval` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dept_type`
--

DROP TABLE IF EXISTS `dept_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dept_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `credits` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dept_type`
--

LOCK TABLES `dept_type` WRITE;
/*!40000 ALTER TABLE `dept_type` DISABLE KEYS */;
INSERT INTO `dept_type` VALUES (1,'cse bouquet',12),(2,'ece bouquet',12),(4,'IT Elective',16),(5,'cse core',NULL),(6,'ece core',NULL),(7,'common core',NULL),(8,'Math Elective',8),(9,'humanities',8),(10,'Science Elective',4),(11,'free electives',12),(12,'honors',16),(13,'BTP',8);
/*!40000 ALTER TABLE `dept_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
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
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');
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
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-10-18 02:35:26.570959'),(2,'auth','0001_initial','2018-10-18 02:35:31.410946'),(3,'admin','0001_initial','2018-10-18 02:35:33.071906'),(4,'admin','0002_logentry_remove_auto_add','2018-10-18 02:35:33.513303'),(5,'admin','0003_logentry_add_action_flag_choices','2018-10-18 02:35:33.932428'),(6,'contenttypes','0002_remove_content_type_name','2018-10-18 02:35:34.831358'),(7,'auth','0002_alter_permission_name_max_length','2018-10-18 02:35:35.311272'),(8,'auth','0003_alter_user_email_max_length','2018-10-18 02:35:35.811172'),(9,'auth','0004_alter_user_username_opts','2018-10-18 02:35:36.230810'),(10,'auth','0005_alter_user_last_login_null','2018-10-18 02:35:36.753268'),(11,'auth','0006_require_contenttypes_0002','2018-10-18 02:35:37.153224'),(12,'auth','0007_alter_validators_add_error_messages','2018-10-18 02:35:37.684944'),(13,'auth','0008_alter_user_username_max_length','2018-10-18 02:35:38.191947'),(14,'auth','0009_alter_user_last_name_max_length','2018-10-18 02:35:38.793558'),(15,'sessions','0001_initial','2018-10-18 02:35:39.734072');
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
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('xtfpmjl4pw2yov6cz1hyuiy3nkplk53e','ZDZmYjllNjM3NzQ3ZGRlYzg4ZjU2NWI5NDY3YzYyOGI3YTRjMDM4NDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5MGZlY2FmOTJlOTMxZTVmNmI2ZjBiMzliYjgwNzE3ZWQ4NTExODg5In0=','2018-11-01 02:51:42.273808');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employee` (
  `Employee_Id` int(11) NOT NULL,
  `Employee_Reg_No` varchar(45) NOT NULL,
  `Employee_First_Name` varchar(45) NOT NULL,
  `Employee_Second_Name` varchar(100) DEFAULT NULL,
  `Employee_Last_Name` varchar(45) DEFAULT NULL,
  `Employee_Name_for_Email` varchar(60) DEFAULT NULL,
  `Employee_Dept` int(11) NOT NULL,
  `Employee_DOJ` date NOT NULL,
  `Employee_Manager` int(11) DEFAULT NULL,
  `Employee_Password` binary(32) DEFAULT '5c16439f353ebe3b555e15ca7f13612b',
  PRIMARY KEY (`Employee_Id`),
  UNIQUE KEY `Employee_Reg_No` (`Employee_Reg_No`),
  KEY `Employee_Dept` (`Employee_Dept`),
  KEY `Employee_Manager` (`Employee_Manager`),
  CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`Employee_Dept`) REFERENCES `Department` (`Department_Id`),
  CONSTRAINT `employee_ibfk_2` FOREIGN KEY (`Employee_Manager`) REFERENCES `employee` (`Employee_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (1,'12345','venaktesh','vinayak','Rao','venkatesh.v@iiits.in',1,'2018-07-07',NULL,_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0'),(2,'12344','Mainak',NULL,'Thakur','mainak.t@iiits.in',1,'2018-07-07',NULL,_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0'),(3,'12354','Paul',NULL,'Braineard','ebpaul@iiits.in',2,'2018-07-07',NULL,_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0'),(4,'12355','Rajendra',NULL,'Prasanth','rajendra.prasath@iiits.in',1,'2018-07-07',NULL,_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0'),(5,'12365','Rangeet',NULL,'mitra','rangeet.mitra@iiits.in',2,'2018-07-07',NULL,_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0'),(6,'12366','Shiv','Ram','Dubey','srdubey@iiits.in',1,'2018-07-07',NULL,_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0'),(7,'12376','Sivaprasad',NULL,'Kotamraju','siva.k@iiits.in',2,'2018-07-07',NULL,_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0'),(8,'12377','Snehasis',NULL,'Mukherjee','snehasis.mukherjee@iiits.in',1,'2018-07-07',NULL,_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0'),(9,'12387','Uma',NULL,'Garimella','uma.garimella@iiits.in',1,'2018-07-07',NULL,_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0'),(10,'12342','vishwanath',NULL,'P','viswanath.p@iiits.in',1,'2018-07-07',NULL,_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0'),(11,'12343','Krishna','Chaitanya',NULL,'krishnachaitanya.a@iiits.in',2,'2018-07-07',NULL,_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0'),(12,'12346','Raja','vara','prasad','yrv.prasad@iiits.in',2,'2018-07-07',NULL,_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0'),(13,'12347','Hrishikesh','venkataraman','NULL','hvraman@iiits.in',1,'2018-07-07',NULL,_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0'),(14,'12348','Divya','Brahmam','NULL','divyabramham.k@iiits.in',2,'2018-07-07',NULL,_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `faculty_adv_batch`
--

DROP TABLE IF EXISTS `faculty_adv_batch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `faculty_adv_batch` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `batch` int(11) DEFAULT NULL,
  `emp_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `emp_id` (`emp_id`),
  KEY `batch` (`batch`),
  CONSTRAINT `faculty_adv_batch_ibfk_2` FOREIGN KEY (`emp_id`) REFERENCES `employee` (`Employee_Id`),
  CONSTRAINT `faculty_adv_batch_ibfk_3` FOREIGN KEY (`batch`) REFERENCES `academic_batch` (`Academic_Batch_Id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `faculty_adv_batch`
--

LOCK TABLES `faculty_adv_batch` WRITE;
/*!40000 ALTER TABLE `faculty_adv_batch` DISABLE KEYS */;
INSERT INTO `faculty_adv_batch` VALUES (5,4,1),(7,4,6),(9,5,9),(10,4,2);
/*!40000 ALTER TABLE `faculty_adv_batch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `posts`
--

DROP TABLE IF EXISTS `posts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `posts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `matter` text,
  `dt` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `posts`
--

LOCK TABLES `posts` WRITE;
/*!40000 ALTER TABLE `posts` DISABLE KEYS */;
INSERT INTO `posts` VALUES (17,'<p>The course Registration Starts at 10AM and ends at 5PM</p>\r\n','2018-11-16 06:50:07'),(18,'<p>Students will be sent the respective links to register</p>\r\n','2018-11-16 06:50:07'),(19,'Today there is no class','2018-11-16 06:50:07'),(20,'ASE project - 1','2018-11-16 06:50:07'),(21,'<p>There should be a max of 24 credits</p>\r\n','2018-11-16 06:50:07'),(25,'Students opting for honors must consult the F.A','2018-11-16 16:58:49');
/*!40000 ALTER TABLE `posts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prediction`
--

DROP TABLE IF EXISTS `prediction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `prediction` (
  `Student_Sem_Course_Reg_Id` int(11) NOT NULL,
  `Student_Sem_Course_Reg_Student_Id` varchar(20) NOT NULL,
  `Student_Sem_Course_Reg_Batch_Sem_Course` int(11) DEFAULT NULL,
  `Student_Sem_Course_Reg_Reg_Status` binary(1) NOT NULL,
  `Student_Sem_Course_Reg_Reg_Date` date NOT NULL,
  `Student_Sem_Course_Reg_Approve_Date` date DEFAULT NULL,
  `Student_Sem_Course_Reg_Is_Auditing` binary(1) NOT NULL,
  `Student_Sem_Course_Reg_Student_Suggestion` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prediction`
--

LOCK TABLES `prediction` WRITE;
/*!40000 ALTER TABLE `prediction` DISABLE KEYS */;
INSERT INTO `prediction` VALUES (34,'20160020130',4,_binary '1','2018-12-10',NULL,_binary '0',NULL),(35,'20160020130',5,_binary '1','2018-12-10',NULL,_binary '0',NULL),(36,'20160020130',3,_binary '1','2018-12-10',NULL,_binary '0',NULL),(37,'20160020130',22,_binary '1','2018-12-10',NULL,_binary '0',NULL),(38,'20160020130',23,_binary '1','2018-12-10',NULL,_binary '0',NULL),(39,'20160010022',1,_binary '1','2018-12-10',NULL,_binary '0',NULL),(40,'20160010022',5,_binary '1','2018-12-10',NULL,_binary '0',NULL),(41,'20160010022',2,_binary '1','2018-12-10',NULL,_binary '0',NULL),(42,'20160010022',7,_binary '1','2018-12-10',NULL,_binary '0',NULL),(43,'20160010022',4,_binary '2','2018-12-10',NULL,_binary '0',NULL),(69,'20160010145',4,_binary '1','2018-12-11',NULL,_binary '0',NULL),(70,'20160010145',5,_binary '1','2018-12-11',NULL,_binary '0',NULL),(71,'20160010145',7,_binary '1','2018-12-11',NULL,_binary '0',NULL),(72,'20160010145',25,_binary '1','2018-12-11',NULL,_binary '0',NULL),(73,'20160010145',22,_binary '1','2018-12-11',NULL,_binary '0',NULL),(74,'20160010021',2,_binary '1','2018-12-11',NULL,_binary '0',NULL),(75,'20160010021',3,_binary '1','2018-12-11',NULL,_binary '0',NULL),(76,'20160010021',7,_binary '1','2018-12-11',NULL,_binary '0',NULL),(77,'20160010021',22,_binary '1','2018-12-11',NULL,_binary '0',NULL),(78,'20160010021',23,_binary '1','2018-12-11',NULL,_binary '0',NULL);
/*!40000 ALTER TABLE `prediction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Student_ID` varchar(20) DEFAULT NULL,
  `Student_First_Name` varchar(45) DEFAULT NULL,
  `Student_Middle_Name` varchar(90) DEFAULT NULL,
  `Student_Last_name` varchar(45) NOT NULL,
  `Student_DOB` date NOT NULL,
  `Student_Gender` varchar(1) NOT NULL,
  `Student_Email` varchar(45) DEFAULT NULL,
  `Student_Mobile` varchar(10) DEFAULT NULL,
  `Student_Blood_Group` varchar(4) NOT NULL,
  `Student_Mother_Tongue` varchar(45) DEFAULT NULL,
  `Student_Registered_Year` varchar(4) NOT NULL,
  `Student_Registered_Degree` int(11) NOT NULL,
  `Student_Registered_Degree_Duration` varchar(5) DEFAULT NULL,
  `Student_Cur_YearofStudy` varchar(5) NOT NULL,
  `Student_Cur_Sem` int(11) NOT NULL,
  `Student_Academic_Status` varchar(10) DEFAULT NULL,
  `is_blacklisted` binary(1) NOT NULL,
  `is_Alumini` binary(1) NOT NULL,
  `Student_Password` binary(32) DEFAULT 'd1612db4d6227cd8e7bc05b1b04e49b3',
  `CGPA` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Student_ID` (`Student_ID`),
  KEY `Student_Registered_Degree` (`Student_Registered_Degree`),
  CONSTRAINT `student_ibfk_1` FOREIGN KEY (`Student_Registered_Degree`) REFERENCES `academic_degree` (`Academic_Degree_Id`)
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (1,'20160010145','Sandeep','NULL','Potla','0000-00-00','â','sandeep.p16@iiits.in','7382386129','B+','TELUGU','2016',1,'4','2018',5,'â€œRegular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',8.5),(2,'20160020163','Vishal','','Prasad','1997-12-03','M','prasadvishal.d16@iiits.in','8374331031','B+','Hindi','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',7),(3,'20160010017','Chandrajeet','','Choudhary','1997-09-13','M','chandrajeet.c16@iiits.in','7073325643','B+','Hindi','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',8),(4,'20160020130','Prudhvi Raj','','Jwala','1999-01-18','M','prudhviraj.j16@iiits.in','9573856978','B+','Telugu','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',6),(5,'2016001003','Dharani','Devi','Akurathi','2018-09-24','F','dharanidhanu.111@iiits.in','8186051240','O+','Telugu','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',9.3),(6,'20160010021','Subhadeep','','Dash','2018-10-15','M','subhadeep.d16@iiits.in','9010128249','O-','Odia','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',4),(7,'20160020143','Abhilash','','Pembarthi','1998-06-11','M','abhilash.p16@iiits.in','7674944554','AB+','telugu','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',9.7),(8,'20160010022','Deepak','','Kumar','1999-06-11','M','deepak.k16@iiits.in','7997003580','B+','Hindi','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',7.4),(9,'20160020142','Venkata Vaishnavi','','Nalluri','1999-06-03','F','venkatavaishnavi.n16@iiits.in','8374632025','B+','Telugu','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',6.9),(10,'20160010006','Anurag','','Gupta','1998-12-22','M','anurag.g16@iiits.in','8574870570','B+','Hindi','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',8.6),(11,'20160010096','Tanmay','','Kalani','1998-03-13','M','tanmay.k16@iiits.in','7023310090','B+','Hindi','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',9.6),(12,'20160010034','Ajit','Jaywant','Jadhav','1998-11-17','M','jadhavajit.j16@iiits.in','7893448255','O+','Marathi','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',5),(13,'20160010019','Sai','Supriya','Doma','1999-03-09','F','saisupriya.d16@iiits.in','9063120536','B+','Telugu','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',5.5),(14,'20160020134','VISHNU','','VARDHAN','1999-08-12','M','vishnuvardhan.k16@iiits.in','9866408945','B+','TELUGU','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',5.8),(15,'20160020148','Rishitha','Reddy','Pulluru','1999-06-04','F','rishitha.p16@iiits.in','7286885255','B+','Telugu','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',4.7),(16,'20160010100','Deeksha','','Ummadi','1999-08-25','F','deeksha.u16@iiits.in','9666484876','B+','Telugu','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',6.8),(17,'20160010087','Shobhit','','Malarya','1997-11-17','M','shobhit.m16@iiits.in','7893445061','B+','Hindi','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',7.4),(18,'20160010037','Maheshwari','','Kotha','1998-12-10','F','Maheshwari.k16@iiits.in','7702480388','O+','Telugu','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',8.8),(19,'20160010056','SRIKARA MOHANA','SAI SACHIN','NEKKANTI','1999-04-30','M','saisachin.n16@iiits.in','7416206368','O+','Telugu','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',6.2),(20,'20160010014','Sudheera','Sivani','Billakurti','1999-09-01','F','sudheerasivani.b16@iiits.in','9951130506','O+','Telugu','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',7.2),(21,'20160020124','Krishna','Vamsi','Dirisala','1998-10-02','M','krishnavamsi.d16@iiits.in','9553508098','B-','Telugu','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',7.6),(22,'20160010078','Venkat','Lokesh Kumar','Sajjanapu','1999-07-08','M','venkatlokeshkumar.s16@iiits.in','9177814265','A+','Telugu','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',7.8),(23,'20160020126','Sai','Keerthi','Doma','1998-04-21','F','saikeerthi.d16@iiits.in','7013015905','A+','Telugu','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',8),(24,'20160020147','Pullela','Mrudula','Shastri','1999-06-10','F','mrudulashastri.p16@iiits.in','8522890196','O+','Telugu','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',8.2),(25,'20160010106','Sree Pragna','','Vinnakoti','1999-04-16','F','sreepragna.v16@iiits.in','9700780875','O+','Telugu','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',5.5),(26,'20160010083','Sarin','Rajendra','Nikose','1998-10-30','M','sarinrajendra.n16@iiits.in','9588691610','B+','Marathi','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',6.5),(27,'20160020118','Dheeraj','','Chappidi','1999-06-15','M','dheeraj.c16@iiits.in','9705382765','O+','Telugu','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',7.5),(28,'20160010098','Hareesh','','Thirukkovalluru','1999-04-11','M','hareesh.t16@iiits.in','8500429398','O+','Telugu','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',8.5),(29,'20160010073','Rohan','','Sukumaran','1997-01-30','M','rohan.s16@iiits.in','7893440516','O+','Malayalam','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',6.6),(30,'20160020138','Manasa','Sai','Karanam','1999-01-06','F','saikaranam.m16@iiits.in','7659022249','O+','Telugu','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',6.4),(31,'20160010067','Pulivarthi','Muni Nihitha','Chowdary','1999-05-30','F','muninihitha.p16@iiits.in','7093889931','O+','Telugu','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',5.2),(32,'20160010057','Satya Sai Prudhvi Krishna','','Nikku','1997-10-22','M','prudhvikrishna.n16@iiits.in','9100910025','O+','Telugu','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',7),(33,'20160020109','Adamya','','Gupta','1999-06-18','M','adamya.g16@iiits.in','8890467850','O+','Hindi','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',8),(34,'20160010004','ANIRUDH','','KANNAN V P','1998-03-31','M','anirudhkannan.v16@iiits.in','9566079994','A+','Tamil','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',9),(35,'20160010094','SURYA','TEJA','ACHANTA','1999-06-10','M','suryateja.a16@iiits.in','9603696399','B+','Telugu','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',9.7),(36,'20160020113','SAI TEJA','','AVADHOOTHA','2018-09-19','M','saiteja.a16@iiits.in','9493946464','O+','Telugu','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',6),(37,'20160020129','ITI','','TRIPATHI','1999-07-19','F','tripathi.i16@iiits.in','9411231043','O+','HINDI','2016',2,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',6),(38,'20160020140','Pranav','','Meejuri','1999-05-13','M','pranav.m16@iiits.in','8142665937','A+','Telugu','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',6.3),(39,'20160010018','chinmay','','Samal','1998-05-13','M','chinmay.s16@iiits.in','9439188224','B+','odia','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',6.6),(40,'20160010068','Sai','Madhu','Chandhana','1999-10-29','F','madhuchandhana.p16@iiits.in','7382272348','B+','Telugu','2016',2,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',6.9),(41,'20160020111','Ashish','Kumar','Patel','1998-12-12','M','ashishkumar.p16@iiits.in','8732006533','B+','Hindi','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',7.2),(42,'20160010086','Shivam','Singh','Yadav','1999-07-07','M','shivamsingh.y16@iiits.in','7897962189','B+','Hindi','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',7.5),(43,'20160010044','Vinoothna Sai','','Kinnera','1998-05-27','F','vinoothnasai.k16@iiits.in','9010872196','B+','Telugu','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',7.8),(44,'20160010015','Veena','Prathyusha','Bollapragada','1999-02-15','F','veenaprathyusha.b16@iiits.in','9494137368','B+','Telugu','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',8.1),(45,'20160010080','SALLA DASHARATHA','SAI','VAMSHI','1999-09-23','M','saivamshi.s16@iiits.in','7799558890','B+','Telugu','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',6.2),(46,'20160020117','Chadalavada','','Mounika','1999-02-01','F','mounika.c16@iiits.in','9492437147','B+','Telugu','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',5.4),(47,'20160010105','Rutvik','','Vijjali','1998-08-30','M','rutvikreddy.v16@iiits.in','8826544135','O+','Telugu','2016',2,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',5.5),(48,'20160010091','Soumik','','Mandal','1998-03-15','M','soumik.m16@iiits.in','9748497565','B+','Bengali','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',5.6),(49,'20160010009','Barinela','','Jahnavi','1999-07-28','F','jahnavi.b16@iiits.in','9515990318','B+','Telugu','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',6.1),(50,'20160010038','K Upendra','Sainath','Reddy','1998-11-25','M','sainathreddy.k16@iiits.in','9493683580','B+','Telugu','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',6.6),(51,'20160010013','Hinduja','','B','1999-09-16','F','hinduja.b16@iiits.in','9493925322','O+','Telugu','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',7.6),(52,'20160010030','Jahnavi','','Gujjula','1998-11-23','F','jahnavi.g16@iiits.in','7013232355','B+','Telugu','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',7.4),(53,'20160010052','Manthri','Sai Krishna Subash','Karthikeya','1998-09-11','M','subashkarthikeya.m16@iiits.in','9553116619','O+','Telugu','2016',1,'4','2018',5,'Regular',_binary '0',_binary '0',_binary '1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',7.5);
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_sem_course_reg`
--

DROP TABLE IF EXISTS `student_sem_course_reg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student_sem_course_reg` (
  `Student_Sem_Course_Reg_Id` int(11) NOT NULL,
  `Student_Sem_Course_Reg_Student_Id` varchar(20) NOT NULL,
  `Student_Sem_Course_Reg_Batch_Sem_Course` int(11) DEFAULT NULL,
  `Student_Sem_Course_Reg_Reg_Status` binary(1) NOT NULL,
  `Student_Sem_Course_Reg_Reg_Date` date NOT NULL,
  `Student_Sem_Course_Reg_Approve_Date` date DEFAULT NULL,
  `Student_Sem_Course_Reg_Is_Auditing` binary(1) NOT NULL,
  `Student_Sem_Course_Reg_Student_Suggestion` text,
  PRIMARY KEY (`Student_Sem_Course_Reg_Id`),
  KEY `Student_Sem_Course_Reg_Batch_Sem_Course` (`Student_Sem_Course_Reg_Batch_Sem_Course`),
  KEY `Student_Sem_Course_Reg_Student_Id` (`Student_Sem_Course_Reg_Student_Id`),
  CONSTRAINT `student_sem_course_reg_ibfk_2` FOREIGN KEY (`Student_Sem_Course_Reg_Batch_Sem_Course`) REFERENCES `academic_course` (`Academic_Course_Id`),
  CONSTRAINT `student_sem_course_reg_ibfk_3` FOREIGN KEY (`Student_Sem_Course_Reg_Student_Id`) REFERENCES `student` (`Student_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_sem_course_reg`
--

LOCK TABLES `student_sem_course_reg` WRITE;
/*!40000 ALTER TABLE `student_sem_course_reg` DISABLE KEYS */;
INSERT INTO `student_sem_course_reg` VALUES (1,'20160020130',4,_binary '1','2018-12-10',NULL,_binary '0',NULL),(2,'20160020130',5,_binary '1','2018-12-10',NULL,_binary '0',NULL),(3,'20160020130',3,_binary '1','2018-12-10',NULL,_binary '0',NULL),(4,'20160020130',22,_binary '1','2018-12-10',NULL,_binary '0',NULL),(5,'20160020130',23,_binary '1','2018-12-10',NULL,_binary '0',NULL),(6,'20160010022',1,_binary '1','2018-12-10',NULL,_binary '0',NULL),(7,'20160010022',5,_binary '1','2018-12-10',NULL,_binary '0',NULL),(8,'20160010022',2,_binary '1','2018-12-10',NULL,_binary '0',NULL),(9,'20160010022',7,_binary '1','2018-12-10',NULL,_binary '0',NULL),(10,'20160010145',4,_binary '1','2018-12-11',NULL,_binary '0',NULL),(11,'20160010145',5,_binary '1','2018-12-11',NULL,_binary '0',NULL),(12,'20160010145',7,_binary '1','2018-12-11',NULL,_binary '0',NULL),(13,'20160010145',25,_binary '1','2018-12-11',NULL,_binary '0',NULL),(14,'20160010145',22,_binary '1','2018-12-11',NULL,_binary '0',NULL),(15,'20160010021',2,_binary '1','2018-12-11',NULL,_binary '0',NULL),(16,'20160010021',3,_binary '1','2018-12-11',NULL,_binary '0',NULL),(17,'20160010021',7,_binary '1','2018-12-11',NULL,_binary '0',NULL),(18,'20160010021',22,_binary '1','2018-12-11',NULL,_binary '0',NULL),(19,'20160010021',23,_binary '1','2018-12-11',NULL,_binary '0',NULL);
/*!40000 ALTER TABLE `student_sem_course_reg` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 trigger poll_insert after insert on student_sem_course_reg
for each row
begin
insert into prediction values(new.Student_Sem_Course_Reg_Id, new.Student_Sem_Course_Reg_Student_Id, new.Student_Sem_Course_Reg_Batch_Sem_Course, new.Student_Sem_Course_Reg_Reg_Status, new.Student_Sem_Course_Reg_Reg_Date, new.Student_Sem_Course_Reg_Approve_Date, new.Student_Sem_Course_Reg_Is_Auditing, new.Student_Sem_Course_Reg_Student_Suggestion);
end */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 trigger poll_update after update on student_sem_course_reg for each row begin update prediction set Student_Sem_Course_Reg_Reg_Status = new.Student_Sem_Course_Reg_Reg_Status where Student_Sem_Course_Reg_Id = new.Student_Sem_Course_Reg_Id ; end */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-12-11  1:19:07
