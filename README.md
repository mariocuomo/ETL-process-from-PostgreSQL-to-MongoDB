# ETL process

A simple project that exaplains how to migrate data from **PostgreSQL** (_Relational database_) to **MongoDB** (_NoSQL database_).
<div align="center">
  <img src="https://github.com/mariocuomo/ETL-process-from-PostgreSQL-to-MongoDB/blob/main/elaborazione.png" width="500px">
</div>

CONFIGURATION<br>
**PostgreSQL**: it runs in localhost:5432 with a database '_music4life_'.<br>
**MongoDB**: it runs in localhost:27017 with a database '_music4life_' and a collection '_concerti_'.


## FIRST METHOD - Python
[python_version](https://github.com/mariocuomo/ETL-process-from-PostgreSQL-to-MongoDB/tree/main/python_version) folder contains one file.<br>
`run.py` starts the **ETL computation** extracting data from PostgreSQL and loading it in MongoDB after a simple transformation.<br>
**REQUIRED**: _psycopg2_ and _pymongo_.<br><br>


## SECOND METHOD - Logstash
[logstash_version](https://github.com/mariocuomo/ETL-process-from-PostgreSQL-to-MongoDB/tree/main/logstash_version) folder contains one file.<br>
`simple-out.conf` starts the **ETL computation** extracting data from PostgreSQL and loading it in MongoDB after a simple transformation using logstash.<br>
**REQUIRED**: _aggregate_ filter, input _jdbc_, output _mongodb_ plugin.<br>
<br>
<br>

`restore.py` is dedicated to **restore** databases (PostgreSQL and MongoDB).

