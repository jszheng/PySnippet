from configparser import ConfigParser

cfg = ConfigParser()
cfg.add_section('server')
cfg.add_section('debug')
cfg.set('server', 'port', '9000')
cfg.set('debug', 'log_errors', 'False')
import sys
cfg.write(sys.stdout)

port = cfg.getint('server', 'port')
print(type(port))
print(port)