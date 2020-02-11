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