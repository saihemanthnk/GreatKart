from .models import Category


def nav_links(request):
    categories = Category.objects.all()
    return {"categories":categories}
