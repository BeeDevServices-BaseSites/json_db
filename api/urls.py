from django.urls import path
from .views import item, careers, course_card

urlpatterns = [
    # Careers
    path('careers/create', careers.create),
    path('careers', careers.get_all),
    path('careers/<int:id>', careers.get_one),
    path('careers/<int:id>/update', careers.update_one),
    path('careers/<int:id>/delete', careers.delete_one),

    # # course_card
    path('course_card/create', course_card.create),
    path('course_card', course_card.get_all),
    path('course_card/<int:id>', course_card.get_one),
    path('course_card/<int:id>/update', course_card.update_one),
    path('course_card/<int:id>/delete', course_card.delete_one),

    # # Employees
    # path('employees/create', employees.create),
    # path('employees', employees.get_all),
    # path('employees/<int:id>', employees.get_one),
    # path('employees/<int:id>/update', employees.update_one),
    # path('employees/<int:id>/delete', employees.delete_one),

    # # Honeycombs
    # path('honeycombs/create', honeycombs.create),
    # path('honeycombs', honeycombs.get_all),
    # path('honeycombs/<int:id>', honeycombs.get_one),
    # path('honeycombs/<int:id>/update', honeycombs.update_one),
    # path('honeycombs/<int:id>/delete', honeycombs.delete_one),
]