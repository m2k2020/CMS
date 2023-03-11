from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request, "main.html")

def login(request):
    return render (request, "accounts/login.html")

def forget(request):
    return render (request, "accounts/forget.html")

def register(request):
    return render (request, "accounts/register.html")

def staff(request):
    return render (request, "accounts/staff.html")

def admins(request):
    return render (request, "accounts/admins.html")

def clients(request):
    return render (request, "accounts/clients.html")

def clients(request):
    return render (request, "accounts/clients.html")

def permissions(request):
    return render (request, "accounts/permissions.html")

def roles(request):
    return render (request, "accounts/roles.html")

def groups(request):
    return render (request, "accounts/groups.html")


#region Case Section

def cases(request):
    return render (request, "cases/case.html")

def pending(request):
    return render (request, "cases/pending.html")

def closed(request):
    return render (request, "cases/closed.html")

def reopen(request):
    return render (request, "cases/reopen.html")

def casetype(request):
    return render (request, "cases/casetype.html")

def evidence(request):
    return render (request, "cases/evidence.html")

def reports(request):
    return render (request, "cases/reports.html")


#endregion

#region Logs Section

def erorlogs(request):
    return render (request, "logs/erorlogs.html")

def userlogs(request):
    return render (request, "logs/userlogs.html")

#endregion

def userdisabled(request):
    return render (request, "userdisabled.html")

def userdeleted(request):
    return render (request, "userdeleted.html")


