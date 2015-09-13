#!/usr/bin/env python2

import gtk
import gobject
from os.path import expanduser

path = expanduser("~") + "/.config/ocaml-xmpp-client/notification.state"
offline = gtk.STOCK_NO
online = gtk.STOCK_YES
icon = gtk.StatusIcon()
icon.set_visible(True)
icon.set_from_stock(gtk.STOCK_NO)

def show_icon():
    gobject.timeout_add(1000, show_icon)
    with open(path, "r") as f:
        status = f.read()
        if status[:9] == "connected":
            icon.set_from_stock(online)
            if status[10:] == "notifications":
                icon.set_blinking(True)
            else:
                icon.set_blinking(False)
        else:
            icon.set_from_stock(offline)

if __name__ == '__main__':
    show_icon()
    gtk.main()
