
from Views.popup_view import *


class PopupController(object):
    def __init__(self):
        self.view = Popup('null', 'null', 'null')
        pass

    def message(self, message):
        pass

    def remove(self, event):
        self.view.delete()      # prev: event.widget.master.delete()


