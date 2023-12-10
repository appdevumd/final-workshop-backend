from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from reviews.models import Review

# Create your views here.
class AppDevClubReviewsView(APIView):
    def get(self, request):
        reviews = []
        for review in Review.objects.filter():
            reviews.append({'review': review.review_text, 'person': review.person})
        return Response({'reviews': reviews})

class CreateAppDevClubReview(APIView):
    def post(self, request):
        print(request.data)
        review = request.data['review']
        person = request.data['personName']
        if review != '':
            new_database_entry = Review(review_text=review, person=person)
            new_database_entry.save()
            return Response({'message': 'success'})
        else:
            return Response({'message': 'failure'})
