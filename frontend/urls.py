from django.conf.urls import patterns, include, url
urlpatterns = patterns(
    '',
    url(r'^$', 'frontend.views.main.index', name='main_index'),
    url(r'^index', 'frontend.views.main.index2', name='main_index2'),
    url(r'^register', 'frontend.views.main.register', name='main_register'),
    url(r'^popular_restaurents', 'frontend.views.main.popular_restaurents', name='main_popular_restaurents'),
    url(r'^order', 'frontend.views.main.order', name='main_order'),
    url(r'^login', 'frontend.views.main.login', name='main_login'),
    url(r'^contact', 'frontend.views.main.contact', name='main_contact'),

    # url('hell', 'views.main.hellow', name='main_hellow'),
    # url(r'^logout/$', 'user.LogoutUser', name='logouturl'),
    #
    # url(r'^user/add/$', 'user.AddUser', name='adduserurl'),
    # url(r'^user/list/$', 'user.ListUser', name='listuserurl'),
    # url(r'^user/edit/(?P<ID>\d+)/$', 'user.EditUser', name='edituserurl'),
    # url(r'^user/delete/(?P<ID>\d+)/$', 'user.DeleteUser', name='deleteuserurl'),
    #
    # url(r'^user/changepwd/$', 'user.ChangePassword', name='changepasswordurl'),
    # url(r'^user/resetpwd/(?P<ID>\d+)/$', 'user.ResetPassword', name='resetpasswordurl'),
    #
    # url(r'^role/add/$', 'role.AddRole', name='addroleurl'),
    # url(r'^role/list/$', 'role.ListRole', name='listroleurl'),
    # url(r'^role/edit/(?P<ID>\d+)/$', 'role.EditRole', name='editroleurl'),
    # url(r'^role/delete/(?P<ID>\d+)/$', 'role.DeleteRole', name='deleteroleurl'),
    #
    # url(r'^permission/deny/$', 'permission.NoPermission', name='permissiondenyurl'),
    #
    # url(r'^permission/add/$', 'permission.AddPermission', name='addpermissionurl'),
    # url(r'^permission/list/$', 'permission.ListPermission', name='listpermissionurl'),
    # url(r'^permission/edit/(?P<ID>\d+)/$', 'permission.EditPermission', name='editpermissionurl'),
    # url(r'^permission/delete/(?P<ID>\d+)/$', 'permission.DeletePermission', name='deletepermissionurl'),
)
