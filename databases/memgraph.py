from neo4j import GraphDatabase
from databases.base import BaseDatabase


class MemgraphDB(BaseDatabase):

    def __init__(self, uri, user, password):
        self.uri = uri
        self.user = user
        self.password = password
        self.driver = None

    def connect(self):
        self.driver = GraphDatabase.driver(
            self.uri,
            auth=(self.user, self.password),
            
        )

    def execute(self, query, parameters=None):
        with self.driver.session() as session:
            result = session.run(query, parameters or {})
            return [record.data() for record in result]

    def execute_write(self, query, parameters=None):
        with self.driver.session() as session:
            session.run(query, parameters or {})

    def close(self):
        if self.driver:
            self.driver.close()