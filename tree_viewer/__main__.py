import gi

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

from .widgets import Window


class Application(Gtk.Application):
    def on_activate(self, _):
        win = Window(application=self)
        win.set_default_size(1300, 800)
        win.set_title("Tree Viewer")
        win.set_visible(True)
        self.win = win
        self.connect('activate', self.on_activate)


app = Application()
app.connect('activate', app.on_activate)

app.run(None)
