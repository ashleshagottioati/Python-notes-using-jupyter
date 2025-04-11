import pandas as pd
import numpy as np
def main():
    stats = []
    avg = 4
    std_dev = 2
    no_of_simulations = 5
    no_of_repititions = 100
    sales_target_vals = [6000, 7000, 7500, 9000]
    probs_sales_target = [0.5, 0.1, 0.3, 0.1]
    
    for i in range(no_of_simulations):
        sales_target = np.random.choice(sales_target_vals, no_of_repititions, p=probs_sales_target)
        vals_target = np.random.normal(avg, std_dev, no_of_repititions).round(2)
        df = pd.DataFrame(index=range(no_of_repititions), data={'values_Target': vals_target, 'Sales_Target': sales_target})
        df['Sales'] = df['values_Target'] * df['Sales_Target']
        df['Comission_Rate'] = df['values_Target'].apply(cal_comission_rate)
        df['Comission_Amount'] = df['Comission_Rate'] * df['Sales']
        stats.append((df['Sales'].sum().round(0), df['Comission_Rate'].sum().round(0), df['Comission_Amount'].sum().round(0)))
        
    for x in stats:
        print(x)

def cal_comission_rate(x):
    if x >= 0.7 and x < 0.99:
        return 0.07
    elif x >= 0.55 and x < 0.7:
        return 0.08
    else:
        return 0.06

if __name__ == '__main__':
    main()
