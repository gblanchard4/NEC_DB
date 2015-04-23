# NEC DB
A relational database using Python and Postgres for Ferris Lab

## Patient Table and Example Patients
CREATE TABLE Patients(PatientID VARCHAR(20) PRIMARY KEY, DOB DATE, Race CHARACTER(1), GestAge INTEGER, BirthWt INTEGER, GestWtAgeAprop CHARACTER(1), Delivery CHARACTER(1), ApgarB INTEGER, Apgar5 INTEGER, Resusc CHAR(1), Rom INTEGER, MatHX TEXT, MatMed TEXT );

INSERT INTO Patients('JN01', 20150422, 'W', 28, 1234, 'Y', 'V', 1, 3, 'B', 1, 'zxcvzxvzcxvzxc'. 'asdfasdfadsf');