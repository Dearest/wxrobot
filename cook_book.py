import pymysql
import random
class CookBook(object):
    @staticmethod
    def random_path():
        db = pymysql.connect("localhost","root","hanchen","find_dinners" )
        cursor = db.cursor()
        cursor.execute("SELECT path from books where id = %d" % (random.randint(1, 200)))
        data = cursor.fetchone()
        db.close()
        return data
    @staticmethod
    def hello():
        return 'hello'