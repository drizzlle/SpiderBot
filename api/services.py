import requests

# n8n webhook URLs
N8N_BASE_URL = "https://drizzle.app.n8n.cloud/webhook"
SCRAPE_URL = f"{N8N_BASE_URL}/scrape"
CHAT_URL = f"{N8N_BASE_URL}/chat"

def scrape_website(url):
    response = requests.post(SCRAPE_URL, json={"url": url})
    if response.text:
        return response.json()
    return {"status": "success", "message": "Scraping started"}

def chat_with_ai(message, user_id):
    session_id = f"user_{user_id}"
    response = requests.post(
        CHAT_URL,
        json={
            "message": message,
            "sessionId": session_id
        }
    )
    result = response.json()
    
    if isinstance(result, list) and len(result) > 0:
        return result[0]
    return result
