import threading
import os


def gui():
    from GUI.GUI import gui
    gui()


def server():
    from GUI.server_gui import server_gi
    server_gi()


t1 = threading.Thread(target=gui(), args=(10,))
t2 = threading.Thread(target=server(), args=(10,))

t1.start()
t2.start()

t1.join()
t2.join()
