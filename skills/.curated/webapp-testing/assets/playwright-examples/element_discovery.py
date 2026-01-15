from playwright.sync_api import sync_playwright


def main() -> None:
    url = "http://localhost:3000"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 900})

        page.goto(url)
        page.wait_for_load_state("networkidle")

        buttons = page.locator("button").all()
        print(f"Found {len(buttons)} buttons:")
        for i, button in enumerate(buttons[:25]):
            text = button.inner_text().strip() if button.is_visible() else "[hidden]"
            print(f"  [{i}] {text}")

        page.screenshot(path="/tmp/page_discovery.png", full_page=True)
        print("Saved screenshot: /tmp/page_discovery.png")

        browser.close()


if __name__ == "__main__":
    main()

