# SYSTEM EXECUTION DIRECTIVE FOR ANTIGRAVITY / CURSOR

Bu repo daha önce Cursor tarafından yarım bırakıldı (scaffolded / partial MVP). Görevin bu projeyi orijinal spesifikasyonlarına sadık kalarak **ürün kalitesine** getirmektir.

## KESİN KURALLAR

1. İlk iş olarak tüm dizini (`backend/`, `frontend/`, `tests/`, `scripts/`, `compose.yaml`, `docs/`) tara. İçinde `TODO`, `FIXME`, `pass`, `NotImplementedError`, sahte (hardcoded/mock) API dönüşleri veya bağlantısız React bileşenleri olan her yeri tespit et.
2. Asla sahte veri dönen endpoint bırakma. Tüm uç noktalar gerçek DB (SQLAlchemy 2 + Alembic) ve gerçek algoritmik servis katmanına bağlı olmalıdır.
3. Kod yazmayı bitirdiğinde mutlaka `ruff`, `pytest`, frontend `tsc`/`vitest`/`build` ve mümkünse Playwright çalıştır. Hata alırsan testi silme; kaynak kodu düzelt.
4. `README.md` ve `docs/GITHUB_METADATA.md` dosyalarını uydurma metrikler olmadan, gerçek test sonuçlarıyla güncelle.
5. **Docker bu makinede YOK.** `compose.yaml` + CI workflow yaz/doğrula; yerelde native `uv` + `pnpm` + SQLite (veya mevcut local path) kullan. `docs/REVIEW_AMENDMENTS.md` bağlayıcıdır ve PRODUCT_SPEC ile çelişirse amendments kazanır.
6. Owner **commit ve `git push origin HEAD` izni verdi.** Conventional commits kullan. `.env`, secrets, `.venv`, `node_modules`, model cache, sqlite/qdrant data push etme.
7. Sibling repolar aynı anda çalışıyor; yalnızca kendi klasörüne yaz. Port aralıklarına uy.
