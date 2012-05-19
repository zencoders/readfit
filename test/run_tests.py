import unittest
import crawler_test

def __main():
    suite=unittest.TestSuite()
    suite.addTest(crawler_test.CrawlerTestCase())

    unittest.TextTestRunner().run(suite)

if __name__=="__main__":
    __main()
