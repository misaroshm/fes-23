from Software import Developer, QA, MobileApp, WebApp, DatasetAPI, Containerization, TeamLead, BusinessAnalyst

developer1 = Developer("Bob")
qa = QA("Emily")
team_lead = TeamLead("Roman")
bus_a = BusinessAnalyst("Nira")

developer1.attach(qa)
developer1.attach(team_lead)
developer1.attach(bus_a)

mobile_app = MobileApp("MyApp", "Android")
web_app = WebApp("WebApp", "PythonBackend", "JSFrontend")
database_api = DatasetAPI("DatabaseAPI")
containerization = Containerization("Containerization")

result = developer1.develop(mobile_app)
result2 = developer1.develop(web_app)
result3 = developer1.develop(database_api)
result4 = developer1.develop(containerization)

if result and result2 and result3 and result4:
    print(f"{developer1.name} received QA result: Some numbers are odd. Fixing issues.")
    print(f"{developer1.name} received fixed dataset: {result}.")




