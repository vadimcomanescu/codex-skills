from playwright.sync_api import sync_playwright


def main() -> None:
    url = "http://localhost:3000"
    console_logs = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 900})

        def on_console(msg):
            console_logs.append(f"[{msg.type}] {msg.text}")

        page.on("console", on_console)
        page.goto(url)
        page.wait_for_load_state("networkidle")

        page.screenshot(path="/tmp/console_logging.png", full_page=True)
        browser.close()

    out = "/tmp/console.log"
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(console_logs))
    print(f"Wrote {len(console_logs)} console messages to {out}")


if __name__ == "__main__":
    main()

