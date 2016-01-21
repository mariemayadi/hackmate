from google.appengine.ext import ndb

class Hacker(ndb.Model):
    hacker_name = ndb.StringProperty()
    slack_id = ndb.StringProperty()
    skills = ndb.StringProperty(repeated = True)

class Group(ndb.Model):
    group_name = ndb.StringProperty()
    description = ndb.TextProperty()
    skills_needed = ndb.StringProperty(repeated = True)
    hackers = ndb.KeyProperty(repeated = True)
