import xmlrpc.client

# info = xmlrpc.client.ServerProxy('https://demo.odoo.com/start').start()
# url, db, username, password = \
#     info['host'], info['database'], info['user'], info['password']
# print(info)

url = 'https://psus-demos-trainiing-l-430089.dev.odoo.com'
db = 'psus-demos-trainiing-l-430089'
username = 'admin' 
password = 'admin'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
print(common.version())

uid = common.authenticate(db, username, password, {})

print(uid)

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
if_access = models.execute_kw(db, uid, password,
    'res.partner', 'check_access_rights',
    ['read'], {'raise_exception': False})

print(if_access)

customers = models.execute_kw(db, uid, password,
    'res.partner', 'search',
    [[['is_company', '=', True], ['customer', '=', True]]])

print(customers)

cust_info = models.execute_kw(db, uid, password,
    'res.partner', 'read',
    [customers], {'fields': ['name', 'country_id', 'comment']})

print(cust_info)

id = models.execute_kw(db, uid, password, 'res.partner', 'create', [{
    'name': "New Partner",
    'phone': '99999900',
}])

print(id)

id_changed =  models.execute_kw(db, uid, password, 'res.partner', 'write', [[id], {
    'name': "Newer partner"
}])
print(id_changed)
# get record name after having changed it
new_name = models.execute_kw(db, uid, password, 'res.partner', 'name_get', [[id]])
print(str(new_name))