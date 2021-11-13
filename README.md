# ETL process

A simple project that exaplains how to migrate data from **PostgreSQL** (_Relational database_) to **MongoDB** (_NoSQL database_).
<div align="center">
  <img src="https://github.com/mariocuomo/ETL-process-from-PostgreSQL-to-MongoDB/blob/main/elaborazione.png" width="500px">
</div>

CONFIGURATION<br>
**PostgreSQL**: it runs in localhost:5432 with a database '_music4life_'.<br>
**MongoDB**: it runs in localhost:27017 with a database '_music4life_' and a collection '_concerti_'.


## FIRST METHOD - Python
There are two files in [python_version](https://github.com/mariocuomo/ETL-process-from-PostgreSQL-to-MongoDB/tree/main/python_version) folder.<br>
`restore.py` is dedicated to **restore** databases (PostgreSQL and MongoDB).<br>
`run.py` starts the **ETL computation** extracting data from PostgreSQL and loading it in MongoDB after a simple transformation.
