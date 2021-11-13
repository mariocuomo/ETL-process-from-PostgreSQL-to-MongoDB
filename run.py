import psycopg2
from pymongo import MongoClient


#===================================
#       ETL - Extract phase
#===================================
connection = psycopg2.connect(database="music4life", user='postgres', password='postgres', host="localhost", port=5432)
cursor = connection.cursor()

sql_context ="""
select Co.id as id_concerto, Ca.id as cantante_id, Ca.id as citta_concerto_id,
       Ca.nome as nome_cantante, Ca.cognome as cognome_cantante,
       Ci_Ca.nome as comune_nascita_cantante,
       Ci_Co.nome as comune_concerto, Ci_Co.provincia as provincia_concerto, Ci_Co.regione as regione_concerto
from concerti as Co, cantanti as Ca,citta as Ci_Ca, citta as Ci_Co
where Ca.citta_nascita=Ci_Ca.id and
      Co.cantante=Ca.id and
      Co.citta=Ci_Co.id;
"""

cursor.execute(sql_context)
records = cursor.fetchall()
connection.close()


#===================================
#       ETL - Transform phase
#===================================
documents=[]
for record in records:
      document={
      "cantante":{
            "nome":record[3],
            "cognome":record[4],
            "comune_di_nascita":record[5]
      },
      "citta":{
            "comune":record[6],
            "provincia":record[7],
            "regione":record[8]
      }
      }
      documents.append(document)



#===================================
#       ETL - Load phase
#===================================
client = MongoClient();
db = client.music4life
col = db.concerti

result = col.insert_many(documents) 
client.close();



#===================================
#       SHOW DOCUMENTS
#===================================
client = MongoClient();
db = client.music4life
col = db.concerti

cursor = col.find({})
for document in cursor:
    print(document)