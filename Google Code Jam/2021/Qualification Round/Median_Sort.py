import sys

def solve(N):
    #get first 3 numbers
    query = [1, 2, 3]
    print(*query)
    sys.stdout.flush()
    median = int(input())
    if median == 1:
        ans = [2, 1, 3]
    elif median == 2:
        ans = [1, 2, 3]
    else:
        ans = [1, 3, 2]

    # Find the correct position for the i-indexed element at current array
    for i in range(4, N+1):
        low = 0
        high = len(ans) - 1
        flag = 0

        query = [ans[low], ans[high], i]
        print(*query)
        sys.stdout.flush()
        median = int(input())
        
        # i,low,...,high
        if median == ans[low]:
            ans = [i] + ans
        #low,...,high,i
        elif median == ans[high]:
            ans = ans + [i]
        #low,...,i,...,high
        else:
            #####################################
            while low < high:
                
                if low + 1 == high:
                    query = [ans[low], ans[high], i]
                    print(*query)
                    sys.stdout.flush()
                    median = int(input())
                    
                    if median == ans[low]:
                        ans = ans[:low] + [i] + ans[low:]
                    elif median == ans[high]:
                        ans = ans[:high+1] + [i] + ans[high+1:]
                    else:
                        ans = ans[:low+1] + [i] + ans[low+1:]
                    flag = 1
                    break
                
                mid = (low + high)//2
                query = [ans[low], ans[mid], i]
                print(*query)
                sys.stdout.flush()
                median = int(input())
                
                # Case 1: i...low...mid...high
                if median == ans[low]:
                    flag = 1
                    ans = ans[:low] + [i] + ans[low:]
                    break
                # Case 2: low...mid...i...high
                elif median == ans[mid]:
                    low = mid + 1
                    if low == high:
                        low = low - 1
                        
                # Case 3: low...i...mid...high
                else:
                    high = mid - 1
                    if low == high:
                        high = high + 1
            
            if flag == 0:
                query = [ans[low], ans[high], i]
                
                print(*query)
                sys.stdout.flush()
                median = int(input())
                
                if median == i:
                    ans = ans[:low+1] + [i] + ans[low+1:]
                elif median == ans[low]:
                    ans = ans[:low] + [i] + ans[low:]
                else:
                    ans = ans[:high+1] + [i] + ans[high+1:]
        ##########################################    
    print(*ans)
    sys.stdout.flush()
    response = int(input())    
    return response   


T, N, Q = map(int, input().split())
for _ in range(T):
  
  s = solve(N)
  if s == -1:
      break


