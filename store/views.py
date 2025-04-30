import logging
import traceback
from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

# Configure logging
logger = logging.getLogger(__name__)

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def add_product(request):
    logger.info("add_product view called")
    if request.method == 'POST':
        logger.info("POST request received")
        form = ProductForm(request.POST)
        if form.is_valid():
            logger.info("Form is valid")
            try:
                form.save()
                logger.info("Product saved successfully")
                return redirect('product_list')
            except Exception as e:
                logger.error(f"Error saving product: {e}")
                logger.error(traceback.format_exc())
                return render(request, 'store/add_product.html', {'form': form, 'error': str(e)})
        else:
            logger.warning(f"Form errors: {form.errors}")
    else:
        logger.info("GET request received")
        form = ProductForm()
    return render(request, 'store/add_product.html', {'form': form})