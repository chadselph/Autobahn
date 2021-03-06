###############################################################################
##
##  Copyright 2011 Tavendo GmbH
##
##  Licensed under the Apache License, Version 2.0 (the "License");
##  you may not use this file except in compliance with the License.
##  You may obtain a copy of the License at
##
##      http://www.apache.org/licenses/LICENSE-2.0
##
##  Unless required by applicable law or agreed to in writing, software
##  distributed under the License is distributed on an "AS IS" BASIS,
##  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
##  See the License for the specific language governing permissions and
##  limitations under the License.
##
###############################################################################

from case import Case

class Case2_2(Case):

   DESCRIPTION = """Send ping with small text payload."""

   EXPECTATION = """Pong with payload echo'ed is sent in reply to Ping. Clean close with normal code."""

   def onOpen(self):
      payload = "Hello, world!"
      self.expected[Case.OK] = [("pong", payload)]
      self.expectedClose = {"failedByMe":True,"closeCode":self.p.CLOSE_STATUS_CODE_NORMAL,"requireClean":True}
      self.p.sendFrame(opcode = 9, payload = payload)
      self.p.closeAfter(1)
