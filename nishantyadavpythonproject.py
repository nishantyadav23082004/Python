#lists below store data like 25 names and their respective marks of the students
Names = ["Abhishek","Anshul","Rain","Aman","Vivek","Shreyansh","Atul","Virat","Hardik","Krunal","Dinesh","Ravindra","Jasprit","Shami","Ritesh","Akshay","Ajay","Ranbir","Narendra","Rahul","Surya","Yogi","Karan","Satyam","Vasu"]
Marks = [65,91,91,67,43,37,55,77,39,47,79,33,32,31,36,37,44,39,80,80,61,65,78,88,97]
Marks2 = [65,91,91,67,43,37,55,77,39,47,79,33,32,31,36,37,44,39,80,80,61,65,78,88,97]
Update = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Rank = []
#highest = max(Marks)
#index1 = Marks.index(highest)
#prevTopper = Names[index1]

#Asking user if he wants to update
ask = input("do you want to update (yes/no): ")

if (ask == "yes") or (ask == "Yes"):
    name = input("Enter name of the student: ")

    #Checking the validity of the name given by the user
    
    if name not in Names:
        print("Please enter a valid name!!!")
    else:

        #Asking the user for updated marks

        updateMarks = int(input("Enter updated marks: "))

        #Updating the marks given by the user in the list
        
        index1 = Names.index(name)
        prevMarks = Marks[index1]
        
        
        
        Marks2[index1] = updateMarks
        difference = updateMarks - prevMarks
        dict1 = dict(zip(Names,Marks))

        #Finding name of the topper(Student with maximum marks)

        for i in Marks2:
            if i == max(Marks2):
                index2 = Marks2.index(i)
        currentTopper = Names[index2]
        print("Name of the student with maximum marks after updation in marks:",currentTopper)
        
        #Finding jump in given student's rank i.e, prev rank - current rank

        prevRank = Marks.index(max(Marks))
        Marks = sorted(Marks)
        currentRank = 0
        
        jump = prevRank - currentRank
        
        print("The jump in rank is:",jump)
