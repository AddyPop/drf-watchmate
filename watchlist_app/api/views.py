#App import
from watchlist_app.models import watchlist, streamplatform, review
from watchlist_app.api.serializers import watchlistSerializers, streamplatformSerializers, reviewSerializers
#view import
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, mixins, generics

#Generic class
class reviewcreate(generics.CreateAPIView):
    serializer_class = reviewSerializers

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        movie = watchlist.objects.get(pk=pk)
        serializer.save(movie)

class reviewlist(generics.ListAPIView):
    #queryset = review.objects.all()
    serializer_class = reviewSerializers

    def get_queryset(self):
        pk = self.kwargs['pk']
        return review.objects.filter(watchlist=pk)

class reviewdetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = review.objects.all()
    serializer_class = reviewSerializers

#UserMixin view
"""class reviewdetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = review.objects.all()
    serializer_class = reviewSerializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class reviewlist(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = review.objects.all()
    serializer_class = reviewSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

"""

#StreamPlatformList
class streamplatformAV(APIView):
    def get(self, request):
        platform = streamplatform.objects.all()
        serializer = streamplatformSerializers(platform, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = streamplatformSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class streamplatformdetailAV(APIView):
    def get(self, request, pk):
        try:
            platform = streamplatform.objects.get(pk=pk)
        except streamplatform.DoesNotExist:
            return Response({'Error':'Platform does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = streamplatformSerializers(platform)
        return Response(serializer.data)

    def put(self, request, pk):
        platform = streamplatform.objects.get(pk=pk)
        serializer = streamplatformSerializers(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        platform = streamplatform.objects.get(pk=pk)
        platform.delete()
        return Response({'Massage': 'Movie deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


#WatchList

class watchlistAV(APIView):
    def get(self, request):
        watch = watchlist.objects.all()
        serializer = watchlistSerializers(watch, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = watchlistSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class watchdetailsAV(APIView):
    def get(self, request, pk):
        try:
            watch = watchlist.objects.get(pk=pk)
        except watchlist.DoesNotExist:
            return Response({'Error': 'Movie does not found!'}, status=status.HTTP_404_NOT_FOUND)
        serializer = watchlistSerializers(watch)
        return Response(serializer.data)

    def put(self, request, pk):
        watch = watchlist.objects.get(pk=pk)
        serializer = watchlistSerializers(watch,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self,request, pk):
        watch = watchlist.objects.get(pk=pk)
        watch.delete()
        return Response({'Massage': 'Movie deleted successfully'},status=status.HTTP_204_NO_CONTENT)

#----------------Function Based View-----------------------
"""
@api_view(['GET','POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializers = MovieSerializers(movies, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializer = MovieSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET','PUT', 'DELETE'])
def movie_details(request, pk):
    if request.method == 'GET':
        try:
            movies = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'Error':'Movie does not found!'}, status=status.HTTP_404_NOT_FOUND)
        serializers = MovieSerializers(movies)
        return Response(serializers.data)

    elif request.method == 'PUT':
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializers(movie,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    elif request.method == 'DELETE':
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)"""



