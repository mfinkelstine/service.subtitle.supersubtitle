# -*- coding: utf-8 -*-

import HTMLParser
import os
import re
import urllib
import urllib2
import unicodedata
import json
import zlib
import shutil
import sys
import bs4

try:
    import xbmc
    import xbmcvfs
    import xbmcaddon
except Exception:
    print "unable to load xbmc modules"
    sys.exit(1)



__addon__       = xbmcaddon.Addon()
__version__     = __addon__.getAddonInfo('version')  # Module version
__scriptname__  = __addon__.getAddonInfo('name')
__language__    = __addon__.getLocalizedString
__profile__     = unicode(xbmc.translatePath(__addon__.getAddonInfo('profile')), 'utf-8')
__temp__        = unicode(xbmc.translatePath(os.path.join(__profile__, 'temp', '')), 'utf-8')

def log(msg):
    xbmc.log((u"### [%s] - %s" % (__scriptname__, msg,)).encode('utf-8'), level=xbmc.LOGDEBUG)

class subtitle(object):
    def __init__(self):
        xbmc.log("[script.renegadestv] Scheduling notifications")

class superSubtitleHelper:
    
    def __init__(self):
        log("[script.renegadestv] Scheduling notifications")
    
    def checkLogin(self,notify_success=False):
        log("login checking ")