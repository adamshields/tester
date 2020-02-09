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
Added tags in DB