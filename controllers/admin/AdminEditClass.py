from ..BaseController import *

class EditClass(BaseHandler):
    def get(self, school_id, class_id):
        self.route('/templates/admin/adminEditClass.html')