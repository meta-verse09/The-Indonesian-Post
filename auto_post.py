import os
import json
import google.generativeai as genai
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# Konfigurasi Gemini API
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def generate_article():
    prompt = (
        "Tuliskan 1 artikel blog yang sangat menarik, informatif, dan ramah SEO "
        "dalam bahasa Indonesia. Topik bebas seputar berita umum, teknologi, atau gaya hidup. "
        "Panjang artikel sekitar 800-1000 kata (maksimal 5000 karakter). "
        "Gunakan format HTML lengkap dengan tag <h3>, <p>, <ul>, <li>, dan <b>. "
        "Format output: Baris pertama adalah JUDUL ARTIKEL (tanpa tag HTML), "
        "dan baris berikutnya adalah isi artikel HTML."
    )
    
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    
    lines = response.text.strip().split('\n')
    title = lines[0].replace('#', '').strip()
    content = '\n'.join(lines[1:])
    return title, content

def main():
    print("Mulai membuat artikel dengan Gemini AI...")
    title, content = generate_article()
    print(f"Artikel berhasil dibuat: {title}")

    # Mengambil kredensial Blogger dari Secrets
    client_secret_data = json.loads(os.environ["BLOGGER_CLIENT_SECRET"])
    blog_id = os.environ["BLOG_ID"]

    print("Siap mengirimkan ke Blogger API...")
    # Proses kirim draf/post ke Blogger v3
    
if __name__ == "__main__":
    main()
