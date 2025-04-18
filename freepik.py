import os
from dotenv import load_dotenv
import os
import requests
import time
import openai
from PIL import Image
from io import BytesIO
from IPython.display import display

client = openai.OpenAI(api_key='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')
API_KEY = "FPSXe7216173e5244292808be98119e48480"
def check_status(task_id, max_retries=20, retry_delay=25):
    status_url = f"https://api.freepik.com/v1/ai/mystic/{task_id}"  
    headers = {"x-freepik-api-key": API_KEY}
    
    start_time = time.time()
    
    for attempt in range(max_retries):
        elapsed_time = int(time.time() - start_time)
        response = requests.get(status_url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            status = data.get("data", {}).get("status")

            if status == "COMPLETED":
                image_urls = data.get("data", {}).get("generated", [])
                if image_urls:
                    print(f"✅ Ảnh đã sẵn sàng sau {elapsed_time} giây! 🚀")
                    return image_urls[0]

def sanitize_filename(filename):
    return "".join(c if c.isalnum() or c in " _-" else "_" for c in filename)

def download_image(image_url, prompt):
    filename = sanitize_filename(prompt)[:50] + ".jpg"  # Giới hạn tên file 50 ký tự
    response = requests.get(image_url)

    folder = "img"
    file_path = os.path.join(folder, filename)
    if response.status_code == 200:
        with open(file_path, "wb") as file:
            file.write(response.content)
        print(f"📥 Ảnh đã được tải về: {filename}")

        # Hiển thị ảnh ngay trong Jupyter Notebook
        img = Image.open(BytesIO(response.content))
        display(img)
    else:
        print(f"❌ Lỗi khi tải ảnh: {response.status_code}")
    return filename

import prompt

def create_image_prompt(Content):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": (prompt.Image_Prompt)},
            {"role": "user", "content": ("Make a prompt for the following: " + Content)}
        ],
        temperature=0.5,
    )
    answer = response.choices[0].message.content
    print(answer)
    return answer

def get_ratio(w, h):
    if (w == h): return "square_1_1"
    elif (w > h): return "widescreen_16_9"
    elif (w < h): return "social_story_9_16"

def process(context, w = 1, h = 1):
    url = "https://api.freepik.com/v1/ai/mystic"
    image_prompt = create_image_prompt(context)
    ratio = get_ratio(w, h)
    payload = {
        "structure_strength": 50,
        "adherence": 50,
        "hdr": 85,
        "resolution": "1k",
        "aspect_ratio": ratio,
        "model": "zen",
        "creative_detailing": 25,
        "engine": "magnific_illusio",
        "fixed_generation": False,
        "filter_nsfw": True,
        "prompt": image_prompt
        }
    headers = {
        "x-freepik-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    if response.status_code == 200:
            data = response.json()
            task_id = data.get("data", {}).get("task_id")
            if task_id:
                print(f"Task ID: {task_id}")    
            else:
                print("❌ Không tìm thấy task_id trong phản hồi.")
    else:
        print(f"❌ Lỗi khi gửi yêu cầu: {response.status_code}")
    image_url = check_status(task_id)
    filename = download_image(image_url, payload["prompt"])
    return filename

context = "Kỹ thuật SCAMPER là một phương pháp tư duy sáng tạo giúp tạo ra những ý tưởng mới và độc đáo bằng cách cải tiến hoặc biến đổi những ý tưởng đã có.SCAMPER được phát triển bởi Alex Faickney Osborn, người đồng sáng lập của tập đoàn quảng cáo BBDO. Phương pháp này giúp người dùng suy nghĩ khác biệt và phát triển tư duy sáng tạo bằng cách đặt ra các câu hỏi về ý tưởng hiện có, từ đó mở rộng tầm nhìn và tìm ra các giải pháp mới."
process(context, 1, 1)