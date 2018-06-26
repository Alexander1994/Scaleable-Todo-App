CREATE DATABASE scaleable_todo_app OWNER postgres;

\connect scaleable_todo_app

CREATE EXTENSION pgcrypto;

CREATE TABLE Users (
    id          SERIAL       PRIMARY KEY,
    email       VARCHAR(255) NOT NULL,
    password    TEXT         NOT NULL
);

/* Temp user for testing */
INSERT INTO Users (email, password) VALUES (
  'admin@admin.co',
  crypt('secret', gen_salt('bf'))
);
