-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Hôte : 172.17.0.3
-- Généré le : mer. 24 mars 2021 à 23:11
-- Version du serveur :  5.6.38-log
-- Version de PHP : 7.4.4
USE ProjetFilRouge;

DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS products CASCADE;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `ProjetFilRouge`
--

-- --------------------------------------------------------

--
-- Structure de la table `products`
--

CREATE TABLE `products` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `nom` varchar(50) COLLATE latin1_bin NOT NULL,
  `description` varchar(300) COLLATE latin1_bin NOT NULL,
  `qte` bigint(20) DEFAULT NULL,
  `prix` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_bin;

--
-- Déchargement des données de la table `products`
--

INSERT INTO `products` (`id`, `nom`, `description`, `qte`, `prix`) VALUES
(1, 'Aspirateur', 'Ceci est un bel aspirateur', 652, 199.99),
(2, 'Lave-vaisselle', 'Ceci est un beau lave-vaisselle', 74563, 599.99);

-- --------------------------------------------------------

--
-- Structure de la table `users`
--

CREATE TABLE `users` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `nom` varchar(60) COLLATE latin1_bin NOT NULL,
  `prenom` varchar(80) COLLATE latin1_bin NOT NULL,
  `mail` varchar(100) COLLATE latin1_bin NOT NULL,
  `telephone` varchar(10) COLLATE latin1_bin DEFAULT NULL,
  `role` enum('admin','membre') COLLATE latin1_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_bin;

--
-- Déchargement des données de la table `users`
--

INSERT INTO `users` (`id`, `nom`, `prenom`, `mail`, `telephone`, `role`) VALUES
(1, 'Bleuse', 'axel', 'axel.bleuse@test.com', '0687563421', 'Membre'),
(2, 'root', 'root', 'root@test.com', '0345678521', 'Admin');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `products`
--
ALTER TABLE `products`
  ADD UNIQUE KEY `product_id` (`id`);

--
-- Index pour la table `users`
--
ALTER TABLE `users`
  ADD UNIQUE KEY `user_id` (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `products`
--
ALTER TABLE `products`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pour la table `users`
--
ALTER TABLE `users`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
