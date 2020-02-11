# Checkout Process

1. Cart -> Checkout View
   - Login/Register or Enter and Email (as Guest)
   - Shipping Address
   - Billing Information
     - Billing Address
     - Credit Card / Payment
     - Coupon Codes

2. Billing App/Component 
   - Billing Profile
     - User or Email (Guest Email)
     - Generate Payment Processor Token (Stripe/BrainTree/Authorize.net)

3. Orders/ Invoices Component
   - Connecting to the Billing Profile
   - Shipping / Billing Address
   - Cart Items
   - Shipment Status - Shipped
   - Order Status - Received
   - Tracking Information
   - Purchase Order Number
   - Order Comments


We created and orders app we added models and configured and migrated
We are Generating the Order ID
has to be random and unique order number

Moved utils to core/utils and updated references in products model

added unique_order_id_generator 

``` python
def unique_order_id_generator(instance):
    """
    This is for a Django Project with and order_id field
    """
    order_new_id = random_string_generator()

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(order_id=order_new_id).exists()
    if qs_exists:
        return unique_slug_generator(instance)
    return order_new_id  
##################################################################

def pre_save_create_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance)

pre_save.connect(pre_save_create_order_id, sender=Order)
```