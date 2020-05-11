# coding:utf-8 

import logging

from .BaseHandler import BaseHandler
from utils.common import storage 

class AvatarHandler(BaseHandler):
	"""头像"""
    @require_logined
	def post(self):
        user_id = self.session.data["user_id"]
		try:
			avatar = self.request.files["avatar"][0]["body"]
		except Exception as e:
			logging.error(e)
			return self.write(dict(errno=RET.PARAMERR,errmsg="参数出错"))
		try:
			img_name = storage(avatar)
	    except Exception as e:
	    	logging.error(e)
	        img_name = None 
	    if  not img_name:
                return self.write({"error":RET.THIRDERR, "errmsg":"qiuiu error"})
	    try:
                ret = self.db.execute("update ih_user_profile set up_avatar=%s where up_user_id=%s", img_name, user_id)
        except Exception as e:
	    	logging.error(e)
	    	return self.write({"error":RET.DBERR, "errmsg":"upload failed"})
	    img_url = image_url_prefix + img_name 
	    self.write({"errno":RET.OK, "errmsg":"OK", "url":img_url})



