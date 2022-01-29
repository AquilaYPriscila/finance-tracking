fout = open('statement.txt', 'w')

def print_statement(income_total,expense_total,savings):
    fout.write('Statement \n')

    fout.write('''
-----------------------------------
Total Income:       ${:.2f}
Total Expenses:     ${:.2f}
Total Savings:      ${:.2f}
----------------------------------
Well done!'''
    .format(income_total, expense_total,savings))
    
    fout.close()
    print('\nYour monthly income and expense statement has been printed in the statement.txt file.')    