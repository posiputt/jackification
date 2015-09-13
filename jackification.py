#!/usr/bin/env python2

import gtk
import gobject
import time
from os.path import expanduser

path = expanduser("~") + "/.config/ocaml-xmpp-client/notification.state"
icon = gtk.StatusIcon()
icon.set_from_stock(gtk.STOCK_NO)
icon.set_visible(True)

def show_icon():
    with open(path, "r") as f:
        status = f.read()
        if status[:9] == "connected":
            icon.set_from_stock(gtk.STOCK_YES)
            if status[10:] == "notifications":
                icon.set_blinking(True)
            else:
                icon.set_blinking(False)
        else:
            icon.set_from_stock(gtk.STOCK_NO)
        gobject.timeout_add(1000, show_icon)

if __name__ == '__main__':
    show_icon()
    gtk.main()
