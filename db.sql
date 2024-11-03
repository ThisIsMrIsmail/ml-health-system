
CREATE TABLE users (
  user_id INT PRIMARY KEY AUTO_INCREMENT,
  user_name VARCHAR(255) NOT NULL,
  user_code VARCHAR(255) NOT NULL,
  user_gender VARCHAR(255),
  user_username VARCHAR(255) NOT NULL,
  user_password VARCHAR(255) NOT NULL,
  user_additional_info TEXT,
  hospital_id INT
);

CREATE TABLE hospitals (
  hospital_id INT PRIMARY KEY AUTO_INCREMENT,
  hospital_name VARCHAR(255) NOT NULL,
  hospital_code VARCHAR(255) NOT NULL,
  location_id INT
);

CREATE TABLE locations (
  location_id INT PRIMARY KEY AUTO_INCREMENT,
  location_address TEXT NOT NULL,
  location_governorate VARCHAR(255) NOT NULL,
  location_nation VARCHAR(255) NOT NULL
);

CREATE TABLE patients (
  patient_id INT PRIMARY KEY AUTO_INCREMENT,
  patient_name VARCHAR(255) NOT NULL,
  patient_pregnancy_status VARCHAR(255) NOT NULL,
  patient_address TEXT NOT NULL,
  patient_code VARCHAR(255) NOT NULL,
  patient_age VARCHAR(255) NOT NULL,
  patient_gender VARCHAR(255) NOT NULL,
  patient_no_of_births VARCHAR(255) NOT NULL,
  patient_phone_no VARCHAR(255) NOT NULL,
  hospital_id INT
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
  patient_id INT
);

ALTER TABLE users
  ADD FOREIGN KEY (hospital_id) REFERENCES hospital (hospital_id);

ALTER TABLE patient
  ADD FOREIGN KEY (hospital_id) REFERENCES hospital (hospital_id);
  
ALTER TABLE hospital
  ADD FOREIGN KEY (location_id) REFERENCES location (location_id);

ALTER TABLE biological_indicators
  ADD FOREIGN KEY (patient_id) REFERENCES patient (patient_id);


-- Insert data into location table
INSERT INTO locations (location_address, location_governorate, location_nation)
VALUES 
  ('1234 Main St, Hurghada', 'Red Sea', 'Egypt'),
  ('5678 Second Ave, Cairo', 'Cairo', 'Egypt'),
  ('9101 Third Blvd, Alexandria', 'Alexandria', 'Egypt'),
  ('4321 Fifth St, Giza', 'Giza', 'Egypt'),
  ('8765 Palm Ave, Luxor', 'Luxor', 'Egypt'),
  ('3456 Olive Rd, Aswan', 'Aswan', 'Egypt'),
  ('6543 Cedar Blvd, Sharm El-Sheikh', 'South Sinai', 'Egypt'),
  ('7890 Walnut St, Port Said', 'Port Said', 'Egypt'),
  ('2345 Maple Ave, Mansoura', 'Dakahlia', 'Egypt'),
  ('6789 Birch Rd, Sohag', 'Sohag', 'Egypt');

-- Insert data into hospital table
INSERT INTO hospitals (hospital_name, hospital_code, location_id)
VALUES 
  ('Hurghada General Hospital', 'HGH123', 1),
  ('Cairo University Hospital', 'CUH456', 2),
  ('Alexandria Medical Center', 'AMC789', 3),
  ('Giza Health Clinic', 'GHC234', 4),
  ('Luxor Health Center', 'LHC567', 5),
  ('Aswan Regional Hospital', 'ARH890', 6),
  ('Sharm El-Sheikh Medical Facility', 'SSMF345', 7),
  ('Port Said Hospital', 'PSH678', 8),
  ('Mansoura Medical Clinic', 'MMC910', 9),
  ('Sohag Health Institute', 'SHI112', 10);

