
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
import json,os
import cgi, cgitb
from resume_parser import resumeparse
import pandas as pd
from io import BytesIO

from django.conf import settings

#data = resumeparse.read_file('C:/Users/aitac/Downloads/resume-parser-master/resume-parser-master/resumes/resume1.docx')

def extracting_candidatename(sample_dict,target,skill):
    cand_list = []
    names_list = []
    ph_list = []
    email_list = []
    skill_list = []
    col_names = ['filename','email','phone','name','total_exp','university','designition','degree','skills','Companies worked at']
    
    for key1,val1 in sample_dict.items():
        for key2,val2 in val1.items():
            if key2 == target :  
                print("before conversion",val2) 	
                val2 = [each_string.lower() for each_string in val2]
                print("after conversion",val2)
                print(skill.lower())
                if skill in val2:
                    print("value",val1["name"])
                    names_list.append(val1["name"])
                    ph_list.append(val1["phone"])
                    email_list.append(val1["email"])
                    skill_list.append(val1["skills"][:6])
                    cand_list.append(key1)
        percentile_list = pd.DataFrame({'name': names_list,'number': ph_list,'email': email_list,'skill': skill_list})
        percentile_list.to_csv("sample.csv")
    return cand_list,percentile_list
	
def index(request):
    return render(request, "webpage1/firstscreen.html")


	
def data_list(file_directory):
    resume_list = []
    data_dict = {}
    for i in os.listdir(file_directory):
        #resume_list.append(i)
        print("file_name",type(i))
        print("file_directory",file_directory)
        print(file_directory+i)
        resume_name_with_comdir = file_directory+i
        print("cmplete directory ",resume_name_with_comdir)
        data = resumeparse.read_file(resume_name_with_comdir)
        file = os.path.basename(i)
        data_dict[file]= data
    return data_dict

	
def ResumeFiletering(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    STATIC_URL = '\\Django_SRIT\\static\\resumes\\' 
    file_directory = BASE_DIR+STATIC_URL
    sample = data_list(file_directory)
    print("dictionary ",sample)
    target = request.POST.get('Target')
    print(target)
    input = request.POST.get('Input')
    print(input)
    res_list,df= extracting_candidatename(sample,target,input)
    print("sample",df)
    emp_records = df.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(emp_records)
    context = {'d': data}
    print("context",context)
    return render(request, 'webpage1/secondscreen.html', context)
    #return render_to_response("webpage1/secondscreen.html", {'datas': df})




