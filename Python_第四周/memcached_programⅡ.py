#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-12-8 14:02
# @Author  : zhdya@zhdya.cn
# @File    : MONDAY.py


### write a rc python program
import os
import sys
from subprocess import Popen, PIPE


class Progress(object):
    '''Memcached service program'''
    def __init__(self, name, program, args, workdir):       ##初始化Progress的几个属性
        self.name = name
        self.program = program
        self.args = args
        self.workdir = workdir


    def _init(self):          ##创建一个方法：初始化--判断是否有这个目录
        '''judge if workdir is exist'''
        if not os.path.exists(self.workdir):
            os.mkdir(self.workdir)
            os.chdir(self.workdir)


    def _PidFile(self):
        '''/tmp/memcached'''
        return os.path.join(self.workdir,"{0}.pid".format(self.name))       ##仅仅是返回这个memcached的绝对路径(/tmp/memcached/memcached.pid)


    def _WritePid(self):
        if self.pid:
            with open(self._PidFile(), 'w') as fw:      ##将进程以w的模式写进去
                fw.write(str(self.pid))     ##写是字符串的类型，不可以int型


    def start(self):        ##启动，需要考虑到，一旦程序正在运行，就不需要再次运行了，给一个反馈信息；
        pid = self._GetPid()
        if pid:
            print("the {0} is running...".format(self.name))
            sys.exit()
        else:
            self._init()
            cmd = self.program + ' ' + self.args        ##/usr/bin/memcached -u nobody -p 11211 -c 1024 -m 64
            p = Popen(cmd, stdout=PIPE, shell=True)
            self.pid = p.pid        ##得到memcached的进程
            self._WritePid()        ##调用_WritePid方法
            print("start {0} successful!!".format(self.name))

    def _GetPid(self):
        pid = Popen(['pidof', self.name], stdout=PIPE)
        pid = pid.stdout.read().strip()
        return pid

    def stop(self):     ##思路：判断进程是否存在，判断pid文件是否存在
        pid = self._GetPid()
        if pid:
            os.kill(int(pid), 15)
            if os.path.exists(self._PidFile()):
                os.remove(self._PidFile())
            print("{0} is stopped".format(self.name))

    def restart(self):
        self.stop()
        self.start()

    def status(self):   ##思路：如果有pid就代表运行，没有就代表没有运行；
        pid = self._GetPid()
        if pid:
            print("the {0} is running...".format(self.name))
        else:
            print("the {0} is stopped...".format(self.name))

    def help(self):     ##定义一个帮助信息
        print("PLS TRY TO USING:[python {0} start|stop|restart|status]".format(__file__))       ##内置变量 __init__ 获得的参数就是文件名


def main():
    name = 'memcached'
    prog = '/usr/bin/memcached'
    args = '-u nobody -p 11211 -c 1024 -m 64'
    wd = '/tmp/memcached'
    pm = Progress(name=name, program=prog, args=args, workdir=wd)
    try:
        cmd = sys.argv[1]
    except Exception as e:
        print("error error la...")
        sys.exit()
    if cmd == 'start':
        pm.start()
    elif cmd == 'stop':
        pm.stop()
    elif cmd == 'restart':
        pm.restart()
    elif cmd == 'status':
        pm.status()
    else:
        pm.help()

if __name__ == '__main__':
    main()