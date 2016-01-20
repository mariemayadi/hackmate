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
import logging
import re
import jinja2
import os
import json

# We need to specify a Jinja environment. Configurations
JINJA_ENVIRONMENT = jinja2.Environment (
    # Loader: Where will my template be stored. Specify where the templates are.
    # auto : is a safety measure. Avoid say entries like <script> tags
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True
)

GROUPS_ENTRIES = [
{'groupname': "Jennifer",
'description' : 'our project is exactly what you think it is. I will let you guess what that means.',
'skills_needed' : [u'skill-fe', u'skill-be']
},
{'groupname': "Mariem",
'description' : 'Hackers matching..what else',
'skills_needed' : [u'skill-be']
}
]

class MainHandler(webapp2.RequestHandler):
    def get(self):
        htmlContent = open('templates/solo-form.html').read()
        self.response.write(htmlContent)


class SoloHackerHandler(webapp2.RequestHandler):
    def post(self):
        logging.info("Inside the handler.")
        solo_hacker_name = self.request.get("name")
        solo_hacker_slackid = self.request.get("slackid")
        solo_hacker_skills = self.request.get("skill")
        solo_obj = {
            "hacker_name": solo_hacker_name,
            "slackID" : solo_hacker_slackid,
            "hacker_skills": solo_hacker_skills,
        }
        # self.response.headers["Content-Type"] = "application/json"
        # self.response.write(json.dumps(solo_obj))
        # self.response.write("Name is: ")
        # self.response.write(solo_hacker_name)
        # self.response.write("Slack ID is: ")
        # self.response.write(solo_hacker_slackid)
        # self.response.write("Skills are: ")
        # self.response.write(solo_hacker_skills)


class GroupInputHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/group.html')
        template_values = {
            "contentArray" : GROUPS_ENTRIES,
        }
        self.response.write(template.render(template_values))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/solo_hacker_info', SoloHackerHandler),
    ('/groupinput', GroupInputHandler),
], debug=True)
