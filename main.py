from util.html_parser import HtmlParser
from comparer import Comparer
from resolver.human_resolver import HumanResolver
from data_source.file_source import FileSource

def main():
    """ This is the entry point"""
    valid_file = False

    filename1 = input("Please enter first html file name:")
    filename2 = input("Please enter the other html file name:")

    try:
        html1 = FileSource(filename1).get_content_and_close()
        html2 = FileSource(filename2).get_content_and_close()
    except IOError:
        print("Unable to open the files. Please make sure they are available and try again.")
        return

    resolver = HumanResolver()
    Comparer(resolver).compare_and_resolve(HtmlParser().extractContent(html1), HtmlParser().extractContent(html2))
    print("Success. Please check the output.html to see the result.")

if __name__ == "__main__":
    main()