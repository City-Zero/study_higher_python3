# coding=utf-8
import pyinotify


class EventHandler(pyinotify.ProcessEvent):
    """事件处理"""

    def my_init(self, **kargs):
        self.fd = kargs['fd']

    def process_IN_MODIFY(self, event):
        print(self.fd.read(), end='')

path = './a'
f = open(path,'r')
wm = pyinotify.WatchManager()
mask = pyinotify.IN_MODIFY
notifier = pyinotify.Notifier(wm,EventHandler(fd=f))
wm.add_watch(path,mask,auto_add=True,rec=True)
print('now starting monitor %s' % path)
print(f.read(),end='')

while True:
    try:
        notifier.process_events()
        if notifier.check_events():
            notifier.read_events()
    except KeyboardInterrupt:
        notifier.stop()
        break