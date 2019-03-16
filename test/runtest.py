from test_comparer import TestComparer
from test_html_parser import TestHtmlParser

try:
    TestComparer().test()
    TestHtmlParser().test()
except AssertionError:
    print("Test failed!")
    raise

print("Test finished with no error.")