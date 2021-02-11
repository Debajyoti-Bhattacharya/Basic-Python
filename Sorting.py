def get_max(a,compare):
    largest = a[0]
    for item in a[1:]:
        if compare(item,largest):
            largest = item
        
    return largest



def bubble_sort(a,compare):
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if compare(a[j],a[j+1]):
                a[j+1] , a[j] = a[j] , a[j+1]
                
                
    return a