from datetime import datetime, date

def quanto_tenho_pra_gastar(dinheiro_total, proximo_dia_pagamento):
    hoje = datetime.today()
    dias_ate_pagamento = 0
    
    if proximo_dia_pagamento <= hoje.day:
        ano = hoje.year if hoje.month != 12 else hoje.year + 1
        mes = hoje.month + 1 if hoje.month != 12 else 1
        data_pagamento = date(ano, mes, proximo_dia_pagamento)
        dias_ate_pagamento = (data_pagamento - hoje.date()).days
        
    else:
        dias_ate_pagamento = proximo_dia_pagamento - hoje.day
    
    return dinheiro_total / dias_ate_pagamento
    
print(quanto_tenho_pra_gastar(3700, 5))