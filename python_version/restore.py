import psycopg2
from pymongo import MongoClient


#================================
#      RESTORE POSTGRESQL
#================================
connection = psycopg2.connect(database="music4life", user='postgres', password='postgres', host="localhost", port=5432)

connection.autocommit = True
cursor = connection.cursor()

sql_context="""

DROP TABLE IF EXISTS concerti;
DROP TABLE IF EXISTS cantanti;
DROP TABLE IF EXISTS citta;

CREATE TABLE CANTANTI (
  id SERIAL PRIMARY KEY,
  nome varchar,
  cognome varchar,
  citta_nascita int
);

CREATE TABLE CITTA (
  id SERIAL PRIMARY KEY,
  nome varchar,
  provincia varchar,
  regione varchar
);

CREATE TABLE CONCERTI (
  id SERIAL PRIMARY KEY,
  cantante int,
  citta int
);

ALTER TABLE CANTANTI ADD FOREIGN KEY ("citta_nascita") REFERENCES "citta" ("id");

ALTER TABLE CONCERTI ADD FOREIGN KEY ("cantante") REFERENCES "cantanti" ("id");

ALTER TABLE CONCERTI ADD FOREIGN KEY ("citta") REFERENCES "citta" ("id");
INSERT INTO CITTA VALUES (1, 'Pomezia', 'Roma', 'Lazio');
INSERT INTO CITTA VALUES (2, 'Pompei', 'Napoli', 'Campania'); 
INSERT INTO CITTA VALUES (3, 'San Menaio', 'Foggia', 'Puglia');
INSERT INTO CITTA VALUES (4, 'Ronciglione', 'Viterbo', 'Lazio'); 
INSERT INTO CITTA VALUES (5, 'Rocca Di Papa', 'Roma', 'Lazio'); 

INSERT INTO CANTANTI VALUES (1, 'Alex', 'Verdi', 1);
INSERT INTO CANTANTI VALUES (2, 'Michael', 'Back', 1); 
INSERT INTO CANTANTI VALUES (3, 'Illis', 'Mick', 2);
INSERT INTO CANTANTI VALUES (4, 'Iorio', 'Leon', 3); 

INSERT INTO CONCERTI VALUES (1, 1, 5);
INSERT INTO CONCERTI VALUES (2, 1, 4); 
INSERT INTO CONCERTI VALUES (3, 2, 1);
INSERT INTO CONCERTI VALUES (4, 3, 2);
"""

cursor.execute(sql_context)
connection.close()


#================================
#      RESTORE MONGODB
#================================
client = MongoClient();
db = client.music4life
db.concerti.drop()

client.close();
