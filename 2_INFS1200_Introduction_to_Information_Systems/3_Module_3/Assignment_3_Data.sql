-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Sep 18, 2020 at 10:02 AM
-- Server version: 5.7.31-0ubuntu0.18.04.1
-- PHP Version: 7.2.24-0ubuntu0.18.04.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `assignment3`
--

-- --------------------------------------------------------

--
-- Table structure for table `Attends`
--

CREATE TABLE `Attends` (
  `id` int(8) NOT NULL,
  `title` varchar(200) NOT NULL,
  `date` date NOT NULL,
  `travelMethod` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Attends`
--

INSERT INTO `Attends` (`id`, `title`, `date`, `travelMethod`) VALUES
(9734109, 'Ekka', '2019-08-09', 'Train'),
(9734109, 'Melbourne Cup', '2017-11-07', 'Bus'),
(9734109, 'Melbourne Cup', '2018-11-06', 'Train'),
(9734109, 'The Happy Prince', '2019-11-27', 'Train'),
(9734109, 'UQ Open Day', '2018-02-11', 'Bus'),
(9734109, 'UQ Open Day', '2019-08-03', 'Train'),
(9734512, 'Ekka', '2019-08-09', 'Train'),
(19084223, 'Ekka', '2018-08-10', 'Bus'),
(19084223, 'Ekka', '2019-08-09', 'Walk'),
(19084223, 'The Nutcracker', '2019-11-30', 'Bus'),
(19084223, 'UQ Open Day', '2018-02-11', 'Bus'),
(19087623, 'Bathurst 1000', '2019-10-10', 'Bus'),
(19087623, 'Ekka', '2017-08-11', 'Bus'),
(19087623, 'Ekka', '2018-08-10', 'Bus'),
(19087623, 'Ekka', '2019-08-09', 'Bus'),
(19087623, 'GC 600', '2018-10-19', 'Train'),
(19087623, 'GC 600', '2019-10-25', 'Bus'),
(19087623, 'The Nutcracker', '2019-11-30', 'Bus'),
(19087623, 'UQ Open Day', '2018-02-11', 'Bus'),
(19088623, 'Ekka', '2019-08-09', 'Train'),
(19088623, 'Melbourne Cup', '2019-11-05', 'Car'),
(19088623, 'UQ Open Day', '2018-02-11', 'Bus'),
(19088644, 'Bathurst 1000', '2017-10-05', 'Bus'),
(19088644, 'Bathurst 1000', '2018-10-04', 'Car'),
(19088644, 'Bathurst 1000', '2019-10-10', 'Car'),
(19088644, 'Ekka', '2019-08-09', 'Train'),
(19088644, 'GC 600', '2016-10-21', 'Bus'),
(19088644, 'GC 600', '2018-10-19', 'Train'),
(19088644, 'GC 600', '2019-10-25', 'Taxi'),
(19088644, 'The Nutcracker', '2019-11-30', 'Bus'),
(19088644, 'UQ Open Day', '2019-08-03', 'Train'),
(19439623, 'Ekka', '2019-08-09', 'Train'),
(19439623, 'K-Drama Appreciation Day', '2020-04-12', 'Bus'),
(19488623, 'Ekka', '2019-08-09', 'Train'),
(19609863, 'UQ Open Day', '2019-08-03', 'Train'),
(22732951, 'Ekka', '2019-08-09', 'Bus'),
(22732951, 'The Nutcracker', '2019-11-30', 'Bus'),
(23982121, 'Ekka', '2019-08-09', 'Train'),
(23987721, 'Ekka', '2019-08-09', 'Train'),
(41284471, 'UQ Open Day', '2018-02-11', 'Bus'),
(42180081, 'UQ Open Day', '2018-02-11', 'Bus'),
(66234500, 'Melbourne Cup', '2017-11-07', 'Bus'),
(66234500, 'Melbourne Cup', '2018-11-06', 'Train'),
(66234500, 'The Happy Prince', '2019-11-27', 'Train'),
(66234500, 'UQ Open Day', '2018-02-11', 'Bus'),
(66234500, 'UQ Open Day', '2019-08-03', 'Train'),
(66234591, 'Ekka', '2019-08-09', 'Bus'),
(66234593, 'Ekka', '2019-08-09', 'Bus'),
(66234594, 'Ekka', '2019-08-09', 'Bus'),
(66234595, 'Bathurst 1000', '2018-10-04', 'Taxi'),
(66234595, 'Bathurst 1000', '2019-10-10', 'Taxi'),
(66234595, 'Bathurst 1000', '2020-10-15', 'Bus'),
(66234595, 'The Happy Prince', '2019-11-27', 'Taxi'),
(66234596, 'UQ Open Day', '2018-02-11', 'Bus'),
(88271481, 'Ekka', '2019-08-09', 'Train'),
(88271481, 'UQ Open Day', '2018-02-11', 'Bus'),
(88271481, 'UQ Open Day', '2019-08-03', 'Bus'),
(88271481, 'UQ Open Day', '2020-02-12', 'Train'),
(88271481, 'UQ Open Day', '2020-08-02', 'Ferry'),
(88272954, 'Ekka', '2019-08-09', 'Bus'),
(88276354, 'Bathurst 1000', '2017-10-05', 'Car'),
(88276354, 'Bathurst 1000', '2018-10-04', 'Bus'),
(88276354, 'Ekka', '2017-08-11', 'Ferry'),
(88276354, 'Ekka', '2018-08-10', 'Bus'),
(88276354, 'Ekka', '2019-08-09', 'Train'),
(88276354, 'Melbourne Cup', '2017-11-07', 'Bus'),
(88276354, 'Melbourne Cup', '2018-11-06', 'Car'),
(89734217, 'Ekka', '2019-08-09', 'Train'),
(89734217, 'UQ Open Day', '2018-02-11', 'Bus'),
(89734217, 'UQ Open Day', '2019-08-03', 'Train'),
(90316354, 'Ekka', '2019-08-09', 'Train'),
(90316354, 'Melbourne Cup', '2017-11-07', 'Bus'),
(90316354, 'Melbourne Cup', '2018-11-06', 'Train'),
(90316354, 'The Happy Prince', '2019-11-27', 'Train'),
(90316354, 'UQ Open Day', '2018-02-11', 'Bus'),
(99002931, 'Bathurst 1000', '2018-10-04', 'Bus'),
(99002931, 'Ekka', '2017-08-11', 'Walk'),
(99002931, 'GC 600', '2019-10-25', 'Train'),
(99002931, 'Melbourne Cup', '2019-11-05', 'Bus'),
(99002931, 'UQ Open Day', '2020-02-12', 'Car'),
(99723671, 'Ekka', '2017-08-11', 'Bus'),
(99723671, 'Ekka', '2018-08-10', 'Car'),
(99723671, 'Ekka', '2019-08-09', 'Bus'),
(99723671, 'K-Drama Appreciation Day', '2020-04-12', 'Bus'),
(99723671, 'The Nutcracker', '2019-11-30', 'Bus'),
(99723671, 'UQ Open Day', '2020-02-12', 'Bus'),
(99732114, 'Ekka', '2019-08-09', 'Train'),
(99732114, 'Melbourne Cup', '2017-11-07', 'Bus'),
(99732114, 'Melbourne Cup', '2018-11-06', 'Train'),
(99732114, 'The Happy Prince', '2019-11-27', 'Train'),
(99732114, 'UQ Open Day', '2019-08-03', 'Train'),
(190876632, 'Ekka', '2019-08-09', 'Train'),
(190876632, 'Melbourne Cup', '2017-11-07', 'Bus'),
(190876632, 'Melbourne Cup', '2018-11-06', 'Train'),
(190876632, 'The Happy Prince', '2019-11-27', 'Bus'),
(196666632, 'Bathurst 1000', '2018-10-04', 'Bus'),
(196666632, 'Ekka', '2017-08-11', 'Bus'),
(196666632, 'Ekka', '2019-08-09', 'Train'),
(196666632, 'GC 600', '2019-10-25', 'Bus'),
(196666632, 'Melbourne Cup', '2019-11-05', 'Bus'),
(196666632, 'UQ Open Day', '2020-02-12', 'Bus');

-- --------------------------------------------------------

--
-- Table structure for table `Event`
--

CREATE TABLE `Event` (
  `title` varchar(200) NOT NULL,
  `date` date NOT NULL,
  `description` text,
  `location` varchar(200) NOT NULL,
  `sponser` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Event`
--

INSERT INTO `Event` (`title`, `date`, `description`, `location`, `sponser`) VALUES
('Bathurst 1000', '2017-10-05', 'Pinnacle of motorsport in Australia held annually on  Mount Panorama Circuit', 'Bathurst, NSW', 'Supercheap Auto'),
('Bathurst 1000', '2018-10-04', 'Pinnacle of motorsport in Australia held annually on  Mount Panorama Circuit', 'Bathurst, NSW', 'Supercheap Auto'),
('Bathurst 1000', '2019-10-10', 'Pinnacle of motorsport in Australia held annually on  Mount Panorama Circuit', 'Bathurst, NSW', 'Supercheap Auto'),
('Bathurst 1000', '2020-10-15', 'Pinnacle of motorsport in Australia held annually on  Mount Panorama Circuit', 'Bathurst, NSW', 'Supercheap Auto'),
('Ekka', '2017-08-11', 'The EKKA is Queensland\'s largest event and your greatest chance throughout the year to find out what life on the farm is really about', '600 Gregory Tce, Bown Hills', 'Queensland Government'),
('Ekka', '2018-08-10', 'The EKKA is Queensland\'s largest event and your greatest chance throughout the year to find out what life on the farm is really about', '600 Gregory Tce, Bown Hills', 'Queensland Government'),
('Ekka', '2019-08-09', 'The EKKA is Queensland\'s largest event and your greatest chance throughout the year to find out what life on the farm is really about', '600 Gregory Tce, Bown Hills', 'Queensland Government'),
('GC 600', '2016-10-21', 'Queensland’s premier Supercars event, it is the final endurance race on the Supercars calendar', 'Surfer\'s Paradise, QLD', 'Vodafone'),
('GC 600', '2017-10-20', 'Queensland’s premier Supercars event, it is the final endurance race on the Supercars calendar', 'Surfer\'s Paradise, QLD', 'Vodafone'),
('GC 600', '2018-10-19', 'Queensland’s premier Supercars event, it is the final endurance race on the Supercars calendar', 'Surfer\'s Paradise, QLD', 'Vodafone'),
('GC 600', '2019-10-25', 'Queensland’s premier Supercars event, it is the final endurance race on the Supercars calendar', 'Surfer\'s Paradise, QLD', 'Vodafone'),
('K-Drama Appreciation Day', '2020-04-12', 'For anyone with a passion for K-Dramas. We\'ll be screening Boys over Flowers, Crash Landing on You and Descendents of the Sun. Get excited! Bring popcorn and your love for K-Drams.', 'Parliament House, Canberra', 'ANU Korean Club'),
('Melbourne Cup', '2017-11-07', 'A prestigious Australian thoroughbred horse race.', 'Flemington Racecourse', 'Victoria Government'),
('Melbourne Cup', '2018-11-06', 'A prestigious Australian thoroughbred horse race.', 'Flemington Racecourse', 'Victoria Government'),
('Melbourne Cup', '2019-11-05', 'A prestigious Australian thoroughbred horse race.', 'Flemington Racecourse', 'Victoria Government'),
('The Happy Prince', '2019-11-27', 'In Oscar Wilde\'s lyrical story, a prince who has lived a carefree live behind his palace walls becomes a magnificent golden statue.', 'Sydney Opera House', 'The Australian Ballet'),
('The Nutcracker', '2019-11-30', 'There\'s nothing like a tradional Nutcracker to get you in the mood for the festive season.', 'Sydney Opera House', 'The Australian Ballet'),
('UQ Open Day', '2018-02-11', 'Explore options at UQ', 'St Lucia, QLD 4072', 'University of Queensland'),
('UQ Open Day', '2019-08-03', 'Explore options at UQ', 'St Lucia, QLD 4072', 'University of Queensland'),
('UQ Open Day', '2020-02-12', 'Explore options at UQ', 'St Lucia, QLD 4072', 'University of Queensland'),
('UQ Open Day', '2020-08-02', 'Explore options at UQ', 'St Lucia, QLD 4072', 'University of Queensland');

-- --------------------------------------------------------

--
-- Stand-in structure for view `EventParticipants`
-- (See below for the actual view)
--
CREATE TABLE `EventParticipants` (
`Title` varchar(200)
,`Date` date
,`Count` bigint(21)
);

-- --------------------------------------------------------

--
-- Table structure for table `Friends`
--

CREATE TABLE `Friends` (
  `requestor` int(8) NOT NULL,
  `requestee` int(8) NOT NULL,
  `startDate` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Friends`
--

INSERT INTO `Friends` (`requestor`, `requestee`, `startDate`) VALUES
(9734109, 19084223, '2017-09-21'),
(9734109, 19087623, '2011-06-30'),
(9734109, 19088644, '2015-12-26'),
(9734109, 22732951, '2015-09-22'),
(9734109, 41284471, '2011-06-19'),
(9734109, 66234500, '2012-04-12'),
(9734109, 89734217, '2012-11-27'),
(9734512, 19084223, '2017-03-14'),
(9734512, 19087623, '2020-09-02'),
(9734512, 19088644, '2016-01-29'),
(9734512, 22732951, '2010-06-27'),
(9734512, 99732114, '2014-12-29'),
(19084223, 19088623, '2015-01-29'),
(19084223, 19088644, '2014-07-15'),
(19084223, 19439623, '2019-07-08'),
(19084223, 19488623, '2020-09-11'),
(19084223, 23982121, '2020-10-30'),
(19084223, 23987721, '2010-10-31'),
(19084223, 41284471, '2017-01-01'),
(19084223, 66234500, '2016-04-09'),
(19084223, 66234593, '2016-09-18'),
(19084223, 66234594, '2017-11-03'),
(19084223, 66234596, '2019-01-24'),
(19084223, 88271481, '2016-01-28'),
(19084223, 88272954, '2020-11-04'),
(19084223, 88276354, '2018-03-14'),
(19084223, 89734217, '2012-08-08'),
(19084223, 90316354, '2020-01-19'),
(19084223, 99732114, '2013-09-13'),
(19084223, 190876632, '2011-07-24'),
(19084223, 196666632, '2016-10-27'),
(19087623, 19088623, '2014-04-07'),
(19087623, 19088644, '2010-10-14'),
(19087623, 19439623, '2017-03-09'),
(19087623, 19488623, '2014-05-31'),
(19087623, 23982121, '2015-05-20'),
(19087623, 23987721, '2018-01-06'),
(19087623, 66234500, '2016-07-03'),
(19087623, 66234593, '2019-02-14'),
(19087623, 66234594, '2012-11-12'),
(19087623, 66234596, '2015-05-01'),
(19087623, 88271481, '2010-11-04'),
(19087623, 88272954, '2019-07-06'),
(19087623, 88276354, '2014-05-27'),
(19087623, 89734217, '2019-03-25'),
(19087623, 90316354, '2014-03-01'),
(19087623, 99732114, '2018-08-11'),
(19087623, 190876632, '2013-02-18'),
(19087623, 196666632, '2017-01-11'),
(19088623, 19088644, '2019-07-31'),
(19088623, 19488623, '2015-04-17'),
(19088623, 22732951, '2011-02-06'),
(19088644, 19439623, '2010-09-05'),
(19088644, 19488623, '2018-11-20'),
(19088644, 22732951, '2014-07-13'),
(19088644, 23982121, '2013-06-05'),
(19088644, 23987721, '2012-01-20'),
(19088644, 66234500, '2017-02-18'),
(19088644, 66234593, '2010-10-12'),
(19088644, 66234594, '2010-01-08'),
(19088644, 66234596, '2018-09-23'),
(19088644, 88271481, '2019-03-10'),
(19088644, 88272954, '2016-11-29'),
(19088644, 88276354, '2015-11-15'),
(19088644, 89734217, '2015-07-12'),
(19088644, 90316354, '2013-10-31'),
(19088644, 99732114, '2017-04-14'),
(19088644, 190876632, '2016-11-07'),
(19088644, 196666632, '2012-10-29'),
(19439623, 22732951, '2013-07-15'),
(19439623, 66234500, '2010-04-30'),
(19439623, 66234596, '2018-04-22'),
(19488623, 22732951, '2014-05-20'),
(19609863, 66234500, '2017-09-11'),
(19609863, 66234596, '2012-08-09'),
(22732951, 23982121, '2020-12-09'),
(22732951, 23987721, '2012-11-05'),
(22732951, 66234500, '2010-11-22'),
(22732951, 66234593, '2010-10-27'),
(22732951, 66234594, '2012-05-07'),
(22732951, 66234596, '2017-08-03'),
(22732951, 88271481, '2017-11-29'),
(22732951, 88272954, '2020-07-20'),
(22732951, 88276354, '2014-09-22'),
(22732951, 89734217, '2013-11-16'),
(22732951, 90316354, '2018-01-03'),
(22732951, 99732114, '2019-10-10'),
(22732951, 190876632, '2011-07-08'),
(22732951, 196666632, '2010-08-06'),
(23982121, 23987721, '2015-03-15'),
(23982121, 38982921, '2019-04-05'),
(23982121, 41284471, '2018-10-16'),
(23982121, 42180081, '2015-03-24'),
(23982121, 99723671, '2020-09-15'),
(23987721, 38982921, '2013-10-21'),
(23987721, 41284471, '2014-01-16'),
(23987721, 42180081, '2018-10-20'),
(23987721, 99723671, '2019-12-19'),
(38982921, 41284471, '2014-06-22'),
(38982921, 42180081, '2011-08-11'),
(38982921, 99723671, '2015-07-28'),
(41284471, 42180081, '2011-06-10'),
(41284471, 66234500, '2020-05-05'),
(41284471, 66234596, '2010-04-07'),
(41284471, 99723671, '2018-10-25'),
(42180081, 99723671, '2016-01-06'),
(66234500, 66234593, '2015-01-10'),
(66234500, 66234594, '2018-01-02'),
(66234500, 66234596, '2018-04-08'),
(66234500, 88271481, '2018-10-30'),
(66234500, 88272954, '2014-06-30'),
(66234500, 88276354, '2015-11-30'),
(66234500, 89734217, '2016-03-02'),
(66234500, 90316354, '2019-03-15'),
(66234500, 99723671, '2019-10-18'),
(66234500, 99732114, '2014-09-09'),
(66234500, 190876632, '2010-11-30'),
(66234500, 196666632, '2018-01-08'),
(66234593, 66234594, '2017-12-04'),
(66234593, 66234596, '2012-06-04'),
(66234594, 66234596, '2020-11-02'),
(66234596, 88271481, '2018-05-22'),
(66234596, 88272954, '2018-04-05'),
(66234596, 88276354, '2014-10-13'),
(66234596, 89734217, '2015-07-17'),
(66234596, 90316354, '2017-06-24'),
(66234596, 99723671, '2014-08-16'),
(66234596, 99732114, '2019-07-27'),
(66234596, 190876632, '2018-09-22'),
(66234596, 196666632, '2012-12-25'),
(88271481, 90316354, '2011-09-03'),
(88272954, 88276354, '2014-01-14'),
(190876632, 196666632, '2013-01-01');

-- --------------------------------------------------------

--
-- Table structure for table `User`
--

CREATE TABLE `User` (
  `id` int(8) NOT NULL,
  `fName` varchar(80) NOT NULL,
  `mInitial` char(1) DEFAULT NULL,
  `lName` varchar(80) NOT NULL,
  `age` int(3) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `email` varchar(100) NOT NULL,
  `nationality` varchar(100) NOT NULL,
  `significantOther` int(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `User`
--

INSERT INTO `User` (`id`, `fName`, `mInitial`, `lName`, `age`, `phone`, `email`, `nationality`, `significantOther`) VALUES
(9734109, 'Eduard', 'A', 'Khil', 19, '+7 8 9912 8733', 'trolleyguy@gmail.com', 'Russian', 89734217),
(9734512, 'Mikhail', 'V', 'Mishustin', 52, '+7 9 4782 0921', 'mikki.mishutin@hotmail.com', 'Russian', 99732114),
(19084223, 'Lucy', 'R', 'Ali', 19, '+61 4 2323 1198', 'lucy.ali1@uq.edu.au', 'Australian', NULL),
(19087623, 'John', 'K', 'Monarch', 32, '+61 4 9999 8888', 'john.monarch@uq.edu.au', 'Australian', NULL),
(19088623, 'Ursula', 'L', 'Smith', 27, '+61 7 8765 1234', 'u.smith@qut.edu.au', 'Bolivian', 19488623),
(19088644, 'Marcus', 'F', 'Jacobs', 68, '+61 7 8335 1334', 'marcus.jacobs@uq.edu', 'Australian', 19439623),
(19439623, 'Nevena', 'Y', 'Ivanovic', 29, '+61 7 2222 1122', 'Nevena@gmail.com', 'Montenegrin', 19088644),
(19488623, 'Leo', 'C', 'Montgomery', 29, '+61 7 8765 1256', 'leolovescars@gmail.com', 'Brazilian', 19088623),
(19609863, 'Edi', NULL, 'Rama', 54, '+35 5 2298 0927', 'edi.rama@uq.edu.au', 'Albanian', NULL),
(22732951, 'Jamie', 'T', 'Sleeman', 60, '+61 7 8192 2984', 'joshua@gmail.com', 'Australian', NULL),
(23982121, 'Hye-sun', NULL, 'Ku', 35, '+61 4 5582 1199', 'ku@uq.edu.au', 'Korean', 23987721),
(23987721, 'Min-ho', NULL, 'Lee', 33, '+61 4 5582 1923', 'lee@uq.edu.au', 'Korean', 23982121),
(38982921, 'Jeong-hyeok', NULL, 'Ri', 74, '+82 8 3378 7123', 'ri.jonghyok@hotmail.com', 'Korean', NULL),
(41284471, 'Bong-soon', NULL, 'Park', 18, '+82 2 3391 2245', 'park.bongsoon@ainsoft.com', 'Korean', NULL),
(42180081, 'Se-ri', NULL, 'Yoon', 20, '+82 2 1187 3982', 'yoon.seri@queen.com', 'Korean', NULL),
(66234500, 'Sven', NULL, 'Kirsch', 13, '+49 3 2217 7820', 'sven.kirsch@uq.edu.au', 'German', NULL),
(66234591, 'Matthieu', NULL, 'Loiselle', 49, '+33 9 0822 3491', 'matt.loiselle@uq.edu.au', 'French', NULL),
(66234592, 'Gabriel', NULL, 'Duperre', 56, '+33 9 0822 3432', 'Gabe.dupe@gmail.comm', 'French', NULL),
(66234593, 'Honore', NULL, 'Avare', 32, '+33 9 0822 3444', 'honore@hotmail', 'French', 66234594),
(66234594, 'Margit', 'N', 'Gade', 37, '+45 3 4491 9923', 'margit.gade1@uq.edu.au', 'Danish', 66234593),
(66234595, 'Lavinia', 'S', 'Pinto', 90, '+55 5 9920 0012', 'lavinia@hotmail.com', 'Brazilian', NULL),
(66234596, 'Yvonne', NULL, 'Holtzmann', 20, '+49 4 8890 2311', 'holtzmann@gmail.com', 'German', NULL),
(88271481, 'Radhiya', 'I', 'Aswad', 20, '+39 7 1182 3374', 'radhiya.aswad@uq.edu.au.com', 'Italian', 90316354),
(88272954, 'Joshua', 'T', 'Hernandez', 61, '+1 7 8192 2984', 'joshua@gmail.com', 'American', 88276354),
(88276354, 'Beatrice', 'P', 'Hernandez', 71, '+1 7 8892 3374', 'beatrice@gmail.com', 'American', 88272954),
(89734217, 'Nadeea', 'K', 'Volianova', 25, '+7 8 0967 9276', 'nadeea@uq.edu.au', 'Russian', 9734109),
(90316354, 'Mahrus', 'P', 'Bitar', 22, '+1 7 2200 3311', 'uq.edu.au@gmail.com', 'American', 88271481),
(99002931, 'Grace', NULL, 'Jeon', 23, '+82 2 8734 3382', 'grace.jeon@uq.edu.au', 'Korean', NULL),
(99723671, 'Man-wol', NULL, 'Jang', 60, '+82 8 2763 2383', 'jang@uq.edu.au', 'Korean', NULL),
(99732114, 'Sofia', 'M', 'Rotaru', 31, '+38 0 1192 8337', 'sofia.rotaru@gmail.com', 'Ukraine', 9734512),
(190876632, 'Ilir', NULL, 'Meta', 89, '+35 5 4678 0927', 'ilirmeta@hotmail.com', 'Albanian', 196666632),
(196666632, 'Monika', NULL, 'Kryemadhi', 60, '+35 5 4621 0927', 'Monika.Kryemadhi@uq.edu.au', 'Albanian', 190876632);

-- --------------------------------------------------------
--
-- Indexes for dumped tables
--

--
-- Indexes for table `Attends`
--
ALTER TABLE `Attends`
  ADD PRIMARY KEY (`id`,`title`,`date`),
  ADD KEY `eventFK` (`title`,`date`);

--
-- Indexes for table `Event`
--
ALTER TABLE `Event`
  ADD PRIMARY KEY (`title`,`date`);

--
-- Indexes for table `Friends`
--
ALTER TABLE `Friends`
  ADD PRIMARY KEY (`requestor`,`requestee`),
  ADD KEY `requesteeFK` (`requestee`);

--
-- Indexes for table `User`
--
ALTER TABLE `User`
  ADD PRIMARY KEY (`id`),
  ADD KEY `sigOtherFK` (`significantOther`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Attends`
--
ALTER TABLE `Attends`
  ADD CONSTRAINT `eventFK` FOREIGN KEY (`title`,`date`) REFERENCES `Event` (`title`, `date`),
  ADD CONSTRAINT `userFK` FOREIGN KEY (`id`) REFERENCES `User` (`id`);

--
-- Constraints for table `Friends`
--
ALTER TABLE `Friends`
  ADD CONSTRAINT `requesteeFK` FOREIGN KEY (`requestee`) REFERENCES `User` (`id`),
  ADD CONSTRAINT `requestorFK` FOREIGN KEY (`requestor`) REFERENCES `User` (`id`);

--
-- Constraints for table `User`
--
ALTER TABLE `User`
  ADD CONSTRAINT `sigOtherFK` FOREIGN KEY (`significantOther`) REFERENCES `User` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
