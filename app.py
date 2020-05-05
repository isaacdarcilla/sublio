import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib


class EntryWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Sublio")
        self.set_size_request(300, 100)

        self.timeout_id = None

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        self.add(vbox)

        self.entry = Gtk.Entry()
        self.entry.set_text("Enter movie name to search")
        self.entry.set_icon_from_icon_name(Gtk.EntryIconPosition.PRIMARY, "system-search-symbolic")
        vbox.pack_start(self.entry, True, True, 0)

        hbox = Gtk.Box(spacing=2)
        vbox.pack_start(hbox, True, True, 0)


win = EntryWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()