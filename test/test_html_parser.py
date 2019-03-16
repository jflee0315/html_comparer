import sys
sys.path.append('../')
from util.html_parser import HtmlParser

class TestHtmlParser():
    def test(self):
        html = "<html><body>This <div style='display:none'>is</div> a test</body></html>"
        assert HtmlParser().extractContent(html) == "This is a test"

if __name__ == "__main__":
    TestHtmlParser().test()