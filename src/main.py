import sys
from scraper import get_article_content


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <news_url>")
        sys.exit(1)

    url = sys.argv[1]
    try:
        title, content = get_article_content(url)
        print(f"Title: {title}\n")
        print(f"Content: {content}\n")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

