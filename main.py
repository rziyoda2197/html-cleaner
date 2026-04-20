import re
from bs4 import BeautifulSoup

class HTMLCleaner:
    def __init__(self, html):
        self.html = html

    def remove_tags(self):
        return re.sub('<.*?>', '', self.html)

    def remove_extra_spaces(self):
        return re.sub('\s+', ' ', self.html)

    def remove_comments(self):
        return re.sub('<!--.*?-->', '', self.html)

    def clean_html(self):
        self.html = self.remove_tags()
        self.html = self.remove_extra_spaces()
        self.html = self.remove_comments()
        return self.html

def main():
    html = """
    <html>
        <body>
            <!-- Bu bir comment -->
            <h1>Hello, World!</h1>
            <p>This is a paragraph with <b>bold</b> and <i>italic</i> text.</p>
            <p>This is another paragraph with extra spaces   between words.</p>
        </body>
    </html>
    """
    cleaner = HTMLCleaner(html)
    cleaned_html = cleaner.clean_html()
    print(cleaned_html)

if __name__ == "__main__":
    main()
```

Kodda quyidagilar qilindi:

1. `HTMLCleaner` klassi yaratildi, u HTML ni tozalash uchun mo'ljallangan.
2. `remove_tags` metodi HTML dan barcha taglarni olib tashlaydi.
3. `remove_extra_spaces` metodi HTML da extra bo'sh joylarni olib tashlaydi.
4. `remove_comments` metodi HTML da barcha commentlarni olib tashlaydi.
5. `clean_html` metodi HTML ni tozalash uchun barcha metodlarni birlashtadi.
6. `main` funktsiyasi HTML ni tozalash uchun `HTMLCleaner` klassidan foydalanadi va natijani konsolga chiqaradi.
