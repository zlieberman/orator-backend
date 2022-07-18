from re import M
from .models import Assignment, Book, Classroom, MissedWord, StudentProfile, UserAssignment
from .serializers import AssignmentSerializer, BookSerializer, MissedWordSerializer, StudentProfileSerializer, UserAssignmentSerializer, UserSerializer, ClassroomSerializer
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
    def student_profile_list(self, request, pk):
        user = User.objects.get(id=pk)
        student_profile_qs = user.studentprofile_set.all()
        serializer = StudentProfileSerializer(student_profile_qs, many=True)
        return Response(serializer.data)  

    @action(detail='False')
    def missed_word_list(self, request, pk):
        user = User.objects.get(id=pk)
        student_profile_qs = user.studentprofile_set.all()
        missed_word_qs = []
        for student_profile in student_profile_qs:
            userassignment_qs = student_profile.userassignment_set.all()
            for userassignment in userassignment_qs:
                missed_word_qs += userassignment.missedword_set.all()
                
        serializer = MissedWordSerializer(missed_word_qs, many=True)
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

    @action(detail='False')
    def student_profile_list(self, request, pk):
        classroom = Classroom.objects.get(id=pk)
        student_profile_qs = classroom.studentprofile_set.all()
        serializer = StudentProfileSerializer(student_profile_qs, many=True)
        return Response(serializer.data)   

    @action(detail='False')
    def user_assignment_list(self, request, pk):
        classroom = Classroom.objects.get(id=pk)
        assignment_qs = classroom.assignment_set.all()
        # now from the assignments get the UserAssignments
        userassignment_qs = []
        for assignment in assignment_qs:
            userassignment_qs += assignment.userassignment_set.all()

        serializer = UserAssignmentSerializer(userassignment_qs, many=True)
        return Response(serializer.data)

    @action(detail='False')
    def missed_word_list(self, request, pk):
        classroom = Classroom.objects.get(id=pk)
        # first get all Assignments
        assignment_qs = classroom.assignment_set.all()
        missedword_qs = []
        # next get all UserAssignments
        for assignment in assignment_qs:
            userassignment_qs = assignment.userassignment_set.all()
            # now for all userassignments get the missed words
            for userassignment in userassignment_qs:
                missedword_qs += userassignment.missedword_set.all()

        serializer = MissedWordSerializer(missedword_qs, many=True)
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

    @action(detail='False')
    def missed_word_list(self, request, pk):
        assignment = Assignment.objects.get(id=pk)
        userassignment_qs = assignment.userassignment_set.all()
        missedword_qs = []
        # now for all userassignments get the missed words
        for userassignment in userassignment_qs:
            missedword_qs += userassignment.missedword_set.all()

        serializer = MissedWordSerializer(missedword_qs, many=True)
        return Response(serializer.data)


class UserAssignmentViewSet(viewsets.ModelViewSet):
    queryset = UserAssignment.objects.all()
    serializer_class = UserAssignmentSerializer

    @action(detail='False')
    def missed_word_list(self, request, pk):
        user_assignment = UserAssignment.objects.get(id=pk)
        missed_word_qs = user_assignment.missedword_set.all()
        serializer = MissedWordSerializer(missed_word_qs, many=True)
        return Response(serializer.data)


class MissedWordViewSet(viewsets.ModelViewSet):
    queryset = MissedWord.objects.all()
    serializer_class = MissedWordSerializer


class StudentProfileViewSet(viewsets.ModelViewSet):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer

    @action(detail='False')
    def user_assignment_list(self, request, pk):
        student_profile = StudentProfile.objects.get(id=pk)
        user_assignment_qs = student_profile.userassignment_set.all()
        serializer = UserAssignmentSerializer(user_assignment_qs, many=True)
        return Response(serializer.data)