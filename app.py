import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Sublio(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Sublio")
        self.set_size_request(450, 200)
        self.timeout_id = None

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.entry = Gtk.Entry()
        self.entry.set_text("Enter movie title")
        vbox.pack_start(self.entry, True, True, 0)



app = Sublio()
app.connect("delete-event", Gtk.main_quit)
app.show_all()
Gtk.main()