from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Category, Comment, Product, ProductReview
from .forms import CommentForm, ProductForm

# Create your views here.

def LikeView(request, pk):
    """ A view to add like button to each product on the product detail page """

    product = get_object_or_404(Product, id=request.POST.get('prod_id'))
    if product.likes.filter(id=request.user.id).exists():
        product.likes.remove(request.user)
    else:
        product.likes.add(request.user)

    return HttpResponseRedirect(reverse('product_detail', args=[str(pk)]))


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search-term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    # Add reviews in the product detail page.

    if request.method == 'POST' and request.user.is_authenticated:
        stars = request.POST.get('stars', 3)
        content = request.POST.get('content', '')

        review = ProductReview.objects.create(product=product, user=request.user, stars=stars, content=content)

        return redirect('product_detail', product_id=product_id)

    context = {
        'product': product
    }

    return render(request, 'products/product_detail.html', context)


# Add Product by Admin
def add_product(request):
    """ Adds product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added Product!')
            # Redirects to the same view
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add Product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


# Edit Product by Admin
def edit_product(request, product_id):
    """ Edits a product in the store """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


# Add Comment
class AddCommentView(CreateView):
    """ A view to add comments to a product """
    model = Comment
    form_class = CommentForm
    template_name = 'products/add_comment.html'
    # fields = '__all__'

    def form_valid(self, form):
        form.instance.product_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('products')


# View Wishlist
@login_required
def wishlist(request):
    """ A view to view all products in user's wishlist """

    products = Product.objects.filter(user_wishlist=request.user)
    return render(request, 'products/user_wish_list.html', {'wishlist': products})


# Add to Wishlist
@login_required
def add_to_wishlist(request, pk):
    """ A view to add products to wishlist """

    product = get_object_or_404(Product, pk=pk)
    url = request.META.get('HTTP_REFERER')
    print("add view")
    print(url)
    if product.user_wishlist.filter(id=request.user.id).exists():
        product.user_wishlist.remove(request.user)
        messages.success(request, product.name + " has been removed to your WishList")
    else:
        product.user_wishlist.add(request.user)
        messages.success(request, "Added " + product.name + " to your WishList")

    return HttpResponseRedirect(url)
