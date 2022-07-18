from django.urls import include, path
from .views import AssignmentViewSet, BookViewSet, ClassroomViewSet, MissedWordViewSet, StudentProfileViewSet, UserAssignmentViewSet, UserViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('classrooms', ClassroomViewSet, basename='classrooms')
router.register('books', BookViewSet, basename='books')
router.register('users', UserViewSet)
router.register('assignments', AssignmentViewSet)
router.register('userassignments', UserAssignmentViewSet)
router.register('missed_words', MissedWordViewSet)
router.register('students', StudentProfileViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]