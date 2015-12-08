from views.views import *
import os.path

STATIC_PATH   = os.path.join(os.path.dirname(__file__), "../static")
TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "../templates")
HANDLERS =[
	   (r"/base/",Base_Handler),
	   (r"/useradd/",Useradd_Handler),
	]
#HANDLERS +=[(r"/chart/", ChartHandler)]
