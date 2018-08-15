
def test_check_info_on_users_page(app):
    user_from_users_page = app.usersproject.get_users_list()[0]
    user_from_edit_user_page = app.usersproject.get_user_info_from_edit_page(0)
    assert user_from_users_page.email == user_from_edit_user_page.email
    assert user_from_users_page.name == user_from_edit_user_page.name
    assert user_from_users_page.role == user_from_edit_user_page.role


def test_check_info_on_view_page(app):
    user_from_view_page = app.usersproject.get_user_from_view_page(0)
    user_from_edit_user_page = app.usersproject.get_user_info_from_edit_page(0)
    assert user_from_view_page.email == user_from_edit_user_page.email
    assert user_from_view_page.name == user_from_edit_user_page.name
    assert user_from_view_page.role == user_from_edit_user_page.role


