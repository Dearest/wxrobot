import imgkit
class ParseHtmlToImg:
    @staticmethod
    def parse(path):
        imgkit.from_url("https://www.xiachufang.com%sprintable/" % path, 'cook_book.jpg')
