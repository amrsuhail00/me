import requests

# رابط الـ m3u الأساسي
source_url = "http://lydexcloud.fyi:80/get.php?username=Amr0111&password=01115667224&type=m3u&output=ts"

# القناة الإضافية
extra_channel = '#EXTINF:-1 tvg-id="" tvg-name="qqqq" group-title="Extra",qqqq\nhttp://lydexcloud.fyi:80/Amr0111/01115667224/369917\n'

# تحميل الملف الأساسي
response = requests.get(source_url)
if response.status_code == 200:
    content = response.text
    # إضافة القناة الجديدة في الأول
    updated_content = extra_channel + content
    
    # حفظ الملف
    with open("familytv.m3u", "w", encoding="utf-8") as f:
        f.write(updated_content)
else:
    print("Error fetching original M3U:", response.status_code)
