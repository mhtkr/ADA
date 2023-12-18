(i)- Merge Sort -

import time
def mergeSort(arr):
if len(arr)>1:
mid = len(arr)//2
arr1=arr[:mid]
arr2=arr[mid:]
mergeSort(arr1)
mergeSort(arr2)
i=j=k=0
while i<len(arr1) and j<len(arr2):
if arr[i]<arr2[j]:
arr[k]=arr1[i]
i+=1
else:
arr[k]=arr2[j]
j+=1
k+=1
while i<len(arr1):
arr[k]=arr1[i]
i+= 1
k+= 1
while j<len(arr2):
arr[k]= arr2[j]
j+=1
k+=1
arr=[]
n=int(input("enter no. of elements in array:"))
print("enter elements:", end="")
for i in range(0,n):
el=int(input())
arr.append(el)
start=time.time()
mergeSort(arr)
end=time.time()
print("sorted list is :", end="")
for i in arr:
print(i, end=" ")
print()
print("time taken for sort:", (end-start)*1000, "ms")

(ii)- Quick Sort –

import time
def partition(arr, l, r):
pivot=arr[r]
i = l-1
for j in range(l, r):
if arr[j]<=pivot:
i=i+1
arr[i], arr[j] = arr[j], arr[i]
arr[i+1], arr[r]= arr[r], arr[i+1]
return i + 1
def quickSort(arr, l, r):
if l< r:
q=partition(arr, l, r)
quickSort(arr, l, q-1)
quickSort(arr, q + 1, r)
arr=[]
n=int(input("enter no. of elements in array:"))
print("enter elements:", end="")
for i in range(0,n):
el=int(input())
arr.append(el)
start=time.time()
quickSort(arr, 0, len(arr)-1)
end=time.time()
print("sorted list is :", end="")
for i in arr:
print(i, end=" ")
print()
print("time taken for sort:", (end-start)*1000, "ms")end=time.time()

(iii) Bubble Sort –

import time
def bubble(arr):
n=len(arr)
for i in range(0,n):
for j in range(0, n-i-1):
if (arr[j]>arr[j+1]):
arr[j], arr[j+1]=arr[j+1], arr[j]
arr=[]
n=int(input("enter no. of elements in array:"))
print("enter elements:", end="")
for i in range(0,n):
el=int(input())
arr.append(el)
start=time.time()
bubble(arr)
end=time.time()
print("sorted list is :", end="")
for i in arr:
print(i, end=" ")
print()
print("time taken for sort:", (end-start)*1000, "ms")

(iv) Selection Sort –

import time
def selection(arr):
n=len(arr)
for i in range(0,n-1):
ind=i
for j in range(i+1, n):
if (arr[ind]>arr[j]):
ind=j
arr[ind], arr[i]=arr[i], arr[ind]
arr=[]
n=int(input("enter no. of elements in array:"))
print("enter elements:", end="")
for i in range(0,n):
el=int(input())
arr.append(el)
start=time.time()
selection(arr)
end=time.time()
print("sorted list is :", end="")
for i in arr:
print(i, end=" ")
print()
print("time taken for sort:", (end-start)*1000, "ms")

(v) Heap Sort -

import time
def heapify(arr, n, i):
largest = i
l=2*i+1
r=2*i+2
if l<n and arr[i]<arr[l]:
largest=l
if r<n and arr[largest]<arr[r]:
largest=r
if largest!=i:
arr[i], arr[largest]=arr[largest], arr[i]
heapify(arr, n, largest)
def heapSort(arr):
n=len(arr)
for i in range(n//2, -1, -1):
heapify(arr, n, i)
for i in range(n-1, 0, -1):
arr[i], arr[0] = arr[0], arr[i]
heapify(arr, i, 0)
arr=[]
n=int(input("enter no. of elements in array:"))
print("enter elements:", end="")
for i in range(0,n):
el=int(input())
arr.append(el)
start=time.time()
heapSort(arr)
end=time.time()
print("sorted list is :", end="")
for i in arr:
print(i, end=" ")
print()
print("time taken for sort:", (end-start)*1000, "ms")
