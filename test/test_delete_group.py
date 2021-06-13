from model.group import Group


def test_delete_first_group(app):
    app.group.ensure_group_exists(Group(name="group to delete"))
    app.group.delete_first_group()
