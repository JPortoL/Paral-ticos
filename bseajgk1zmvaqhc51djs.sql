-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: bseajgk1zmvaqhc51djs-mysql.services.clever-cloud.com:3306
-- Tiempo de generación: 23-11-2023 a las 02:34:22
-- Versión del servidor: 8.0.22-13
-- Versión de PHP: 8.2.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bseajgk1zmvaqhc51djs`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clinico`
--

CREATE TABLE `clinico` (
  `id` int NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='funciona';

--
-- Volcado de datos para la tabla `clinico`
--

INSERT INTO `clinico` (`id`, `nombre`, `apellido`, `email`) VALUES
(1, 'Pepe', 'Morales', 'Pepemor.gmail.com'),
(2, 'Rene', 'Casanova Dominguez', 'Renovado@unal.edu.co'),
(3, 'Santiago', 'Mier', 'mier@mier.mier'),
(4, 'Maylen', 'Echavez', 'test@test.com');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `examenes`
--

CREATE TABLE `examenes` (
  `id` int NOT NULL,
  `tipo_id` int NOT NULL,
  `fecha_creacion` date NOT NULL,
  `fecha_interpretacion` date DEFAULT NULL,
  `paciente_id` int NOT NULL,
  `resultado_id` int DEFAULT NULL,
  `estado` varchar(50) NOT NULL,
  `clinico_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `examenes`
--

INSERT INTO `examenes` (`id`, `tipo_id`, `fecha_creacion`, `fecha_interpretacion`, `paciente_id`, `resultado_id`, `estado`, `clinico_id`) VALUES
(10, 2, '2023-11-22', '2023-11-22', 1213, 10, 'finalizado', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `resultados`
--

CREATE TABLE `resultados` (
  `id` int NOT NULL,
  `fecha` date NOT NULL,
  `valor_numerico` double DEFAULT NULL,
  `valor_texto` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `valor_booleano` tinyint(1) DEFAULT NULL,
  `clinico_id` int NOT NULL,
  `interpretacion` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `clinico_interpreta_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `resultados`
--

INSERT INTO `resultados` (`id`, `fecha`, `valor_numerico`, `valor_texto`, `valor_booleano`, `clinico_id`, `interpretacion`, `clinico_interpreta_id`) VALUES
(10, '2023-11-22', 10.6, NULL, NULL, 2, 'Usted está muy mal', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_examen`
--

CREATE TABLE `tipo_examen` (
  `id` int NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `es_numero` tinyint(1) NOT NULL DEFAULT '0',
  `limite_superior` double DEFAULT NULL,
  `limite_inferior` double DEFAULT NULL,
  `es_imagen` tinyint(1) NOT NULL DEFAULT '0',
  `es_texto` tinyint(1) NOT NULL DEFAULT '0',
  `es_booleano` tinyint(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `tipo_examen`
--

INSERT INTO `tipo_examen` (`id`, `nombre`, `es_numero`, `limite_superior`, `limite_inferior`, `es_imagen`, `es_texto`, `es_booleano`) VALUES
(1, 'sida', 0, NULL, NULL, 0, 0, 1),
(2, 'nivel glucosa sangre', 1, 10, 2, 0, 0, 0),
(3, 'radiografia', 0, NULL, NULL, 1, 0, 0),
(4, 'lesiones', 0, NULL, NULL, 0, 1, 0);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `clinico`
--
ALTER TABLE `clinico`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email_unique` (`email`);

--
-- Indices de la tabla `examenes`
--
ALTER TABLE `examenes`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `unique` (`resultado_id`),
  ADD KEY `tipo_id` (`tipo_id`),
  ADD KEY `clinico_interpretador_id` (`clinico_id`);

--
-- Indices de la tabla `resultados`
--
ALTER TABLE `resultados`
  ADD PRIMARY KEY (`id`),
  ADD KEY `clinico_id` (`clinico_id`),
  ADD KEY `clinico_interpreta_id` (`clinico_interpreta_id`);

--
-- Indices de la tabla `tipo_examen`
--
ALTER TABLE `tipo_examen`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `clinico`
--
ALTER TABLE `clinico`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `examenes`
--
ALTER TABLE `examenes`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `resultados`
--
ALTER TABLE `resultados`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `tipo_examen`
--
ALTER TABLE `tipo_examen`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `examenes`
--
ALTER TABLE `examenes`
  ADD CONSTRAINT `examenes_ibfk_1` FOREIGN KEY (`tipo_id`) REFERENCES `tipo_examen` (`id`),
  ADD CONSTRAINT `examenes_ibfk_2` FOREIGN KEY (`resultado_id`) REFERENCES `resultados` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `FK_clinico_id` FOREIGN KEY (`clinico_id`) REFERENCES `clinico` (`id`);

--
-- Filtros para la tabla `resultados`
--
ALTER TABLE `resultados`
  ADD CONSTRAINT `resultados_ibfk_1` FOREIGN KEY (`clinico_id`) REFERENCES `clinico` (`id`),
  ADD CONSTRAINT `resultados_ibfk_2` FOREIGN KEY (`clinico_interpreta_id`) REFERENCES `clinico` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
