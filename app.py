import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib


class Sublio(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Sublio")
        self.set_size_request(310, 40)

        self.timeout_id = None

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        self.add(vbox)

        self.entry = Gtk.Entry()
        self.entry.set_text("Enter movie name to search for subtitle")
        self.entry.set_icon_from_icon_name(Gtk.EntryIconPosition.PRIMARY, "system-search-symbolic")
        self.entry.connect("key-release-event", self.on_key_release)
        vbox.pack_start(self.entry, True, True, 0)

    def on_key_release(self, widget, event):
        self.label.set_text(widget.get_text())

win = Sublio()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()