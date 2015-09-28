#!/usr/bin/env python2

import sys
import gtk
import gobject
from os.path import expanduser
from os.path import isfile

offline = gtk.STOCK_NO
online = gtk.STOCK_YES
icon = gtk.StatusIcon()
icon.set_visible(True)
icon.set_from_stock(gtk.STOCK_NO)

def show_icon(path=expanduser('~')+'/.config/ocaml-xmpp-client/notification.state'):
    gobject.timeout_add(1000, show_icon)
    with open(path, "r") as f:
        status = f.read()
        if status[:9] == "connected":
            icon.set_from_stock(online)
        else:
            icon.set_from_stock(offline)
        if status[-13:] == "notifications":
            icon.set_blinking(True)
        else:
            icon.set_blinking(False)

if __name__ == '__main__':
    try:
        path = sys.argv[1]
        if not path[-1] == "/":
            path = path + "/"
        path = path + "notification.state"
        if isfile(path):
            show_icon(path)
        else:
            print "Error: not a valid notification.stat file. Exiting."
            quit()
    except:
        print "no path given, using default"
        show_icon()
    gtk.main()
