from django.test import TestCase
from .models import Top, Middle, Bottom


class RegressionTests(TestCase):

    def test_for_query_result_incomplete_with_inheritance(self):
        """ https://github.com/bconstantin/django_polymorphic/issues/15 """

        top = Top()
        top.save()
        middle = Middle()
        middle.save()
        bottom = Bottom()
        bottom.save()

        expected_queryset = [top, middle, bottom]
        self.assertQuerysetEqual(Top.objects.all(), [repr(r) for r in expected_queryset])

        expected_queryset = [middle, bottom]
        self.assertQuerysetEqual(Middle.objects.all(), [repr(r) for r in expected_queryset])

        expected_queryset = [bottom]
        self.assertQuerysetEqual(Bottom.objects.all(), [repr(r) for r in expected_queryset])