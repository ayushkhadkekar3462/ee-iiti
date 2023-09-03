from rest_framework.views import APIView
from .serializer import ResearchSerializers, PapersSerializers, ProjectsSerializers, PGLabsSerializer, UGLabsSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Research, Projects, Papers, PGLabs, UGLabs
from achievements.models import Books
import pandas as pd
from people.models import MTech, Phd, BTech


# def faculty():
#     df = pd.read_csv(r'D:\projects\ee-iiti\backend\ee\research\data.csv')
#     print("silfkjshdjkh")
#     name = df.name.tolist()
#     roll_no = df.roll_no.tolist()
#     year = df.year.tolist()
#     for i in range(len(name)):
#         data = BTech.objects.create(name=name[i],
#                                     roll_no=roll_no[i],
#                                     year=year[i])
#         data.save()


class ResearchView(APIView):
    def post(self, request):
        if request.method == "POST":
            serializer = ResearchSerializers(data=request.data)
            if serializer.is_valid():
                data = serializer.create(request.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "{} method is not allowed".format(request.method)})


class GetResearchView(APIView):
    def get(self, request):
        if request.method == "GET":

            try:
                research = Research.objects.all()
            except research.DoesNotExist:
                return Response({"error": "No research"}, status=404)
            research = ResearchSerializers(research, many=True)
            return Response(research.data)
        return Response({"message": "{} method is not allowed".format(request.method)})


class ProjectView(APIView):
    def post(self, request):
        if request.method == "POST":
            serializer = ProjectsSerializers(data=request.data)
            if serializer.is_valid():
                data = serializer.create(request.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "{} method is not allowed".format(request.method)})


class GetProjectView(APIView):
    def get(self, request):
        if request.method == "GET":
            try:
                project = Projects.objects.all()
            except project.DoesNotExist:
                return Response({"error": "No project"}, status=404)
            project = ProjectsSerializers(project, many=True)
            return Response(project.data)
        return Response({"message": "{} method is not allowed".format(request.method)})


class LabsView(APIView):
    def post(self, request):
        if request.method == "POST":
            serializer = PGLabsSerializer(data=request.data)
            if serializer.is_valid():
                data = serializer.create(request.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "{} method is not allowed".format(request.method)})


class GetUGLabsView(APIView):
    def get(self, request):
        # faculty()
        print("hwloooo")
        if request.method == "GET":
            try:
                Lab = UGLabs.objects.all()
            except Lab.DoesNotExist:
                return Response({"error": "No Labs"}, status=404)
            Lab = UGLabsSerializer(Lab, many=True)
            return Response(Lab.data)
        return Response({"message": "{} method is not allowed".format(request.method)})


class GetPGLabsView(APIView):
    def get(self, request):
        # faculty()
        print("hwloooo")
        if request.method == "GET":
            try:
                Lab = PGLabs.objects.all()
            except Lab.DoesNotExist:
                return Response({"error": "No Labs"}, status=404)
            Lab = PGLabsSerializer(Lab, many=True)
            return Response(Lab.data)
        return Response({"message": "{} method is not allowed".format(request.method)})


class PapersView(APIView):
    def post(self, request):
        if request.method == "POST":
            serializer = PapersSerializers(data=request.data)
            if serializer.is_valid():
                data = serializer.create(request.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "{} method is not allowed".format(request.method)})


class GetPapersView(APIView):
    def get(self, request):
        if request.method == "GET":
            try:
                paper = Papers.objects.all()
            except paper.DoesNotExist:
                return Response({"error": "No papers"}, status=404)
            paper = ResearchSerializers(paper, many=True)
            return Response(paper.data)
        return Response({"message": "{} method is not allowed".format(request.method)})


class GetResearchBySpecialisation(APIView):
    def get(self, request, specialization):
        if request.method == "GET":
            try:
                research = Research.objects.filter(
                    specialization=specialization).values()
                print(research)
                people = []
                for i in research:
                    if i['person'] not in people:
                        people.append(i['person'])
            except Research.DoesNotExist:
                return Response({"message": "Research not found"}, status=status.HTTP_404_NOT_FOUND)
            return Response({"research": research, "people": people})
        return Response({"message": "{} method is not allowed".format(request.method)})
