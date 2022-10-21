from django.urls import path

from .views import (RegisterView, RetrieveUserView, UpdateGeneralSettingView,
                    UpdatePasswordView)

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register_user"),
    path('me/', RetrieveUserView.as_view(), name="retrieve_user"),
    # path('updatepassword/', UpdatePasswordView.as_view(), name="update_password"),
    # path('generalsetting/', UpdateGeneralSettingView.as_view(),
    #      name="update_general_setting"),

]
