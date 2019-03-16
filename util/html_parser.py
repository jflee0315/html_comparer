import re
class HtmlParser:
    def __init__(self):
        pass
    """
    This will remove all the scripts, tags and comments
    """
    def extractContent(self,html):
        return self.__removeTags(self.__removeScripts(self.__removeComments(html)))

    def __removeScripts(self,html):
        pattern = "< *script *[^>]* *>.*?(?!< */ *script *>).?< */ *script *>"
        return re.sub(pattern, "", html, flags = re.IGNORECASE | re.DOTALL)

    def __removeTags(self,html):
        pattern = "< */? *[^>]+ *>"
        return re.sub(pattern, "", html)

    def __removeComments(self,html):
        pattern = "< *! *- *-([^\-]|[\r\n]|-[^\-])+ *- *- *>"
        return re.sub(pattern, "", html)