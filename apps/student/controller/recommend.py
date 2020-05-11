from index.models import NepLearnStatus
from student.models import NepStudent
import math
import numpy as np

def init_data(stu_1, stu_2):
    ls_obj = NepLearnStatus.objects.filter(student_id__in=[stu_1, stu_2])

    user_data = {}
    for each_item in ls_obj:
        if each_item.student_id in user_data.keys():
            user_data[each_item.student_id][each_item.course_id] = each_item.learn_frequency
        else:
            user_data[each_item.student_id] = {each_item.course_id: each_item.learn_frequency}

    return user_data

def Euclid(stu1_id, stu2_id):
    user_data = init_data(stu1_id, stu2_id)

    distance = 0
    if len(user_data) == 1:
        return 1
    else:
        for each_cour in user_data[stu1_id].keys():
            if each_cour in user_data[stu2_id].keys():
                distance += math.pow(float(user_data[stu1_id][each_cour] - float(user_data[stu2_id][each_cour])), 2)
        return 1/(1+math.sqrt(distance))


def cos_sim(stu1_id, stu2_id):
    user_data = init_data(stu1_id, stu2_id)
    if len(user_data) == 1:
        return 0
    else:
        vector_1, vector_2 = [], []
        for each_item in user_data[stu1_id]:
            vector_1.append(user_data[stu1_id][each_item])
            vector_2.append(user_data[stu2_id][each_item] if each_item in user_data[stu2_id].keys() else 0)

        for each_item in user_data[stu2_id]:
            if each_item not in user_data[stu1_id]:
                vector_1.append(0)
                vector_2.append(user_data[stu2_id][each_item])

        vector_1, vector_2 = np.mat(vector_1), np.mat(vector_2)
        num = float(vector_1 * vector_2.T)
        denom = np.linalg.norm(vector_1) * np.linalg.norm(vector_2)
        cos = num / denom
        return cos

def get_cloest(stu_id):
    stu_obj = NepStudent.objects.all()
    self_ls = NepLearnStatus.objects.filter(student_id=stu_id)
    self_cour = []
    recommend_cour = []
    recommend_cour_id = []
    for each_self_ls in self_ls:
        self_cour.append(each_self_ls.course_id)

    stu_sim = []
    for each_stu in stu_obj:
        sim = Euclid(stu_id, each_stu.id)
        if sim > 0:
            stu_sim.append((each_stu.id, sim))

    stu_sim.sort(key= lambda item: item[1], reverse=False)

    for each_sim in stu_sim:
        ls_obj = NepLearnStatus.objects.filter(student_id=each_sim[0])
        for each_cour in ls_obj:
            each_cour_id = each_cour.course_id
            if each_cour_id not in self_cour :
                if each_cour_id not in recommend_cour_id:
                    recommend_cour.append((each_cour_id, each_sim[0], each_sim[1]))
                    recommend_cour_id.append(each_cour_id)
            if len(recommend_cour) >= 3:
                return recommend_cour
    return recommend_cour