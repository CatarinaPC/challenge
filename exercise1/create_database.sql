DROP TABLE IF EXISTS Scores;

CREATE TABLE Scores (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  patient_id INTEGER, -- FK to Patients table
  scores TEXT, -- json data
  date DATE
);

INSERT INTO Scores (patient_id, scores, date) VALUES
(1323, "{'satisfaction': 9, 'pain': 2, 'fatigue': 2}", "2020-06-25"),
(9032, "{'satisfaction': 2, 'pain': 7, 'fatigue': 5}", "2020-06-30"),
(2331, "{'satisfaction': 7, 'pain': 1, 'fatigue': 1}", "2020-07-05"),
(2303, "{'satisfaction': 8, 'pain': 9, 'fatigue': 0}", "2020-07-12"),
(1323, "{'satisfaction': 10, 'pain': 0, 'fatigue': 0}", "2020-07-09"),
(2331, "{'satisfaction': 8, 'pain': 9, 'fatigue': 5}", "2020-07-20");