from membertypes import TeamLead, QA, SoftwareArchitect, BusinessAnalyst, Developer
from software import Software, MobileApp, WebApp, DatabaseAPI, Containerization, Deployment
from software import SoftwarePipeline, Observer
from typing import List, Tuple

# 1. create team

# common devs
dev1, dev2 = Developer("Sam", 3, ["Python"]), Developer("Sean", 4, ["JS"])
# architect
arch = SoftwareArchitect("Lol", 6, ["Python", "JS"])
# team lead
leader = TeamLead("Euclid", 5, ["Python", "JavaScript"], [dev1, dev2])
# qa engineer
qa = QA("Thomas", 5)
# business analyst
ba = BusinessAnalyst("Jack", 4)


# 2. create software pipeline based on software list

# soft list
software_list: list[Software] = [MobileApp("Android Application"), WebApp("Python Backend"),
                                 DatabaseAPI("DB API"), Containerization("Containerization"),
                                 Deployment("Deployment")]

# create pipeline and set it with observer
software_pipeline = SoftwarePipeline()
software_pipeline.attach(Observer("QA"))

# adding
for i in range(len(software_list)):
    software_pipeline.add_stage(software_list[i])

dev1.perform_duty()
dev2.perform_duty()
arch.perform_duty()
leader.perform_duty()
qa.perform_duty()
ba.perform_duty()

software_pipeline.develop()
software_pipeline.test()
software_pipeline.deploy()
