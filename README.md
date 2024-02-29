# Gulpy
**A Django API for bulk insertion of products and their variants**


# Installing gulpy dependencies
  As a precondition, it is recommended that before installing the
  dependencies, you first create a virtual environment. 
  ```
  $(venv) pip install -r requirements.txt
  ```

# Dependencies that may require your attention for gulpy to run
  After installing the dependencies, a certain package will require
  some tweaking for gulpy to work. The name of the dependency is
  django-bulkmodel.
  
  If, and when, you run gulpy before tweaking this dependency, you
  **might** get the following error, given the current django version provided in 
 requirements.txt. The Error reads:
 ### Unexpected keyword argument, 'providing_args'.
 To resolve the issue, follow the following steps:
 1. Open the file in venv/lib/python<your_version>/site-packages/bulkmodel/signals.py
 2. Replace every occurrence providing_args = [']. For instance:
    ```
       # Before Replacement:
       pre_bulk_create = ModelSignal(providing_args=['instances'])
    ```
    ```
         # After Replacement:
         pre_bulk_create = ModelSignal('instances')
    ```
 3. If you come across a list passed as an instance of the class
    ModelSignal, similar steps apply:
    ```
       # Before Replacement:
       pre_bulk_create = ModelSignal(providing_args=['item_1, item_2 ... item_n'])
    ```
    ```
    # After Replacement:
    pre_bulk_create = ModelSignal(['item_1', 'item_2', ... ,'item_n'])
 
 That's it! 


# Generating fake data
To generate fake data, follow the code fence below.

    ```
        $ python3 manage.py shell

        >>> from products import fake
        >>> fake.products(1000) # create 1000 fake products
        >>> fake.variants(1000) # create 1000 fake variants
    ```


