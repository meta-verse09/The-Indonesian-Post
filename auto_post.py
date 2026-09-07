import os
import random
import google.generativeai as genai

# Inisialisasi Gemini API
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

TOPIC_IDEAS = [
    "hidden gem beaches in Lombok and Raja Ampat",
    "must-try authentic Indonesian street foods and their history",
    "breathtaking volcano hiking destinations in Java and Bali",
    "traditional Indonesian coffee culture and best specialty beans",
    "exotic islands in East Indonesia for diving and snorkeling",
    "rich flavors of Sumatran cuisine: Rendang and beyond",
    "cultural heritage sites and ancient temples in Yogyakarta",
    "traditional Indonesian desserts and refreshing tropical drinks"
]

def generate_article():
    selected_topic = random.choice(TOPIC_IDEAS)
    
    prompt = f"""
    You are an expert travel journalist and food writer for 'The Indonesian Post', a blog dedicated to showcasing Indonesia's natural beauty and culinary heritage to international readers.

    Topic angle: Focus on {selected_topic}.

    Requirements:
    1. Language: Engaging, natural, and descriptive English suitable for foreign tourists and travel enthusiasts.
    2. Length: Approximately 800 to 1,200 words (structured for easy reading).
    3. Content Structure:
       - Engaging introduction highlighting Indonesia's charm.
       - Detailed sections covering specific destinations or culinary dishes with location context.
       - Practical tips for travelers (best time to visit, flavor profiles, etiquette, etc.).
       - Inspiring conclusion.
    4. HTML Formatting:
       - Use clean HTML tags (<h3>, <p>, <ul>, <li>, <b>, <em>).
       - DO NOT include <html>, <head>, <body>, or ```html markdown tags.
       - Include 1-2 relevant Unsplash placeholder image tags with clear alt text and caption. Example: 
         <img src="[https://images.unsplash.com/photo-1537996194471-e657df975ab4?auto=format&fit=crop&w=800&q=80](https://images.unsplash.com/photo-1537996194471-e657df975ab4?auto=format&fit=crop&w=800&q=80)" alt="Indonesia Nature" style="width:100%; border-radius:8px; margin:15px 0;">
    5. Output Format:
       - FIRST LINE MUST BE THE ARTICLE TITLE (No HTML tags, no quotes, just plain text).
       - ALL SUBSEQUENT LINES MUST BE THE HTML CONTENT.
    """
    
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    
    lines = response.text.strip().split('\n')
    title = lines[0].replace('#', '').replace('*', '').strip()
    content = '\n'.join(lines[1:])
    return title, content

def main():
    print("Generating English travel/culinary article for 'The Indonesian Post'...")
    title, content = generate_article()
    print(f"Article Generated Successfully!\nTitle: {title}")
    
if __name__ == "__main__":
    main()
