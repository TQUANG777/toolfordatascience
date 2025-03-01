def decimal_num():
    while True:
        try: 
            n=float(input('Input a decimal:'))
            if n<0:
                print('Please enter a positive number.')
            else:
                print(n)
                break
        except:
            print('Please enter a positive number.')

def convert_db_to_kg():
    while True:
        try:
            n=float(input('Enter db:'))
            print('DB->KG:',n*0.453592)
            break
        except:
            print('Try again.')

def convert_inch_to_m():
    while True:
        try:
            n=float(input('Enter height by inch:'))
            print('Inch->M:',n*0.0254)
            break
        except:
            print('Try again.')

def bmi():
    print('What you want to input in SI or imperial:')
    print('0.SI unit(default).')
    print('1.Imperial unit.')
    while True:
        try:
            choice=input('Your choice:')
            
            if choice=='0':
                while True:
                    nang=float(input('Enter your weight(kg):'))
                    cao=float(input('Enter your height(m):'))
                    break
            elif choice=='0':
                nang=float(input('Enter your weight(db):'))
                cao=float(input('Enter your height(inch):'))
                convert_db_to_kg(nang)
                convert_inch_to_m(cao)
                break
            bmi=nang/cao**2
            if bmi<18.5:
                c='Thick'
            elif 18.5<=bmi<=25:
                c='Average'
            elif bmi>25:
                c='Obey'
            print('Your bmi:',round(bmi,1),'Your class:',c)
        except:
            print('Try again.')
def weighted_average(scores, weights):
    """
    Calculate the weighted average of scores.

    Parameters:
    scores (list of float): The list of scores.
    weights (list of float): The list of weights corresponding to the scores.

    Returns:
    float: The weighted average of the scores.
    """
    if len(scores) != len(weights):
        raise ValueError("The length of scores and weights must be the same.")
    
    total_weight = sum(weights)
    if total_weight == 0:
        raise ValueError("The sum of weights must not be zero.")
    
    weighted_sum = sum(score * weight for score, weight in zip(scores, weights))
    
    return weighted_sum / total_weight


def main():
    choice=input('Chọn câu:')
    if choice=='1':
        decimal_num()
        convert_db_to_kg()
        convert_inch_to_m()
        bmi()
    elif choice=='2':
        scores = [10, 5, 6, 7]
        weights = [1, 2, 3, 4]
        print('(',tuple(scores),',',tuple(weights),')')
        print(weighted_average(scores, weights))


    #elif choice=='3':
    

if __name__=='__main__':
    main()
    
    
        

        


        
        
    