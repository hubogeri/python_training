from sys import maxsize


class Contact:

    def __init__(self, fname=None, mname=None, lname=None, nick=None, title=None, comp=None, addr=None,
                 home=None, mobile=None, work=None, fax=None, email1=None, email2=None, email3=None,
                 homepage=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None, ayear=None,
                 secaddr=None, secphone=None, note=None, id =None):
        self.fname = fname
        self.mname = mname
        self.lname = lname
        self.nick = nick
        self.title = title
        self.comp = comp
        self.addr = addr
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.secaddr = secaddr
        self.secphone = secphone
        self.note = note
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.fname, self.lname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.fname == other.fname and self.lname == other.lname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

