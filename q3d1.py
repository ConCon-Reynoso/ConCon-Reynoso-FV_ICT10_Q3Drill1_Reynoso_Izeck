from pyscript import document, display
from pyodide.ffi import create_proxy

def general_weighted_average(e):
    
    #get student's name
    first_name = document.getElementById("first_name").value
    last_name = document.getElementById("last_name").value

    #list of subjects
    subjects = ['Science', 'Math', 'English', 'Filipino', 'ICT', 'PE']

    #get grades from input fields
    science_grade = document.getElementById('science_grade').value
    math_grade = document.getElementById('math_grade').value
    english_grade = document.getElementById('english_grade').value
    filipino_grade = document.getElementById('filipino_grade').value
    ict_grade = document.getElementById('ict_grade').value
    pe_grade = document.getElementById('pe_grade').value

    #calculate GWA
    weighted_sum = (float(science_grade) * 5 + float(math_grade) * 5 + float(english_grade) * 5 + float(filipino_grade) * 3 + float(ict_grade) * 2 + float(pe_grade) * 1)
    total_units = (5 * 3) + 3 + 2 + 1
    gwa = weighted_sum / total_units

    summary = f"""{subjects[0]}: {float(science_grade):.0f}
{subjects[1]}: {float(math_grade):.0f}
{subjects[2]}: {float(english_grade):.0f}
{subjects[3]}: {float(filipino_grade):.0f}
{subjects[4]}: {float(ict_grade):.0f}
{subjects[5]}: {float(pe_grade):.0f}
    """

    #prepare summary of grades
    display(f'Name: {first_name}, {last_name}', target="student_info")
    display(summary, target='summary')
    display(f'Your General Weighted Average is {gwa:.2f}', target='output')


    if gwa > 75 and gwa <= 100:
        display('Status: Passed', target='status')
    elif gwa == 75:
        display('Status: Passed!...Barely', target='status')
    elif gwa < 75 and gwa >= 0:
        display('Status: Failed', target='status')
    elif gwa < 0:
        display('Status: Impossible! You have ventured into the realm of the unknown.', target='status')
    else:
        display('Status: Incredible! You have exceeded what was thought to be possible. You have broken your limits. You have gone further beyond. Plus Ultra!', target='status')

   #document.getElementById('student_info').innerText = f'Name: {first_name}, {last_name}\n{summary}\nYour General Weighted Average is {gwa:.2f}'
submit_button = document.getElementById('general_weighted_average') 
submit_button.addEventListener('click', create_proxy(general_weighted_average)) 