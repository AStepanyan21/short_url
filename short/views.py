from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import URL
from .serializers import URLSerializer


class URLSet(APIView):
    queryset = URL.objects.all()
    serializer_class = URLSerializer

    def get(self, request, format=None):
        snippets = URL.objects.all()
        serializer = URLSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = URLSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


url_set = URLSet.as_view()


def get_short_url(request, url):
    bases_url = URL.objects.get(short_url=url)
    return redirect(bases_url.base_url)
