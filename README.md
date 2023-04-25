# Social-Media-Functionality-Using-FastAPI

# Tech Stack Used:

Langauge: Python
Packages: FastAPI, pydantic, SQLAlchemy, uvicorn, Psycopg 2
Tools: Postman API, PostgreSQL (pgAdmin4, psql)

# Tech Stack Explained:

- ***FastAPI*** is used for easier API development. It is a very high performance API-System and it is on par with Node.js and Go Language. This library helps the developers to use the REST interface for thier applications. The best part of FastAPI is that it can handle creation of databases as well its schemas. It also creates documentation for the API implementation. This is one of the best features of FastAPI.

- ***SQLAlchemy*** is a database toolkit for Python. It is an open-source tool kit and object relational mapper (ORM) for Python programming. SQLAlchemy can be used to automatically load tables from a database using something called reflection. Reflection is the process of reading the database and building the metadata based on that information. The queries written in SQLAlchemy is very much similar to the Normal SQL. The syntax is a little bit different. This blogs explains the entire working of SQLAlchemy. I have used it as a reference. 

***(SQLAlchemy — Python Tutorial - Medium)[https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91]

- PostgreSQL is one fot he most widely used database management tools. PostgreSQL comes under the SQL category but it is a bit different from the Normal SQL Database Management. It uses the concept of Classes and Objects. It combines the advantages of OOPS and SQL together. It comes in very handy when we are dealing with API/RESTFUL Architectures. Also, PostgreSQL provides wide range of supported functionality so that developers can easily make use of libraries to connect the database to the code. For this application, each and every criteria was matching to use PostgreSQL. Hence, I have used PostgreSQL as the database.

***(IBM's Introduction to PostgreSQL)[https://www.ibm.com/topics/postgresql]

- ***uvicorn*** is a ASGI web implementation library in Python. It is a low-level server application interface for async frameworks. Before this library there was no module which catered to this need. We had to create huge code base for creation of interfaces.

***[PyPI Installation of uvicorn] (https://pypi.org/project/uvicorn/)
