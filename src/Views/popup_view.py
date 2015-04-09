from Tkinter import Frame, Label, Button, Canvas, ALL
from Models.config import *



conf = ConfigFile()


class Popup(object):
    def __init__(self, title, content, buttons):

        self.title = title
        self.content = content
        self.buttons = buttons
        self.popup = ""

    def display(self, frame_obj):

        canvas_popup = Canvas(frame_obj, background=conf.left_nav_background)
        # canvas_popup.config(x=0, y=0)
        canvas_popup.place(x=(frame_obj.sw/2), y=(frame_obj.sh/2)-100)

        if self.title != "":
            title_label = Label(canvas_popup, text=self.title, fg=conf.main_text_color)
            title_label.config(highlightbackground=conf.left_nav_background, background=conf.left_nav_background)
            title_label.grid(row=0, sticky='e,w', padx=10, pady=10)

        if self.content != "":
            content_label = Label(canvas_popup, text=self.content, fg=conf.main_text_color)
            content_label.config(highlightbackground=conf.left_nav_background, background=conf.left_nav_background)
            content_label.grid(row=1, sticky='e,w', padx=10, pady=10)

        if self.content != "":
            action_button = Button(canvas_popup, text="Ok", fg=conf.main_text_color)
            action_button.config(highlightbackground=conf.left_nav_background, background=conf.left_nav_background)
            action_button.bind("<Button-1>", self.dismiss)
            action_button.grid(row=2, sticky='e,w', padx=10, pady=10)

    def dismiss(self, event):
        print "dismiss class event"
        canvas = event.widget.master
        canvas.destroy()
        del self





