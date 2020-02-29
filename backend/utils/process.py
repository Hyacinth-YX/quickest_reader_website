from utils import config
import subprocess
import os
def process_ner(NER_RETURN):

    results = {
        "name":[],
        "address":[],
        "book":[],
        "company":[],
        "game":[],
        "government":[],
        "movie":[],
        "organization":[],
        "position":[],
        "scene":[],
        "time":[]
        }
    origin_tokens,output_labels,_IOB_parsed = NER_RETURN
    assert len(origin_tokens) == len(_IOB_parsed)
    for idx in range(len(_IOB_parsed)):
        tokens = origin_tokens[idx]
        labels = _IOB_parsed[idx]
        for _label in labels:
            label_text = list(_label.keys())[0]
            label_span = _label[label_text]
            label_token = "".join(tokens[label_span[0]:label_span[1]+1])
            if label_text == "LOC":
                label_text = "position"
            if label_text == "ORG":
                label_text = "organization"
            if label_text == "T":
                label_text =  "time"
            if label_text == "PER":
                label_text = "name"
            if len(label_token) <= 1:
                continue
            results[label_text].append(label_token)

    return results

def start_analyze(filename):

    output_files = os.listdir(config.nlp_process_output)
    if filename[:-4] + "_NER_CLUE.txt" not in output_files:
        subprocess.call(
            "python manage.py -m NER --f %s --env bert" %(config.uploaded_file_path + filename),
            shell= True,
            cwd = config.nlp_project_path
        )
    
    #然后制作思维导图
    if filename[:-4] + "_treedata.txt" not in output_files:
        subprocess.call(
            "python manage.py -G %s --env bert" %(config.uploaded_file_path + filename),
            shell= True,
            cwd = config.nlp_project_path
        )

    #最后制作思维导图
    if filename[:-4] + "_summary.txt" not in output_files:
        subprocess.call(
            "python manage.py -m TEXT_SUMMARY --f %s --env skydownacai" %(config.uploaded_file_path + filename),
            shell= True,
            cwd = config.nlp_project_path
        )