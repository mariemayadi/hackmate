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

# new_entry = Group(
#                 group_name = "MariemANDJennifer",
#                 description = "This is an awesome project you should aal h=join",
#                 skills_needed = ["Back End","Java Guru", "CSS Pro"],
#                 #hackers = [ahBkZXZ-aGFja21hdGUtYXBwchMLEgZIYWNrZXIYgICAgIDglwoM]
#                 hackers = Hacker.query(Hacker.hacker_name == "test2").fetch(keys_only=True)
#                 #hackers = ndb.Key(Hacker.hacker_name,"test1").get()
# )
#
# new_entry.put()
