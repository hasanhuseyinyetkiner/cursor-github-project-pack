# Cursor + GitHub: Engineering Workflow Pack (5 Portfolio Apps)

Bu paket, Cursor / Antigravity Agent ile **beş ayrı ürün reposunu** kanıta dayalı şekilde geliştirmek ve (owner onayıyla) yayınlamak için hazırlanmış bir **mühendislik workflow / prompt pack**'tir — ürün kaynak kodu değildir.

Promptlar İngilizce yazıldı; ürün README ve teknik belgeler uluslararası ziyaretçilere yönelik İngilizce olacak.

## Önerilen sıra

1. `hr-policy-copilot` — RAG, doküman işleme, kaynak gösteren cevaplar.
2. `hiring-process-miner` — Event-log analitiği (pandas çekirdek; PM4Py opsiyonel).
3. `workforce-optimizer` — Kısıt programlama, bağımsız doğrulayıcı, **özel roster grid**.
4. `fairhire-audit` — ML metrikleri, model denetimi.
5. `skillgraph` — Bilgi grafiği; embeddings varsayılan kapalı / opsiyonel.

Güncel shipped/planned özeti: [`docs/IMPLEMENTATION_STATUS.md`](docs/IMPLEMENTATION_STATUS.md).

## Başlama adımları

1. Cursor'da **ürün klasörünü** aç (örneğin `hr-portfolio/hr-policy-copilot`). Her ürün ayrı repository.
2. `common/.cursor/rules/` içindeki iki `.mdc` dosyasını ürünün `.cursor/rules/` dizinine kopyala (veya senkron tut).
3. Scaffolded repo için önce [`prompts/antigravity/00-SYSTEM.md`](prompts/antigravity/00-SYSTEM.md), sonra ilgili `prompts/antigravity/0X-*.md`. Boş repo için tarihsel greenfield: `prompts/0X-*.md` (PRODUCT_SPEC ile aynı sınıfta: **historical brief**).
4. Agent'a dosya/terminal yetkisini yalnızca planı inceledikten sonra ver.
5. İlk geçişte Phase 1/MVP; devam için `templates/CURSOR_CONTINUE_PROMPT.md`.
6. Her aşamada gerçek testleri çalıştır. Başarısız testleri düzeltmeden "tamamlandı" deme.
7. Çalışan UI'dan ekran görüntüsü al (`docs/screenshots/`). Sahte screenshot yok.
8. `templates/README_REVIEW_PROMPT.md` ile README doğrulaması.
9. Public öncesi `templates/RELEASE_CHECKLIST.md` + `templates/GITHUB_PUBLISH.md` (**mevcut remote'lar için**; `gh repo create --public --push` yok).

## Ortak teknoloji tercihleri

- Frontend: React + Vite + TypeScript, Tailwind CSS, TanStack Query, React Router, Lucide, Vitest, React Testing Library, Playwright.
- Backend: Python 3.12+ (doğrulanmış sürüm), FastAPI, Pydantic v2, SQLAlchemy v2, Alembic, pytest, httpx, Ruff.
- Veritabanı: **Yerel native yol: SQLite kabul / tercih** (aynı modeller). **Compose + CI: PostgreSQL.** README hangi yolun nerede doğrulandığını yazmalı.
- Altyapı: `compose.yaml` + GitHub Actions (Compose smoke genelde CI'da); `.env.example`, `.gitignore`, `Makefile` isteğe bağlı.
- Yüksek kalite: Gerçek hata mesajları, loading/empty states, erişilebilirlik, responsive tasarım, doğrulanabilir demo. **Planned ≠ shipped.**

## Git / yayın politikası (varsayılan)

- Yerel düzenleme OK; yerel commit yalnızca owner isterse.
- **`git push` yok.** Visibility değiştirme yok. Deploy yok. Canlı profil README overwrite yok.
- Push / public / LICENSE seçimi: owner'ın **bu sohbette açık** onayı + checklist.

## Dosyaların anlamı

- `prompts/*.md`: Greenfield / **tarihsel** ürün promptları.
- `prompts/antigravity/*`: Scaffolded repo audit/implement + sistem kuralları.
- `common/.cursor/rules/engineering.mdc`: Mühendislik, güvenlik, test, **git/lisans defaults**.
- `common/.cursor/rules/github-documentation.mdc`: README ve belgeler.
- `templates/PROJECT_README_TEMPLATE.md`: Ürün README şablonu.
- `templates/PROFILE_README_TEMPLATE.md`: Profil README taslağı (`hasanhuseyinyetkiner/hasanhuseyinyetkiner` — **push etme**).
- `templates/README_REVIEW_PROMPT.md`: README audit komutu.
- `templates/CURSOR_CONTINUE_PROMPT.md`: Devam komutu.
- `templates/RELEASE_CHECKLIST.md`: Public öncesi kontroller (lisans = owner kararı).
- `templates/GITHUB_PUBLISH.md`: **Mevcut** remote'lar için yayın rehberi.
- `docs/DESIGN_REVIEW.md`: Tarihsel audit + CURRENT VERIFICATION STATUS.
- `docs/IMPLEMENTATION_STATUS.md`: Shipped vs outdated pack claims.
- `docs/LICENSING.md`: Geliştirme kısıtı / release ihtiyacı / owner-pending ayrımı.

## Önemli doğruluk notu

Bu paket **ürünün kodu değil**. Demo, test, metrik ve ekran görüntülerini agent'ın gerçekten üretmesi gerekir. Hiçbir prompt kusursuz çıktıyı garanti etmez.
