# jackification
a very simple systray icon for [jackline](https://github.com/hannesm/jackline)

hear this!
----------
this program does not work with current versions of jackline.
i will fix this, but right now i'm too lazy or preoccupied.
sorry for the inconvenience. Feel free to fork, though.

requirements
------------
needs pyGTK >= 2.10 to be installed.
the package (on linux mint) is called "python-gtk2"
written and tested with pyGTK 2.24.0 on linux mint

usage
-----
run script.
it defaults to notification.state in jackline's default config directory:
~/.config/ocaml-xmpp-client/
you can give a custom directory as an argument like so:
$ jackification (customdir)

what happen!
------------
if jackline is not running or disconnected, a red icon will be visible.
if jackline is connected, a green icon will be visible.
if there are notifications, the icon will blink.
