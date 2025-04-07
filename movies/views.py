from rest_framework import generics, views, response
from django.db.models import Count, Avg
from rest_framework.permissions import IsAuthenticated
from movies.models import Movie
from movies.serializers import MovieModelSerializer
from app.permissions import GlobalDefaultPermission
from reviews.models import Review


class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer


#exemplo de Serializer expecifico/ dinamico.
    #def get_serializer_class(self):
    #    if self.request.method == 'GET':
    #        return MovieListDatailSerializer
    #    return MovieModelSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer


class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()

    def get(self, request):
        #buscar todos os dados 
        #montar resposta
        #devolver resposta pro user com estatisticas 
        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
        total_reviews = Review.objects.count()
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']
        return response.Response(
            data={
                'total_movies':total_movies,
                'movies_by_genre': movies_by_genre,
                'total_reviews':total_reviews,
                'average_stars':round (average_stars, 1) if average_stars else 0,
                },
            status=200,
        )
    
   
   
   
   
   
   
   
   
   
    #def post(self, request):

    #utilizando serializer
#def get(self, request):
    #total_movies = self.queryset.count()
    #movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
    #total_reviews = Review.objects.count()
    #average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']
    
    #    data={
    #        'total_movies':total_movies,
    #        'movies_by_genre': movies_by_genre,
    #        'total_reviews':total_reviews,
    #        'average_stars':round (average_stars, 1) if average_stars else 0,
    #        }
    #        serializer = MovieStatSerializer(data=data)
    #        serializer.is_valid(raise_exception=True)

    #        #return response.Response(
    #        data=serializer.validated_data
    #    status=200,
    #   )
    #em serializers.py criar unma classe exemplo MovieStatsSErializer(serializers.Serializer):
    # com os dados 
    #    total_movies = serializers.IntegerField()
    #    movies_by_genre = serializers.ListField(child=serializers.DictField(fields={'genre_name': serializers.CharField(), 'count': serializers.IntegerField()}))
    #    total_reviews = serializers.IntegerField()
    #    average_stars = serializers.FloatField()
    #    #usar o serializer.validated_data para retornar os dados
    #