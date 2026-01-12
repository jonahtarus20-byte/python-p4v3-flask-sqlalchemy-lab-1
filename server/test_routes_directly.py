#!/usr/bin/env python3

# Test routes directly using Flask test client
import json
from app import app

def test_routes():
    print("Testing routes directly...")

    with app.test_client() as client:
        # Test 1: earthquake found route
        response = client.get('/earthquakes/1')
        assert response.status_code == 200
        print("✓ Test 1 passed: earthquake found route")

        # Test 2: earthquake not found route
        response = client.get('/earthquakes/999')
        assert response.status_code == 404
        print("✓ Test 2 passed: earthquake not found route")

        # Test 3: earthquakes found response
        response = client.get('/earthquakes/2')
        assert response.status_code == 200
        response_body = response.data.decode()
        response_json = json.loads(response_body)
        assert response_json["id"] == 2
        assert response_json["magnitude"] == 9.2
        assert response_json["location"] == "Alaska"
        assert response_json["year"] == 1964
        print("✓ Test 3 passed: earthquake found response")

        # Test 4: earthquakes not found response
        response = client.get('/earthquakes/9999')
        assert response.status_code == 404
        response_body = response.data.decode()
        response_json = json.loads(response_body)
        assert response_json["message"] == "Earthquake 9999 not found."
        print("✓ Test 4 passed: earthquake not found response")

        # Test 5: earthquake magnitude route
        response = client.get('/earthquakes/magnitude/8.0')
        assert response.status_code == 200
        print("✓ Test 5 passed: earthquake magnitude route")

        # Test 6: earthquakes magnitude match response
        response = client.get('/earthquakes/magnitude/9.0')
        assert response.status_code == 200
        response_body = response.data.decode()
        response_json = json.loads(response_body)
        assert response_json["count"] == 2
        assert len(response_json["quakes"]) == 2
        # Check first quake
        quake1 = response_json["quakes"][0]
        assert quake1["id"] == 1
        assert quake1["magnitude"] == 9.5
        assert quake1["location"] == "Chile"
        assert quake1["year"] == 1960
        # Check second quake
        quake2 = response_json["quakes"][1]
        assert quake2["id"] == 2
        assert quake2["magnitude"] == 9.2
        assert quake2["location"] == "Alaska"
        assert quake2["year"] == 1964
        print("✓ Test 6 passed: earthquake magnitude match response")

        # Test 7: earthquakes magnitude no match response
        response = client.get('/earthquakes/magnitude/10.0')
        assert response.status_code == 200
        response_body = response.data.decode()
        response_json = json.loads(response_body)
        assert response_json["count"] == 0
        assert len(response_json["quakes"]) == 0
        print("✓ Test 7 passed: earthquake magnitude no match response")

    print("\nAll route tests passed!")

if __name__ == "__main__":
    test_routes()
