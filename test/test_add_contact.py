# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_contact(Contact(fname="myfirstname", mname="mymiddlename", lname="mylastname", nick="mynickname", title="mytitle", comp="mycompany", addr="myaddress", home="80000000000", mobile="89999999999", work="88888888888", fax="87777777777", email1="email1", email2="email2", email3="email3", homepage="mypage.com", bday="1", bmonth="January", byear="1995", aday="1", amonth="January", ayear="2025", secaddr="mysecondaryaddress", secphone="mysecondaryhome", note="mynotes"))
    app.session.logout()


