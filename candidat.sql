-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : Dim 08 nov. 2020 à 17:18
-- Version du serveur :  10.4.13-MariaDB
-- Version de PHP : 7.3.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `hatem`
--

-- --------------------------------------------------------

--
-- Structure de la table `candidat`
--

CREATE TABLE `candidat` (
  `id_C` int(11) NOT NULL,
  `Nom` varchar(30) NOT NULL,
  `Prenom` varchar(30) NOT NULL,
  `e_mail` varchar(200) NOT NULL,
  `Date_naissance` date NOT NULL,
  `num_tel` varchar(8) NOT NULL,
  `dispo` int(11) NOT NULL,
  `nb_ann_exp` int(11) NOT NULL,
  `msg` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `candidat`
--

INSERT INTO `candidat` (`id_C`, `Nom`, `Prenom`, `e_mail`, `Date_naissance`, `num_tel`, `dispo`, `nb_ann_exp`, `msg`) VALUES
(1, 'ouerfelli', 'amal', 'amalamal@gmail.com', '2020-11-26', '25631458', 1, 2, 'hhhhh'),
(2, 'juini', 'hatem', 'juini@gmail.com', '2020-11-04', '25987630', 2, 1, 'chay'),
(26, 'Ouerfelli', 'Amal', 'ouerfelliiamal@gmail.com', '2002-07-08', '92226657', 2, 2, 'h'),
(27, 'Ouerfelli', 'Amal', 'ouerfelliial@gmail.com', '2002-07-08', '92226658', 2, 1, 'hhh');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `candidat`
--
ALTER TABLE `candidat`
  ADD PRIMARY KEY (`id_C`),
  ADD UNIQUE KEY `num_tel` (`num_tel`),
  ADD UNIQUE KEY `e_mail` (`e_mail`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `candidat`
--
ALTER TABLE `candidat`
  MODIFY `id_C` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
