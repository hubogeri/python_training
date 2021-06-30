from selenium.webdriver.support.ui import Select
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def press_add_new_from_nav_pane(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.press_add_new_from_nav_pane()
        self.input_general_info(contact)
        self.input_phone(contact)
        self.input_social_network_info(contact)
        self.input_birth_date(contact)
        self.input_anniversary_date(contact)
        self.input_second_info(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.app.press_home_page_from_nav_pane()
        # submit contact editing
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill contact form
        self.input_general_info(contact)
        self.input_phone(contact)
        self.input_social_network_info(contact)
        self.input_birth_date(contact)
        self.input_anniversary_date(contact)
        self.input_second_info(contact)
        # submit contact updating
        wd.find_element_by_name("update").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_first_contact()
        # submit contact deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # press yes on browser confirmation prompt
        wd.switch_to_alert().accept()
        self.app.press_home_page_from_nav_pane()
        self.contact_cache = None

    def input_second_info(self, contact):
        wd = self.app.wd
        self.change_field_value("address2", contact.secaddr)
        self.change_field_value("phone2", contact.secphone)
        self.change_field_value("notes", contact.note)

    def input_anniversary_date(self, contact):
        wd = self.app.wd
        self.change_option_from_drop_down("aday", contact.aday)
        self.change_option_from_drop_down("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)

    def input_birth_date(self, contact):
        wd = self.app.wd
        self.change_option_from_drop_down("bday", contact.bday)
        self.change_option_from_drop_down("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)

    def input_social_network_info(self, contact):
        wd = self.app.wd
        self.change_field_value("email", contact.email1)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)

    def input_phone(self, contact):
        wd = self.app.wd
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)

    def input_general_info(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.fname)
        self.change_field_value("middlename", contact.mname)
        self.change_field_value("lastname", contact.lname)
        self.change_field_value("nickname", contact.nick)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.comp)
        self.change_field_value("address", contact.addr)

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_option_from_drop_down(self, option_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(option_name).click()
            Select(wd.find_element_by_name(option_name)).select_by_visible_text(text)

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def ensure_contact_exists(self, contact):
        if self.count() == 0:
            self.create(contact)

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                name = element.find_element_by_xpath('//td[3]').text
                surname = element.find_element_by_xpath('//td[2]').text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(fname=name, lname=surname, id=id))
        return list(self.contact_cache)
