class FileSource:
    def __init__(self, filename):
        self.file = open(filename, "r")
    def get_content_and_close(self):
        try:
            content = self.file.read()
        finally:
            self.file.close()
        return content
    def repr():
        return "FileSource at '{}'".format(self.file.name)