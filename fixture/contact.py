from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def init_add_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.init_add_new_contact()
        self.input_general_info(contact.fname, contact.mname, contact.lname, contact.nick, contact.title, contact.comp,
                                contact.addr)
        self.input_phone(contact.home, contact.mobile, contact.work, contact.fax)
        self.input_email(contact.email1, contact.email2, contact.email3)
        self.input_homepage(contact.homepage)
        self.input_birth_date(contact.bday, contact.bmonth, contact.byear)
        self.input_anniversary_date(contact.aday, contact.amonth, contact.ayear)
        self.input_second_info(contact.secaddr, contact.secphone, contact.note)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.return_to_home_page()

    def input_second_info(self, secaddr, secphone, note):
        wd = self.app.wd
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(secaddr)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(secphone)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(note)

    def input_anniversary_date(self, aday, amonth, ayear):
        wd = self.app.wd
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(aday)
        wd.find_element_by_xpath("(//option[@value='1'])[2]").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(amonth)
        wd.find_element_by_xpath("(//option[@value='January'])[2]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(ayear)

    def input_birth_date(self, bday, bmonth, byear):
        wd = self.app.wd
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(bday)
        wd.find_element_by_xpath("//option[@value='1']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(bmonth)
        wd.find_element_by_xpath("//option[@value='January']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(byear)

    def input_homepage(self, homepage):
        wd = self.app.wd
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(homepage)

    def input_email(self, email1, email2, email3):
        wd = self.app.wd
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(email1)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(email3)

    def input_phone(self, home, mobile, work, fax):
        wd = self.app.wd
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(fax)

    def input_general_info(self, fname, mname, lname, nick, title, comp, addr):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(fname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(mname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(lname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(nick)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(comp)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(addr)