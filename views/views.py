# -*- coding: utf-8 -*- 
import tornado.web
class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
       return self.application.db

class Base_Handler(BaseHandler):
    def get(self):
	self.render("base.html")

class Useradd_Handler(BaseHandler):
    def get(self):
	self.render("useradd.html")
