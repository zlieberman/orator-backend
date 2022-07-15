from re import M
from .models import Assignment, Book, Classroom, MissedWord, UserAssignment
from .serializers import AssignmentSerializer, BookSerializer, MissedWordSerializer, UserAssignmentSerializer, UserSerializer, ClassroomSerializer
from rest_framework import viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import action


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    search_fields = ['title', 'description']
    filter_backends = (filters.SearchFilter,)



class UserViewSet(viewsets.ModelViewSet):
    search_fields = ['username', 'email']
    filter_backends = (filters.SearchFilter,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail='False')
    def user_assignment_list(self, request, pk):
        user = User.objects.get(id=pk)
        user_assignment_qs = user.userassignment_set.all()
        serializer = UserAssignmentSerializer(user_assignment_qs, many=True)
        return Response(serializer.data)

    @action(detail='False')
    def classroom_list(self, request, pk):
        user = User.objects.get(id=pk)
        user_classroom_qs = user.classroom_set.all()
        serializer = ClassroomSerializer(user_classroom_qs, many=True)
        return Response(serializer.data)


class ClassroomViewSet(viewsets.ModelViewSet):
    search_fields = ['teacher_id__id']
    filter_backends = (filters.SearchFilter,)
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)

    @action(detail='False')
    def book_list(self, request, pk):
        classroom = Classroom.objects.get(id=pk)
        book_qs = classroom.book_set.all()
        serializer = BookSerializer(book_qs, many=True)
        return Response(serializer.data)

    @action(detail='False')
    def assignment_list(self, request, pk):
        classroom = Classroom.objects.get(id=pk)
        assignment_qs = classroom.assignment_set.all()
        serializer = AssignmentSerializer(assignment_qs, many=True)
        return Response(serializer.data)


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

    @action(detail='False')
    def user_assignment_list(self, request, pk):
        assignment = Assignment.objects.get(id=pk)
        user_assignment_qs = assignment.userassignment_set.all()
        serializer = UserAssignmentSerializer(user_assignment_qs, many=True)
        return Response(serializer.data)


class UserAssignmentViewSet(viewsets.ModelViewSet):
    queryset = UserAssignment.objects.all()
    serializer_class = UserAssignmentSerializer

    @action(detail='False')
    def missed_word_list(self, request, pk):
        assignment = Assignment.objects.get(id=pk)
        user_assignment_qs = assignment.userassignment_set.all()
        serializer = UserAssignmentSerializer(user_assignment_qs, many=True)
        return Response(serializer.data)


class MissedWordViewSet(viewsets.ModelViewSet):
    queryset = MissedWord.objects.all()
    serializer_class = MissedWordSerializer