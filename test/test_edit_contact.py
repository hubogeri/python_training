from model.contact import Contact
from random import randrange


def test_edit_some_contact(app):
    app.contact.ensure_contact_exists(Contact(fname="contact to edit"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(fname="updatedmyfirstname", mname="updatedmymiddlename", lname="updatedmylastname",
                nick="updatedmynickname", title="updatedmytitle", comp="updatedmycompany", addr="updatedmyaddress",
                home="90000000000", mobile="99999999999", work="98888888888", fax="97777777777", email1="updatedemail1",
                email2="updatedemail2", email3="updatedemail3", homepage="updatedmypage.com", bday="3", bmonth="March",
                byear="1996", aday="4", amonth="April", ayear="2026", secaddr="updatedmysecondaryaddress",
                secphone="updatedmysecondaryhome", note="updatedmynotes")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
