#from django_filters.rest_framework import DjangoFilterBackend
#from rest_framework.generics import get_object_or_404
#from rest_framework.permissions import IsAdminUser
#from rest_framework.filters import SearchFilter
#from rest_framework.response import Response
#from rest_framework.views import APIView
#from rest_framework import generics
#from .permissions import IsAdminOrCreateOnly
#from .filters import DateRangeFilterBackend

#class HomiyView(generics.ListCreateAPIView):
    #permission_classes = [IsAdminOrCreateOnly]
    #queryset = Homiy.objects.all()
    #serializer_class = serializers.HomiySerializer
    #filter_backends = [DateRangeFilterBackend, SearchFilter, DjangoFilterBackend]
    #search_fields = ['full_name', 'company_name']
    #filterset_fields = ['money', 'status']
    #date_range_filter_fields = ['date_created']


#class HomiyDetailView(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [IsAdminUser]
    #queryset = Homiy.objects.all()
    #serializer_class = serializers.HomiySerializer

# Print funksiyasi
# Mualif Men
# Quydagi kod Hello so'zini konsolga chiqaradi.

#print(2+4*2)
ism = "Abdulloh"
#print(ism)
#ism = "Muhammad"
#print(ism)

#a = 6 
#b = 7 
#c = (a+b)**2
#print(c)

#shaxar = "Qoqon"
#viloyat = "Farg'ona 😂"
#print(viloyat +' '+ shaxar)

#sharif  = "Ali"
#ism_sharif = f"{ism} {sharif}"
#print(f"Mening ismim {sharif} {ism} bo'ladi!")

#print('Hello \tworld!')
#print("Hello \nworld")
#ism = "hali"
#sharif = "vali"
#ism_sharif = f"{ism} {sharif}"
#ism_sharif = ism_sharif.upper()
#print(ism_sharif)
#print(ism_sharif.lower())
#print(ism_sharif.title())
#print(ism_sharif.capitalize()) 
