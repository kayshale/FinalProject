-- phpMyAdmin SQL Dump
-- version 4.0.10deb1ubuntu0.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 06, 2020 at 07:04 AM
-- Server version: 5.5.62-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `ortizk_IS437`
--

-- --------------------------------------------------------

--
-- Table structure for table `Admin`
--

CREATE TABLE IF NOT EXISTS `Admin` (
  `AdminID` int(11) NOT NULL,
  `fname` varchar(20) NOT NULL,
  `lname` varchar(20) NOT NULL,
  `title` varchar(30) NOT NULL,
  `contact` int(10) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  PRIMARY KEY (`AdminID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Admin`
--

INSERT INTO `Admin` (`AdminID`, `fname`, `lname`, `title`, `contact`, `username`, `password`) VALUES
(1, 'Raiza', 'Ortiz', 'Billing Coordinator', 1234567890, 'raiza', '1234'),
(2, 'Yaimaraliz', 'Rodriguez', 'Patient Intake Coordinator', 1231234444, 'yai', '4444'),
(3, 'Sasha', 'Rodriguez', 'Chief of Human Resources', 2147483647, 'sasha', '3258');

-- --------------------------------------------------------

--
-- Table structure for table `Patient`
--

CREATE TABLE IF NOT EXISTS `Patient` (
  `PatientID` int(12) NOT NULL,
  `fname` varchar(20) NOT NULL,
  `lname` varchar(20) NOT NULL,
  `DOB` date NOT NULL,
  `SSN` int(9) NOT NULL,
  `Notes` varchar(150) NOT NULL,
  `PCPID` int(12) NOT NULL,
  PRIMARY KEY (`PatientID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Patient`
--

INSERT INTO `Patient` (`PatientID`, `fname`, `lname`, `DOB`, `SSN`, `Notes`, `PCPID`) VALUES
(1001, 'Denise', 'Mullings', '1998-03-18', 909765421, 'Swimmer - developing gills, might turn into a fish soon.', 5662),
(1233, 'Test', 'Dummy', '2010-02-16', 112223344, 'Test', 1111),
(1234, 'Kayshale', 'Ortiz', '1998-05-14', 123456789, 'Stressed Out\r\nCoffee Addict - High Risk of Cardiac Complications', 5647),
(2222, 'Joel', 'Hinkley', '1996-08-07', 111223333, 'Bad back - Workers Comp Injury, referred to physical therapy', 5647),
(5544, 'Shamiah', 'McCall', '1997-03-18', 333547865, 'Iron Deficient - Recommend adding tofu and spinach to diet', 5662),
(8877, 'Natasha', 'Infante', '1998-07-24', 111558888, 'Wine Addict - High Risk. Stop drinking wine.', 5647),
(9012, 'Meilat', 'Abraham', '1997-08-03', 589745677, 'Addicted to Chai Lattes - Health at Risk. No more Chai Lattes for you :)', 5662);

-- --------------------------------------------------------

--
-- Table structure for table `Provider`
--

CREATE TABLE IF NOT EXISTS `Provider` (
  `PCPID` int(12) NOT NULL,
  `Name` varchar(40) NOT NULL,
  `DOH` date NOT NULL,
  `SSN` int(9) NOT NULL,
  `Specialty` varchar(40) NOT NULL,
  PRIMARY KEY (`PCPID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Provider`
--

INSERT INTO `Provider` (`PCPID`, `Name`, `DOH`, `SSN`, `Specialty`) VALUES
(1111, 'Dr. Keena Powell, MD', '2020-04-09', 978844922, 'Oncology'),
(5647, 'Dr. Jeanne Beveridge, MD', '2020-03-28', 978844920, 'Everything'),
(5662, 'Dr. Asiyah Piper, MD', '2020-03-28', 707453344, 'Pediatrics, Nutrition');

-- --------------------------------------------------------

--
-- Table structure for table `Transaction`
--

CREATE TABLE IF NOT EXISTS `Transaction` (
  `TransactionID` int(11) NOT NULL,
  `Date` date NOT NULL,
  `Amount` decimal(10,2) NOT NULL,
  `Status` varchar(10) NOT NULL,
  `Insurance` varchar(40) NOT NULL,
  `Notes` varchar(150) NOT NULL,
  `AdminID` int(11) NOT NULL,
  `PatientID` int(12) NOT NULL,
  `PCPID` int(12) NOT NULL,
  PRIMARY KEY (`TransactionID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Transaction`
--

INSERT INTO `Transaction` (`TransactionID`, `Date`, `Amount`, `Status`, `Insurance`, `Notes`, `AdminID`, `PatientID`, `PCPID`) VALUES
(46568900, '2020-05-04', 150.00, 'Open', 'United Health', 'qpowndiaKM', 1, 1001, 5647),
(46568906, '2020-05-05', 15.00, 'Open', 'United Health', 'jwqspi', 1, 1001, 5647),
(49598609, '2020-04-30', 200.00, 'Closed', 'United Health', 'Insurance Claim submitted on 04/25/2020 for Patient visit on 04/20/2020 to United Health.', 1, 1234, 5647),
(123598678, '2020-05-01', 110.00, 'Closed', 'Anthem', 'Insurance claim submitted on 05/01/2020 for patient visit on 05/01/2020.', 1, 1001, 5662),
(145533620, '2020-05-01', 20.00, 'Open', 'Anthem', 'Co-Pay for visit on 05/01/2020. Please contact us or your insurance provider with any questions.', 1, 1001, 5662),
(145598222, '2020-05-04', 10.00, 'Open', 'United Health', 'Co-pay for visit on 50/04/2020. Please contact us or your insurance provider with any questions!', 1, 2222, 5647),
(145598600, '2020-04-24', 20.00, 'Closed', 'Blue Cross Blue Shield', 'Co-Pay for visit on 04/24/2020. Please contact us or your provider if there are any questions!', 1, 5544, 5647),
(147498600, '2020-04-24', 30.00, 'Open', 'NYS Medicaid', 'Co-Pay for visit on 04/24/2020. Please contact us or your healthcare provider if there are any questions!', 1, 8877, 5647),
(147498688, '2020-04-25', 10.00, 'Open', 'United Health', 'Co-Pay for visit on 04/25/2020. Please contact us or your insurance provider for any questions!', 1, 1234, 5647),
(147498997, '2020-04-24', 200.00, 'Open', 'Blue Cross Blue Shield', 'Co-Pay for visit on 04/24/2020. Please contact us or your insurance provider with any questions!', 1, 9012, 5662),
(147598611, '2020-04-28', 120.00, 'Open', 'NYS Medicaid', 'Insurance Claim submitted on 04/24/2020 for visit on 04/24/2020 to NYS Medicaid.', 1, 8877, 5647),
(155598666, '2020-05-04', 120.00, 'Closed', 'United Health', 'Claim submitted on 05/04/2020 for patient visit on 05/04/2020.', 1, 2222, 5647);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
