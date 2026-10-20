# Cursor + GitHub: 5 Ürünlük Portföy Paketi

Bu paket, Cursor Agent ile **beş ayrı açık kaynak ürünü** adım adım geliştirmek için hazırlandı. Promptlar İngilizce yazıldı; README ve teknik belgeler uluslararası GitHub ziyaretçilerine yönelik İngilizce olacak.

## Önerilen sıra

1. `hr-policy-copilot` — RAG, doküman işleme, kaynak gösteren AI.
2. `hiring-process-miner` — Veri analitiği, süreç madenciliği.
3. `workforce-optimizer` — Kısıt programlama, matematiksel doğrulama.
4. `fairhire-audit` — ML metrikleri, model denetimi.
5. `skillgraph` — Bilgi grafiği, açıklanabilir öneriler.

## Başlama adımları

1. Cursor'da **boş bir klasör** aç (örneğin `hr-policy-copilot`). Her ürün için ayrı klasör/repository aç.
2. `common/.cursor/rules/` klasöründeki iki `.mdc` dosyasını ürün klasörünün `.cursor/rules/` dizinine kopyala. Cursor Project Rules bu dosyaları kalıcı olarak kullanır.
3. İlgili `prompts/0X-*.md` dosyasının **tamamını** Cursor Agent'a yapıştır. Agent'ın dosya oluşturma ve terminal çalıştırma yetkisini yalnızca inceleyerek ver.
4. İlk geçişte öncelikle Phase 1/MVP'yi tamamlat; aşamalar bittiğinde aynı promptu yeniden vermek yerine `templates/CURSOR_CONTINUE_PROMPT.md` ile devam et.
5. Her aşamada gerçek testleri çalıştır. Başarısız testleri düzeltmeden 'tamamlandı' kabul etme.
6. Gerçek çalışan arayüzden ekran görüntüleri al, `docs/screenshots/` dizinine koy. Yapay/fake ürün screenshot'ı kullanma.
7. `templates/README_REVIEW_PROMPT.md` ile Cursor'a nihai GitHub README, repo metadata ve demo doğrulaması yaptır.
8. GitHub'a göndermeden önce `templates/RELEASE_CHECKLIST.md` kontrol listesini uygula; sonra `templates/GITHUB_PUBLISH.md` rehberini izle.

## Ortak teknoloji tercihleri

- Frontend: React + Vite + TypeScript, Tailwind CSS, TanStack Query, React Router, Lucide, Vitest, React Testing Library, Playwright.
- Backend: Python 3.12+ (uyumlu sürümleri doğrula), FastAPI, Pydantic v2, SQLAlchemy v2, Alembic, pytest, httpx, Ruff.
- Veritabanı: PostgreSQL. Basit ve kısa ömürlü prototipte SQLite kabul edilebilir; son Docker akışında PostgreSQL kullanılmalı.
- Altyapı: Docker, Compose, GitHub Actions, `.env.example`, `.gitignore`, `Makefile`.
- Yüksek kalite: Gerçek hata mesajları, loading/empty states, erişilebilirlik, responsive tasarım, doğrulanabilir demo.

## Dosyaların anlamı

- `prompts/*.md`: Her ürünün **Cursor'a tek başına verilebilen** ayrıntılı promptu.
- `common/.cursor/rules/engineering.mdc`: Mühendislik, güvenlik, test ve geliştirme disiplini.
- `common/.cursor/rules/github-documentation.mdc`: Profesyonel README ve belgeler için kurallar.
- `templates/PROJECT_README_TEMPLATE.md`: Gerçek repo verileriyle doldurulacak İngilizce README şablonu.
- `templates/PROFILE_README_TEMPLATE.md`: Kişisel GitHub profili için ayrı İngilizce README.
- `templates/README_REVIEW_PROMPT.md`: Cursor'a README kalitesini son kontrolden geçirme komutu.
- `templates/CURSOR_CONTINUE_PROMPT.md`: Cursor aşamaları arasında kaldığında tutarlı devam etme komutu.
- `templates/RELEASE_CHECKLIST.md`: Public yayın öncesi kalite kontrolleri.
- `templates/GITHUB_PUBLISH.md`: GitHub'a yükleme ve profil README kurulumu.

## Önemli doğruluk notu

Bu paket **ürünün kodu değil**, ürünleri Cursor'da geliştirmek için ayrıntılı plan ve çalışma talimatlarıdır. Demo, test, deployment, metrik ve ekran görüntülerini Cursor'un gerçekten üretmesi/çalıştırması gerekir. Hiçbir prompt kusursuz çıktıyı garanti etmez; kodu ve sonuçları gözden geçir.
