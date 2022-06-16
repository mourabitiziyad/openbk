def debits(transactions):
    total_debit = transactions['debit'].astype(float)
    total_debit = total_debit.sum()

    return total_debit

def credits(transactions):
    total_credit = transactions['credit'].astype(float)
    total_credit = total_credit.sum()
    
    return total_credit

def net_movements(transactions):
    net_mov = credits(transactions) - debits(transactions)
    
    return net_mov