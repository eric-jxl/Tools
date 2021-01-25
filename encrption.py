# -*- coding:utf-8 -*-
'''
@Author  : Eric
@Time    : 2020-07-31 11:42
'''

import odoorpc


my_odoo = odoorpc.ODOO('shxijzh.rhfssc.com',port=443,protocol='jsonrpc+ssl')
my_odoo.login('shxijzhdb','system','admin2020')

# res =  my_odoo.execute('purchase.order','read',[86],['order_line'])
# print  str(res).replace('u\'','\'').decode('unicode-escape')

# ret = my_odoo.execute('account.invoice.line','write',[191,193,167,194],{'account_analytic_id':16})
# print ret

# ret =  my_odoo.execute('purchase.order.line','read',[105],[])
# print  str(ret).replace('u\'','\'').decode('unicode-escape')

my_odoo.logout()



# def write_remote(url, dbname, username, pwd, model, ids, value):
#     assert isinstance(ids, list), 'ids must be list'
#     assert isinstance(value, dict), 'value must be dict'
#     my_odoo = odoorpc.ODOO(url, port=443, protocol='jsonrpc+ssl')
#     my_odoo.login(dbname, username, pwd)
#     my_odoo.execute_kw(model, 'write', ids, value)


# write_remote('gaojing.rhfssc.com', 'gaojingdb', 'system', 'zaq1xsw2',
#              'sale.order', [56], {'amount_house_area': 330.00})


