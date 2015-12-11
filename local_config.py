#!/usr/bin/python
#coding:utf-8

import os

BASE_PATH = '/Users/CMGS/Documents/Workplace/work/automatic/armin'

LOCAL_REPO_DIR = os.path.join(BASE_PATH, 'repos')
PKEY_DIR = os.path.join(BASE_PATH, 'keys')

ARMIN_PUB_KEY = os.path.join(BASE_PATH, 'root', 'root.pub')

LOCAL_ULIMIT_CONF = os.path.join(BASE_PATH, 'optimize', 'limits.conf')
LOCAL_SYSCTL_FILE = os.path.join(BASE_PATH, 'optimize', 'sysctl.py')

LOCAL_SERVICES_DIR = os.path.join(BASE_PATH, 'services')
