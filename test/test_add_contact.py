# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(fname="myfirstname", mname="mymiddlename", lname="mylastname", nick="mynickname",
                               title="mytitle", comp="mycompany", addr="myaddress", home="80000000000",
                               mobile="89999999999", work="88888888888", fax="87777777777", email1="email1",
                               email2="email2", email3="email3", homepage="mypage.com", bday="1", bmonth="January",
                               byear="1995", aday="2", amonth="February", ayear="2025", secaddr="mysecondaryaddress",
                               secphone="mysecondaryhome", note="mynotes")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
