from django.urls import path
from . import views


urlpatterns = [
    path('create-employee/', views.create_employee_view, name='create_employee'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('employee-list/', views.employee_list_view, name='employee_list'),  # Employee list route
    path('', views.home_view, name='home'),  # Home URL
    path('employee/<int:id>/', views.employee_detail_view, name='employee_detail'),  # Detail route (if needed)
#     path('employee/edit/<int:id>/', views.employee_edit_view, name='employee_edit'),  # Edit employee
    path('employee/delete/<int:id>/', views.employee_delete_view, name='employee_delete'),  # Delete employee
    # path('employee/edit/<int:id>/', views.employee_edit_view, name='employee_edit'),
    # path('create-employee/', views.create_employee_view, name='create_employee'),
    # path('create-employee/', views.create_employee, name='create_employee'), 
    # path('create-employee/', views.create_employee, name='create_employee'),
    path('success/', views.success_view, name='success_page'),
    # path('employee/edit/<int:pk>/', views.edit_employee_view, name='edit_employee'),
    path('employee/edit/<int:pk>/', views.employee_edit_view, name='employee_edit'),  # Correct pattern using 'pk'
]


from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







