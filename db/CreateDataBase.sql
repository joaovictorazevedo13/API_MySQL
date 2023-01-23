USE api_mysql

CREATE TABLE `api_mysql`.`carros` (
  `id_Carros` INT NOT NULL AUTO_INCREMENT,
  `marca` VARCHAR(100) NOT NULL,
  `modelo` VARCHAR(100) NOT NULL,
  `ano` INT NOT NULL,
  PRIMARY KEY (`id_Carros`));