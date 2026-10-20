# SYSTEM EXECUTION DIRECTIVE FOR ANTIGRAVITY / CURSOR

Bu repo daha önce Cursor tarafından yarım bırakıldı (scaffolded / partial MVP). Görevin bu projeyi orijinal spesifikasyonlarına sadık kalarak **ürün kalitesine** getirmektir.

## KESİN KURALLAR

1. İlk iş olarak tüm dizini (`backend/`, `frontend/`, `tests/`, `scripts/`, `compose.yaml`, `docs/`) tara. İçinde `TODO`, `FIXME`, `pass`, `NotImplementedError`, sahte (hardcoded/mock) API dönüşleri veya bağlantısız React bileşenleri olan her yeri tespit et.
2. Asla sahte veri dönen endpoint bırakma. Tüm uç noktalar gerçek DB (SQLAlchemy 2 + Alembic) ve gerçek algoritmik servis katmanına bağlı olmalıdır.
3. Kod yazmayı bitirdiğinde mutlaka `ruff`, `pytest`, frontend `tsc`/`vitest`/`build` ve mümkünse Playwright çalıştır. Hata alırsan testi silme; kaynak kodu düzelt.
4. `README.md` ve `docs/GITHUB_METADATA.md` dosyalarını uydurma metrikler olmadan, gerçek test sonuçlarıyla güncelle.
5. **Docker bu makinede YOK.** `compose.yaml` + CI workflow yaz/doğrula; yerelde native `uv` + `pnpm` + SQLite (veya mevcut local path) kullan. Compose/PostgreSQL yolu **CI** için; yerel native yol SQLite olabilir. `docs/REVIEW_AMENDMENTS.md` bağlayıcıdır ve PRODUCT_SPEC ile çelişirse amendments kazanır.
6. **Git / remote (varsayılan):** Yerel dosya düzenleme ve (istenirse) **yerel** conventional commit **izinli**. **`git push` YASAK.** Repo visibility değiştirme (private↔public) **YASAK.** Deploy / dış servise yayın **YASAK.** `gh repo create`, `gh repo edit --visibility`, force-push ve remote overwrite **YASAK.** Push veya visibility yalnızca owner bu sohbette **açıkça ve o repo için** yeniden yetki verdiğinde. `.env`, secrets, `.venv`, `node_modules`, model cache, sqlite/qdrant data asla stage etme.
7. Sibling repolar aynı anda çalışıyor; yalnızca kendi klasörüne yaz. Port aralıklarına uy.
8. **Lisans:** `LICENSE` dosyası oluşturma veya bir lisans seçme. README'de "License: pending owner decision" yeterli (geliştirme dönemi kısıtı). Yayın öncesi lisans owner kararıdır — sessizce seçme.
9. `docs/PRODUCT_SPEC.md` **tarihsel geliştirme brifi**dir; güncel gerçek `docs/REVIEW_AMENDMENTS.md`, kod ve (varsa) `docs/IMPLEMENTATION_STATUS.md` / README shipped tablosudur. Çelişkide amendments + kod kazanır.
