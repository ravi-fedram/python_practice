#A (90-100), B (80-89), C (70-79), D (60-69), F (below 60)
marks = 60
grdae = ""
if marks < 60:
    grdae = 'F'
elif 60<= marks < 70:
    grdae = 'D'
elif 70<= marks < 80:
    grdae = 'C'
elif 80 <= marks < 90:
    grdae = 'B'
elif 90 <= marks <= 100:
    grdae = 'A'

print("Your grade is ",grdae)
