CREATE TABLE `books` (
	`id` int NOT NULL AUTO_INCREMENT,
	`isbn_10` char(20) NOT NULL UNIQUE,
	`isbn_13` char(20) UNIQUE,
	`title` char(255) NOT NULL,
	`description` TEXT NOT NULL,
	`language` char(100) NOT NULL,
	`release_date` DATE NOT NULL,
	`genre_id` char(50) NOT NULL,
	`editor_id` int NOT NULL,
	`price_new` int NOT NULL,
	`price_used` int NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `authors` (
	`id` int NOT NULL AUTO_INCREMENT,
	`first_name` char(50) NOT NULL,
	`last_name` char(50) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `book_authors` (
	`author_id` int NOT NULL,
	`book_id` int NOT NULL,
	PRIMARY KEY (`author_id`,`book_id`)
);

CREATE TABLE `genres` (
	`id` char(50) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `editors` (
	`id` int NOT NULL AUTO_INCREMENT,
	`name` char(100) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `transactions` (
	`id` int NOT NULL AUTO_INCREMENT,
	`quantity` int NOT NULL,
	`book_state` char(1) NOT NULL,
	`book_id` int NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `languages` (
	`id` char(100) NOT NULL,
	PRIMARY KEY (`id`)
);

ALTER TABLE `books` ADD CONSTRAINT `books_fk0` FOREIGN KEY (`language`) REFERENCES `languages`(`id`);

ALTER TABLE `books` ADD CONSTRAINT `books_fk1` FOREIGN KEY (`genre_id`) REFERENCES `genres`(`id`);

ALTER TABLE `books` ADD CONSTRAINT `books_fk2` FOREIGN KEY (`editor_id`) REFERENCES `editors`(`id`);

ALTER TABLE `book_authors` ADD CONSTRAINT `book_authors_fk0` FOREIGN KEY (`author_id`) REFERENCES `authors`(`id`);

ALTER TABLE `book_authors` ADD CONSTRAINT `book_authors_fk1` FOREIGN KEY (`book_id`) REFERENCES `books`(`id`);

ALTER TABLE `transactions` ADD CONSTRAINT `transactions_fk0` FOREIGN KEY (`book_id`) REFERENCES `books`(`id`);

