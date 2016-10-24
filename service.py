# -*- coding: utf-8 -*- 

'''
    Super Subtitle Add-on
    Copyright (C) 2016 Mrknow

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


import codecs, glob, os, shutil, sys, time, urllib
import xbmc , xbmcaddon, xbmcgui, xbmcplugin , xbmcvfs


__addon__       = xbmcaddon.Addon()
__author__      = __addon__.getAddonInfo('author')
__scriptid__    = __addon__.getAddonInfo('id')
__scriptname__  = __addon__.getAddonInfo('name')
__version__     = __addon__.getAddonInfo('version')
__language__    = __addon__.getLocalizedString

__cwd__ = unicode(xbmc.translatePath(__addon__.getAddonInfo('path')), 'utf-8')
__profile__ = unicode(xbmc.translatePath(__addon__.getAddonInfo('profile')), 'utf-8')
__resource__ = unicode(xbmc.translatePath(os.path.join(__cwd__, 'resources', 'lib')), 'utf-8')
__temp__ = unicode(xbmc.translatePath(os.path.join(__profile__, 'temp')), 'utf-8')

sys.path.append(__resource__)