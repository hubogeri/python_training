from model.group import Group


def test_edit_first_group(app):
     app.group.edit_first_group(Group(name="updatedtestname", header="updatedtestheader", footer="updatedtestfooter"))

def test_edit_first_group_name(app):
     app.group.edit_first_group(Group(name="updatedtestname"))


def test_edit_first_group_header(app):
     app.group.edit_first_group(Group(header="updatedtestheader"))


def test_edit_first_group_footer(app):
     app.group.edit_first_group(Group(footer="updatedtestfooter"))