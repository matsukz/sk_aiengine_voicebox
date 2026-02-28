from openai import OpenAI

# アカウントトークンを発行しておく
# https://manual.sakura.ad.jp/cloud/ai-engine/02-howto.html
account_token = ""

# さくらのAI Engineの「利用可能な音声モデル」からモデルIDとボイスIDを確認して入力
# Ex.「春日部つむぎ」の「ノーマル」を使用する場合
model_id = "kasukabetsumugi"
voice_id = "normal"

# 読んでもらう文章を指定する
text = "こんにちは！"

client = OpenAI(
    api_key=account_token,  
    base_url = "https://api.ai.sakura.ad.jp/v1/"
)

response = client.audio.speech.create(
    model = model_id,
    voice = voice_id,
    input = text
)

# output.wavとして保存
response.write_to_file("output.wav")
