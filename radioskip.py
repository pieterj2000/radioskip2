from __future__ import annotations
import urwid


radios = [
    { "name": "Radio538" },
    { "name": "SkyRadio" },
    { "name": "Radio10"  },
    { "name": "Veronica" },
    { "name": "Q-Music" },
    { "name": "Radio 1" },
    { "name": "Radio 2" },
    { "name": "Sublime" },
    { "name": "SlamFM" },
    { "name": "3FM" },
    { "name": "Radio 4" },
    { "name": "Radio 5" },
    { "name": "FunX" },
    { "name": "100% NL" },
    { "name": "KINK" },
    { "name": "Soul Radio" },
    { "name": "Arrow Classic Rock" },
    { "name": "classicnl" },
    { "name": "Studio040" },
    { "name": "StuBru" },
]

def quit_on_ctrl_q(key: str) -> None:
    if key == "ctrl q":
        raise urwid.ExitMainLoop()


palette = [
    ("key", "light green,bold", "dark blue"),
    ("footer", "default,bold", "dark blue"),
    ("header", "default,bold", "dark blue")
]

radiolistgroup = []
radiolist = [ urwid.RadioButton(radiolistgroup, r["name"]) for r in radios ]
radiolistpile = urwid.Pile(radiolist)

header = urwid.AttrMap(urwid.Text("Radioskip2", align="center"), "header")
footer = urwid.AttrMap(urwid.Text(["TODO, en quit is ", ("key", "Ctrl+Q")]), "footer")
frame = urwid.Frame(urwid.Filler(radiolistpile,valign="top"), header=header, footer=footer)

urwid.MainLoop(frame, palette, unhandled_input=quit_on_ctrl_q).run()