# Algorithms: Design and Analysis, Part 1
# Week 1: merge sort
# Python 2.7.11

def mergeSort(list):
    print "- Working list: ",list
    if len(list)>1:
        mid = len(list)/2
        lefthalf = list[:mid]
        righthalf = list[mid:]
        
        print "Left half: ",lefthalf
        mergeSort(lefthalf)
        print "Right half: ",righthalf
        mergeSort(righthalf)
        
        i=0; j=0; k=0;
        # sort left and right half into list
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                list[k]=lefthalf[i]
                i=i+1
            else:
                list[k]=righthalf[j]
                j=j+1
            k=k+1
        
        while i < len(lefthalf):
            list[k]=lefthalf[i]
            i=i+1
            k=k+1
        
        while j < len(righthalf):
            list[k]=righthalf[j]
            j=j+1
            k=k+1
    print "Merged list: ",list

list = [3,6,2,1,8,9,4,0,7]
#list = []
#list = [1]
#list = [1,2,3]
#list = [3,2,1]

print "# List:", list
mergeSort(list)
print "# Solution:", list