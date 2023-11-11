from django.db import models
from django.db import connection

class ProductDetailsManger(models.Manager):
    def get_product_details(self):
        with connection.cursor() as cursor:
            cursor.callproc("GetProductDetails")
            results = cursor.fetchall()
            return results
        
# Create your models here.
class ProductDetails(models.Model):
    # Define fields that match the data structure of the stored procedure result
    productId = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=255)
    productBrand = models.CharField(max_length=255)
    productCategory = models.CharField(max_length=255)
    productSubcategory = models.CharField(max_length=255)
    productDescription = models.CharField(max_length=255)
    productPrice = models.DecimalField(max_digits=10, decimal_places=2)
 
    class Meta:
        managed = False
        db_table = 'getproductdetails'
    
class Product(models.Model):
    product_id = models.AutoField(db_column='prdIdpk', primary_key=True)  # Field name made lowercase.
    product_name = models.CharField(db_column='prdName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    product_brand = models.ForeignKey('Productbrand', models.DO_NOTHING, db_column='prdBrandIdfk', blank=True, null=True)  # Field name made lowercase.
    product_category = models.ForeignKey('Productcategory', models.DO_NOTHING, db_column='prdCategoryIdfk', blank=True, null=True)  # Field name made lowercase.
    product_Subcategory = models.ForeignKey('Productsubcategory', models.DO_NOTHING, db_column='prdSubCategoryIdfk', blank=True, null=True)  # Field name made lowercase.
    product_description = models.CharField(db_column='prdDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    product_price = models.DecimalField(db_column='prdPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproduct'


class ProductBrand(models.Model):
    productBrandId = models.AutoField(db_column='prdBrandIdpk', primary_key=True)  # Field name made lowercase.
    productBrandName = models.CharField(db_column='prdBrandName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    productBrandDescription = models.CharField(db_column='prdBrandDesc', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproductbrand'


class ProductCategory(models.Model):
    productCategoryId = models.AutoField(db_column='prdCategoryIdpk', primary_key=True)  # Field name made lowercase.
    productCategoryName = models.CharField(db_column='prdCategoryName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    productCategoryDescription = models.CharField(db_column='prdCategoryDesc', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproductcategory'


class ProductSubcategory(models.Model):
    productSubcategoryId = models.AutoField(db_column='prdSubCategoryIdpk', primary_key=True)  # Field name made lowercase.
    productSubcategoryNmae = models.CharField(db_column='prdSubCategoryName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    productSubcategoryDescription = models.CharField(db_column='prdSubCategoryDesc', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblproductsubcategory'