import redis
import ssl
from databases.base import BaseDatabase


class FalkorDB(BaseDatabase):

    def __init__(self, host, port, username, password):
        self.host = host
        self.port = int(port)
        self.username = username
        self.password = password
        self.client = None

    def connect(self):
        self.client = redis.Redis(
            host=self.host,
            port=self.port,
            username=self.username,
            password=self.password,
            ssl=True,
            ssl_cert_reqs=ssl.CERT_NONE,
            ssl_check_hostname=False,
            decode_responses=True,
            socket_connect_timeout=30,
            socket_timeout=30,
            health_check_interval=30,
            retry_on_timeout=True,
        )

        print("Connecting to FalkorDB...")
        print(self.client.ping())

    def execute(self, query, parameters=None):
        if parameters:
            for key, value in parameters.items():
                query = query.replace(f"${key}", f'"{value}"')

        return self.client.execute_command(
            "GRAPH.QUERY",
            "benchmark",
            query
        )

    def execute_write(self, query, parameters=None):
        if parameters:
            for key, value in parameters.items():
                query = query.replace(f"${key}", f'"{value}"')

        return self.client.execute_command(
            "GRAPH.QUERY",
            "benchmark",
            query
        )

    def close(self):
        if self.client:
            self.client.close()