# Need to come back and visit forloop.counter and available methods 
# https://www.codingforentrepreneurs.com/courses/ecommerce/templates/forloop-counter-cycle

# Columns & Rows Commit
# 1-a Basic Search View
# Display Query to User
# # 6:33 in video - added get_context_data to view so query now == self.request.get('q') about to use it in the template

# Creating the Search form
# https://www.codingforentrepreneurs.com/courses/ecommerce/search-component/creating-search-form

# Better Lookups with Q
# https://www.codingforentrepreneurs.com/courses/ecommerce/search-component/better-lookups-q

"""
We are going to improve the query because it only searches based on the Title field
So we import the Q lookup into the views right now

Q makes lookups for it.  Example Q(title__icontains=query) | Q(description__icontains=query)


example

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None)
        if query is not None:
            lookups = Q(title__icontains=query) | Q(description__icontains=query) # You add the lookups you want to use with Q then return the Products.objects.filter(lookups)
            return Product.objects.filter(lookups).distinct()                     # then return the Products.objects.filter(lookups) # with distinct() # distinct makes sure multiple things matching it this keeps it from showing duplicates
        return Product.objects.featured()
"""

"""
Moving Q into the model manager so we can do our lookups in the DB model not the view model
you have to update your models

##########################################################################################################################

I added to ProductQuerySet & ProductManager search methods under the models.py and they are actually all callable example 

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None)
        if query is not None:
            return Product.objects.search(query) <-- ACTUALLY USING SEARCH FROM MODELS
        return Product.objects.featured()
##########################################################################################################################

improving search method more adding search


fixing space in shirts search using Tags

we have to use tags
it would look similar to this 
Q(tag__name__icontains=query) # if there was a foreign key to this tag
"""

# TAG COMPONENT
# https://www.codingforentrepreneurs.com/courses/ecommerce/search-component/tag-component

# Make a new component called tags

# Basically adding the Tag model class for lookups
# Adding products manytomanyfield that looks up from Products Model
# Added to Admin
# Migrated
# Added tags in DB

# Show how to do a reverse lookup, 

# example get a product based off a tag and tag based off a product

# Shell Commands for a Brief intro to Foreign Keys
# https://www.codingforentrepreneurs.com/courses/ecommerce/search-component/shell-commands-brief-intro-foreign-keys
# https://github.com/codingforentrepreneurs/eCommerce/tree/a85117d052ceaa054f1b025613bbbc46695ea0c0

cd src/
python manage.py shell
from tags.models import Tag

Tag.objects.all() # Show All
Tag.objects.last() # Gets Last on in this case Black
black = Tag.objects.last()
black.title
black.slug

black.products # Shows ManyRelatedManager 

black.products.all() # Shows a Queryset Related to the items in produsts # [<Product: T-SHIRT>, <Product: Hat>, <Product: T-shirt>]

# this gives me the ability to do stuff like 
black.products.all().first() # Which returns the first Product in this case its <Product: T-SHIRT> basically goes from the black tag to the tshirt product


cd src/
python manage.py shell
from products.models import Product

# we have a queryset
qs = Product.objects.all() # Now qs is == Product.objects.all()

tshirt = qs.first() # Grab the first Product TSHIRT

tshirt

# now we can do all the get of the product info
tshirt.title
tshirt.description

# Using reverse for tag to access tag through the model product
tshirt.tag_set # Shows ManyRelatedManager 
tshirt.tag_set.all() # Shows all Tags related to the Tshirt Product that was selected # Returns Queryset <QuerySet [<Tag: T shirt>, <Tag: TShirt>, <Tag: T-shirt>, <Tag: Red>, <Tag: Black>]>
tshirt.tag_set.filter(title__iexact='Black') # I get the actual tag and it brings back that item 


# Finish off Search Query based off tags
# https://www.codingforentrepreneurs.com/courses/ecommerce/search-component/search-related-model
# https://github.com/codingforentrepreneurs/eCommerce/tree/908e3e07bc2e3ec5f157f6a06f59ad01395b4a2d

# Updated Q to contain Tags
# Q(tag__title__icontains=query) this is kind of like when we did # tshirt.tag_set.filter(title__iexact='Black')

# Tags are done in Lookup with Q pretty robust search so far

# CART COMPONENTS ***************** NEW SECTION
# https://www.codingforentrepreneurs.com/courses/ecommerce/cart-component


# # Cart App
# https://www.codingforentrepreneurs.com/courses/ecommerce/cart-component/cart-app
# https://github.com/codingforentrepreneurs/eCommerce/tree/ab6ba98698080e5290f0c72e94edc6ebea229a4e

# CREATE NEW COMPONENT CALLED CARTS

# START OF DJANGO SESSIONS
# https://www.codingforentrepreneurs.com/courses/ecommerce/cart-component/django-sessions
# https://github.com/codingforentrepreneurs/eCommerce/tree/4b2544743e5b3c650231cf10f8f4ba3f85e10382

# Django Sessions basically stores the time that any given user is on the website using the session. Sessions can expire and hang around etc...
# Sessions can be used for names and all kinds of things
# sessions are stored in the database, you can store it in a cookie but speed is an issue thats why db is used for sessions

# here is the documentation for sessions
# https://docs.djangoproject.com/en/3.0/topics/http/sessions/

# sessions have all these different values based on print(dir(request.session))


<django.contrib.sessions.backends.db.SessionStore object at 0x0000021471ACEF70>
['TEST_COOKIE_NAME', 'TEST_COOKIE_VALUE', '_SessionBase__not_given', '_SessionBase__session_key', '__class__', 
'__contains__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', 
'__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', 
'__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_get_new_session_key', '_get_or_create_session_key', 
'_get_session', '_get_session_from_db', '_get_session_key', '_hash', '_session', '_session_key', '_set_session_key', 
'_validate_session_key', 'accessed', 'clear', 'clear_expired', 'create', 'create_model_instance', 'cycle_key', 
'decode', 'delete', 'delete_test_cookie', 'encode', 'exists', 'flush', 'get', 'get_expire_at_browser_close', 
'get_expiry_age', 'get_expiry_date', 'get_model_class', 'get_session_cookie_age', 'has_key', 'is_empty', 'items', 
'keys', 'load', 'model', 'modified', 'pop', 'save', 'serializer', 'session_key', 'set_expiry', 'set_test_cookie', 
'setdefault', 'test_cookie_worked', 'update', 'values']
[09/Feb/2020 16:51:41] "GET /cart/ HTTP/1.1" 200 3559


# CART MODEL
# https://www.codingforentrepreneurs.com/courses/ecommerce/cart-component/cart-model
# https://github.com/codingforentrepreneurs/eCommerce/tree/0441dc0e50937eaec64bafa4f9258de70db7efc9