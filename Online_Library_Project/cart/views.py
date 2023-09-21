from django.shortcuts import render, redirect
from books_list.models import Book
from .models import CartItem
from django.contrib import messages

def view_cart(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)
    context = {'cart_items': cart_items}
    return render(request, 'cart/view_cart.html', context)

def add_to_cart(request, book_id):
    user = request.user
    book = get_object_or_404(Book, pk=book_id)
    
    # Check the number of items in the user's cart
    cart_items_count = CartItem.objects.filter(user=user).count()
    
    if cart_items_count >= 2:
        messages.error(request, "You can only have up to 2 books in your cart.")
    else:
        cart_item, created = CartItem.objects.get_or_create(user=user, book=book)
        messages.success(request, f"Book '{book.title}' added to your cart.")
    
    return redirect('view_cart')

def remove_from_cart(request, cart_item_id):
    user = request.user
    cart_item = get_object_or_404(CartItem, pk=cart_item_id, user=user)
    cart_item.delete()
    messages.success(request, "Book removed from your cart.")
    return redirect('view_cart')
