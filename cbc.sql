-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 19, 2024 at 08:51 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cbc`
--

-- --------------------------------------------------------

--
-- Table structure for table `anemia_test_results`
--

CREATE TABLE `anemia_test_results` (
  `test_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `LYM` float DEFAULT NULL,
  `NEUT` float DEFAULT NULL,
  `MONO` float DEFAULT NULL,
  `EOS` float DEFAULT NULL,
  `BASO` float DEFAULT NULL,
  `HGB` float DEFAULT NULL,
  `HCT` float DEFAULT NULL,
  `MCV` float DEFAULT NULL,
  `MCH` float DEFAULT NULL,
  `MCHC` float DEFAULT NULL,
  `RDW` float DEFAULT NULL,
  `PLT` float DEFAULT NULL,
  `MPV` float DEFAULT NULL,
  `RBC` float DEFAULT NULL,
  `WBC` float DEFAULT NULL,
  `diseased` int(11) DEFAULT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `covid_test_results`
--

CREATE TABLE `covid_test_results` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `LYM` float DEFAULT NULL,
  `NEUT` float DEFAULT NULL,
  `MONO` float DEFAULT NULL,
  `EOS` float DEFAULT NULL,
  `BASO` float DEFAULT NULL,
  `HGB` float DEFAULT NULL,
  `HCT` float DEFAULT NULL,
  `MCV` float DEFAULT NULL,
  `MCH` float DEFAULT NULL,
  `MCHC` float DEFAULT NULL,
  `RDW` float DEFAULT NULL,
  `PLT` float DEFAULT NULL,
  `MPV` float DEFAULT NULL,
  `diseased` int(11) DEFAULT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `diabetes_test_results`
--

CREATE TABLE `diabetes_test_results` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `HGB` float DEFAULT NULL,
  `MCHC` float DEFAULT NULL,
  `MCH` float DEFAULT NULL,
  `MCV` float DEFAULT NULL,
  `MPV` float DEFAULT NULL,
  `RBC` float DEFAULT NULL,
  `PLT` float DEFAULT NULL,
  `RDW` float DEFAULT NULL,
  `WBC` float DEFAULT NULL,
  `diseased` int(11) DEFAULT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `selected_progress` varchar(255) DEFAULT NULL,
  `feedback` text DEFAULT NULL,
  `satisfaction_level` int(11) DEFAULT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `news`
--

CREATE TABLE `news` (
  `id` int(11) NOT NULL,
  `title` text DEFAULT NULL,
  `content` text DEFAULT NULL,
  `image_url` text DEFAULT NULL,
  `link` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `news`
--

INSERT INTO `news` (`id`, `title`, `content`, `image_url`, `link`) VALUES
(1, 'LO NGẠI LÀN SÓNG COVID 19 MỚI', 'Theo Bộ Y tế Malaysia, số ca mắc mới COVID-19 đã tăng gần 15%, lên 1.230 ca trong tuần từ ngày 12 - 18/5.', 'image1.jpg', 'https://covid19.gov.vn/'),
(2, 'BỆNH THIẾU MÁU: NGUYÊN NHÂN, TRIỆU CHỨNG', 'Thiếu máu là một bệnh lý nguy hiểm, có thể gây suy kiệt và dẫn đến tử vong. Người bệnh cần biết các triệu chứng thiếu máu ', 'image2.jpg', 'https://tamanhhospital.vn/thieu-mau/');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `anemia_test_results`
--
ALTER TABLE `anemia_test_results`
  ADD PRIMARY KEY (`test_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `covid_test_results`
--
ALTER TABLE `covid_test_results`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `diabetes_test_results`
--
ALTER TABLE `diabetes_test_results`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_user` (`user_id`);

--
-- Indexes for table `news`
--
ALTER TABLE `news`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `anemia_test_results`
--
ALTER TABLE `anemia_test_results`
  MODIFY `test_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `covid_test_results`
--
ALTER TABLE `covid_test_results`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `diabetes_test_results`
--
ALTER TABLE `diabetes_test_results`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `feedback`
--
ALTER TABLE `feedback`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `news`
--
ALTER TABLE `news`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `anemia_test_results`
--
ALTER TABLE `anemia_test_results`
  ADD CONSTRAINT `anemia_test_results_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE SET NULL;

--
-- Constraints for table `covid_test_results`
--
ALTER TABLE `covid_test_results`
  ADD CONSTRAINT `covid_test_results_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE SET NULL;

--
-- Constraints for table `diabetes_test_results`
--
ALTER TABLE `diabetes_test_results`
  ADD CONSTRAINT `diabetes_test_results_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE SET NULL;

--
-- Constraints for table `feedback`
--
ALTER TABLE `feedback`
  ADD CONSTRAINT `feedback_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE SET NULL;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
