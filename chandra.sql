CREATE TABLE `auto_stats` (
	`stat_id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
	`c_ts` INT(10) UNSIGNED NOT NULL,
	`name` VARCHAR(255) NOT NULL COLLATE 'utf8_general_ci',
	`description` TEXT NOT NULL COLLATE 'utf8_general_ci',
	`function` VARCHAR(255) NOT NULL COLLATE 'utf8_general_ci',
	`status_id` INT(10) UNSIGNED NOT NULL,
	`template_id` INT(10) UNSIGNED NOT NULL,
	`active` INT(10) UNSIGNED NOT NULL DEFAULT '1',
	`active_filters` VARCHAR(255) NOT NULL COLLATE 'utf8_general_ci',
	PRIMARY KEY (`stat_id`) USING BTREE,
	UNIQUE INDEX `function` (`function`) USING BTREE,
	INDEX `template_id` (`template_id`) USING BTREE
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB
AUTO_INCREMENT=3;


CREATE TABLE `auto_stat_casinos` (
	`entry_id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
	`c_ts` INT(10) UNSIGNED NOT NULL,
	`stat_id` INT(10) UNSIGNED NOT NULL,
	`casino_id` INT(10) UNSIGNED NOT NULL,
	PRIMARY KEY (`entry_id`) USING BTREE,
	INDEX `stat_id` (`stat_id`, `casino_id`) USING BTREE
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB
AUTO_INCREMENT=8
;


