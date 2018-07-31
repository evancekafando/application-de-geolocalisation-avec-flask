# sudo -u postgresql psql
# \c postgresql  -> You are now connected to database "postgresql" as user "postgresql".

CREATE TABLE users (
	uid serial PRIMARY KEY,
	prenom VARCHAR(100) not null,
	nom VARCHAR(100) not null,
	email VARCHAR(120) not null unique,
	pwdhash VARCHAR(100) not null
);




