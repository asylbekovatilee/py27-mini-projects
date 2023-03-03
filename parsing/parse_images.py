import requests, json

image_url = https://www.google.com/imgres?imgurl=https://www.seiu1000.org/sites/main/files/main-images/camera_lense_0.jpeg&imgrefurl=https://www.seiu1000.org/post/image-dimensions&h=3176&w=4764&tbnid=449X1Cy510tOqM&q=image&tbnh=100&tbnw=150&usg=AI4_-kRlu_jDY0MQkXgAtgzQIJ1Ee-CoZw&vet=1&docid=6QLAx3t1h27U3M&client=ubuntu-chr&sa=X&ved=2ahUKEwi7k-bvjL_9AhU_CRAIHRzaD58Q9QF6BAgAEAg

response = requests.get(image_url)

with open("test.jpg", "wb") as file:
    file.write(response.content)