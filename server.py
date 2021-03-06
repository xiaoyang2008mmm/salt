# -*- coding: utf-8 -*- 
import tornado.httpserver, os 
import tornado.ioloop 
import tornado.web,torndb 
from handlers.handlers import HANDLERS , STATIC_PATH , TEMPLATE_PATH

from tornado.options import define, options, parse_command_line

define("port", default=88, help="run on the given port", type=int)
define("mysql_host", default="127.0.0.1:3306", help="account database host")
define("mysql_database", default="assets", help="account database name")
define("mysql_user", default="saltapi", help="account database user")
define("mysql_password", default="Salt#@!20151022", help="account database password")




class Application(tornado.web.Application):
    def __init__(self):
	handlers=HANDLERS
	settings = {                                                        
       	    "static_path": STATIC_PATH ,
     	    "template_path": TEMPLATE_PATH,
     	    "login_url": "/login/",                                                 
            "debug": True,                                                      
     	    "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",                          
	    #"xsrf_cookies":True,                                                  
	}                                                                   
                                                                    

     	tornado.web.Application.__init__(self, handlers, **settings)
	try:
	    self.db = torndb.Connection(                                               
        	host=options.mysql_host, database=options.mysql_database,                             
         	user=options.mysql_user, password=options.mysql_password,charset='utf8')
	except:
	     print  "mysql数据库连接不上"
	    	

def main():
    parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
