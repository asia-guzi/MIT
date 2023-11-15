
import random
import string


def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.


    '''
    if len(sequence)==1:
        return [sequence]
       
    else:
        lista=[]
        temp = [a for a in sequence]
      
        for letter in sequence:
            ltemp = temp.copy()
            ltemp.remove(letter)
            nsequence = "".join(ltemp)
           
            lista.extend([(letter+a) for a in get_permutations(nsequence) ])
        return lista
    

def check (expected_output, actual_output):
    output = True
    l1 = len(expected_output) 
    l2 = len(actual_output)
    
    if  not l1 == l2:
        output = False
        
    else:
        out = expected_output[:]
        
        for a in actual_output:
            if a in out:
                out.remove(a)
                
            else:
                output = False
                break  

   
    assert output==True, "Function does not work properly"  
    print("Function does work properly")    

def alternate(sequence, pas, lista):
    
    ind = len(sequence)-len(pas)-1
    if ind == 0:
        for x in sequence:
            
            print(pas+x)
            print(lista)
            if x in pas or (pas+x) in lista:
                        pass
            else:
                lista.append(pas+x)

    else:
        for x in sequence:
        
            if x in pas:
                
                pass
            else:
                    
                alternate(sequence, pas+x, lista)
        
        return lista


if __name__ == '__main__':
   #EXAMPLE
   # example_input1 = 'abc'
   # example_output1 = get_permutations(example_input1)
   # expected_output1 = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
   # print('Input:', example_input1)
   # print('Expected Output:', expected_output1)
   # print('Actual Output:', example_output1)
   # check( expected_output1 , example_output1)

 
 
   for i in range(1,11):

    print("Try no.",i)
    example_input2 = random.sample(string.ascii_lowercase, 4)
    example_output2 = get_permutations(example_input2)
    # expected_output2 = recursionless(example_input2)
    expected_output2 = alternate(example_input2,"",[])
    print("Input", example_input2)
    print('Expected Output:', expected_output2)
    print('Actual Output:', example_output2)
    check( expected_output2,example_output2)

    
