-- MySQL dump 10.13  Distrib 8.0.43, for Win64 (x86_64)
--
-- Host: localhost    Database: ev_app
-- ------------------------------------------------------
-- Server version	8.0.43

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ev_charger_details`
--

DROP TABLE IF EXISTS `ev_charger_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ev_charger_details` (
  `id` int NOT NULL AUTO_INCREMENT,
  `station_name` varchar(150) NOT NULL,
  `longitude` decimal(10,7) DEFAULT NULL,
  `latitude` decimal(10,7) DEFAULT NULL,
  `AC` int DEFAULT '0',
  `DC` int DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ev_charger_details`
--

LOCK TABLES `ev_charger_details` WRITE;
/*!40000 ALTER TABLE `ev_charger_details` DISABLE KEYS */;
INSERT INTO `ev_charger_details` VALUES (21,'Sai Krishna Charging Station',78.4866710,17.3850440,5,2),(22,'GreenVolt Charging Hub',77.5945660,12.9715990,8,3),(23,'EcoCharge Station',72.8776550,19.0759830,10,5),(24,'ChargeXpress Delhi',77.2090210,28.6139390,12,6),(25,'PowerUp EV Station',80.2707180,13.0826800,7,2),(26,'ZapCharge Hyderabad',78.4866710,17.3850440,6,4),(27,'ElectroFast Pune',73.8562550,18.5204300,9,3),(28,'Bolt EV Hub Jaipur',75.7872700,26.9124340,4,1),(29,'AmpVolt Ahmedabad',72.5713650,23.0225050,11,6),(30,'Voltify Chennai',80.2707180,13.0826800,8,5),(31,'FlashCharge Lucknow',80.9461660,26.8466950,5,2),(32,'SuperVolt Chandigarh',76.7794190,30.7333150,7,4),(33,'ChargePoint Noida',77.3910290,28.5355170,6,3),(34,'TurboCharge Bhopal',77.4126130,23.2599330,10,2),(35,'HyperVolt Surat',72.8310620,21.1702400,9,5),(36,'Energex Kochi',76.2673030,9.9312330,4,2),(37,'MaxCharge Patna',85.1375660,25.5940950,6,3),(38,'SwiftVolt Indore',75.8577270,22.7195680,7,4),(39,'NeoCharge Guwahati',91.7362370,26.1445180,3,1),(40,'UltraVolt Nagpur',79.0881580,21.1458000,12,7);
/*!40000 ALTER TABLE `ev_charger_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_cars`
--

DROP TABLE IF EXISTS `user_cars`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_cars` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `car_number` varchar(20) NOT NULL,
  `model` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `car_number` (`car_number`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_cars`
--

LOCK TABLES `user_cars` WRITE;
/*!40000 ALTER TABLE `user_cars` DISABLE KEYS */;
INSERT INTO `user_cars` VALUES (1,'raj123','raj@123','MH12AB4321','Hyundai Kona EV'),(2,'neha01','neha@pass','DL05XY6789','MG ZS EV'),(3,'arjunX','arj@1234','KA03MN4567','Tata Nexon EV'),(4,'simran9','simmy@99','GJ01AB1234','Mahindra eVerito'),(5,'vivek77','vivekpass','TN09CD8765','BYD e6'),(6,'anu88','anu@pass','RJ14EF3456','Kia EV6'),(7,'krishna7','krish@007','UP32GH9876','Tata Tiago EV'),(8,'deepakX','deep@999','WB20IJ6543','Hyundai Ioniq 5'),(9,'priya22','priya@22','CH01JK1122','Honda City Hybrid'),(10,'akash321','akash@pass','MP09LM7788','Tata Tigor EV'),(11,'meena45','meena@45','OD02OP2233','Renault Zoe'),(12,'sunil99','sunil@99','KL07QR4455','Nissan Leaf'),(13,'pawan11','pawan@11','PB10ST6677','Tesla Model 3'),(14,'kiran65','kiran@65','BR06UV8899','Tata Nexon EV'),(15,'ravi007','ravi@007','HR26WX3344','MG Comet EV'),(16,'swati55','swati@55','JK02YZ5566','Mahindra XUV400'),(17,'manoj33','manoj@33','AS01GH7788','BYD Atto 3'),(18,'geeta77','geeta@77','UK07KL9900','Kia Soul EV'),(19,'amit99','amit@99','AP28MN1122','Hyundai Kona EV'),(20,'sneha88','sneha@88','TS07PQ3344','Tata Tiago EV');
/*!40000 ALTER TABLE `user_cars` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-09-17  2:21:50
