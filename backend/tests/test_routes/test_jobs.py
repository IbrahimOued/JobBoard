import json


def test_create_job(client):
    data = {
        "title": "SDE 1 Yahoo",
        "company": "testhoo",
        "company_url": "https://www.kreezus.com",
        "location": "France, Paris",
        "description": "Testing",
        "date_posted": "2022-07-20"
    }
    response = client.post("/jobs/create-job", json.dumps(data))
    assert response.status_code == 200
