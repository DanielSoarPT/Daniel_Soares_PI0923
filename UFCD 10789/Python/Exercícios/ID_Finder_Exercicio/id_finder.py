import requests

user = []

for id in range(9001, 10000):
    f = open("ids.txt", "a")
    url = f'https://trainingserver.atec.pt/TrainingServer/Mulberry/JSON/Controls/Calendar/getCalendarDataSource.ashx?command=_SelectAllSchedulesDataSetGivenByUserId&oId={id}&idField=DataValueField&titleField=DataTextField&startDateField=DataStartField&endDateField=DataEndField&backgroundColorField=&textColorField=textcolor&eventColorField=color&description=description&picField=pic&urlField=url&start=1747004400&end=1747609200&_=1747129792488'

    response = requests.get(url)

    print(f"\n+ A procurar o ID {id} +")

    if 'Rogélio' in response.text and 'Sessão como Formador' in response.text:
        user.append(id)
        print("[!] - O formador Rogélio foi encontrado no horário do ID: ", id)
        f.write(str(id)+ '\n')
    else:
        print("[!] - O formador Rogélio não foi encontrado no horário do ID: ", id)
        id += 1

print("- IDs encontrados! -")
for id in user:
    print(f"{id}\n")