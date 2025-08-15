import requests

# رابط ملف m3u الأصلي
original_url = "http://lydexcloud.fyi:80/get.php?username=Amr0111&password=01115667224&type=m3u&output=ts"

# القناة الجديدة qqqq
new_channel_name = "#EXTINF:-1 group-title=\"Sports\" tvg-logo=\"\",qqqq"
new_channel_link = "http://lydexcloud.fyi:80/Amr0111/01115667224/369917"

# تحميل الملف الأصلي
r = requests.get(original_url)
r.raise_for_status()
original_content = r.text.strip()

# دمج القناة في الأول
new_content = f"{new_channel_name}\n{new_channel_link}\n{original_content}"

# حفظ الملف
with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(new_content)

print("تم إنشاء playlist.m3u بنجاح.")
