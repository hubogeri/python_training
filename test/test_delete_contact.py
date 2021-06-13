from model.contact import Contact


def test_delete_first_contact(app):
    app.contact.ensure_contact_exists(Contact(fname="contact to delete"))
    app.contact.delete_first_contact()
