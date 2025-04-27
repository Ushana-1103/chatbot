import requests
import time

def test_server():
    print("Testing server connection...")
    try:
        response = requests.get('http://localhost:8080')
        print(f"Server responded with status code: {response.status_code}")
        print("Server is running correctly!")
    except requests.exceptions.ConnectionError:
        print("Could not connect to server. Server might not be running.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    test_server()
    input("Press Enter to exit...") 