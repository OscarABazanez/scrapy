from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions import AssertionTest
from madison_search import HomePageTest


assertions_test = TestLoader().loadTestsFromTestCase(AssertionTest)
search_test = TestLoader().loadTestsFromTestCase(HomePageTest)

smoke_test = TestSuite([assertions_test, search_test])

kwargs = {
    'output': 'smoke-report'
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)
