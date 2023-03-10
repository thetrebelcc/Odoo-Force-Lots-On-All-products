### TEST LOCALLY BEFORE RUNNING

# Import the necessary libraries
import xmlrpc.client

# Set up connection to the Odoo server
odoo_url = 'http://localhost:8069'
odoo_db = 'my_database'
odoo_username = 'admin'
odoo_password = 'admin'
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(odoo_url))
uid = common.authenticate(odoo_db, odoo_username, odoo_password, {})
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(odoo_url))

# Search for all products in the database
product_ids = models.execute_kw(odoo_db, uid, odoo_password, 'product.template', 'search', [[]])

print("Found {} products".format(len(product_ids)))

# Set all products to use lot codes
for product_id in product_ids:
    models.execute_kw(db, uid, password, 'product.template', 'write', [[product_id], {'tracking': 'lot'}])
    print("Set product {} to use lot codes".format(product_id))
    

print("All products have been set to use lot codes!")

