DROP DATABASE IF EXISTS ml_db;

CREATE DATABASE ml_db;
USE ml_db;

CREATE TABLE users (
  user_id INT PRIMARY KEY AUTO_INCREMENT,
  user_name VARCHAR(255) NOT NULL,
  user_gender VARCHAR(255) NOT NULL,
  user_code VARCHAR(255) NOT NULL,
  user_username VARCHAR(255) NOT NULL,
  user_password VARCHAR(255) NOT NULL,
  user_additional_info TEXT,
  hospital_id INT NOT NULL
);

CREATE TABLE hospital (
  hospital_id INT PRIMARY KEY AUTO_INCREMENT,
  hospital_name VARCHAR(255) NOT NULL,
  hospital_code VARCHAR(255) NOT NULL,
  location_id INT NOT NULL
);

CREATE TABLE location (
  location_id INT PRIMARY KEY AUTO_INCREMENT,
  location_address TEXT NOT NULL,
  location_governorate VARCHAR(255) NOT NULL,
  location_nation VARCHAR(255) NOT NULL
);

CREATE TABLE patient (
  patient_id INT PRIMARY KEY AUTO_INCREMENT,
  patient_name VARCHAR(255) NOT NULL,
  patient_pregnancy_status VARCHAR(255) NOT NULL,
  patient_address TEXT NOT NULL,
  patient_code VARCHAR(255) NOT NULL,
  patient_age VARCHAR(255) NOT NULL,
  patient_gender VARCHAR(255) NOT NULL,
  patient_no_of_births VARCHAR(255) NOT NULL,
  patient_phone_no VARCHAR(255) NOT NULL,
  hospital_id INT NOT NULL
);

CREATE TABLE biological_indicators (
  bio_indicators_id INT PRIMARY KEY AUTO_INCREMENT,
  bio_indicators_patient_code VARCHAR(255) NOT NULL,
  bio_indicators_date TEXT NOT NULL,
  bio_indicators_time VARCHAR(255) NOT NULL,
  bio_indicators_average_temperature VARCHAR(255) NOT NULL,
  bio_indicators_blood_pressure VARCHAR(255) NOT NULL,
  bio_indicators_blood_sugar VARCHAR(255) NOT NULL,
  bio_indicators_health_status VARCHAR(255) NOT NULL,
  patient_id INT NOT NULL
);

ALTER TABLE users
  ADD FOREIGN KEY (hospital_id) REFERENCES hospital (hospital_id);

ALTER TABLE patient
  ADD FOREIGN KEY (hospital_id) REFERENCES hospital (hospital_id);
  
ALTER TABLE hospital
  ADD FOREIGN KEY (location_id) REFERENCES location (location_id);

ALTER TABLE biological_indicators
  ADD FOREIGN KEY (patient_id) REFERENCES patient (patient_id);