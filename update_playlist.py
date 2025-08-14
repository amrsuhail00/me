import requests

# رابط الـ m3u الأصلي
SOURCE_URL = "http://lydexcloud.fyi:80/get.php?username=Amr0111&password=01115667224&type=m3u&output=ts"

# بيانات القناة الجديدة
NEW_CHANNEL_NAME = "Bein sport g"
NEW_CHANNEL_URL = "https://filmszone.shop:443/play/Q0XBH20Ej_eF9bqIOgR19dpHnCl96zqSwy8Shq-NDus/ts"

# تحميل القائمة الأصلية
print("Downloading original playlist...")
response = requests.get(SOURCE_URL)
response.raise_for_status()
original_playlist = response.text

# تكوين القناة الجديدة
new_channel = f'#EXTINF:-1 tvg-id="" tvg-name="{NEW_CHANNEL_NAME}" tvg-logo="" group-title="Custom",{NEW_CHANNEL_NAME}\n{NEW_CHANNEL_URL}\n'

# دمج القناة الجديدة مع القائمة الأصلية
final_playlist = "#EXTM3U\n" + new_channel + original_playlist.split("\n", 1)[1]

# حفظ الملف الناتج
with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(final_playlist)

print("Playlist updated successfully!")
