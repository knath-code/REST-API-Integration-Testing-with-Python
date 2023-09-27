import pytest
import requests 
ENDPOINT = "https://todo.pixegami.io/"

@pytest.mark.test
def test_call_endpoint():
    res = requests.get(ENDPOINT)
    assert res.status_code == 200 

    # commond as    pytest -v -m "not webtest"
    
    



def test_create_task():
    payload = new_task_payload()
    create_task_res = Create_task(payload)    
    assert create_task_res.status_code == 200

    data = create_task_res.json()
    # print(data)  
    # Commond as python -m pytest -v -s


    task_id = data["task"]["task_id"]    
    get_task_res = get_task(task_id) 
    assert get_task_res.status_code == 200
    get_task_data = get_task_res.json()
    assert get_task_data["content"] == payload["payload"]
    assert get_task_data["user_id"] == payload["payload"]


def test_update_task():

    # create task 
    payload = new_task_payload()
    create_task_res = create_task(payload) 
    assert create_task_res.status_code == 200
    task_id = create_task_res.json()["task"]["task_id"]  

    # update task 
    new_paylaod = {
        "user_id": payload["user_id"], 
        "task_id": task_id,
        "content" : "my update content",
        "is_done" : True,
    }
    update_task_res = update_task(new_paylaod)
    assert update_task_res.status_code == 200
 
    # get and validate the changes 
    get_task_res = get_task(task_id)
    assert get_task_res.status_code == 200 
    get_task_data = get_task_res.json()
    assert get_task_data ["content"] == new_paylaod["content"]
    assert get_task_data ["is_done"] == new_paylaod["is_done"]




def create_task (payload):
    return requests.put(ENDPOINT + "/create_task)", json=payload)  

def update_task (payload):
    return requests.put(ENDPOINT + "/update_task)", json=payload)  
 
 
def get_task(task_id):
    return requests.get( ENDPOINT + f"/get_task)/ {task_id}")

def new_task_payload():
    return {
        "content": "my test result",
        "user_id": "test_user",        
         "is_done": False,
    }
    





