

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

-- 資料表結構 `Department`

CREATE TABLE `Department` (
  `DepartmentID` varchar(4) NOT NULL,
  `DepartmentName` varchar(100) NOT NULL,
  `CostCenter` char(8) NOT NULL,
  `CreatedAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `UpdatedAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ;

-- 傾印資料表的資料 `Department`

INSERT INTO `Department` (`DepartmentID`, `DepartmentName`, `CostCenter`, `CreatedAt`, `UpdatedAt`) VALUES
('DT10', 'Human Resource', '25100010', '2025-03-06 03:14:08', '2025-03-06 03:14:08'),
('DT20', 'Finance', '25100020', '2025-03-06 03:14:08', '2025-03-06 03:14:08'),
('DT21', 'Compliance', '25100022', '2025-03-06 03:14:08', '2025-03-06 03:14:08'),
('DT30', 'Sales', '25120030', '2025-03-06 03:14:08', '2025-03-06 03:14:08'),
('DT32', 'Marketing', '25120032', '2025-03-06 03:14:08', '2025-03-06 03:14:08'),
('DT33', 'Logistic', '25120033', '2025-03-06 03:14:08', '2025-03-06 03:14:08'),
('DT40', 'IT', '25100030', '2025-03-06 03:14:08', '2025-03-06 03:14:08');

-- --------------------------------------------------------

-- 資料表結構 `Employee`

CREATE TABLE `Employee` (
  `EmployeeID` varchar(10) NOT NULL,
  `FirstName` varchar(50) NOT NULL,
  `LastName` varchar(50) NOT NULL,
  `DateOfBirth` date NOT NULL,
  `Gender` enum('Male','Female','Other') NOT NULL,
  `HireDate` date NOT NULL,
  `JoinDate` date NOT NULL,
  `DepartmentID` varchar(4) DEFAULT NULL,
  `JobTitle` varchar(100) NOT NULL,
  `CompEmail` varchar(100) NOT NULL,
  `PrivateEmail` varchar(100) DEFAULT NULL,
  `PhoneNumber` varchar(20) DEFAULT NULL,
  `Address` text,
  `StatusID` varchar(4) DEFAULT NULL,
  `CreatedAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `UpdatedAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- 傾印資料表的資料 `Employee`

INSERT INTO `Employee` (`EmployeeID`, `FirstName`, `LastName`, `DateOfBirth`, `Gender`, `HireDate`, `JoinDate`, `DepartmentID`, `JobTitle`, `CompEmail`, `PrivateEmail`, `PhoneNumber`, `Address`, `StatusID`, `CreatedAt`, `UpdatedAt`) VALUES
('51001', 'Charlotte', 'FENG', '2001-06-08', 'Female', '2022-11-09', '2022-11-09', 'DT10', 'Human Resourse Assistant', 'CharlotteFENG@stitch.com', 'pinksalt10@gmail.com', '0918493020', 'Hsinchu, Taiwan', 'ST10', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51002', 'James', 'LEE', '1990-03-15', 'Male', '2020-01-12', '2020-01-12', 'DT10', 'HR Specialist', 'JamesLEE@stitch.com', 'jameslee@gmail.com', '0912003456', 'Taipei, Taiwan', 'ST10', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51003', 'Olivia', 'CHEN', '1995-09-22', 'Female', '2021-02-10', '2021-02-10', 'DT20', 'Financial Analyst', 'OliviaCHEN@stitch.com', 'oliviachen@yahoo.com', '0921005678', 'New Taipei, Taiwan', 'ST10', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51004', 'Ethan', 'WANG', '1988-04-10', 'Male', '2017-10-20', '2017-10-20', 'DT21', 'Compliance Officer', 'EthanWANG@stitch.com', 'ethanwang@hotmail.com', '0933007890', 'Kaohsiung, Taiwan', 'ST10', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51005', 'Sophia', 'LIN', '1992-12-30', 'Female', '2022-08-15', '2022-08-15', 'DT30', 'Sales Assistant', 'SophiaLIN@stitch.com', 'sophialin@gmail.com', '0955001234', 'Taichung, Taiwan', 'ST90', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51006', 'Lucas', 'TSAI', '1989-11-15', 'Male', '2019-05-05', '2019-05-05', 'DT32', 'Marketing Specialist', 'LucasTSAI@stitch.com', 'lucastsai@yahoo.com', '0966002345', 'Tainan, Taiwan', 'ST10', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51007', 'Emma', 'HUANG', '1993-07-07', 'Female', '2018-12-18', '2018-12-20', 'DT33', 'Logistics Coordinator', 'EmmaHUANG@stitch.com', 'emmahuang@hotmail.com', '0977003456', 'Taoyuan, Taiwan', 'ST11', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51008', 'Noah', 'CHOU', '1986-10-05', 'Male', '2010-11-01', '2010-11-01', 'DT40', 'IT Support', 'NoahCHOU@stitch.com', 'noahchou@gmail.com', '0988004567', 'Hsinchu, Taiwan', 'ST10', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51009', 'Ava', 'WU', '1996-04-18', 'Female', '2023-04-10', '2023-04-10', 'DT30', 'Sales Assistant', 'AvaWU@stitch.com', 'avawu@yahoo.com', '0999005678', 'Miaoli, Taiwan', 'ST10', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51010', 'Liam', 'YANG', '1990-02-20', 'Male', '2010-05-25', '2010-05-25', 'DT20', 'Finance Manager', 'LiamYANG@stitch.com', 'liamyang@gmail.com', '0910006789', 'Changhua, Taiwan', 'ST10', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51011', 'Isabella', 'LAI', '1997-11-02', 'Female', '2021-06-15', '2021-06-15', 'DT30', 'Sales Assistant', 'IsabellaLAI@stitch.com', 'isabellalai@hotmail.com', '0920007890', 'Yunlin, Taiwan', 'ST20', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51012', 'Mason', 'KUO', '1985-09-08', 'Male', '2008-01-30', '2008-01-30', 'DT30', 'Sales Manager', 'MasonKUO@stitch.com', 'masonkuo@gmail.com', '0930008901', 'Pingtung, Taiwan', 'ST10', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51013', 'Mia', 'TENG', '1999-09-29', 'Female', '2023-03-10', '2023-03-10', 'DT32', 'Marketing Assistant', 'MiaTENG@stitch.com', 'miateng@gmail.com', '0940009012', 'Keelung, Taiwan', 'ST90', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51014', 'Henry', 'CHANG', '1982-04-25', 'Male', '2005-12-20', '2005-12-20', 'DT33', 'Logistics Supervisor', 'HenryCHANG@stitch.com', 'henrychang@gmail.com', '0950000123', 'Hualien, Taiwan', 'ST10', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51015', 'Charlotte', 'HSU', '1998-10-17', 'Female', '2022-05-25', '2022-05-25', 'DT40', 'IT Support', 'CharlotteHSU@stitch.com', 'charlottehsu@gmail.com', '0960001234', 'Taitung, Taiwan', 'ST11', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51016', 'William', 'FAN', '1991-04-03', 'Male', '2016-05-10', '2016-05-10', 'DT10', 'HR Manager', 'WilliamFAN@stitch.com', 'williamfan@gmail.com', '0970002345', 'Penghu, Taiwan', 'ST10', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51017', 'Grace', 'CHIU', '2000-07-12', 'Female', '2023-03-05', '2023-03-07', 'DT30', 'Sales Assistant', 'GraceCHIU@stitch.com', 'gracechiu@gmail.com', '0980003456', 'Taipei, Taiwan', 'ST20', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51018', 'Jack', 'LU', '1987-07-19', 'Male', '2011-12-12', '2011-12-12', 'DT21', 'Compliance Manager', 'JackLU@stitch.com', 'jacklu@gmail.com', '0990004567', 'New Taipei, Taiwan', 'ST10', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51019', 'Emily', 'WEN', '1993-11-25', 'Female', '2017-07-20', '2017-07-22', 'DT30', 'Senior Sales Executive', 'EmilyWEN@stitch.com', 'emilywen@gmail.com', '0911115678', 'Taichung, Taiwan', 'ST10', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51020', 'Daniel', 'SHIH', '1996-12-07', 'Male', '2021-01-15', '2021-01-15', 'DT32', 'Marketing Manager', 'DanielSHIH@stitch.com', 'danielshih@gmail.com', '0922226789', 'Kaohsiung, Taiwan', 'ST10', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51021', 'Hannah', 'FANG', '1998-08-24', 'Female', '2022-03-22', '2022-03-22', 'DT33', 'Logistics Assistant', 'HannahFANG@stitch.com', 'hannahfang@gmail.com', '0933337890', 'Hsinchu, Taiwan', 'ST10', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51022', 'Matthew', 'CHENG', '1983-04-09', 'Male', '2004-10-05', '2004-10-05', 'DT40', 'IT Director', 'MatthewCHENG@stitch.com', 'matthewcheng@gmail.com', '0944448901', 'Tainan, Taiwan', 'ST10', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51023', 'Zoe', 'HO', '2001-03-14', 'Female', '2023-05-10', '2023-05-12', 'DT30', 'Sales Assistant', 'ZoeHO@stitch.com', 'zoeho@gmail.com', '0955559012', 'Yunlin, Taiwan', 'ST10', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51024', 'Nathan', 'KANG', '1990-05-21', 'Male', '2013-05-20', '2013-05-20', 'DT20', 'Senior Accountant', 'NathanKANG@stitch.com', 'nathankang@gmail.com', '0966660123', 'Taipei, Taiwan', 'ST11', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51025', 'Leah', 'YU', '2001-10-28', 'Female', '2023-07-01', '2023-07-01', 'DT30', 'Sales Assistant', 'LeahYU@stitch.com', 'leahyu@gmail.com', '0977771234', 'New Taipei, Taiwan', 'ST90', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51026', 'Benjamin', 'KIM', '1994-02-11', 'Male', '2019-06-10', '2019-06-12', 'DT30', 'Sales Assistant', 'BenjaminKIM@stitch.com', 'benjaminkim@gmail.com', '0911223344', 'Taipei, Taiwan', 'ST10', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51027', 'Victoria', 'SUN', '1997-01-25', 'Female', '2022-03-01', '2022-03-01', 'DT20', 'Finance Specialist', 'VictoriaSUN@stitch.com', 'victoriasun@yahoo.com', '0922113344', 'New Taipei, Taiwan', 'ST10', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51028', 'Oliver', 'CHANG', '1988-06-14', 'Male', '2015-01-07', '2015-01-09', 'DT21', 'Compliance Analyst', 'OliverCHANG@stitch.com', 'oliverchang@hotmail.com', '0933224455', 'Kaohsiung, Taiwan', 'ST10', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51029', 'Eleanor', 'KUO', '1993-02-18', 'Female', '2019-08-20', '2019-08-20', 'DT30', 'Sales Assistant', 'EleanorKUO@stitch.com', 'eleanorkuo@gmail.com', '0955335566', 'Taichung, Taiwan', 'ST10', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51030', 'Ethan', 'FANG', '1985-10-30', 'Male', '2009-01-15', '2009-01-15', 'DT32', 'Marketing Director', 'EthanFANG@stitch.com', 'ethanfang@gmail.com', '0966446677', 'Tainan, Taiwan', 'ST10', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51031', 'Sophia', 'HU', '1999-12-09', 'Female', '2021-04-05', '2021-04-05', 'DT33', 'Logistics Assistant', 'SophiaHU@stitch.com', 'sophiahu@hotmail.com', '0977557788', 'Taoyuan, Taiwan', 'ST20', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51032', 'Caleb', 'LIU', '1990-04-22', 'Male', '2013-07-20', '2013-07-20', 'DT40', 'Software Engineer', 'CalebLIU@stitch.com', 'calebliu@gmail.com', '0988668899', 'Hsinchu, Taiwan', 'ST10', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51033', 'Lily', 'WANG', '1996-07-03', 'Female', '2023-09-15', '2023-09-15', 'DT10', 'HR Intern', 'LilyWANG@stitch.com', 'lilywang@gmail.com', '0999779900', 'Miaoli, Taiwan', 'ST20', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51034', 'Gabriel', 'LIN', '1991-04-05', 'Male', '2018-03-10', '2018-03-12', 'DT20', 'Senior Accountant', 'GabrielLIN@stitch.com', 'gabriellin@yahoo.com', '0910889011', 'Changhua, Taiwan', 'ST10', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51035', 'Anna', 'YANG', '2000-02-20', 'Female', '2023-05-10', '2023-05-10', 'DT21', 'Compliance Intern', 'AnnaYANG@stitch.com', 'annayang@gmail.com', '0921990122', 'Yunlin, Taiwan', 'ST90', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51036', 'Nathan', 'CHEN', '1987-03-12', 'Male', '2011-02-22', '2011-02-22', 'DT30', 'Sales Executive', 'NathanCHEN@stitch.com', 'nathanchen@gmail.com', '0932001233', 'Pingtung, Taiwan', 'ST10', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51037', 'Zoe', 'LI', '1998-11-09', 'Female', '2022-11-30', '2022-12-02', 'DT32', 'Marketing Coordinator', 'ZoeLI@stitch.com', 'zoeli@gmail.com', '0943112344', 'Keelung, Taiwan', 'ST10', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51038', 'Samuel', 'CHIU', '1982-12-07', 'Male', '2005-12-10', '2005-12-10', 'DT33', 'Logistics Manager', 'SamuelCHIU@stitch.com', 'samuelchiu@gmail.com', '0954223455', 'Hualien, Taiwan', 'ST10', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51039', 'Emily', 'WU', '1999-05-05', 'Female', '2023-01-20', '2023-01-20', 'DT40', 'Junior IT Support', 'EmilyWU@stitch.com', 'emilywu@gmail.com', '0965334566', 'Taitung, Taiwan', 'ST90', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51040', 'Henry', 'HSU', '1993-08-14', 'Male', '2017-05-11', '2017-05-11', 'DT10', 'HR Manager', 'HenryHSU@stitch.com', 'henryhsu@gmail.com', '0976445677', 'Penghu, Taiwan', 'ST10', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51041', 'Christina', 'KUO', '2001-05-17', 'Female', '2023-04-07', '2023-04-07', 'DT20', 'Junior Accountant', 'CharlotteKUO@stitch.com', 'christinakuo@gmail.com', '0987556788', 'Taipei, Taiwan', 'ST20', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51042', 'Mason', 'SHIH', '1985-06-23', 'Male', '2012-10-15', '2012-10-15', 'DT21', 'Compliance Manager', 'MasonSHIH@stitch.com', 'masonshih@gmail.com', '0998667899', 'New Taipei, Taiwan', 'ST10', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51043', 'Grace', 'TENG', '1993-12-19', 'Female', '2018-03-27', '2018-03-27', 'DT30', 'Senior Sales Executive', 'GraceTENG@stitch.com', 'graceteng@gmail.com', '0919778900', 'Taichung, Taiwan', 'ST10', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51044', 'Daniel', 'WEN', '1996-10-10', 'Male', '2021-04-18', '2021-04-20', 'DT32', 'Marketing Manager', 'DanielWEN@stitch.com', 'danielwen@gmail.com', '0920889011', 'Kaohsiung, Taiwan', 'ST10', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51045', 'Evelyn', 'LU', '1998-08-02', 'Female', '2022-02-15', '2022-02-15', 'DT33', 'Logistics Intern', 'EvelynLU@stitch.com', 'evelynlu@gmail.com', '0931990122', 'Hsinchu, Taiwan', 'ST90', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51046', 'Owen', 'CHENG', '1984-03-07', 'Male', '2004-10-30', '2004-10-30', 'DT40', 'IT Director', 'OwenCHENG@stitch.com', 'owencheng@gmail.com', '0942001233', 'Tainan, Taiwan', 'ST10', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51047', 'Leah', 'HO', '2001-10-01', 'Female', '2023-07-18', '2023-07-18', 'DT30', 'Sales Intern', 'LeahHO@stitch.com', 'leahho@gmail.com', '0953112344', 'Yunlin, Taiwan', 'ST20', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51048', 'Lucas', 'KANG', '1990-05-11', 'Male', '2014-04-20', '2014-04-20', 'DT20', 'Finance Officer', 'LucasKANG@stitch.com', 'lucaskang@gmail.com', '0964223455', 'Taipei, Taiwan', 'ST10', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51049', 'Chloe', 'YU', '2000-08-28', 'Female', '2023-07-01', '2023-07-01', 'DT10', 'Data Analyst', 'ChloeYU@stitch.com', 'chloeyu@gmail.com', '0975334566', 'New Taipei, Taiwan', 'ST90', '2025-03-06 08:06:09', '2025-03-11 07:29:14'),
('51050', 'Ryan', 'TSAI', '1987-11-19', 'Male', '2010-12-05', '2010-12-05', 'DT30', 'Sales Manager', 'RyanTSAI@stitch.com', 'ryantsai@gmail.com', '0986445677', 'Taichung, Taiwan', 'ST10', '2025-03-06 08:06:09', '2025-03-11 07:29:14');

-- --------------------------------------------------------

-- 資料表結構 `Salary`

CREATE TABLE `Salary` (
  `SalaryID` int NOT NULL,
  `EmployeeID` varchar(10) NOT NULL,
  `DepartmentID` varchar(4) NOT NULL,
  `BaseSalary` decimal(10,2) NOT NULL,
  `Bonus` decimal(10,2) DEFAULT '0.00',
  `CreatedAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `UpdatedAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ;

-- 傾印資料表的資料 `Salary`

INSERT INTO `Salary` (`SalaryID`, `EmployeeID`, `DepartmentID`, `BaseSalary`, `Bonus`, `CreatedAt`, `UpdatedAt`) VALUES
(1, '51001', 'DT10', 35000.00, 5000.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(2, '51002', 'DT10', 42000.00, 6000.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(3, '51003', 'DT20', 52000.00, 7500.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(4, '51004', 'DT21', 55000.00, 8000.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(5, '51005', 'DT30', 33000.00, 4000.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(6, '51006', 'DT32', 47000.00, 6000.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(7, '51007', 'DT33', 45000.00, 6500.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(8, '51008', 'DT40', 68000.00, 10000.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(9, '51009', 'DT30', 33000.00, 4000.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(10, '51010', 'DT20', 70000.00, 12000.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(11, '51011', 'DT30', 40000.00, 5500.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(12, '51012', 'DT30', 75000.00, 13000.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(13, '51013', 'DT32', 33000.00, 4000.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(14, '51014', 'DT33', 62000.00, 9000.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(15, '51015', 'DT40', 58000.00, 7500.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(16, '51016', 'DT10', 80000.00, 15000.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(17, '51017', 'DT30', 40000.00, 5000.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(18, '51018', 'DT21', 90000.00, 20000.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(19, '51019', 'DT30', 68000.00, 12000.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(20, '51020', 'DT32', 75000.00, 13000.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(21, '51021', 'DT33', 35000.00, 4500.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(22, '51022', 'DT40', 85000.00, 18000.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(23, '51023', 'DT30', 30000.00, 0.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(24, '51024', 'DT20', 65000.00, 11000.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(25, '51025', 'DT30', 33000.00, 4000.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(26, '51026', 'DT30', 33000.00, 4000.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(27, '51027', 'DT20', 55000.00, 7500.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(28, '51028', 'DT21', 58000.00, 9000.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(29, '51029', 'DT30', 35000.00, 5000.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(30, '51030', 'DT32', 83000.00, 17000.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(31, '51031', 'DT33', 35000.00, 4500.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(32, '51032', 'DT40', 75000.00, 12000.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(33, '51033', 'DT10', 30000.00, 0.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(34, '51034', 'DT20', 60000.00, 9500.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(35, '51035', 'DT21', 30000.00, 0.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(36, '51036', 'DT30', 75000.00, 13000.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(37, '51037', 'DT32', 52000.00, 7500.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(38, '51038', 'DT33', 67000.00, 12000.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(39, '51039', 'DT40', 33000.00, 4000.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(40, '51040', 'DT10', 80000.00, 15000.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(41, '51041', 'DT20', 30000.00, 0.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(42, '51042', 'DT21', 90000.00, 20000.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(43, '51043', 'DT30', 70000.00, 12000.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(44, '51044', 'DT32', 75000.00, 13000.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(45, '51045', 'DT33', 30000.00, 0.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(46, '51046', 'DT40', 85000.00, 18000.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(47, '51047', 'DT30', 30000.00, 0.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(48, '51048', 'DT20', 60000.00, 9500.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(49, '51049', 'DT10', 33000.00, 4000.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16'),
(50, '51050', 'DT30', 75000.00, 13000.00, '2025-03-06 08:16:16', '2025-03-06 08:16:16');

-- --------------------------------------------------------

-- 資料表結構 `Status`

CREATE TABLE `Status` (
  `StatusID` varchar(4) NOT NULL,
  `StatusName` varchar(50) NOT NULL,
  `Description` text,
  `CreatedAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `UpdatedAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ;

-- 傾印資料表的資料 `Status`

INSERT INTO `Status` (`StatusID`, `StatusName`, `Description`, `CreatedAt`, `UpdatedAt`) VALUES
('ST10', 'Perm', 'Permanent Employee', '2025-03-06 03:00:35', '2025-03-06 03:00:35'),
('ST11', 'Probation', 'Probation Period', '2025-03-06 03:00:35', '2025-03-06 03:00:35'),
('ST19', 'LTA', 'Long-term Absence', '2025-03-06 03:00:35', '2025-03-06 03:00:35'),
('ST20', 'Temp', 'Temporary Employee', '2025-03-06 03:00:35', '2025-03-06 03:00:35'),
('ST90', 'Ext', 'External Employee', '2025-03-06 03:00:35', '2025-03-06 03:00:35');

-- 已傾印資料表的索引

-- 資料表索引 `Department`

ALTER TABLE `Department`
  ADD PRIMARY KEY (`DepartmentID`);

-- 資料表索引 `Employee`

ALTER TABLE `Employee`
  ADD PRIMARY KEY (`EmployeeID`),
  ADD UNIQUE KEY `CompEmail` (`CompEmail`),
  ADD UNIQUE KEY `PrivateEmail` (`PrivateEmail`),
  ADD KEY `DepartmentID` (`DepartmentID`),
  ADD KEY `StatusID` (`StatusID`);


-- 資料表索引 `Salary`

ALTER TABLE `Salary`
  ADD PRIMARY KEY (`SalaryID`),
  ADD KEY `EmployeeID` (`EmployeeID`),
  ADD KEY `DepartmentID` (`DepartmentID`);


-- 資料表索引 `Status`

ALTER TABLE `Status`
  ADD PRIMARY KEY (`StatusID`);


-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)



-- 使用資料表自動遞增(AUTO_INCREMENT) `Salary`

ALTER TABLE `Salary`
  MODIFY `SalaryID` int NOT NULL AUTO_INCREMENT;


-- 已傾印資料表的限制式



-- 資料表的限制式 `Employee`

ALTER TABLE `Employee`
  ADD CONSTRAINT `Employee_ibfk_1` FOREIGN KEY (`DepartmentID`) REFERENCES `Department` (`DepartmentID`),
  ADD CONSTRAINT `Employee_ibfk_2` FOREIGN KEY (`StatusID`) REFERENCES `Status` (`StatusID`);


-- 資料表的限制式 `Salary`

ALTER TABLE `Salary`
  ADD CONSTRAINT `Salary_ibfk_1` FOREIGN KEY (`EmployeeID`) REFERENCES `Employee` (`EmployeeID`),
  ADD CONSTRAINT `Salary_ibfk_2` FOREIGN KEY (`DepartmentID`) REFERENCES `Department` (`DepartmentID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
