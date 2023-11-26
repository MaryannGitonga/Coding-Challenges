import unittest
import resp

class TestRedis(unittest.TestCase):
    def test_simple_string_resp(self):
        resp_instance = resp.RESP()

        self.assertEqual(resp_instance.deserialize('+hello world\r\n'), 'hello world')
        self.assertEqual(resp_instance.deserialize('+OK\r\n'), 'OK')

        self.assertEqual(resp_instance.deserialize('-Error message\r\n'), 'Error message')

        # self.assertEqual(resp_instance.deserialize('$-1\r\n'), 'bulk string')
        # self.assertEqual(resp_instance.deserialize('*1\r\n$4\r\nping\r\n'), 'array')
        # self.assertEqual(resp_instance.deserialize('*2\r\n$4\r\necho\r\n$11\r\nhello world\r\n'), 'array')
        # self.assertEqual(resp_instance.deserialize("*2\r\n$3\r\nget\r\n$3\r\nkey\r\n"), 'array')
        # self.assertEqual(resp_instance.deserialize('$0\r\n\r\n'), 'bulk string')
        # self.assertEqual(resp_instance.deserialize(':1000\r\n'), 'integer')    

if __name__ == '__main__':
    unittest.main()