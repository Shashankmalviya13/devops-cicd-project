
import unittest
import json
from http.server import HTTPServer
from threading import Thread
from urllib.request import urlopen
from urllib.error import HTTPError

from app import DevOpsHandler


class TestDevOpsApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.server = HTTPServer(
            ("127.0.0.1", 0),
            DevOpsHandler
        )

        cls.port = cls.server.server_address[1]

        cls.thread = Thread(
            target=cls.server.serve_forever,
            daemon=True
        )
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def test_homepage(self):
        with urlopen(
            f"http://127.0.0.1:{self.port}/"
        ) as response:
            self.assertEqual(response.status, 200)
            page = response.read().decode()

        self.assertIn("My First DevOps Project", page)

    def test_health(self):
        with urlopen(
            f"http://127.0.0.1:{self.port}/health"
        ) as response:
            self.assertEqual(response.status, 200)
            data = json.loads(response.read().decode())

        self.assertEqual(data["status"], "healthy")


if __name__ == "__main__":
    unittest.main()
