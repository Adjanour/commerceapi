# Generated by Django 4.2.6 on 2023-11-11 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(db_column='prdIdpk', primary_key=True, serialize=False)),
                ('product_name', models.CharField(blank=True, db_column='prdName', max_length=255, null=True)),
                ('product_description', models.CharField(blank=True, db_column='prdDescription', max_length=255, null=True)),
                ('product_price', models.DecimalField(blank=True, db_column='prdPrice', decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'tblproduct',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductBrand',
            fields=[
                ('productBrandId', models.AutoField(db_column='prdBrandIdpk', primary_key=True, serialize=False)),
                ('productBrandName', models.CharField(blank=True, db_column='prdBrandName', max_length=255, null=True)),
                ('productBrandDescription', models.CharField(blank=True, db_column='prdBrandDesc', max_length=255, null=True)),
            ],
            options={
                'db_table': 'tblproductbrand',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('productCategoryId', models.AutoField(db_column='prdCategoryIdpk', primary_key=True, serialize=False)),
                ('productCategoryName', models.CharField(blank=True, db_column='prdCategoryName', max_length=255, null=True)),
                ('productCategoryDescription', models.CharField(blank=True, db_column='prdCategoryDesc', max_length=255, null=True)),
            ],
            options={
                'db_table': 'tblproductcategory',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('productId', models.AutoField(primary_key=True, serialize=False)),
                ('productName', models.CharField(max_length=255)),
                ('productBrand', models.CharField(max_length=255)),
                ('productCategory', models.CharField(max_length=255)),
                ('productSubcategory', models.CharField(max_length=255)),
                ('productDescription', models.CharField(max_length=255)),
                ('productPrice', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'getproductdetails',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductSubcategory',
            fields=[
                ('productSubcategoryId', models.AutoField(db_column='prdSubCategoryIdpk', primary_key=True, serialize=False)),
                ('productSubcategoryNmae', models.CharField(blank=True, db_column='prdSubCategoryName', max_length=255, null=True)),
                ('productSubcategoryDescription', models.CharField(blank=True, db_column='prdSubCategoryDesc', max_length=255, null=True)),
            ],
            options={
                'db_table': 'tblproductsubcategory',
                'managed': False,
            },
        ),
    ]
