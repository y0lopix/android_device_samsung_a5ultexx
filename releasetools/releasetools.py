# Copyright (C) 2019 LineageOS Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import subprocess

ANDROID_BUILD_TOP = os.getenv('ANDROID_BUILD_TOP')

def FullOTA_InstallEnd(self):
  AddFirmwareFlash(self, self.input_zip)

def IncrementalOTA_InstallEnd(self):
  AddFirmwareFlash(self, self.target_zip)

def AddFirmwareFlash(self, input_zip):
  """Include required binaries to the output zip"""
  
  self.script.AppendExtra('if is_substring("A500HXX", getprop("ro.bootloader")) then')
  self.script.AppendExtra('ui_print("Hardware detected: A500H");')
  self.script.Mount("/system")
  self.script.AppendExtra('run_program("/sbin/sh", "-c", "busybox rm -f /system/vendor/etc/permissions/*nfc*");')
  self.script.AppendExtra('run_program("/sbin/sh", "-c", "busybox rm -f /system/app/Nfc*");')
  self.script.AppendExtra('run_program("/sbin/sh", "-c", "busybox rm -f /system/app/Tag");')
  self.script.AppendExtra('run_program("/sbin/sh", "-c", "busybox rm -f /system/vendor/etc/*nfc*");')
  self.script.AppendExtra('run_program("/sbin/sh", "-c", "busybox rm -f /system/vendor/etc/nfc*");')
  self.script.AppendExtra('run_program("/sbin/sh", "-c", "busybox rm -f /system/lib/libnfc*");')
  self.script.AppendExtra('run_program("/sbin/sh", "-c", "busybox rm -f /system/vendor/bin/hw/*nfc*");')
  self.script.AppendExtra('run_program("/sbin/sh", "-c", "busybox rm -f /system/vendor/etc/init/*nfc*");')
  self.script.AppendExtra('run_program("/sbin/sh", "-c", "busybox rm -f /system/vendor/lib/hw/nfc*");')
  self.script.AppendExtra('run_program("/sbin/sh", "-c", "busybox rm -f /system/vendor/lib/hw/*nfc*");')
  self.script.AppendExtra('run_program("/sbin/sh", "-c", "busybox rm -f /system/vendor/etc/nfc");')
  self.script.AppendExtra('run_program("/sbin/sh", "-c", "busybox rm -f /system/vendor/firmware/nfc");')
  self.script.AppendExtra('run_program("/sbin/sh", "-c", "busybox rm -f /system/vendor/lib/*nfc*");')
  self.script.Unmount("/system")
  self.script.AppendExtra('endif;')

