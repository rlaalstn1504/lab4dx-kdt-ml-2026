import csv
import random
import time
from playwright.sync_api import Playwright, sync_playwright


SECTION_URL = "https://news.naver.com/section/101"
CSV_PATH = "naver_economy_news.csv"
MAX_ARTICLES = 100


def clean_text(text: str) -> str:
    return " ".join(text.split()) if text else ""


def safe_inner_text(page, selector: str, timeout: int = 3000) -> str:
    try:
        locator = page.locator(selector).first

        if locator.count() == 0:
            return ""

        return clean_text(locator.inner_text(timeout=timeout))

    except:
        return ""


def human_delay(min_sec=0.3, max_sec=1.2):
    time.sleep(random.uniform(min_sec, max_sec))


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(
        headless=False,
        slow_mo=100
    )

    context = browser.new_context()

    page = context.new_page()

    print("경제 뉴스 페이지 접속 중...")

    page.goto(SECTION_URL, wait_until="networkidle")

    human_delay(1.0, 2.0)

    news_area = page.locator("#newsct")

    print("기사 링크 수집 중...")

    links = news_area.locator("a").evaluate_all(
        """
        elements => [...new Set(
            elements
                .map(a => a.href)
                .filter(href => /\\/article\\/\\d+\\/\\d+/.test(href))
                .filter(href => !href.includes('/comment/'))
        )]
        """
    )

    print(f"수집 후보 링크 수: {len(links)}")

    saved_count = 0

    with open(CSV_PATH, "w", newline="", encoding="utf-8-sig") as f:

        writer = csv.DictWriter(
            f,
            fieldnames=[
                "title",
                "press",
                "journalist",
                "time",
                "body",
                "url"
            ]
        )

        writer.writeheader()

        for idx, link in enumerate(links, start=1):

            if saved_count >= MAX_ARTICLES:
                print(f"\n최근 뉴스 {MAX_ARTICLES}개 수집 완료")
                break

            article_page = context.new_page()

            try:
                print(f"\n[{idx}] 기사 접속 중...")
                print(link)

                article_page.goto(link, wait_until="networkidle")

                # 사람처럼 랜덤 대기
                human_delay(0.5, 1.5)

                # 제목
                title = safe_inner_text(
                    article_page,
                    "#title_area span"
                )

                # 본문
                body = safe_inner_text(
                    article_page,
                    "#dic_area"
                )

                # 시간
                time_text = safe_inner_text(
                    article_page,
                    ".media_end_head_info_datestamp_time"
                )

                if not title or not body:
                    print(f"[{idx}] 제목/본문 없음 → 제외")
                    continue

                # 언론사
                press = safe_inner_text(
                    article_page,
                    ".media_journalistcard_summary_press"
                )

                # 예비 selector
                if not press:
                    press = safe_inner_text(
                        article_page,
                        ".media_end_head_top_logo_text"
                    )

                # 기자명
                journalist = safe_inner_text(
                    article_page,
                    ".media_end_head_journalist_name"
                )

                # 예비 selector
                if not journalist:
                    journalist = safe_inner_text(
                        article_page,
                        ".media_journalistcard_summary_name_text"
                    )

                # CSV 즉시 저장
                writer.writerow({
                    "title": title,
                    "press": press,
                    "journalist": journalist,
                    "time": time_text,
                    "body": body,
                    "url": link
                })

                # 즉시 디스크 반영
                f.flush()

                saved_count += 1

                print(f"[{saved_count}/{MAX_ARTICLES}] 저장 완료")
                print(f"언론사: {press}")
                print(f"기자: {journalist}")
                print(f"제목: {title}")

            except Exception as e:
                print(f"[{idx}] 수집 실패")
                print(link)
                print(e)

            finally:
                article_page.close()

                # 다음 기사 전 랜덤 대기
                human_delay(0.7, 2.0)

    context.close()
    browser.close()

    print("\n크롤링 종료")


with sync_playwright() as playwright:
    run(playwright)