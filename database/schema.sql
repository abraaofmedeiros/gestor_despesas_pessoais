CREATE TABLE IF NOT EXISTS `usuario` (
	`id` integer primary key NOT NULL UNIQUE,
	`nome` TEXT NOT NULL,
	`username` TEXT NOT NULL UNIQUE,
	`senha` TEXT NOT NULL,
	`meta_mensal` REAL NOT NULL
);
CREATE TABLE IF NOT EXISTS `categoria` (
	`id` integer primary key NOT NULL UNIQUE,
	`usuario` INTEGER NOT NULL,
	`nome_categoria` INTEGER NOT NULL,
FOREIGN KEY(`usuario`) REFERENCES `usuario`(`id`)
);
CREATE TABLE IF NOT EXISTS `despesa` (
	`id` integer primary key NOT NULL UNIQUE,
	`usuario` INTEGER NOT NULL,
	`categoria` INTEGER NOT NULL,
	`nome_despesa` TEXT NOT NULL,
	`valor` REAL NOT NULL,
	`data` REAL NOT NULL,
FOREIGN KEY(`usuario`) REFERENCES `usuario`(`id`),
FOREIGN KEY(`categoria`) REFERENCES `categoria`(`id`)
);