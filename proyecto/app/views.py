from django.shortcuts import render
import datetime
from .models import *
from django.http import JsonResponse
import json
from .utils import cookieCart, cartData, guestOrder

def store(request):
    data = cartData(request)
    cartItems = data['cartItems']

    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'generales/store.html', context)

def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    items = data['items']
    order = data['order']
        
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'generales/cart.html', context)

def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    items = data['items']   
    order = data['order']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'generales/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('productId:', productId)
    print('action:', action)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1
    
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('El producto fue agregado', safe=False)

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def processOrder(request):
    try:
        transaction_id = datetime.datetime.now().timestamp()
        data = json.loads(request.body)

        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
        else:
            customer, order = guestOrder(request, data)

        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if abs(total - order.get_cart_total) > 0.01:
            return JsonResponse({'error': 'Total no coincide con el carrito'}, status=400)

        order.complete = True
        order.save()

        if order.shipping:
            shipping_data = data.get('shipping', {})
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                direccion=shipping_data.get('direccion', ''),
                ciudad=shipping_data.get('ciudad', ''),
                departamento=shipping_data.get('departamento', ''),
                pais=shipping_data.get('pais', ''),
                zip=shipping_data.get('zip', ''),
            )

        return JsonResponse('El pago fue procesado', safe=False)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

