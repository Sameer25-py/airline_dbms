DROP DATABASE IF EXISTS Flight_Management;
CREATE DATABASE Flight_Management;
USE Flight_Management;
/*------------------------------------------------------------------------------------------- */

/* -------------------- Passenger ----------------------------------*/

CREATE TABLE PASSENGER (
  Pass_ID integer AUTO_INCREMENT,
  Pass_CNIC  char(13),
  Name varchar(255),
  Nationality varchar(25),
  Address varchar(255),
  Phone_no char(13) UNIQUE,
  PRIMARY KEY (Pass_ID)
);


/* ----------------------------- Reciptionist -------------------------- */

CREATE TABLE RECEPTIONIST (
  Receptionist_ID integer AUTO_INCREMENT,
  CNIC char(13) UNIQUE,
  Name varchar(50),
  Phone_no char(11) UNIQUE,
  PRIMARY KEY (Receptionist_ID,CNIC,Phone_no)
);

/* --------------------------------------- Admin ----------------------- */

CREATE TABLE ADMINISTRATOR (
  Admin_ID integer AUTO_INCREMENT,
  Name varchar(50),
  CNIC char(13) UNIQUE,
  Phone_no char(11) UNIQUE,
  PRIMARY KEY (Admin_ID,CNIC,Phone_no)
);

/* ----------------------------------- Plane -------------------------*/

CREATE TABLE PLANE (
  
  Plane_Name char(7) UNIQUE,
  PRIMARY KEY(Plane_Name)
  
  );

/* ----------------------------------------- Flights --------------------- */

CREATE TABLE FLIGHTS (
  Flight_ID integer AUTO_INCREMENT,
  Departure_City  char(3),
  Arrival_City  char(3),
  Departure_time TIME NOT NULL,
  Arrival_time TIME NOT NULL,
  Price int(20),
  Plane_Name char(7) REFERENCES PLANE(Plane_Name),
  Flight_date  DATE NOT NULL,
  PRIMARY KEY (Flight_ID)

);
/*--------------------------------- HISTORY ---------------------------*/

CREATE TABLE HISTORY(
 ID integer AUTO_INCREMENT,
 Flight_id int REFERENCES FLIGHTS(Flight_id),
 Pass_id int REFERENCES PASSENGER (Pass_ID),
 PRIMARY KEY (ID)
);