-- Insert data into users table
INSERT INTO users (user_name, user_code, user_gender, user_username, user_password, user_additional_info, hospital_id)
VALUES 
  ('Dr. Ahmed Hassan', 'DR001', 'Male', 'ahmed_hassan', 'password123', 'Specialist in Cardiology', 1),
  ('Dr. Sarah Ali', 'DR002', 'Female', 'sarah_ali', 'password123', 'Pediatrician', 2),
  ('Dr. Youssef Ibrahim', 'DR003', 'Male', 'youssef_ibrahim', 'password123', 'Orthopedic Surgeon', 3),
  ('Dr. Mona Youssef', 'DR004', 'Female', 'mona_youssef', 'password123', 'Dermatologist', 4),
  ('Dr. Kareem Omar', 'DR005', 'Male', 'kareem_omar', 'password123', 'Radiologist', 5),
  ('Dr. Noura Fathy', 'DR006', 'Female', 'noura_fathy', 'password123', 'Neurologist', 6),
  ('Dr. Tarek Mahmoud', 'DR007', 'Male', 'tarek_mahmoud', 'password123', 'General Practitioner', 7),
  ('Dr. Layla Said', 'DR008', 'Female', 'layla_said', 'password123', 'Oncologist', 8),
  ('Dr. Amr Ali', 'DR009', 'Male', 'amr_ali', 'password123', 'Gynecologist', 9),
  ('Dr. Hana Rashed', 'DR010', 'Female', 'hana_rashed', 'password123', 'Pulmonologist', 10);

-- Insert data into patient table
INSERT INTO patients (patient_name, patient_pregnancy_status, patient_address, patient_code, patient_age, patient_gender, patient_no_of_births, patient_phone_no, hospital_id)
VALUES 
  ('Amina Mahmoud', 'Not Pregnant', '1234 Elm St, Cairo', 'PT001', '45', 'Female', '2', '01000000001', 2),
  ('Karim Adel', 'Not Pregnant', '5678 Oak St, Hurghada', 'PT002', '32', 'Male', '0', '01000000002', 1),
  ('Noura Sayed', 'Pregnant', '9101 Pine St, Alexandria', 'PT003', '29', 'Female', '1', '01000000003', 3),
  ('Salma Hossam', 'Pregnant', '4321 Palm St, Giza', 'PT004', '27', 'Female', '1', '01000000004', 4),
  ('Yassin Fathy', 'Not Pregnant', '8765 Willow Ave, Luxor', 'PT005', '60', 'Male', '0', '01000000005', 5),
  ('Hanan Raouf', 'Pregnant', '3456 Cypress Rd, Aswan', 'PT006', '31', 'Female', '2', '01000000006', 6),
  ('Ali Ghanem', 'Not Pregnant', '6543 Cherry St, Sharm El-Sheikh', 'PT007', '40', 'Male', '0', '01000000007', 7),
  ('Dina Lotfy', 'Not Pregnant', '7890 Walnut Blvd, Port Said', 'PT008', '36', 'Female', '3', '01000000008', 8),
  ('Sara El Masry', 'Pregnant', '2345 Cedar Ave, Mansoura', 'PT009', '28', 'Female', '0', '01000000009', 9),
  ('Omar Nasr', 'Not Pregnant', '6789 Maple St, Sohag', 'PT010', '50', 'Male', '0', '01000000010', 10);

-- Insert 3 biological indicator entries for each patient

