import json
import os
import re
import shutil
from datetime import date

SCHEDULE_FILE = "drafts/schedule.json"
INDEX_FILE = "index.html"
SITEMAP_FILE = "sitemap.xml"


def load_schedule():
    with open(SCHEDULE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_schedule(schedule):
    with open(SCHEDULE_FILE, "w", encoding="utf-8") as f:
        json.dump(schedule, f, indent=4, ensure_ascii=False)


def build_active_card(entry):
    return (
        f'<a href="{entry["target"]}" class="card-glow rounded-2xl overflow-hidden group">\n'
        f'                    <div class="h-40 flex items-center justify-center" '
        f'style="background: linear-gradient(135deg, {entry["card_gradient"]});">\n'
        f'                        <span class="text-6xl">{entry["card_emoji"]}</span>\n'
        f"                    </div>\n"
        f'                    <div class="p-6">\n'
        f'                        <p class="{entry["card_color_class"]} text-xs font-semibold '
        f'uppercase tracking-wider mb-2">{entry["card_label"]}</p>\n'
        f'                        <h3 class="text-white font-bold text-base mb-2 '
        f'group-hover:{entry["card_color_class"]} transition-colors">'
        f'{entry["card_title"]}</h3>\n'
        f'                        <p class="text-gray-500 text-xs">{entry["card_desc"]}</p>\n'
        f"                    </div>\n"
        f"                </a>"
    )


def update_index(entry):
    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        html = f.read()

    start_marker = f"<!-- BLOG-CARD:{entry['card_id']}:START -->"
    end_marker = f"<!-- BLOG-CARD:{entry['card_id']}:END -->"

    pattern = re.compile(
        re.escape(start_marker) + r".*?" + re.escape(end_marker), re.DOTALL
    )

    active_card = build_active_card(entry)
    replacement = f"{start_marker}\n                {active_card}\n                {end_marker}"
    html = pattern.sub(replacement, html)

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(html)


def update_sitemap(entry):
    if not os.path.exists(SITEMAP_FILE):
        return

    with open(SITEMAP_FILE, "r", encoding="utf-8") as f:
        xml = f.read()

    if entry["target"] in xml:
        return

    new_entry = (
        f"  <url>\n"
        f"    <loc>https://bioparfaite.com/{entry['target']}</loc>\n"
        f"    <lastmod>{entry['date']}</lastmod>\n"
        f"    <changefreq>monthly</changefreq>\n"
        f"    <priority>0.7</priority>\n"
        f"  </url>\n"
    )

    xml = xml.replace("</urlset>", new_entry + "</urlset>")

    with open(SITEMAP_FILE, "w", encoding="utf-8") as f:
        f.write(xml)


def main():
    today = date.today().isoformat()
    schedule = load_schedule()
    published = False

    for entry in schedule:
        if entry["date"] <= today and not entry["published"]:
            print(f"Publishing: {entry['target']} (scheduled {entry['date']})")

            if os.path.exists(entry["draft"]):
                shutil.copy2(entry["draft"], entry["target"])
                print(f"  Copied {entry['draft']} -> {entry['target']}")
            else:
                print(f"  WARNING: Draft not found: {entry['draft']}")
                continue

            update_index(entry)
            print(f"  Updated blog card in {INDEX_FILE}")

            update_sitemap(entry)
            print(f"  Updated {SITEMAP_FILE}")

            entry["published"] = True
            published = True

    if published:
        save_schedule(schedule)
        print("\nDone — articles published.")
    else:
        print("Nothing to publish today.")


if __name__ == "__main__":
    main()
