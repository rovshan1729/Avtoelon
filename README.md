# Avtoelon

from rest_framework.exceptions import ValidationError
from rest_framework import generics
from rest_framework.response import Response
from blog.models import Region, District, School, Student, Test
from django.db import models
from django.contrib.postgres.aggregates import ArrayAgg
from django.contrib.postgres.expressions import ArraySubquery
from django.db.models.functions import JSONObject
from django.db.models import OuterRef
from django.db.models.functions import Coalesce


class BlogListAPIView(generics.GenericAPIView):

    def get(self, request):
        # regions = Region.objects.all().annotate(
        #     student_res=models.Avg("districts__schools__students__tests__percentage")
        # )
        # # print(regions.__dict__)
        # for region in regions:
        #     print(region.student_res)

        # 2
        # districts = (
        #     District.objects.filter(region_id=OuterRef("id"))
        #     .annotate(
        #         result=Coalesce(models.Avg("schools__students__tests__percentage"), 0)
        #     )
        #     .values(json=JSONObject(title="title", result="result"))
        #     .order_by("-result", "title")[:3]
        # )
        # regions = Region.objects.all().annotate(student_res=ArraySubquery(districts))
        # print(regions.__dict__)
        # for region in regions:
        #     print(region.title)
        #     print(region.student_res)
        #     print("___________")

        # 4

        return Response("hello")
