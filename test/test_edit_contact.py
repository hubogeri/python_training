from model.contact import Contact


def test_edit_first_contact(app):
     app.session.login(username="admin", password="secret")
     app.contact.edit_first_contact(Contact(fname="updatedmyfirstname", mname="updatedmymiddlename", lname="updatedmylastname", nick="updatedmynickname",
                               title="updatedmytitle", comp="updatedmycompany", addr="updatedmyaddress", home="90000000000", mobile="99999999999",
                               work="98888888888", fax="97777777777", email1="updatedemail1", email2="updatedemail2", email3="updatedemail3",
                               homepage="updatedmypage.com", bday="2", bmonth="March", byear="1996", aday="2", amonth="March",
                               ayear="2026", secaddr="updatedmysecondaryaddress", secphone="updatedmysecondaryhome", note="updatedmynotes"))
     app.session.logout()