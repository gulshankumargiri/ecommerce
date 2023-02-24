from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    title = models.CharField(max_length=150)
    desc = RichTextUploadingField()
    image = models.ImageField(upload_to="image")  # optional

# cart product
# class Cart(models.Model):
#     user = models.ForeignKey(User)
#     active = models.BooleanField(default=True)
#     order_date = models.DateField(null=True)
#     payment_type = models.CharField(max_length=100, null=True)
#     payment_id = models.CharField(max_length=100, null=True)

#     def __unicode__(self): 
#             return "%s" % (self.user)

#     def add_to_cart(self, book_id):
#         book = Book.objects.get(pk=book_id)
#         try:
#             preexisting_order = BookOrder.objects.get(book=book, cart=self)
#             preexisting_order.quantity += 1
#             preexisting_order.save()
#         except BookOrder.DoesNotExist:
#             new_order = BookOrder.objects.create(
#                 book=book,
#                 cart=self,
#                 quantity=1
#                 )
#             new_order.save()

#             def __unicode__(self):
#                 return "%s" % (self.book_id)


#     def remove_from_cart(self, book_id):
#         book = Book.objects.get(pk=book_id)
#         try:
#             preexisting_order = BookOrder.objects.get(book=book, cart=self)
#             if preexisting_order.quantity > 1:
#                 preexisting_order.quantity -= 1
#                 preexisting_order.save()
#             else:
#                 preexisting_order.delete()
#         except BookOrder.DoesNotExist:
#             pass