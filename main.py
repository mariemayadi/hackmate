#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import re

class MainHandler(webapp2.RequestHandler):
    def get(self):
        htmlContent = open('templates/solo-form.html').read()
        self.response.write(htmlContent)

class SoloHackerHandler(webapp2.RequestHandler):
    def post(self):
        solo_name = self.request.get("soloname")
        self.response.write("I recieved a request to send ")
        self.response.write(solo_name)
        self.response.write("With these traits: ")
        skills = []
        for key,value in self.request.POST.items():
            re_obj = re.search(r'^skill-(.*)',key)
            if re_obj and value == "on":
                skills.append(re_obj.group(0)
        print skills



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/solohackerinput', SoloHackerHandler),
], debug=True)
