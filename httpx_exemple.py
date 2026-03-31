import httpx

# response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
#
# print(response.status_code)
# print(response.json())
#
# data = {
#     "title": "Новая задача",
#     "completed": False,
#     "userId": 1
# }
# response = httpx.post("https://jsonplaceholder.typicode.com/todos/")
#
# print(response.status_code)
# print(response.json())
#
# headers = {"Authorization": "Bearer my_secret_token"}
# response = httpx.get("https://httpbin.org/get", headers=headers)
#
# print(response.status_code)
# # print(response.request.headers)
# # print(response.headers)
# print(response.json())
#
# params = {"userId": 1}
# response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
#
# print(response.request.url)
# print(response.status_code)
# print(response.json())

# files = {"file": ("example.txt", open("example.txt", "rb"))}
# response = httpx.post("https://httpbin.org/post", files=files)
#
# print(response.status_code)
# print(response.json())
#
# with httpx.Client(
#         headers={"Authorization": "Bearer my_secret_token"},
#         base_url="https://jsonplaceholder.typicode.com/") as client:
#     response1 = client.get("todos/1")
#     response2 = client.get("todos/2")
#
# print(response1.json())
# print(response2.json())

try:
    response = httpx.get("https://httpbin.org/delay/5")
except Exception as e:
    print(f"Ошибка таймаута: {e}")
