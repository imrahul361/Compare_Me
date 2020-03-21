import difflib 

file1 = raw_input("Enter the Path of 1st File!! ")
file2 = raw_input("Enter the Path of 2nd File!! ")

file1_lines = open(file1).readlines()
file2_lines = open(file2).readlines()
diff = difflib.HtmlDiff().make_file(file1_lines, file2_lines, file1, file2)

html_file = raw_input("Enter the Path for HTML Report!! ")
diff_report = open(html_file, 'w')
diff_report.write(diff)
diff_report.close()

print("Successfully Done\n")