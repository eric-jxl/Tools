# -*- coding:utf-8 -*-
'''
@Author  : Eric
@Time    : 2020-12-02 11:01
@IDE     : PyCharm
'''

# import os, base64
# print os.path.abspath(os.path.join(os.getcwd()))
# os.chdir(r'/Users/eric/Documents/File/tools')
# with open ('s.jpg', 'rb') as icon:
#     iconData = icon.read()
# iconData = base64.b64encode(iconData)
# print iconData
# LIMIT = 60
# liIcon = []
# while True:
#     sLimit = iconData[:LIMIT]
#     iconData = iconData[LIMIT:]
#     liIcon.append('\'%s\'' % sLimit)
#     if len(sLimit) < LIMIT:
#         break
# print os.linesep.join(liIcon)

# from apscheduler.schedulers.blocking import BlockingScheduler
# from datetime import datetime
# # 输出时间
# def job():
#     print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# # BlockingScheduler
# scheduler = BlockingScheduler()
# scheduler.add_job(job, 'cron', day_of_week='1-5', hour=18, minute=00)
# # scheduler.add_job(job, 'interval', seconds=3,id='job_id')
# scheduler.start()
# scheduler.shutdown(wait=False)

# fixme：预算预删除代码

# @api.multi
# def do_submit(self, need_check=True):
#     # TODO:费用提交检查分析账户的余额/
#     if not self.expense_line_ids:
#         raise UserError(_(u'请输入报销内容！'))
#
#     if self.expense_line_ids:
#
#         total = 0.0
#         balance = 0.0
#         txt = ''
#         for r in self.expense_line_ids.mapped('analytic_account_id'):
#             budget_analytic = self.env['crossovered.budget.lines'].search([('analytic_account_id', '=', r.id)])
#             for val in budget_analytic:
#                 budget_name = val.analytic_account_id.name
#                 date_from = min(budget_analytic.mapped('date_from'))
#                 date_to = max(budget_analytic.mapped('date_to'))
#                 val.sudo()._compute_practical_amount()
#                 new_balance = self.env['crossovered.budget.lines'].search(
#                     [('analytic_account_id', '=', val.analytic_account_id.id),
#                      ('date_from', '>=', date_from), ('date_to', '<=', date_to)])
#                 # 执行计算等函数
#                 # for crossovered in new_balance:
#                 #     crossovered._compute_practical_amount()
#                 #     crossovered._compute_balance()
#
#                 balance = min([-i for i in new_balance.mapped('new_balance')])
#
#                 total = sum(self.expense_line_ids.filtered(lambda x: x.analytic_account_id.name == budget_name)
#                             .mapped('unit_amount'))
#
#             for i in range(len(budget_analytic) / 2):
#                 txt += '%s分析账户' % (budget_name)
#         if need_check and total > balance:
#             strings = str(txt) + '现已超预算，是否继续提交或审批?'
#             return self.jump_to_wizard('do_submit', strings)
#         else:
#             super(HrExpenseSheet, self).do_submit()

# @api.multi
# def do_approved(self, need_check=True):
#     # fixme 审批检查分析账户余额
#     expense_ids = self.expense_line_ids
#     if expense_ids:
#         account_list = expense_ids.mapped('analytic_account_id')
#         total = 0.0
#         balance = 0.0
#         txt = ''
#         for r in account_list:
#             budget_analytic = self.env['crossovered.budget.lines'].search([('analytic_account_id', '=', r.id)])
#             for val in budget_analytic:
#                 budget_name = val.analytic_account_id.name
#                 date_from = min(budget_analytic.mapped('date_from'))
#                 date_to = max(budget_analytic.mapped('date_to'))
#
#                 val.sudo()._compute_practical_amount()
#                 # val.commit()
#                 new_balance = self.env['crossovered.budget.lines'].search(
#                     [('analytic_account_id', '=', val.analytic_account_id.id),
#                      ('date_from', '>=', date_from), ('date_to', '<=', date_to)])
#
#                 balance = min([-i for i in new_balance.mapped('new_balance')])
#                 total = sum(expense_ids.filtered(lambda x: x.analytic_account_id.name == budget_name)
#                             .mapped('unit_amount'))
#             for i in range(len(budget_analytic) / 2):
#                 txt += '%s分析账户' % (budget_name)
#         if need_check and total > balance:
#             strings = str(txt) + '现已超预算，是否继续提交或审批?'
#             return self.jump_to_wizard('do_approved', strings)
#         else:
#             super(HrExpenseSheet, self).do_approved()
