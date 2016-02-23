#!/usr/bin/python
#
# Runner with stdout/stderr catcher
#
from sys import argv
from subprocess import Popen, PIPE
import os, io
from threading import Thread
from queue import Queue,Empty

def __main__():
    if (len(argv) > 1) and (argv[-1] == "-sub-"):
        import time, sys
        print("Application runned!")
        time.sleep(2)
        print("Slept 2 second")
        time.sleep(1)
        print("Slept 1 additional second")
        time.sleep(2)
        sys.stderr.write("Stderr output after 5 seconds")
        print("Eol on stdin")
        sys.stderr.write("Eol on stderr\n")
        time.sleep(1)
        print("Wow, we have end of work!")
    else:
        os.environ["PYTHONUNBUFFERED"]="1"
        try:
            p = Popen( argv + ["-sub-"],
                       bufsize=0, # line-buffered
                       stdin=PIPE, stdout=PIPE, stderr=PIPE )
        except WindowsError as W:
            if W.winerror==193:
                p = Popen( argv + ["-sub-"],
                           shell=True, # Try to run via shell
                           bufsize=0, # line-buffered
                           stdin=PIPE, stdout=PIPE, stderr=PIPE )
            else:
                raise
        inp = Queue()
        sout = io.open(p.stdout.fileno(), 'rb', closefd=False)
        serr = io.open(p.stderr.fileno(), 'rb', closefd=False)
        def Pump(stream, category):
            queue = Queue()
            def rdr():
                while True:
                    buf = stream.read1(8192)
                    if len(buf)>0:
                        queue.put( buf )
                    else:
                        queue.put( None )
                        return
            def clct():
                active = True
                while active:
                    r = queue.get()
                    try:
                        while True:
                            r1 = queue.get(timeout=0.005)
                            if r1 is None:
                                active = False
                                break
                            else:
                                r += r1
                    except Empty:
                        pass
                    inp.put( (category, r) )
            for tgt in [rdr, clct]:
                th = Thread(target=tgt)
                th.setDaemon(True)
                th.start()
        Pump(sout, 'stdout')
        Pump(serr, 'stderr')

        while p.poll() is None:
            # App still working
            try:
                chan,line = inp.get(timeout = 1.0)
                if chan=='stdout':
                    print("STDOUT>>", line, "<?<")
                elif chan=='stderr':
                    print(" ERROR==", line, "=?=")
            except Empty:
                pass
        print("Finish")

if __name__ == '__main__':
    __main__()