# Author: Guillaume Lecomte <guillaume86@gmail.com>

import os
import subprocess

import sickbeard

from sickbeard import logger, common
from sickbeard.exceptions import ex

class synoDsmNotifier:

  def notify_snatch(self, ep_name):
    if sickbeard.SYNODSM_NOTIFY_ONSNATCH:
      self._notify(common.notifyStrings[common.NOTIFY_SNATCH], ep_name)

  def notify_download(self, ep_name):
    if sickbeard.SYNODSM_NOTIFY_ONDOWNLOAD:
      self._notify(common.notifyStrings[common.NOTIFY_DOWNLOAD], ep_name)
  
  def test_notify(self):
    return self._notify('Test notification', "This is a test notification from Sick Beard", force=True)

  def _notify(self, title, message, force=False):
    if not sickbeard.USE_SYNODSM and not force:
      return False
      
    synonotify_cmd = ['/usr/syno/bin/synodsmnotify', '@users', title, message]
    logger.log(u"Executing command "+str(synonotify_cmd))
    try:
      p = subprocess.Popen(synonotify_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=sickbeard.PROG_DIR)
      out, err = p.communicate() #@UnusedVariable
      logger.log(u"Script result: "+str(out), logger.DEBUG)
    except OSError, e:
      logger.log(u"Unable to run synodsmnotify: "+ex(e))


notifier = synoDsmNotifier
