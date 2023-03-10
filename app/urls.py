from django.urls import path
from app import views

urlpatterns = [
    path("",views.index, name="index"),

    #region Account Links 
    path("login/",views.login, name="login"),
    path("forget/",views.forget, name="forget"),
    path("register/",views.register, name="register"),
    path("staff/",views.staff, name="staff"),
    path("admins/",views.admins, name="admins"),
    path("clients/",views.clients, name="clients"),
    path("permissions/",views.permissions, name="permissions"),
    path("roles/",views.roles, name="roles"),
    path("groups/",views.groups, name="groups"),
    #endregion


    #region Cases
    path("cases/",views.cases, name="cases"),
    path("pending/",views.pending, name="pending"),
    path("closed/",views.closed, name="closed"),
    path("reopen/",views.reopen, name="reopen"),
    path("casetype/",views.casetype, name="casetype"),
    path("evidence/",views.evidence, name="evidence"),
    path("reports/",views.reports, name="reports"),
    #endregion
]