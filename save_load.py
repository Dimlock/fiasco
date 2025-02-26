import json


def save(file_dict):
    # test_json = {
    #     "template": {
    #         "name": "тест",
    #         "description": "тестовое описание",
    #         "lists": {
    #             "relations": {
    #                 "categories": [
    #                     {
    #                         "name": "имя категории",
    #                         "elements": []
    #                     },
    #                     {
    #                         "name": "имя второй категории",
    #                         "elements": []
    #                     }
    #                 ]
    #             },
    #             "other_lists": [
    #                 {
    #                     "name": "название другого списка",
    #                     "categories": [
    #                         {
    #                             "name": "имя другой категории",
    #                             "elements": []
    #                         },
    #                         {
    #                             "name": "имя второй другой категории",
    #                             "elements": []
    #                         }
    #                     ]
    #                 },
    #                 {
    #                     "name": "2nd other list",
    #                     "categories": [
    #                         {
    #                             "name": "2nd list 1st cat",
    #                             "elements": []
    #                         },
    #                         {
    #                             "name": "2nd list 2nd cat",
    #                             "elements": []
    #                         }
    #                     ]
    #                 }
    #             ]
    #         }
    #     }
    # }

    with open(f"templates/{file_dict["name"]}.json", "w", encoding="UTF-8") as f:
        json.dump(file_dict, f, indent=4, ensure_ascii=False)


def load(file_path):
    with open(file_path, "r", encoding="UTF-8") as f:
        return json.load(f)
