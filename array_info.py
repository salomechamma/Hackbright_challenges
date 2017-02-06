# Brief

# Sometimes we need information about the list/arrays we're dealing with. You'll have to write such a function in this kata. Your function must provide the following informations:

#     Length of the array
#     Number of integer items in the array
#     Number of float items in the array
#     Number of string character items in the array
#     Number of whitespace items in the array

# The informations will be supplied in arrays that are items of another array. Like below:

# Output array = [[array length],[no of integer items],[no of float items],[no of string chars items],[no of whitespace items]]
# Added Difficulty

# If any item count in the array is zero, you'll have to replace it with a None/nil/null value (according to the language). And of course, if the array is empty then return 'Nothing in the array!. For the sake of simplicity, let's just suppose that there are no nested structures. 
# Examples:
# array_info([1,2,3.33,4,5.01,'bass','kick',' '])--------->[[8],[3],[2],[2],[1]]    
# array_info([0.001,2,' '])------------------------------>[[3],[1],[1],[None],[1]]   
# array_info([])----------------------------------------->'Nothing in the array!'
# array_info([' '])-------------------------------------->[[1],[None],[None],[None],[1]]

def array_info(x):

    array1 = [len([i for i in x if type(i)== int])]
    array2 = [len([i for i in x if type(i)== float])]
    array3 = [len([i for i in x if type(i)== str and i != ' '])]
    array4 = [len([i for i in x if i== ' '])]
    array0 = [array1[0]+array2[0]+array3[0]+array4[0]]
    array5 = [array0,array1,array2,array3,array4]
    array6 = [ i if i != [0] else [None] for i in array5]
    array7 = [ i for i in array6 if i != [None]]
    if len(array7)>0:
        return array6
    else:
        return 'Nothing in the array!'

    # or 
def array_info2(x):
    array_info=lambda x: [[len(x)],[len([a for a in x if type(a)==int]) or None],
    [len([a for a in x if type(a)==float]) or None],
    [len([a for a in x if type(a)==str and a!=" "]) or None],
    [len([a for a in x if a==" "]) or None]] if len(x) else 'Nothing in the array!'

    