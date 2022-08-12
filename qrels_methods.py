import os
import shutil

def get_line(topic_no, line):
        if topic_no <= 9: 
            line = line[4:-2]
        else:
            line = line[5:-2]
        return line

def qrels2lines(topic_no):
    qrels = []
    
    with open('./cds-files/qrels2021.txt', 'r') as r:
        for line in r.readlines():
            #print(f"{line[0]} and {line[1]}")
            # 1자리 토픽
            if topic_no <= 9:
                if (line[0] == str(topic_no)) and (line[1] == ' '):
                    qrels.append(line.replace('\n', ''))
            # 2자리 토픽
            else:
                if (line[0] == str(topic_no//10)) and (line[1] == str(topic_no%10)):
                    qrels.append(line.replace('\n', ''))
    print(f"Topic {topic_no}: {len(qrels)}")
    
    return qrels

def save_qrel2files(topic_no, qrels, origin, copy, list_of_id, list_of_path):
    qrels_0, qrels_1, qrels_2 = [], [], []

    for line in qrels:
        if line[-1] == '0':
            qrels_0.append(line)
        elif line[-1] == '1':
            qrels_1.append(line)
        elif line[-1] == '2':
            qrels_2.append(line)

    print(f"Counts of Topic {topic_no} -> 0: {len(qrels_0)}, 1: {len(qrels_1)}, 2: {len(qrels_2)}")

    # qrels_0_path: real paths
    qrels_0_path = []
    qrels_1_path = []
    qrels_2_path = []

    for line in qrels_0:
        pos = list_of_id.index(get_line(topic_no, line))
        qrels_0_path.append(list_of_path[pos])

    for line in qrels_1:
        pos = list_of_id.index(get_line(topic_no, line))
        qrels_1_path.append(list_of_path[pos])

    for line in qrels_2:
        pos = list_of_id.index(get_line(topic_no, line))
        qrels_2_path.append(list_of_path[pos])

    for path in qrels_0_path:
        path = origin + path
        cp = copy + "/0"

        if not os.path.exists(cp):
            os.makedirs(cp)
        shutil.copy(path, cp)

    for path in qrels_1_path:
        path = origin + path
        cp = copy + "/1"

        if not os.path.exists(cp):
            os.makedirs(cp)
        shutil.copy(path, cp)

    for path in qrels_2_path:
        path = origin + path
        cp = copy + "/2"

        if not os.path.exists(cp):
            os.makedirs(cp)
        shutil.copy(path, cp)
    
    print(f"Topic {topic_no} is done.")