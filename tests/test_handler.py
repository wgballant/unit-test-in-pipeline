import unittest
import lambda_function


class TestHandlerCase(unittest.TestCase):

    def test_response(self):
        print("testing response.")
        event={'Country':'USA'}
        result = lambda_function.lambda_handler(event, None)
        print(result)
        self.assertEqual(result['statusCode'], 200)
        self.assertIn('Hello World!', result['body'])


if __name__ == '__main__':
    unittest.main()
