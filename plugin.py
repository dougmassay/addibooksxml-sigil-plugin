# -*- coding: utf-8 -*-
# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab

from __future__ import unicode_literals, division, absolute_import, print_function

import os
import sys
import zipfile
from datetime import datetime, timedelta

from compatibility_utils import PY2, unicode_str
from unipath import pathof

from utilities import expanduser, file_open
from updatecheck import UpdateChecker, delta

if PY2:
    from Tkinter import Tk
    import tkFileDialog as tkinter_filedialog
    import tkMessageBox as tkinter_msgbox
else:
    from tkinter import Tk
    import tkinter.filedialog as tkinter_filedialog
    import tkinter.messagebox as tkinter_msgbox


_DEBUG_ = False

prefs = {}

XMLFILE = 'com.apple.ibooks.display-options.xml'


def fileChooser():
    localRoot = Tk()
    localRoot.withdraw()
    file_opt = {}
    file_opt['parent'] = None
    file_opt['title']= 'Select iBooks XML file'
    file_opt['defaultextension'] = '.xml'
    # retrieve the initialdir from JSON prefs
    file_opt['initialdir'] = unicode_str(prefs['use_file_path'], 'utf-8')
    file_opt['multiple'] = False
    file_opt['filetypes'] = [('XML Files', ('.xml'))]
    localRoot.quit()
    return tkinter_filedialog.askopenfilename(**file_opt)

def show_msgbox(title, msg, msgtype='info'):
    localRoot = Tk()
    localRoot.withdraw()
    localRoot.option_add('*font', 'Helvetica -12')
    localRoot.quit()
    if msgtype == 'info':
        return tkinter_msgbox.showinfo(title, msg)
    elif msgtype == 'error':
        return tkinter_msgbox.showerror(title, msg)

def run(bk):
    global prefs
    prefs = bk.getPrefs()

    # set default preference values
    if 'use_file_path' not in prefs:
        prefs['use_file_path'] = expanduser('~')
    if 'check_for_updates' not in prefs:
        prefs['check_for_updates'] = True
    if 'last_time_checked' not in prefs:
        prefs['last_time_checked'] = str(datetime.now() - timedelta(hours=delta+1))
    if 'last_online_version' not in prefs:
        prefs['last_online_version'] = '0.1.0'

    if prefs['check_for_updates']:
        chk = UpdateChecker(prefs['last_time_checked'], prefs['last_online_version'], bk._w)
        update_available, online_version, time = chk.update_info()
        # update preferences with latest date/time/version
        prefs['last_time_checked'] = time
        if online_version is not None:
            prefs['last_online_version'] = online_version
        if update_available:
            title = 'Plugin Update Available'
            msg = 'Version {} of the {} plugin is now available.'.format(online_version, bk._w.plugin_name)
            show_msgbox(title, msg, 'info')

    if 'META-INF/{}'.format(XMLFILE) in bk._w.other:
        title = 'File Already Present!'
        msg = 'The {} file is already present. Please delete it before trying to add another'.format(XMLFILE)
        show_msgbox(title, msg, 'error')
        return 0

    if _DEBUG_:
        print('Python sys.path: {}\n'.format(sys.path))

    inpath = fileChooser()
    if inpath == '' or not os.path.exists(inpath):
        print('iBooks XML file selection canceled!')
        bk.savePrefs(prefs)
        return 0

    if _DEBUG_:
        print('Path to XML file: {}\n'.format(inpath))

    # Save last directory accessed to JSON prefs
    prefs['use_file_path'] = pathof(os.path.dirname(inpath))

    # Save prefs to json
    bk.savePrefs(prefs)

    try:
        with file_open(inpath,'rb')as fp:
            data = fp.read()
    except:
        title = 'Unexpected error!'
        msg = 'Error reading the {} file. Perhaps it is corrupt or missing?'.format(XMLFILE)
        show_msgbox(title, msg, 'error')
        return -1

    if _DEBUG_:
        print('Internal epub href: META-INF/{}\n'.format(XMLFILE))

    bk.addotherfile('META-INF/{}'.format(XMLFILE), data)

    return 0

def main():
    print ('I reached main when I should not have\n')
    return -1

if __name__ == "__main__":
    sys.exit(main())
