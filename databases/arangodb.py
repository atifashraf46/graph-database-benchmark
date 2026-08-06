from arango import ArangoClient
from databases.base import BaseDatabase


class ArangoDB(BaseDatabase):

    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.db = None

    def connect(self):
        client = ArangoClient(hosts=self.host)

        self.db = client.db(
            "_system",
            username=self.username,
            password=self.password
        )

    def execute(self, query, parameters=None):
        return list(
            self.db.aql.execute(
                query,
                bind_vars=parameters or {}
            )
        )

    def execute_write(self, query, parameters=None):
        self.db.aql.execute(
            query,
            bind_vars=parameters or {}
        )

    def close(self):
        pass