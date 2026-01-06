from django.db import models

# Create your models here.

class Products(models.Model):
    
    product_name = models.CharField(max_length=25)
    image = models.ImageField(upload_to="prod_imgs" , null=True)
    product_summery = models.CharField(max_length=30)
    product_is_active = models.BooleanField(default=False)
    slug = models.SlugField(max_length=50 , unique=True , blank=False)

    def __str__(self):
        return f"{self.product_name} | {self.product_is_active}"


class Laptop(models.Model):

    LAPTOP_TYPE = [
        ('New' , 'New'),
        ('Used' , 'Used'),
    ]
    

    LAPTOP_BRAND = [
        ('HP' , 'HP'),
        ('Lenovo' , 'Lenovo'),
        ('Asus' , 'Asus'),
        ('Acer' , 'Acer'),
        ('Dell' , 'Dell'),
        ('Surface' , 'Surface'),
    ]


    HAVE_GPU = [
        ('Integrated' , 'Integrated'),
        ('Dedicated ' , 'Dedicated '),
    ]

    CPU_KIND = [
        ('Intel Core i3' , 'Intel Core i3'),
        ('Intel Core i5' , 'Intel Core i5'),
        ('Intel Core i7' , 'Intel Core i7'),
        ('Intel Core i9' , 'Intel Core i9'),
        ('AMD Ryzen 3' , 'AMD Ryzen 3'),
        ('AMD Ryzen 5' , 'AMD Ryzen 5'),
        ('AMD Ryzen 7' , 'AMD Ryzen 7'),
        ('AMD Ryzen 9' , 'AMD Ryzen 9'),
        ('AMD A4' , 'AMD A4'),
        ('AMD A6' , 'AMD A6'),
        ('AMD A8' , 'AMD A8'),
        ('AMD A10' , 'AMD A10'),
        
    ]

    STORAGE_CAPACITY = [
        ('250 GB' , '250 GB'),
        ('256 GB' , '256 GB'),
        ('500 GB' , '500 GB'),
        ('512 GB' , '512 GB'),
        ('650 GB' , '650 GB'),
        ('1 TB' , '1 TB'),
        ('2 TB' , '2 TB'),
        ('4 TB' , '4 TB'),
        ('8 TB' , '8 TB'),
    ]

    STORAGE_TYPE = [
        ('SSD' , 'SSD') ,
        ('HDD' , 'HDD') 
    ]

    type = models.CharField(max_length=40 , choices=LAPTOP_TYPE , null=True , blank=True)
    image = models.ImageField(upload_to="lap_imgs", null=True)
    brand = models.CharField(max_length=10 , choices=LAPTOP_BRAND)
    laptop_model = models.CharField(max_length=30 , null=False , blank=False)
    cpu_kinds = models.CharField(max_length=100 , choices=CPU_KIND)
    cpu_detail = models.CharField(max_length=10)
    ram = models.IntegerField()
    storage = models.CharField(max_length=50 , choices=STORAGE_CAPACITY)
    storage_type = models.CharField(max_length=50 , choices=STORAGE_TYPE)
    gpu = models.CharField(choices=HAVE_GPU)
    gpu_detail = models.CharField(max_length=50 , blank=True)
    price = models.IntegerField()
    description = models.TextField(max_length=500 , blank=True)
    product = models.ForeignKey(Products , on_delete=models.CASCADE , related_name="p_laptops")

    def __str__(self):
        return f"{self.brand} | {self.laptop_model}"
    
    def __str__(self):
        return f"{self.brand} - {self.laptop_model} | price: {self.price:,}"
    

class Computer(models.Model):
    
    mb = models.CharField(max_length=50)
    cpu = models.CharField(max_length=50)
    ram = models.CharField(max_length=40)
    power = models.CharField(max_length=40)
    gpu = models.CharField(max_length=50)
    case = models.CharField(max_length=50 , null=True , blank=True) 
    image = models.ImageField(upload_to="comp_imgs" , null=True)
    product = models.ForeignKey(Products , on_delete=models.CASCADE , related_name="p_computers")

    def __str__(self):
        return f"{self.mb} - {self.cpu}"


class GameConsole(models.Model):

    CONSOLE_MODEL = [
        ('PlayStation', 'PlayStation') ,
        ('Xbox', 'Xbox')
    ]
    
    CONSOLE_TYPE = [
        ('New' , 'New') , 
        ('Used' , 'Used') , 
    ]

    console = models.CharField(max_length=15 , choices=CONSOLE_MODEL)
    type = models.CharField(max_length=10 , choices=CONSOLE_TYPE)
    description = models.TextField(max_length=300)
    image = models.ImageField(upload_to="consols_imgs" , null=True)
    price = models.IntegerField()
    product = models.ForeignKey(Products , on_delete=models.CASCADE , related_name="p_gameconsoles")
    
    def __str__(self):
        return f"{self.console} - {self.type} | price: {self.price:,}"
    

