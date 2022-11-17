from django.urls import path

from . import views

app_name = "tasks"

urlpatterns = [

    path("", views.index, name="index"),
    path("start", views.start, name="start"),
    path("salvar", views.salvar, name="salvar"),
    path("editar/<int:id>", views.editar, name="editar"),
    path("update/<int:id>", views.update, name="update"),
    path("delete/<int:id>", views.delete, name="delete"),
    path("cadastrar", views.cadastrar, name="cadastrar"),
    path("add", views.add, name="add"),
    path("sobre", views.sobre, name="sobre"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("<int:funcionario_id>", views.funcionario, name="funcionario"),
    path("<int:funcionario_id>/cadastro", views.cadastro, name="cadastro")
   
]