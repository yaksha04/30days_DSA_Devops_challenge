arr=[1,2,3,4,5,6,7]
def rotate(arr,k):
    n=len(arr)
    k=k%n
    arr[:]=arr[-k:]+arr[:-k]
rotate(arr,4)
print(arr)
