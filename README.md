# MiddleEast-ML

Using public datasets to find correlations between violence and economic turmoil in areas of interest in the Middle East using Spark-ML on Postgres

### Instructions
- You need to connect to the Postgres database. Enter your credentials in config.yaml
	```
		psql:
		    dbname: 'dbname'
		    user: 'username'
		    host: 'localhost'
		    password: ''
		    data: '/Users/Username/Downloads/iraq-stats/iraq-stats/ibc-incidents.csv'
		    sparkHome: '/Users/Username/Downloads/spark-1.6.2-bin-hadoop2.6'
		    sparkClass: '/Users/Username/Downloads/iraq-stats/iraq-stats/postgresql-9.4.1208.jre6.jar'
	```


	#### Dependencies
	You can find the data here:
	
	https://www.iraqbodycount.org/

	Spark Driver for Postgres:
	
	https://jdbc.postgresql.org/download/postgresql-9.4.1208.jre6.jar
