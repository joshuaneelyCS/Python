def check_row_types(row):
    if len(row) != 8:
        print("Length incorrect! (should be 8): " + str(row))
        return False
    ind = 0
    while ind < len(row):
        if type(row[ind]) != float:
            print("Type of element incorrect: " + str(row[ind]) + " which is " + str(type(row[ind])))
            return False
        ind += 1
    return True
	
# define your functions here

def convert_row_type(list):
    newList = []
    for element in range(0, len(list)):
        if element is str:
            newNum = float(list[element].strip())
            newList.append(newNum)
        else:
            newList.append(float(list[element]))
    return(newList)

# Ex. [1300.0, 3.61, 10.0, 7.0, 95.0, 86.0, 91.0, 94.0]
def split_score_grades(list):
    scores = []
    grades = []
    #Loops through the first half of the list and adds values to scores
    for element in range(0, int(len(list)/2)):
        scores.append(list[element])
    #Loops through the second half of the list and adds values to grades
    for element in range(0, int(len(list)/2)):
        grades.append(list[element+4])
    # returns two values
    return (scores, grades)

# Ex. [1300.0, 3.61, 10.0, 7.0]
def calculate_score(list):
    calc_score = ((list[0] / 160) * 0.3) + ((list[1] * 2) * 0.4) + (list[2] * 0.1) + (list[3] * 0.2)
    return(calc_score)

# Ex. [1300.0, 3.61, 10.0, 7.0]
def is_outlier(list):
    # if interest is 0 or if normalized GPA is 2 greater than normalized SAT score
    if list[2] == 0 or (list[1] * 2) > (2+(list[0] / 160)):
        return True
    return False

# Ex. [1330,3.48,1,2]
def calculate_score_improved(list):
    if calculate_score(list) >= 6 or is_outlier(list):
        return True
    return False

# ['91', '85', '97', '88']
def grade_outlier(list):
    new_list = list[:]
    new_list.sort(reverse=True)
    if new_list[-1] < (new_list[-2]-20):
        return True
    return False

# [87,87,88,96]
def grade_improvement(list):
    for grade_index in range(1, len(list)):
        # if the grade is less than the grade of the previous semester, return false
        if list[grade_index] < list[grade_index-1]:
            return False
    return True


def main():

    # Variables
    filename = "admission_algorithms_dataset.csv"
    names = []
    scores = []
    grades = []

    # Open writing files
    student_scores = open('student_scores.csv', 'w')
    chosen_students = open('chosen_students.csv', 'w')
    outliers_file = open('outliers.csv', 'w')
    chosen_improved = open('chosen_improved.csv', 'w')
    better_improved = open('better_improved.csv', 'w')
    composite_chosen = open('composite_chosen.csv', 'w')


    # opens and reads the file
    with open('admission_algorithms_dataset.csv', 'r') as myFile:

        print("Processing " + filename + "...")
        data = myFile.readlines()

        # Loops through each string item in the parent list data
        for lines in range(0, len(data)):

            #Skips the first line of headers
            if lines != 0:

                # stores each element between ',' in a list called myList
                myList = data[lines].split(',')
                # appends the first item: the students name, to a new list called names
                names.append(myList[0])
                # removes the name from the original list
                myList.remove(myList[0])

                # converts myList into integers
                myList = convert_row_type(myList)

                # checks row types
                check_row_types(myList)
                data[lines] = myList
                # splits the scores and the grades and adds them to the two main lists
                s, g = split_score_grades(myList)
                scores.append(s)
                grades.append(g)

                # calculates score
                new_score = calculate_score(s)

                # lines - 1 because the 1st index of headers is skipped, but the name is still stored in 0 in list names
                student_scores.write(f"{names[lines-1]},{new_score:.2f}\n")

                # if their overall score is greater than or equal to 6, they are written on the chosen student file
                if new_score >= 6:
                    chosen_students.write(f"{names[lines-1]}\n")

                #if they are an outlier, they are written on the outlier list
                if is_outlier(s) == True:
                    outliers_file.write(f"{names[lines-1]}\n")

                # if they have an overall score of six or are an outlier with a score >= 5, they are written to the chosen improved list
                if new_score >= 6 or is_outlier(s) and new_score >= 5:
                    chosen_improved.write(f"{names[lines-1]}\n")

                # if returns true, it writes their name and scores to better_improved csv file
                if calculate_score_improved(s):
                    better_improved.write(f'{names[lines-1]},{s[0]},{s[1]},{s[2]},{s[3]}\n')

                if new_score >= 6 or (new_score >= 5 and (is_outlier(s) or grade_outlier(g) or grade_improvement(g))):
                    composite_chosen.write(f"{names[lines-1]}\n")


    student_scores.close()
    chosen_students.close()
    outliers_file.close()
    chosen_improved.close()
    better_improved.close()
    composite_chosen.close()











    # TODO: make sure to close all files you've opened!

    print("done!")

# this bit allows us to both run the file as a program or load it as a
# module to just access the functions
if __name__ == "__main__":
    main()
