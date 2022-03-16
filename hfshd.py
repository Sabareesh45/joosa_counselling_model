from tkinter import *
import pandas as pd
import math

root = Tk()
root.geometry('800x500')
root.resizable(0, 0)
root.title("JoSAA counselling")

Label(root, text='JoSAA counselling', font='arial 20 bold').pack()

##enter link
linkstu = StringVar()
Label(root, text='Paste student data location Here:', font='arial 15 bold').place(x=160, y=60)
link_enter = Entry(root, width=70, textvariable=linkstu).place(x=150, y=90)

linkcol = StringVar()
Label(root, text='Paste college data location Here:', font='arial 15 bold').place(x=160, y=150)
link_enter = Entry(root, width=70, textvariable=linkcol).place(x=150, y=180)

# function to download video


def Executer():
    url1 =(str(linkstu.get()))

    url2 = (str(linkcol.get()))

    def prepcol(col, gres=0.3, cres=0.25):
        coldic = {}
        for i in range(col.shape[0]):
            # for i in range(1):

            # For every college
            name_col = col.iloc[i]['Name of College']
            matr = {}

            for j in range(1, col.shape[1]):
                # For every branch
                branch = []
                dic = {}
                name_branch = col.columns[j]
                total = col.iloc[i][col.columns[j]]

                pwd_seat = math.ceil(0.05 * total)
                total = total - pwd_seat
                res_seat = math.ceil(cres * total)
                gen_seat = total - res_seat
                fo_seat = math.ceil(gen_seat * gres)
                mo_seat = gen_seat - fo_seat
                fr_seat = math.ceil(gres * res_seat)
                mr_seat = res_seat - fr_seat

                dic['mo'] = mo_seat
                dic['fo'] = fo_seat
                dic['mr'] = mr_seat
                dic['fr'] = fr_seat
                dic['pwd'] = pwd_seat

                branch.append(dic)
                branch.append([])

                matr[name_branch] = branch

            coldic[name_col] = matr

        return coldic

    def prepare_stud(stu):
        stu = stu.sort_values(stu.columns[2], axis=0)
        stu = stu.set_index(stu.columns[2]).reset_index()

        studic = {}
        for i in range(stu.shape[0]):
            # for i in range (1):
            dic = {}
            dic["Name"] = stu.iloc[i][stu.columns[2]]
            dic["Rollno"] = stu.iloc[i][stu.columns[1]]
            dic["Gender"] = stu.iloc[i][stu.columns[3]]
            dic["Caste"] = stu.iloc[i][stu.columns[4]]
            dic['PWD'] = stu.iloc[i][stu.columns[5]]
            dic['Rank'] = stu.iloc[i][stu.columns[0]]
            rno = stu.iloc[i][stu.columns[0]]
            # lis=[stu.iloc[i][stu.columns[2]],stu.iloc[i][stu.columns[1]],stu.iloc[i][stu.columns[3]],stu.iloc[i][stu.columns[4]],stu.iloc[i][stu.columns[5]]]
            prefl = []
            for j in range(6, stu.shape[1]):
                if isinstance(stu.iloc[i][stu.columns[j]], float):
                    break

                prefl.append((stu.iloc[i][stu.columns[j]].split("_")))
            # lis.append(prefl)
            dic["prefl"] = prefl
            studic[rno] = dic

        return studic

    col_csv = pd.read_csv(url2)#("C:/Users/pranav/Desktop/New folder/Inputs/Test small/College.csv") 
    stu_csv = pd.read_csv(url1)#("C:/Users/pranav/Desktop/New folder/Inputs/Test small/Student.csv")

    print("Data Inputted")

    college = prepcol(col_csv, gres=0.3, cres=0.25)
    student = prepare_stud(stu_csv)

    print("Data prepared")

    for i in student.keys():
        # for all students
        studata = student[i]
        status = 0
        gender = studata["Gender"]
        caste = studata['Caste']
        pwd = studata['PWD']
        prefli = studata["prefl"]
        l = len(prefli)

        if gender == "M" and caste == 'Gen' and pwd == 'No':
            prefno = 1
            for j in range(l):

                current_pref = prefli[j]
                curr_col = current_pref[0]
                curr_branch = current_pref[1]

                if college[curr_col][curr_branch][0]['mo'] > 0:
                    status = 1
                    college[curr_col][curr_branch][1].append(studata['Rollno'])
                    studata["Seat Allotted"] = current_pref
                    college[curr_col][curr_branch][0]['mo'] -= 1

                if status == 1:
                    studata["Preference Number"] = prefno
                    break
                prefno += 1

            if status == 0:
                studata["Seat Allotted"] = "Sorry, you got no seat"
                studata["Preference Number"] = 0
            # studata.pop(-2)
            student[i] = studata

        elif gender == "M" and caste == 'Res' and pwd == 'No':
            prefno = 1
            for j in range(l):

                current_pref = prefli[j]
                curr_col = current_pref[0]
                curr_branch = current_pref[1]
                if college[curr_col][curr_branch][0]["mo"] > 0:
                    status = 1
                    college[curr_col][curr_branch][1].append(studata['Rollno'])
                    studata["Seat Allotted"] = current_pref
                    college[curr_col][curr_branch][0]['mo'] -= 1
                elif college[curr_col][curr_branch][0]["mr"] > 0:
                    status = 1
                    college[curr_col][curr_branch][1].append(studata['Rollno'])
                    studata["Seat Allotted"] = current_pref
                    college[curr_col][curr_branch][0]['mr'] -= 1
                if status == 1:
                    studata["Preference Number"] = prefno
                    break
                prefno += 1

            if status == 0:
                studata["Seat Allotted"] = "Sorry, you got no seat"
                studata["Preference Number"] = 0
            # studata.pop(-2)

            student[i] = studata

        elif gender == "F" and caste == 'Gen' and pwd == 'No':
            prefno = 1
            for j in range(l):

                current_pref = prefli[j]
                curr_col = current_pref[0]
                curr_branch = current_pref[1]
                if college[curr_col][curr_branch][0]["fo"] > 0:
                    status = 1
                    college[curr_col][curr_branch][1].append(studata['Rollno'])
                    studata["Seat Allotted"] = current_pref
                    college[curr_col][curr_branch][0]['fo'] -= 1
                elif college[curr_col][curr_branch][0]["mo"] > 0:
                    status = 1
                    college[curr_col][curr_branch][1].append(studata['Rollno'])
                    studata["Seat Allotted"] = current_pref
                    college[curr_col][curr_branch][0]['mo'] -= 1
                if status == 1:
                    studata["Preference Number"] = prefno
                    break
                prefno += 1

            if status == 0:
                studata["Seat Allotted"] = "Sorry, you got no seat"
                studata["Preference Number"] = 0
            # studata.pop(-2)
            student[i] = studata

        elif gender == "F" and caste == 'Res' and pwd == 'No':
            prefno = 1
            for j in range(l):

                current_pref = prefli[j]
                curr_col = current_pref[0]
                curr_branch = current_pref[1]
                if college[curr_col][curr_branch][0]["fo"] > 0:
                    status = 1
                    college[curr_col][curr_branch][1].append(studata['Rollno'])
                    studata["Seat Allotted"] = current_pref
                    college[curr_col][curr_branch][0]['fo'] -= 1
                elif college[curr_col][curr_branch][0]["mo"] > 0:
                    status = 1
                    college[curr_col][curr_branch][1].append(studata['Rollno'])
                    studata["Seat Allotted"] = current_pref
                    college[curr_col][curr_branch][0]['mo'] -= 1
                elif college[curr_col][curr_branch][0]["fr"] > 0:
                    status = 1
                    college[curr_col][curr_branch][1].append(studata['Rollno'])
                    studata["Seat Allotted"] = current_pref
                    college[curr_col][curr_branch][0]['fr'] -= 1
                elif college[curr_col][curr_branch][0]["mr"] > 0:
                    status = 1
                    college[curr_col][curr_branch][1].append(studata['Rollno'])
                    studata["Seat Allotted"] = current_pref
                    college[curr_col][curr_branch][0]['mr'] -= 1
                if status == 1:
                    studata["Preference Number"] = prefno
                    break
                prefno += 1

            if status == 0:
                studata["Seat Allotted"] = "Sorry, you got no seat"
                studata["Preference Number"] = 0

            # studata.pop(-2)
            student[i] = studata

        elif pwd == 'Yes':
            prefno = 1
            for j in range(l):
                current_pref = prefli[j]
                curr_col = current_pref[0]
                curr_branch = current_pref[1]
                if college[curr_col][curr_branch][0]["mo"] > 0:
                    status = 1
                    college[curr_col][curr_branch][1].append(studata['Rollno'])
                    studata["Seat Allotted"] = current_pref
                    college[curr_col][curr_branch][0]['mo'] -= 1
                elif college[curr_col][curr_branch][0]["pwd"] > 0:
                    status = 1
                    college[curr_col][curr_branch][1].append(studata['Rollno'])
                    studata["Seat Allotted"] = current_pref
                    college[curr_col][curr_branch][0]['pwd'] -= 1
                if status == 1:
                    studata["Preference Number"] = prefno
                    break
                prefno += 1

            if status == 0:
                studata["Seat Allotted"] = "Sorry, you got no seat"
                studata["Preference Number"] = 0

            # studata.pop(-2)
            student[i] = studata

    dfc = pd.DataFrame(college)
    dfc = dfc.transpose()
    dfc.to_csv(r"C:\Users\Sabareesh\Desktop\Newfolder\Outputs\College data.csv",index=True)#give loaction where u want the outputs to get saved.

    stu = pd.DataFrame(student)
    stu = stu.transpose()
    stu = stu.sort_values(stu.columns[1], axis=0)
    stu = stu.set_index(stu.columns[1]).reset_index()
    stu.to_csv(r"C:\Users\Sabareesh\Desktop\New folder\Outputs\Student data.csv", index=False)#give loaction where u want the outputs to get saved.

    for i in college.keys():
        out = {}
        d1 = college[i]
        for j in d1.keys():
            rol = d1[j][1]
            out[j] = rol
        df = pd.DataFrame.from_dict(out, orient='index')
        df = df.transpose()
        df = df.rename_axis("{}".format(i))
        df.to_csv(r"C:\Users\pranav\Desktop\New folder\Outputs\{}.csv".format(i), index=False)

    print('Data submitted')


    Label(root, text='Executed successfully', font='impact 14 ').place(x=180, y=210)


Button(root, text='Execute', font='arial 15 bold', bg='red', padx=2, command=Executer).place(x=180,y=250)

root.mainloop()
