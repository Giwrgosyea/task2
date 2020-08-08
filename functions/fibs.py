import time


def fib_rec(n):
    '''
    generate fibonacci sequence of given number

    :param n: input number

    returns list
    '''
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        x = fib_rec(n - 1) ## create fibonacci(n-1)
        x.append(sum(x[:-3:-1]))  ## sum the 2 last items and add in list
        return x

def fix_fib(x):
    '''
    replace 0,1,1 with the sum of them

    :param n: input sequence

    returns list 
    '''
    return [2] + x[3:] 


def summ(arr,lis,total,ret):
    '''
    create the sequence that sum to that number from the available fibonacci sequence

    :param arr: fibonacci sequence
    :param lis: list with the sequences 
    :param total: target total sum of each sequence 

    returns list 

    '''
    sum=0
    for i in lis:
        sum+=i

    if sum == total:
        ret.append(lis)


    if sum >= total:
        return

    else:
        for j in range(len(arr)):
            n=arr[j]
            rem=arr[j:]
            summ(rem,lis+[n],total,ret)

    return ret

def task2(n):
    start_time = time.time()
    fib_seq=fix_fib(fib_rec(n)) ## generate fibonacci sequence of given number
    uniq_fib_seq= list(set(list(fib_seq))) ## create unique list of fibonacci sequence
    v = summ(uniq_fib_seq,[],n,[]) ## generate the sequences from the fibonacci sequence that sum to given number
    elapsed_time = time.time() - start_time
    return v,elapsed_time,len(v)


