from django.contrib import admin
from library.models import Book, Borrowing, Reader,Ordering

admin.site.register(Book)
admin.site.register(Borrowing)
admin.site.register(Reader)
admin.site.register(Ordering)

admin.site.name = '信息管理'
admin.site.site_header = '信息管理'
