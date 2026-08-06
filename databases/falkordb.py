import redis
from databases.base import BaseDatabase


class FalkorDB(BaseDatabase):

    def __init__(self, host, port, password):
        self.host = host
        self.port = port
        self.password = password
        self.client = None

    def connect(self):
        self.client = redis.Redis(
            host=self.host,
            port=int(self.port),
            password=self.password,
            decode_responses=True
        )

        self.client.ping()

    def execute(self, query, parameters=None):
        return self.client.execute_command("GRAPH.QUERY", "benchmark", query)

    def execute_write(self, query, parameters=None):
        return self.client.execute_command("GRAPH.QUERY", "benchmark", query)

    def close(self):
        if self.client:
            self.client.close()