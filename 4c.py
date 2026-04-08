import matplotlib.pyplot as plt

subjects = ["Math", "Science", "English", "Computer", "History"]
marks = [85, 90, 78, 92, 80]

# Pie Chart
plt.figure()
plt.pie(marks, labels=subjects, autopct='%1.1f%%')
plt.title("Pie Chart of Marks")
plt.show()

# Bar Chart
plt.figure()
plt.bar(subjects, marks)
plt.title("Bar Chart of Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()