"""This is a resolver that generates readable reports for human"""
class HumanResolver:
    def __init__(self):
        pass
    def generate_html_report(self, diffs):
        output_head = "<html><head><style>#less p{background-color:#ff7373}#addition p{background-color:#61ccc3}</style></head><body><h1>Difference Report</h1>"
        output_foot = "</body></html>"
        less = "<div id='less'><h2>Less</h2>"
        for diff in diffs[-1]:
            diff = diff.replace("\n", "<br>")
            less += "<p>{}</p>".format(diff)
        addition = "<div id='addition'><h2>Addition</h2>"
        for diff in diffs[1]:
            diff = diff.replace("\n", "<br>")
            addition += "<p>{}</p>".format(diff)
        return output_head + less + addition + output_foot

    def resolve(self, diffs):
        self.__write(self.generate_html_report(diffs))

    def __write(self, output):
        write_file = None
        try:
            write_file = open("output.html", "w")
            write_file.write(output)
        except IOError:
            print("Unable to write to the file 'output.html'.")
        finally:
            if write_file is not None:
                write_file.close()