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