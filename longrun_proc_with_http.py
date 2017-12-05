import subprocess
import threading
import time
import urllib


def output_reader(proc):
    for line in iter(proc.stdout.readline, b''):
        print('got line: {0}'.format(line.decode('utf-8')), end='')


def main():
    proc = subprocess.Popen(['python3', '-u', '-m', 'http.server', '8070'],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)

    t = threading.Thread(target=output_reader, args=(proc,))
    t.start()

    try:
        time.sleep(0.2)
        for i in range(4):
            resp = urllib.request.urlopen('http://localhost:8070')
            assert b'Directory listing' in resp.read()
            time.sleep(0.1)
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=0.2)
            print('== subprocess exited with rc =', proc.returncode)
        except subprocess.TimeoutExpired:
            print('subprocess did not terminate in time')
    t.join()


if __name__ == '__main__':
    main()
