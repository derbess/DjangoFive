from django.views import View
from django.shortcuts import render
from myapp1.models import Brand

class BrandListView(View):

    def get(self, request):
        brands = Brand.objects.all()
        return render(request, 'brand_list.html', {
            "title": "Вторая страница",
            "brands": brands
        })