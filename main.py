import os

from flask import Flask

app = Flask(__name__)

PAGE = """<!doctype html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Quản lý Homestay Trung tâm Đà Nẵng</title>
  <style>
    :root { color-scheme: light; font-family: Inter, system-ui, Arial, sans-serif; }
    * { box-sizing: border-box; }
    body { margin: 0; color: #172033; background: #f4f7fb; }
    header { padding: 22px max(24px, calc((100vw - 1040px) / 2)); color: white; background: #123b68; }
    .brand { font-weight: 700; letter-spacing: .02em; }
    main { max-width: 1040px; margin: 56px auto; padding: 0 24px; }
    .hero { padding: 48px; border-radius: 20px; color: white; background: linear-gradient(125deg, #155e75, #2563a6); box-shadow: 0 18px 48px #123b6826; }
    .tag { display: inline-block; padding: 7px 12px; border: 1px solid #ffffff66; border-radius: 99px; font-size: 14px; }
    h1 { max-width: 760px; margin: 20px 0 12px; font-size: clamp(32px, 5vw, 52px); line-height: 1.1; }
    .intro { max-width: 680px; color: #e2efff; font-size: 18px; line-height: 1.7; }
    .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; margin-top: 24px; }
    .card { padding: 22px; border: 1px solid #e4eaf2; border-radius: 14px; background: white; }
    .card h2 { margin: 0 0 8px; font-size: 18px; }
    .card p { margin: 0; color: #596579; line-height: 1.6; }
    footer { margin-top: 30px; color: #738096; font-size: 14px; text-align: center; }
    @media (max-width: 600px) { main { margin: 28px auto; } .hero { padding: 30px 24px; } }
  </style>
</head>
<body>
  <header><div class="brand">ĐÀ NẴNG · HOMESTAY</div></header>
  <main>
    <section class="hero">
      <span class="tag">Bản giới thiệu đề tài</span>
      <h1>Quản lý Homestay khu vực trung tâm Đà Nẵng</h1>
      <p class="intro">Website hỗ trợ quản lý thông tin homestay, phòng nghỉ và đặt phòng trong khu vực trung tâm thành phố Đà Nẵng.</p>
    </section>
    <section class="grid" aria-label="Các chức năng dự kiến">
      <article class="card"><h2>🏠 Quản lý homestay</h2><p>Lưu thông tin cơ sở lưu trú, địa chỉ và tiện nghi.</p></article>
      <article class="card"><h2>🛏️ Quản lý phòng</h2><p>Theo dõi loại phòng, giá và tình trạng phòng.</p></article>
      <article class="card"><h2>📅 Quản lý đặt phòng</h2><p>Ghi nhận lịch đặt và thông tin khách lưu trú.</p></article>
    </section>
    <footer>Đồ án đang trong giai đoạn khởi tạo · Python · MySQL</footer>
  </main>
</body>
</html>"""


@app.get("/")
def home():
    return PAGE


@app.get("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
