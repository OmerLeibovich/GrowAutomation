import json
from PostmanGrow import app

def test_GetPaymentPageLink():
    client = app.test_client()
    response = client.post("/GetPaymentPageLink")
    assert response.status_code == 200
    data = response.get_json()
    assert "url" in data
    assert data["url"].startswith("https://")

def test_WithoutRequiredField():
    client = app.test_client()
    response = client.post("/WithoutRequiredField")
    data = response.get_json()
    assert "חסר" in json.dumps(data, ensure_ascii=False) or "שדה" in json.dumps(data, ensure_ascii=False)

def test_WrongValue():
    client = app.test_client()
    response = client.post("/WrongValue")
    data = response.get_json()
    assert "לא תקין" in json.dumps(data, ensure_ascii=False) or "שגיאה" in json.dumps(data, ensure_ascii=False) or "לא ניתן" in json.dumps(data, ensure_ascii=False)
