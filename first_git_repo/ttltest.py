def cal_average(scores):
    valid_scores = [score for score in scores if isinstance(score, int) and 0 <= score <= 100]
    if not valid_scores:
        return "Error"
    avg = sum(valid_scores) / len(valid_scores)
    return f"{avg:.2f}"

def calculate_class_average(data):
    valid_scores = [score for course in data.values() for score in course if 0 <= score <= 100]
    if not valid_scores:
        return "Error"
    avg = sum(valid_scores) / len(valid_scores)
    return f"{avg:.2f}({len(valid_scores)})"

def signature(firstname_lastname):
    sum_chars = sum(ord(char) for char in firstname_lastname)
    start_line = 7 + sum_chars % 17
    return (start_line, start_line + 30, start_line + 60)

def write_signature_line(output_file, name):
    output_file.write("-" * 20 + f"{name}" + "-" * 20 + "\n")

def main():
    with open("data.txt" , "r") as data_file:
        lines = data_file.readlines()

    data = {}
    student_names = []
    for line in lines[1:]:
        parts = line.strip().split(",")
        name = parts[0]
        scores = [int(score) if score.isdigit() and int(score)<=100 and int(score)>=0 else "Error" for score in parts[1:]]
        data[name] = scores
        student_names.append(name)

    student_names.sort()
    signline=signature("Shoaeb Shaik")

    with open("data.txt", "w") as output_file:
        output_file.write("Student Name,IS300,IS310,IS340,Average\n")
        
        for index,name in enumerate(student_names):
            scores = data[name]
            avg = cal_average(scores)
            if index+2 in signline:
                write_signature_line(output_file,"Shoaeb Shaik")
            output_file.write(f"{name},{','.join(map(str, scores))},{avg}\n")

        output_file.write("Class Average")
        for i, course in enumerate(["IS300", "IS310", "IS340"]):
            scores = [data[name][i] for name in student_names if isinstance(data[name][i], int)]
            avg = calculate_class_average({course: scores})
            output_file.write(f",{avg}")
        output_file.write("\n")

if __name__ == "__main_":
    main()