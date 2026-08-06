from gqlalchemy import Memgraph
from databases.base import BaseDatabase


class MemgraphDB(BaseDatabase):

    def __init__(self, uri, user, password):
        self.uri = uri
        self.user = user
        self.password = password
        self.db = None

    def connect(self):
        host = self.uri.replace("bolt+s://", "").replace("bolt://", "")
        if ":" in host:
            host, port = host.split(":")
            port = int(port)
        else:
            port = 7687

        self.db = Memgraph(
            host=host,
            port=port,
            username=self.user,
            password=self.password,
            encrypted=True,
        )

    def execute(self, query, parameters=None):
        if parameters:
            for key, value in parameters.items():
                query = query.replace(f"${key}", f'"{value}"')

        result = self.db.execute_and_fetch(query)
        return list(result)

    def execute_write(self, query, parameters=None):
        if parameters:
            for key, value in parameters.items():
                query = query.replace(f"${key}", f'"{value}"')

        self.db.execute(query)

    def close(self):
        pass