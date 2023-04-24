import glob
import sys
import pandas as pd 

all_files = "output/*/*.txt"

result_file = open("result.csv","w")
result_file.write("voter_counter~voter_id~voter_name~husband_name~father_name~house_number~age~gender~filename" + "\n")

for text_file in glob.glob(all_files):
    print(text_file)

    voter_counter = None
    voter_id = None
    voter_name = None
    husband_name = None
    father_name = None
    house_number  = None
    age = None
    gender = None

    
    
    with open(text_file) as handle:
        all_lines = [line.strip() for line in handle]
    
        none_count = 0
        for line in all_lines:

        
            print(line)
            if line.strip().isnumeric():
                voter_counter = line
            else:
                pass
            
            if line.strip().startswith(('S','T','H')):
                voter_id = line
            else:
                pass

            if len(line) > 1:
                if line[0].isdigit():
                    if len(line.split(" ")) == 2:
                        voter_counter = line.split(" ")[0]
                        voter_id = line.split(" ")[1]

                if line[0].isalpha():
                    if len(line.split(" ")) == 1:
                        voter_id = line.split(" ")[0]

                else:
                    pass


            
            if ' வாக்காளர் பெயர்:' in line:
                voter_counter = line.split(" ")[0]
                voter_id = line.split(" ")[1]
                voter_name = line.split('வாக்காளர் பெயர்: ')[-1]
                
            if 'வாக்காளர் பெயர்:' in line:
                voter_name = line.split('வாக்காளர் பெயர்: ')[-1]
            else:
                pass



            if 'கணவர் பெயர்:' in line:
                husband_name = line.split("புதிய")[0].split("கணவர் பெயர்: ")[-1]
            else:
                pass


            if 'தந்தை பெயர்:' in line:
                father_name = line.split("புதிய")[0].split("தந்தை பெயர்: ")[-1]
            else:
                pass

            if "எண்:" in line:
                if "வயது" in line:
                    b = line.split(" ")
                    house_number = ''.join((b[b.index('எண்:')+1:b.index('வயது:')]))
                else:
                    house_number = line.split("எண்:")[-1].strip()
            else:
                pass


            if "எண் :" in line:
                if "வயது" in line:
                    b = line.split(" ")
                    house_number = ''.join((b[b.index('எண்')+1:b.index('வயது:')]))
                else:
                    house_number = line.split("எண் :")[-1].strip()
            else:
                pass

            

            if "வயது" in line:
                if "இனம்" in line:
                    b = line.split(" ")
                    age = ''.join((b[b.index('வயது:')+1:b.index('இனம்:')]))
                else:
                    age = line.split("வயது:")[-1].strip()
            else:
                pass
            
            
            if "இனம்" in line:
                if "பெண்" in line:
                    gender = "பெண்"
                if "ஆண்" in line:
                    gender = "ஆண்"
            else:
                pass


            """
            if voter_counter is not None:
                print(f"counter = {voter_counter}")
            if voter_id is not None:
                print(f"voter_id = {voter_id}")
            if voter_name is not None:
                print(f"voter_name = {voter_name}")

            if husband_name is not None:
                print(f"husband_name = {husband_name}")

            if father_name is not None:
                print(f"father_name = {father_name}")

            if house_number is not None:
                print(f"house number = {house_number}")

            if age is not None:
                print(f"age = {age}")

            if gender is not None:
                print(f"gender = {gender}")
            """    
            
            if voter_counter is None:
                voter_counter = "None"

            if voter_id is None:
                voter_id = "None"

            if voter_name is None:
                voter_name = "None"

            if husband_name is None:
                husband_name = "None"

            if father_name is None:
                father_name = "None"

            if house_number is None:
                house_number = "None"

            if age is None:
                age = "None"

            if gender is None:
                gender = "None"

            
#    result_line = f"{voter_counter~voter_id~voter_name~husband_name~father_name~house_number~age~gender}"
#    print(result_line)
#    result_file.write(result_line)

    none_count = 0
    all_content = [voter_counter, voter_id, voter_name, husband_name, father_name, house_number, age, gender]

    for item in all_content:
        if item == "None":
            none_count = none_count + 1
    
    print(none_count) 
    if not none_count >2:

        result_line = voter_counter + "~" + voter_id + "~" + voter_name + "~" + husband_name + "~"  + father_name + "~" + house_number +"~" + age +"~" + gender + "~" + text_file
        print(result_line)
        result_file.write(result_line + "\n")


    #print(line.split(" "))
    #sys.exit()
