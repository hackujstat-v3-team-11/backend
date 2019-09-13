import random,string
''' Proposer of answer variants based on type of response:
    a) percentage
    b) integer number
    c) decimal (float)
'''
from django.views.debug import cleanse_setting
    
def propose_percentage_answer(answer,N_answers=4,range_symbol='-'):
    # input float in range 0.0-1.0
    response = random.randint(0,N_answers-1)
    min_step = 0.03;
    if answer < 0.01:
        answer = 0.01;
    elif answer > 0.99:
        answer = 0.99;
    else:
        answer = 0.01*int(100*answer)
        
    while response*min_step > answer:
        response -= 1;
    while (N_answers-response-1)*min_step > (1.0-answer):
        response += 1;
    
    before,range_before = response+1,answer;
    after,range_after = N_answers-response,1.0-answer;    
    steps = list( range( int(100.0*min_step),int(100.0*min(range_after/after,range_before/before)),1) )
    
    if len(steps) == 0:
        chosen_step = min_step;
    else:
        chosen_step = 0.01*steps[random.randint(0,len(steps)-1)];
    
    chosen_left = 0.01*float(int(100.0*(answer-0.5*chosen_step)))
    start = chosen_left-((before-1)*chosen_step);
    
    answer_ranges = [];
    for i in range(N_answers+1):
        answer_ranges.append(int(100*(start+i*chosen_step)) )
        
    answer_list = [];
    for i,answer in enumerate(answer_ranges[:-1]):
        answer_list.append( list(string.ascii_uppercase)[i]+': '+
                str(answer_ranges[i])+range_symbol+str(answer_ranges[i+1])+' %' )
    
    return({'answers':answer_list, 'correct': response })

def propose_integer_answer(answer,keep_non_negative=True,N_answers=4,range_symbol='-'):
    response = random.randint(0,N_answers-1)
    min_step = 10;
    
    if keep_non_negative:
        if answer < 0:
            answer = 0;
        while response*min_step > answer:
            response -= 1;
        
        before,range_before = response+1,answer;
                    
        steps = list( range( min_step,int(range_before/before),1) )
        if len(steps) == 0:
            chosen_step = random.randint(5,77);
        else:
            chosen_step = steps[random.randint(0,len(steps)-1)];
    else:
        order = len(str(abs(answer)));
        xorder = max(1,int(abs(answer)/10**order));
        if order > 2:
            steps = list( range( 10**(order-2),3*xorder*10**(order-1),10**(order-2) ) )
            if len(steps) == 0:
                chosen_step = min_step;
            else:
                chosen_step = steps[random.randint(0,len(steps)-1)];        
        else:
            chosen_step = random.randint(min_step,100)
        before,range_before = response+1,answer;
    if keep_non_negative:
        chosen_left = max(0,answer - chosen_step//2);
    else:
        chosen_left = answer - chosen_step//2;
        
    start = chosen_left-((before-1)*chosen_step);
    
    answer_ranges = [];
    for i in range(N_answers+1):
        answer_ranges.append( (start+i*chosen_step) )
        
    answer_list = [];
    for i,answer in enumerate(answer_ranges[:-1]):
        if answer_ranges[i] > 0 and answer_ranges[i+1] > 0:
            answer_list.append( list(string.ascii_uppercase)[i]+': '+
                    str(answer_ranges[i])+range_symbol+str(answer_ranges[i+1]) )
        else:
            answer_list.append( list(string.ascii_uppercase)[i]+': '+
                    str(answer_ranges[i])+'..'+str(answer_ranges[i+1]) )
    
    return( {'answers':answer_list, 'correct': response } )
        

#===============================================================================
# propose_integer_answer(answer,decimal_separator=',',N_answers=4,range_symbol='-'):  
#===============================================================================

        
if __name__ == '__main__':

    # print(propose_percentage_answer(0.31))
    print(propose_integer_answer(-17,keep_non_negative=False))