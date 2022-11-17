import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

builder = Gtk.Builder()
builder.get_object("entry1")

class Handler:
    def __init__(self):
        self.acc = 0
        self.name = "uNkNowN"
    def on_destroy(self, *args):
        Gtk.main_quit()
    def on_b1_pressed(self, buttons):
        self.acc += 1
        global builder
        if (builder.get_object("entry1").get_text() != ''):
            self.name = builder.get_object("entry1").get_text()
        else:
            self.name = "uNkNowN"
        print("Hello {} ({})".format(self.name, self.acc))

builder.add_from_file("teste_1.glade")
builder.connect_signals(Handler())

window = builder.get_object("window1")
window.show_all()

Gtk.main()