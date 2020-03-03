import sys
sys.path.append("..")
from utils.http import *
from utils.errors import *
from utils.config import*
from utils.process import*
import os
import json
import subprocess
import threading

@HttpWrapper
def test(request):
    return "Connection Success!" 

@HttpWrapper
def getFileList(request):
    return os.listdir(uploaded_file_path)

@HttpWrapper
def getFileContent(request):
    filename = request.GET.get("name")
    print(uploaded_file_path + filename)
    try:
        with open(uploaded_file_path + filename,encoding="utf-8") as f:
            return f.read()
    except:
        raise NoValue()

@HttpWrapper
def uploadFile(request): 
    filename = request.GET.get("filename")
    data     = request.GET.get("data")
    with open(uploaded_file_path + filename,"w",encoding="utf-8") as f:
         f.write(data)
    return filename

@HttpWrapper
def ner(request):
    try:
        filename = request.GET.get("filename")[:-4]
        with open(nlp_process_output + filename + "_NER_CLUE.txt",encoding="utf-8") as f:
            NER_CLUE = process_ner(json.loads(f.read()))
        with open(nlp_process_output + filename + "_NER_PEOPLEDAILY.txt",encoding="utf-8") as f:
            NER_PEOPLEDAILY = process_ner(json.loads(f.read()))
        results = dict([key,list(set(NER_CLUE[key] + NER_PEOPLEDAILY[key]))] for key in NER_CLUE)
        return results
    except:
        raise NoValue()
@HttpWrapper
def mindgraph(request):
    try:
        filename = request.GET.get("filename")[:-4]
        with open(nlp_process_output + filename + "_treedata.txt",encoding="utf-8") as f:
            tree = json.loads( f.read())
        return tree
    except:
        raise NoValue()

@HttpWrapper
def summary(request):
    try:
        filename = request.GET.get("filename")[:-4]
        with open(nlp_process_output + filename + "_summary.txt",encoding="utf-8") as f:
            summary = f.read()
        return summary
    except:
        raise NoValue()
@HttpWrapper
def analyze(request):
    filename = request.GET.get("filename")
    analyze_thread = threading.Thread(
        target=start_analyze,
        args= (filename,)
    )
    analyze_thread.start()
    return True