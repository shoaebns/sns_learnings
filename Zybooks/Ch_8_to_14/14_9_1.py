# TODO: Declare any necessary variables here. 
      
      
# TODO: Read a file name from the user and read the tsv file here. 
   
   
# TODO: Compute student grades and exam averages, then output results to a text file here. 
def calculate_letter_grade(average_score):
    if average_score >= 90:
        return 'A'
    elif average_score >= 80:
        return 'B'
    elif average_score >= 70:
        return 'C'
    elif average_score >= 60:
        return 'D'
    else:
        return 'F'

def main():
    file_name = input("Enter the name of the TSV file: ")
    students = []

    try:
        with open(file_name, 'r') as tsv_file:
            for line in tsv_file:
                data = line.strip().split('\t')
                last_name, first_name, midterm1, midterm2, final = data
                midterm1, midterm2, final = map(int, [midterm1, midterm2, final])
                average_score = (midterm1 + midterm2 + final) / 3
                letter_grade = calculate_letter_grade(average_score)
                students.append((last_name, first_name, midterm1, midterm2, final, letter_grade))

        with open('report.txt', 'w') as report_file:
            for student in students:
                report_file.write('\t'.join(map(str, student)) + '\n')

            # Calculate and append the average exam scores
            midterm1_avg = sum(student[2] for student in students) / len(students)
            midterm2_avg = sum(student[3] for student in students) / len(students)
            final_avg = sum(student[4] for student in students) / len(students)

            report_file.write("\nAverages: midterm1 {:.2f}, midterm2 {:.2f}, final {:.2f}\n".format(midterm1_avg, midterm2_avg, final_avg))

        print("Report generated in 'report.txt'")

    except FileNotFoundError:
        print("File not found: " + file_name)

if __name__ == "__main__":
    main()
