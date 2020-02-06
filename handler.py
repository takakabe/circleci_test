import requests
import unittest

def main(event, context):
    response = requests.get('https://www.kabegiwablog.com/')

    return response.status_code


class test(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main('',''),200)

if __name__ == '__main__':
    unittest.main()
    main('', '')
