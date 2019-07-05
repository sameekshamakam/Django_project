from django.contrib import admin
from .models import dept_master,sub_dept,book,user,review

admin.site.register(dept_master)
admin.site.register(sub_dept)
admin.site.register(book)
#admin.site.register(bidding)
admin.site.register(user)
admin.site.register(review)



# for registering the models in admin panel
