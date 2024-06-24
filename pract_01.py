                              # REVERSE A SENTENCE #
def Reverse_sen(Sentence) :
    word=Sentence.split()
    reverse_word=word[::-1]
    reverse_sen=" ".join(reverse_word)
    return reverse_sen
Sentence=input("Enter a Sentence :")
print("the Reversed Sentence :",Reverse_sen(Sentence))    
                   #FIBONACCOI SERIES
def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]
    for i in range(2,n) :
        fibonacci_sequence.append(fibonacci_sequence[-1]+fibonacci_sequence[-2])
    return fibonacci_sequence

# Test the function by printing the Fibonacci sequence up to 10
fibonacci_up_to_10 = generate_fibonacci(10)
print(fibonacci_up_to_10)
                         ### INSERATTION SORT ###
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Test the function with an example array
example_array = [12, 11, 13, 5, 6]
sorted_array = insertion_sort(example_array)
print("Sorted array:", sorted_array)
                    #TEST FOR ARMSTRONG  #
number=int(input("Enter your number :"))
sum=0
remp=number
while remp > 0 :
    digit=remp%10
    sum+=digit**3
    remp//=10
if number==sum :
    print(number,"is a armstrong number ")
else :
    print(number,"is not armstrong number ")
                  #  BUBBLE SORT #
def bubble_sort(arr) :
    for i in range(len(arr)) :
        for j in range(0,len(arr)-i-1) :
            if arr[j]>arr[j+1] :
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr            


print("sorted array using bubble sort :",bubble_sort(example_array))


