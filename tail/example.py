#!/usr/bin/python
import sys, os, pyinotify

notifier = None
monfile = None
lastsize = 0
wm = None
wd = 0


def roll_file(filename):
    global lastsize
    fd = open(filename, 'r')
    try:
        newsize = os.fstat(fd).st_size
        if newsize <= lastsize: return
        os.lseek(fd, lastsize, os.SEEK_SET)
        while True:
            data = os.read(fd, 4096)
            if not data: break
            sys.stdout.write(data)
        sys.stdout.flush()

        pos = os.lseek(fd, 0, os.SEEK_CUR)
        lastsize = pos if pos != lastsize else newsize
    finally:
        os.close(fd)


class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        if monfile == event.pathname:
            global wd
            wd = wm.add_watch(monfile, pyinotify.IN_MODIFY).values()[0]
            roll_file(monfile)

    def process_IN_DELETE(self, event):
        global wd, lastsize
        if monfile == event.pathname:
            if wd > 0:
                try:
                    wm.rm_watch(wd, quiet=False)
                except pyinotify.WatchManagerError:
                    pass
                wd = 0
            lastsize = 0

    def process_IN_MOVED_FROM(self, event):
        self.process_IN_DELETE(event)

    def process_IN_MOVED_TO(self, event):
        self.process_IN_DELETE(event)
        self.process_IN_CREATE(event)

    def process_IN_MODIFY(self, event):
        roll_file(monfile)


def main():
    global notifier, lastsize, wm, wd, monfile
    monfile = os.path.abspath('./a')
    print(
        "path={0}".format(monfile)
    )

    lastsize = os.stat(monfile).st_size

    wm = pyinotify.WatchManager()
    notifier = pyinotify.Notifier(wm, EventHandler())
    wd = wm.add_watch(monfile, pyinotify.IN_MODIFY)
    wm.add_watch(os.path.dirname(monfile),
                 pyinotify.IN_DELETE | pyinotify.IN_CREATE | pyinotify.IN_MOVED_FROM | pyinotify.IN_MOVED_TO)
    print(
        "watching {0} ...".format(monfile)
    )

    while True:
        notifier.process_events()
        if notifier.check_events():
            notifier.read_events()


if __name__ == "__main__":
    try:
        main()
    finally:
        if notifier: notifier.stop()