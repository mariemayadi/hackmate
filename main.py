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
from models import Hacker
from models import Group
from google.appengine.ext import ndb

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
'skills_needed' : ['Back End', 'Java Master']
},
{'groupname': "Mariem",
'description' : 'Hackers matching..what else',
'skills_needed' : ['Front End', 'HTML Wizard']
}
]

class MainHandler(webapp2.RequestHandler):
    def get(self):
        main_page_content = open('mainpage.html').read()
        self.response.write(main_page_content)

class SoloFormHandler(webapp2.RequestHandler):
    def get(self):
        solo_form = open('templates/solo-form.html').read()
        self.response.write(solo_form)

class SoloHackerHandler(webapp2.RequestHandler):
    def post(self):
        logging.info("Inside the DB handler stufff now in group.")
        solo_hacker_name = self.request.get("name")
        solo_hacker_slackid = self.request.get("slackid")
        solo_hacker_skills = self.request.get("skill")
        logging.warning(solo_hacker_skills)
        solo_obj = {
            "hacker_name": solo_hacker_name,
            "slackID" : solo_hacker_slackid,
            "hacker_skills": solo_hacker_skills,
        }


        new_hacker = Hacker (
            hacker_name =  self.request.get("name"),
            slack_id =  self.request.get("slackid"),
            skills = json.loads(self.request.get("skill"))
        )
        new_hacker.put()
        # self.redirect('/groupinput')

        # will be working on databases tomorrow
        # self.response.headers["Content-Type"] = "application/json"
        # self.response.write(json.dumps(solo_obj))


class GroupInputHandler(webapp2.RequestHandler):
    # def get(self):
    def get(self):

        # logging.info("Inside the DB handler stufff now in group.")
        # solo_hacker_name = self.request.get("name")
        # solo_hacker_slackid = self.request.get("slackid")
        # solo_hacker_skills = self.request.get("skill")
        # logging.warning(solo_hacker_skills)
        # solo_obj = {
        #     "hacker_name": solo_hacker_name,
        #     "slackID" : solo_hacker_slackid,
        #     "hacker_skills": solo_hacker_skills,
        # }
        #
        #
        # new_hacker = Hacker (
        #     hacker_name =  self.request.get("name"),
        #     slack_id =  self.request.get("slackid"),
        #     skills = json.loads(self.request.get("skill"))
        # )
        # new_hacker.put()


        template = JINJA_ENVIRONMENT.get_template('templates/team_template.html')
        template_values = {
            "contentArray" : GROUPS_ENTRIES,
        }
        self.response.write(template.render(template_values))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/solo_hacker_form', SoloFormHandler),
    ('/solo_hacker_info', SoloHackerHandler),
    ('/groupinput', GroupInputHandler),
], debug=True)
