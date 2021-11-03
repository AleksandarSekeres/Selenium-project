import requests
import unittest
import Constants

class httpsTest(unittest.TestCase):
    def test_webpage_status(self):
        try:
            r=requests.get(Constants.BASE_URL, timeout=10)
            r.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            print("Http Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
        except requests.exceptions.RequestException as err:
            print("Oops: other error occurred:", err)

        else:
            print('website' + Constants.BASE_URL + 'is up')

if __name__ == '__main__':
    unittest.main()
