from playwright.sync_api import sync_playwright
import os


def main() -> None:
    html_file_path = os.path.abspath("path/to/your/file.html")
    url = f"file://{html_file_path}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 900})

        page.goto(url)
        page.screenshot(path="/tmp/static_page.png", full_page=True)

        # Adjust selectors to match your page.
        # page.click("text=Click Me")

        browser.close()

    print("Static HTML automation completed.")


if __name__ == "__main__":
    main()