-- Patient PT001
INSERT INTO biological_indicators (bio_indicators_patient_code, bio_indicators_date, bio_indicators_time, bio_indicators_average_temperature, bio_indicators_blood_pressure, bio_indicators_blood_sugar, bio_indicators_health_status, patient_id)
VALUES 
  ('PT001', '2024-10-01', '10:30 AM', '36.6', '120/80', '90', 'Stable', 1),
  ('PT001', '2024-10-02', '11:15 AM', '36.7', '118/79', '95', 'Stable', 1),
  ('PT001', '2024-10-03', '9:45 AM', '36.8', '115/78', '88', 'Stable', 1),
  ('PT001', '2024-10-04', '8:00 AM', '37.0', '117/76', '93', 'Slightly Elevated', 1),
  ('PT001', '2024-10-05', '10:00 AM', '36.5', '116/75', '90', 'Stable', 1),
  ('PT001', '2024-10-06', '12:30 PM', '36.9', '118/80', '92', 'Stable', 1),
  ('PT001', '2024-10-07', '2:00 PM', '37.1', '120/83', '98', 'Stable', 1),
  ('PT001', '2024-10-08', '3:30 PM', '37.2', '122/85', '110', 'Elevated', 1),
  ('PT001', '2024-10-09', '4:15 PM', '36.8', '119/79', '85', 'Stable', 1),
  ('PT001', '2024-10-10', '5:00 PM', '36.7', '117/78', '87', 'Stable', 1);

-- Patient PT002
INSERT INTO biological_indicators (bio_indicators_patient_code, bio_indicators_date, bio_indicators_time, bio_indicators_average_temperature, bio_indicators_blood_pressure, bio_indicators_blood_sugar, bio_indicators_health_status, patient_id)
VALUES 
  ('PT002', '2024-10-01', '10:30 AM', '37.0', '130/85', '100', 'Stable', 2),
  ('PT002', '2024-10-02', '11:15 AM', '37.1', '128/82', '102', 'Stable', 2),
  ('PT002', '2024-10-03', '9:45 AM', '36.9', '127/83', '105', 'Stable', 2),
  ('PT002', '2024-10-04', '8:00 AM', '36.8', '125/80', '108', 'Slightly Elevated', 2),
  ('PT002', '2024-10-05', '10:00 AM', '37.2', '132/86', '110', 'Stable', 2),
  ('PT002', '2024-10-06', '12:30 PM', '37.3', '133/88', '115', 'Elevated', 2),
  ('PT002', '2024-10-07', '2:00 PM', '36.7', '131/84', '97', 'Stable', 2),
  ('PT002', '2024-10-08', '3:30 PM', '37.0', '130/85', '99', 'Stable', 2),
  ('PT002', '2024-10-09', '4:15 PM', '36.8', '129/82', '104', 'Stable', 2),
  ('PT002', '2024-10-10', '5:00 PM', '37.1', '128/81', '107', 'Stable', 2);

-- Patient PT003
INSERT INTO biological_indicators (bio_indicators_patient_code, bio_indicators_date, bio_indicators_time, bio_indicators_average_temperature, bio_indicators_blood_pressure, bio_indicators_blood_sugar, bio_indicators_health_status, patient_id)
VALUES 
  ('PT003', '2024-10-01', '10:30 AM', '36.8', '115/75', '95', 'Stable', 3),
  ('PT003', '2024-10-02', '11:15 AM', '36.9', '114/74', '98', 'Stable', 3),
  ('PT003', '2024-10-03', '9:45 AM', '36.7', '113/73', '94', 'Stable', 3),
  ('PT003', '2024-10-04', '8:00 AM', '37.1', '116/78', '99', 'Slightly Elevated', 3),
  ('PT003', '2024-10-05', '10:00 AM', '36.5', '112/70', '92', 'Stable', 3),
  ('PT003', '2024-10-06', '12:30 PM', '36.8', '115/75', '100', 'Stable', 3),
  ('PT003', '2024-10-07', '2:00 PM', '37.2', '117/79', '103', 'Stable', 3),
  ('PT003', '2024-10-08', '3:30 PM', '36.6', '113/72', '91', 'Stable', 3),
  ('PT003', '2024-10-09', '4:15 PM', '37.0', '116/78', '98', 'Stable', 3),
  ('PT003', '2024-10-10', '5:00 PM', '36.7', '114/75', '96', 'Stable', 3);