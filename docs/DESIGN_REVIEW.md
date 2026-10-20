# Tasarım İncelemesi — Üretime Geçiş Engelleyici Bakış

> **Document role:** This file is a **historical pre-implementation design audit** of the pack prompts/rules (findings below).  
> For “what was fixed in product repos / what remains,” see **[CURRENT VERIFICATION STATUS](#current-verification-status)** at the bottom and [`IMPLEMENTATION_STATUS.md`](IMPLEMENTATION_STATUS.md). Do not delete or rewrite the original findings; mark them resolved/superseded in the status table instead.

**Kapsam:** `prompts/01..05`, `common/.cursor/rules/*.mdc`, `START_HERE.md`, `templates/*`.
**Tarih:** 2026-10-20. **Yöntem:** Spec metni satır numarasıyla alıntılandı; dış kütüphane iddiaları birincil kaynaktan (PyPI, GitHub Security Advisories, resmi dokümantasyon) doğrulandı; ortam iddiaları bu makinede komut çalıştırılarak doğrulandı. Kanıtı olmayan hiçbir bulgu listeye alınmadı.

**Önem ölçeği:** `BLOCKER` (bu hâliyle "done" denemez) · `HIGH` (doğruluk/güvenlik ihlali olası) · `MEDIUM` (belirli koşulda yanlış sonuç/operasyon sorunu) · `LOW` (sürtünme, maliyet).

## Özet

| ID | Bulgu | Önem |
| --- | --- | --- |
| C-1 | Definition of Done Docker'a bağlı, geliştirme makinesinde Docker yok | BLOCKER |
| C-2 | Kimlik doğrulamasız API, Compose varsayılanıyla tüm ağ arayüzlerine açılır | HIGH |
| C-3 | CPU-yoğun işler API sürecinde; iş durumu süreçle birlikte ölür (SPOF) | HIGH |
| C-4 | Kurallar arası çelişki: lisans seçimi ve push yasağı | MEDIUM |
| C-5 | sentence-transformers → torch CUDA tekerlekleri; imaj/CI boyutu | MEDIUM |
| C-6 | Beş ürün aynı varsayılan portları kullanır | LOW |
| HR-1 | PostgreSQL ↔ Qdrant çift yazımı atomik değil | HIGH |
| HR-2 | rank-bm25 bellek içi indeks; çoklu worker'da tutarsız arama | HIGH |
| HR-3 | Yüklenen PDF/DOCX ayrıştırma DoS (doğrulanmış pypdf açıkları) | HIGH |
| HR-4 | "Eski chunk'ları sil" ile "geçmiş cevabın kaynağını göster" çelişir | MEDIUM |
| HR-5 | "Tam offline" iddiasının gizli ağ bağımlılığı (model indirme) | MEDIUM |
| HPM-1 | PM4Py AGPL-3.0 — repo lisansını belirler | BLOCKER (karar) |
| HPM-2 | pandas ve PM4Py için ortak sıralama sözleşmesi tanımlı değil | MEDIUM |
| HPM-3 | Yerel saat → UTC dönüşümünde DST belirsizliği | MEDIUM |
| WFO-1 | "Tekrarlanabilir" çözüm iddiası CP-SAT varsayılanlarıyla sağlanamaz | HIGH |
| WFO-2 | Doğal roster görünümü FullCalendar Premium (ticari lisans) | MEDIUM |
| WFO-3 | SQLite fallback timezone bilgisini kaybeder | MEDIUM |
| FHA-1 | "Kalibre skor" kapısı tanımsız | MEDIUM |
| FHA-2 | Korunan öznitelik saklama/silme mekanizması tanımsız | MEDIUM |
| FHA-3 | Parquet desteği için motor bağımlılığı eksik | LOW |
| SKG-1 | NetworkX bellek içi graf ile PostgreSQL kaynak gerçekliği ayrışır | HIGH |

---

## Ortak (tüm ürünler)

### C-1 · Definition of Done Docker'a bağlı, makinede Docker yok — `BLOCKER`
- **Kanıt:** `prompts/01` s.59 "`docker compose up --build` should work"; `START_HERE.md` s.29 "Docker, Compose"; bu makinede `docker --version` → *not recognized*; WSL Ubuntu içinde de `docker: command not found`; `psql` de yok.
- **Arıza mekanizması:** Agent DoD'yi yerelde doğrulayamaz; ya adımı sessizce atlar ya da README'ye doğrulanmamış Quick Start yazar (`github-documentation.mdc` s.17 "exact verified commands" kuralını ihlal).
- **Etki:** README'deki birincil kurulum yolu hiç çalıştırılmadan yayımlanır; ilk ziyaretçi bozuk komutla karşılaşır.
- **Doğrulama testi:** GitHub Actions'ta (ubuntu runner'da Docker var) `docker compose up --build -d` + `/ready` 200 bekleyen bir `compose-smoke` job'ı; yerelde ise native yol (`uv run` + `pnpm dev`) için aynı smoke testi.
- **Öneri:** İki yol tanımla: (1) native geliştirme yolu yerelde doğrulanır; (2) Compose yolu yalnızca CI'da doğrulanır ve README bunu açıkça belirtir.

### C-2 · Kimlik doğrulamasız API ağa açılır — `HIGH`
- **Kanıt:** `engineering.mdc` s.18 yerel tek kullanıcılı demoya izin verir; `prompts/01` s.37 "Show delete-all-data action in demo", auth yalnızca aynı satırdaki "If implementing multi-user access" koşuluyla; hiçbir prompt bind adresi belirtmez.
- **Arıza mekanizması:** Compose'ta `ports: "8000:8000"` Docker'da host'un tüm arayüzlerine bağlanır. Aynı ağdaki biri doküman yükleyebilir, okuyabilir veya "delete all" çağırabilir.
- **Etki:** HR verisi (politika, aday event log'u, korunan öznitelikler) kimlik doğrulamasız erişime açılır.
- **Doğrulama testi:** `docker compose config` çıktısında her `ports` girdisinin `127.0.0.1:` ile başladığını assert eden CI adımı; ikinci bir hosttan `curl` erişiminin reddedildiğini gösteren manuel test.
- **Öneri:** Varsayılan bind `127.0.0.1`; `APP_ENV=demo` dışında auth olmadan başlamayı reddet; UI'da kalıcı "demo — yerel kullanım" bandı.

### C-3 · CPU-yoğun işler API sürecinde, iş durumu süreçle ölür — `HIGH` (SPOF)
- **Kanıt:** `prompts/01` s.41 `IngestionJob` varlığı var ama stack'te (s.13–18) kuyruk/worker yok. `prompts/03` s.14 "add async queue only if justified", fakat s.49 API'si `POST /api/optimization-runs` + `GET /api/optimization-runs/{id}` (asenkron şekilli). `prompts/04` s.26 bootstrap CI.
- **Arıza mekanizması:** `async def` içinde embedding, PDF ayrıştırma, PM4Py keşfi, CP-SAT veya bootstrap çağrısı event loop'u bloklar; `/health` zaman aşımına düşer, orkestratör konteyneri yeniden başlatır. İş thread'e taşınırsa bu kez durum bellekte kalır; yeniden başlatmada satırlar sonsuza dek `RUNNING` olarak takılır. API süreci hem sunucu hem worker olduğu için tek arıza noktasıdır.
- **Etki:** UI'da hiç bitmeyen iş; yanlış "çözülüyor" durumu; sağlık kontrolü kaynaklı restart döngüsü.
- **Doğrulama testi:** (a) Uzun bir iş başlatıp `/health` p95 gecikmesini ölç (<200 ms beklenir). (b) İş sürerken API'yi öldür ve yeniden başlat; `GET` sonucunun `FAILED`/`ABANDONED` olduğunu, `RUNNING` olmadığını assert et.
- **Öneri:** CPU işini `run_in_threadpool` veya süreç havuzuna taşı; `heartbeat_at` kolonu olan kalıcı iş tablosu kullan; başlangıçta bayat işleri temizleyen bir "reaper" çalıştır; CP-SAT'ta `num_workers` sınırla.

### C-4 · Kurallar arası çelişki: lisans ve push — `MEDIUM`
- **Kanıt:** `github-documentation.mdc` s.9 "`LICENSE` only after confirming licensing choice"; buna karşın her prompt README'de "selected license" ister (`01` s.70, `02` s.69, `03` s.66, `04` s.63, `05` s.67). `engineering.mdc` s.25 "Do not create remote repos, push commits" diyor; repolar artık var.
- **Arıza mekanizması:** Agent ya kilitlenir ya da lisansı tek taraflı seçer. HPM-1 nedeniyle lisans seçimi serbest değildir.
- **Doğrulama testi:** CI'da `pip-licenses`/`license-checker` ile bağımlılık lisanslarını repo `LICENSE`'ı ile karşılaştıran adım.

### C-5 · torch CUDA tekerlekleri — `MEDIUM`
- **Kanıt:** `prompts/01` s.15 ve `prompts/05` s.13 sentence-transformers ister; bu paket torch'a bağımlıdır. PyPI'daki Linux torch tekerleği varsayılan olarak `nvidia-*` CUDA paketlerini de çeker.
- **Arıza mekanizması:** Docker imajı ve CI önbelleği GB'lar seviyesine çıkar; CI süresi ve runner disk alanı sorun olur. GPU zaten kullanılmaz.
- **Doğrulama testi:** CI'da `docker image ls` boyutu için bir eşik; `uv tree | grep nvidia` boş olmalı.
- **Öneri:** `uv` index ayarıyla `https://download.pytorch.org/whl/cpu` kaynağını torch'a sabitle.

### C-6 · Port çakışması — `LOW`
- **Kanıt:** `START_HERE.md` s.25–30 beş ürüne aynı stack'i dikte eder; varsayılan portlar (8000/5173/5432) aynıdır.
- **Etki:** Aynı makinede iki ürün aynı anda çalışmaz (paralel geliştirme ve ekran görüntüsü alma dahil).
- **Öneri ve test:** Ürün başına port aralığı belirle (aşağıdaki ekler bölümüne bak); smoke testi bu portlarla çalıştır.

---

## 01 · HR Policy Copilot

### HR-1 · PostgreSQL ↔ Qdrant çift yazımı — `HIGH`
- **Kanıt:** s.14–15 metadata PostgreSQL'de, vektörler Qdrant'ta; s.26 "replacing a document supersedes its old version, removes stale Qdrant chunks".
- **Arıza mekanizması:** Versiyon değişimi = PG commit + Qdrant delete/upsert. İkisi arasında çökme veya Qdrant hatası olursa "superseded" bir politikanın chunk'ları aranabilir kalır ve kaynak olarak gösterilir. Bu, ürünün ana vaadi olan "doğrulanabilir cevap"ı doğrudan çiğner.
- **Doğrulama testi:** PG commit'inden sonra, Qdrant silmesinden önce exception enjekte et. Sorgunun superseded versiyondan hiçbir chunk döndürmediğini assert et.
- **Öneri:** Kaynak gerçeklik PG olsun. Qdrant sonuçlarını PG'deki `is_current` chunk ID kümesiyle post-filtrele. Uzlaştırma (reconcile) komutu/job'ı ekle.

### HR-2 · rank-bm25 bellek içi indeks — `HIGH`
- **Kanıt:** s.15 "rank-bm25". Kütüphane kaynağı (`BM25.__init__`) korpusu kurulumda bellekte indeksler; kalıcılık ve artımlı ekle/sil API'si yoktur (dorianbrown/rank_bm25).
- **Arıza mekanizması:** `uvicorn --workers N` ile her worker kendi indeksini kurar; worker A'ya yapılan yükleme worker B'de görünmez, hibrit sonuç isteğin hangi worker'a düştüğüne bağlı olur. Yeniden başlatmada indeks kaybolur. Her yükleme tüm korpusu yeniden kurar (O(N)). Kategori ve tenant filtreleri de bu indekse ayrıca uygulanmalıdır (s.37).
- **Doğrulama testi:** 2 worker çalıştır, doküman yükle, aynı sorguyu 20 kez sor; sonuç kümelerinin aynı olduğunu assert et.
- **Öneri:** Sparse retrieval için PostgreSQL full-text (`tsvector` + `ts_rank`) veya Qdrant sparse vektörleri kullan. Ya da indeksi PG'deki `corpus_version`'a bağla ve versiyon değişince yeniden kur.

### HR-3 · Upload ayrıştırma DoS — `HIGH`
- **Kanıt:** s.16 pypdf + python-docx; s.37 yalnızca boyut sınırı, MIME ve isim kontrolü. pypdf'te doğrulanmış sonsuz döngü açıkları: CVE-2026-59936 (<6.14.1, kapatılmamış inline image), CVE-2026-84309 (<6.16.0), GHSA-9mx8-4j7g-633p ve GHSA-qfv9-64jg-mh7p (<6.20.1, 2026-10-12). DOCX bir ZIP arşividir.
- **Arıza mekanizması:** Küçük boyutlu, kötü niyetli bir PDF bir CPU çekirdeğini süresiz kilitler. Boyut sınırı CPU süresini sınırlamaz. ZIP bombası da sıkıştırılmış boyut sınırını geçer.
- **Doğrulama testi:** CVE-2026-59936'nın yayımlanmış PoC baytlarıyla upload; işin N saniye içinde `FAILED` olduğunu assert et. Sıkıştırma oranı >100 olan DOCX'in reddedildiğini assert et.
- **Öneri:** `pypdf>=6.20.1` sabitle; ayrıştırmayı zaman ve bellek sınırlı alt süreçte yap; sayfa sayısı ve açılmış boyut sınırı koy.

### HR-4 · Silinen chunk ile geçmiş cevap kaynağı çelişkisi — `MEDIUM`
- **Kanıt:** s.26 "removes stale Qdrant chunks" ve aynı satırda "clearly indicates which version supported each past answer"; s.34 "snippets must correspond exactly to stored extracted text".
- **Arıza mekanizması:** Chunk silinirse eski konuşmadaki citation çözülemez (404) veya yeni versiyonun metnine yanlış bağlanır.
- **Doğrulama testi:** Soru sor → dokümanı değiştir → eski konuşmayı aç; citation'ın eski versiyon metnini ve versiyon numarasını gösterdiğini assert et.
- **Öneri:** Chunk'ları PG'de soft-delete et (`superseded_at`); yalnızca vektörü kaldır. `Citation` kaydı snippet metni, hash ve `version_id` snapshot'ı saklasın.

### HR-5 · "Tam offline" iddiasının gizli ağ bağımlılığı — `MEDIUM`
- **Kanıt:** s.31 "work fully offline after dependencies/models are installed"; s.59 "start with realistic demo data without external API keys"; s.36 "Qdrant downtime gracefully" ama degrade davranışı tanımsız.
- **Arıza mekanizması:** sentence-transformers modeli ilk kullanımda Hugging Face Hub'dan indirilir; ağ yoksa model yüklenemez ve sorgu 500 verir. Qdrant düşerse ne olacağı belirsizdir.
- **Doğrulama testi:** `HF_HUB_OFFLINE=1` ve boş önbellekle başlat: `/ready` `degraded` raporlamalı, sorgu BM25 kanıtıyla veya açık bir hata nedeniyle dönmeli. Aynısı Qdrant kapalıyken.
- **Öneri:** Modeli build sırasında indir (`make models`); BM25-only degrade modunu `/ready` ve UI'da göster.

## 02 · Hiring Process Miner

### HPM-1 · PM4Py AGPL-3.0 — `BLOCKER` (karar gerekli)
- **Kanıt:** s.13 PM4Py zorunlu. PyPI `pm4py`: "License: AGPL-3.0-or-later". Proje sitesine göre PM4Py'ı import eden yazılım covered work sayılır ve ağ üzerinden sunulursa tüm uygulamanın kaynağı AGPL ile sunulmalıdır.
- **Arıza mekanizması:** Repo MIT/Apache ile lisanslanır ve PM4Py'a bağlıysa lisans beyanı yanıltıcı olur; bunu fark eden bir işveren veya kullanıcı için ciddi bir güven kaybıdır.
- **Doğrulama testi:** CI'da `pip-licenses --fail-on="GNU Affero General Public License v3"` (repo AGPL değilse).
- **Öneri:** Ya repo AGPL-3.0 olur, ya da PM4Py opsiyonel bir adaptöre (ayrı extra) itilir. s.61 KPI'ların pandas ile bağımsız üretilmesini zaten istediği için çekirdek PM4Py'sız çalışabilir.

### HPM-2 · Ortak sıralama sözleşmesi yok — `MEDIUM`
- **Kanıt:** s.56 "explicit stable tie-breaker for equal timestamps"; s.61 KPI'lar pandas ile, görselleştirme PM4Py ile ayrı hesaplanır.
- **Arıza mekanizması:** Eşit zaman damgalı olaylarda iki uygulama farklı sıralama yaparsa DFG kenar sayıları ile KPI tabloları birbiriyle çelişir; "matematiksel izlenebilirlik" farkı kaybolur.
- **Doğrulama testi:** Eşit zaman damgalı fixture'da pandas DFG ile PM4Py DFG kenar sayılarının birebir eşit olduğunu assert et.
- **Öneri:** Tek bir `canonical_order(df)` fonksiyonu (timestamp, kaynak satır no) tanımla; her iki yol da yalnızca onun çıktısını tüketsin.

### HPM-3 · DST belirsizliği — `MEDIUM`
- **Kanıt:** s.21 "timestamp timezone selection"; s.60 "negative durations".
- **Arıza mekanizması:** Örneğin `Europe/Berlin`'de 2026-10-25 02:30 iki kez yaşanır. Naive CSV saatini bu bölgeye yerelleştirmek ya hata fırlatır ya da sessizce bir tarafı seçer; sonuç negatif süre veya yanlış sıralamadır.
- **Doğrulama testi:** Belirsiz ve var olmayan (ileri alınan) yerel saatler içeren fixture; politika (`raise`/`earliest`/`flag`) kalite raporunda görünmeli.
- **Öneri:** UTC sakla; belirsiz saatleri reddet ya da açıkça işaretle.

## 03 · Workforce Optimizer

### WFO-1 · "Tekrarlanabilir" iddiası CP-SAT varsayılanlarıyla sağlanamaz — `HIGH`
- **Kanıt:** s.56 "explicit reproducible solver settings; allow reasonable time limit". OR-Tools ekibinin yanıtına göre CP-SAT ancak `interleave_search=true` ile deterministiktir (performans maliyetiyle). `max_time_in_seconds` duvar saati sınırıdır; `max_deterministic_time` ayrı bir parametredir. Varsayılan durumda tüm çekirdekler kullanılır.
- **Arıza mekanizması:** Aynı girdi, aynı seed ve duvar saati sınırıyla makine yüküne göre farklı atama veya farklı objective üretilir. "Bu vardiya neden bu kişide?" açıklaması koşudan koşuya değişir.
- **Doğrulama testi:** Aynı instance'ı 10 kez çöz; atama hash'lerinin aynı olduğunu assert et (reproducible modda).
- **Öneri:** "Reproducible" modda `interleave_search=True`, sabit `num_workers`, `random_seed` ve `max_deterministic_time` kullan; parametreleri `OptimizationRun` kaydına yaz.

### WFO-2 · FullCalendar Premium lisansı — `MEDIUM`
- **Kanıt:** s.12 "FullCalendar (check suitable current license)". fullcalendar.io/license: standart eklentiler MIT; Resource Timeline ve Vertical Resource görünümleri Premium (ticari lisans gerekir; AGPL dışı açık kaynakta anahtar repoya konamaz).
- **Arıza mekanizması:** Çalışan × zaman roster'ı doğal olarak "resource timeline" görünümüdür; agent bunu seçerse ürün lisans uyarısıyla çalışır veya lisans ihlali oluşur.
- **Doğrulama testi:** CI'da `package.json` içinde `@fullcalendar/resource*` ve `fullcalendar-scheduler` olmadığını assert et.
- **Öneri:** Yalnızca MIT görünümleri (`timeGrid`/`dayGrid`) kullan veya özel bir roster ızgarası yaz.

### WFO-3 · SQLite fallback timezone kaybı — `MEDIUM`
- **Kanıt:** s.20 "timezone-aware timestamps"; `START_HERE.md` s.28 kısa prototipte SQLite'a izin veriyor; C-1 nedeniyle yerelde PG yok. SQLite'ın yerel DATETIME tipi yoktur ve SQLAlchemy'nin SQLite `DateTime` tipi zaman dilimi ofsetini saklamaz.
- **Arıza mekanizması:** Yerel testler naive datetime ile geçer, CI'daki PostgreSQL'de aware datetime ile davranış değişir. Gece yarısını aşan vardiyalar ve dinlenme kuralı hesapları dialect'e göre farklı sonuç verir.
- **Doğrulama testi:** Aware datetime'ı DB'den round-trip et; `tzinfo is not None` ve UTC eşitliğini her iki dialect'te assert et.
- **Öneri:** UTC'yi zorlayan bir `TypeDecorator` (aware giriş, aware çıkış) kullan; CI matrisinde PostgreSQL servisi olsun.

## 04 · FairHire Audit

### FHA-1 · "Kalibre skor" kapısı tanımsız — `MEDIUM`
- **Kanıt:** s.27 "Score threshold slider only when properly calibrated/interpretable probability or continuous score exists".
- **Arıza mekanizması:** Kalibrasyonun nasıl belirleneceği tanımsız olduğu için agent ya her skoru kabul eder (yanıltıcı eşik simülasyonu) ya da keyfi bir kural uydurur.
- **Doğrulama testi:** [0,1] dışı skor → slider devre dışı ve gerekçesi görünür; kullanıcı beyanı + Brier skoru + reliability tablosu raporda yer alır.
- **Öneri:** Kapı = skor türü kullanıcı tarafından beyan edilir (olasılık / sıralama skoru) + aralık kontrolü + kalibrasyon özeti. Sistem asla "kalibre" diye karar vermez, yalnızca kanıt gösterir.

### FHA-2 · Korunan öznitelik saklama ve silme — `MEDIUM`
- **Kanıt:** s.59 "access-controlled, minimally retained and deletable"; veri modeli (s.19) ham dataset'i ve `GroupMetric`'i saklar, ancak TTL veya silme kaskadı tanımlı değil.
- **Arıza mekanizması:** Ham dosya, PG satırları ve türetilmiş grup metrikleri farklı yerlerde kalır; "sil" yalnızca birini siler.
- **Doğrulama testi:** Dataset sil → dosya sistemi, ilgili tüm tablolar ve rapor dışa aktarımlarında kalıntı olmadığını assert et.

### FHA-3 · Parquet motoru eksik — `LOW`
- **Kanıt:** s.19 "Accept CSV/Parquet"; s.13 stack'te `pyarrow`/`fastparquet` yok. `pandas.read_parquet` motor olmadan ImportError verir.
- **Doğrulama testi:** Temiz ortamda Parquet upload integration testi.

## 05 · SkillGraph

### SKG-1 · NetworkX bellek grafı ile PG kaynak gerçekliği — `HIGH`
- **Kanıt:** s.16 "NetworkX service-based graph storage for MVP, persisting nodes/edges in PostgreSQL"; s.27 kullanıcı ontolojiyi düzenleyebilir; s.43 "differences after ontology edits can be explained".
- **Arıza mekanizması:** Düzenleme PG'ye yazılır, ama diğer worker'lardaki bellek grafı bayat kalır. Aynı profil için öneri, isteğin düştüğü worker'a göre değişir ve `RecommendationTrace` hangi graf versiyonunun kullanıldığını kanıtlayamaz.
- **Doğrulama testi:** 2 worker çalıştır, worker A'da düzenleme yap, 20 öneri isteği gönder; tüm yanıtlarda `graph_version`'ın aynı olduğunu ve yeni kenarı yansıttığını assert et.
- **Öneri:** PG'de monoton `graph_version` tut; her istekte versiyonu karşılaştır ve gerekirse grafı yeniden yükle; trace'e versiyonu yaz.

---

## Çapraz kontrol: spec'in iyi yaptıkları (değiştirme)
- Sahte metrik, badge ve screenshot yasağı; açık "abstention" ve "INFEASIBLE" davranışı.
- Bağımsız doğrulayıcı (WFO), pandas ile bağımsız KPI (HPM) ve embedding'siz baseline (SKG). Bunlar doğru mimari kararlar.
- HR kararlarının otomatikleştirilmesinin açıkça yasaklanması.

Bu bulguların bağlayıcı karşılıkları her ürün reposunda `docs/REVIEW_AMENDMENTS.md` dosyasına işlenmiştir; `docs/PRODUCT_SPEC.md` en üstte bu dosyaya yönlendirir ve çelişkide amendments geçerlidir.

---

## CURRENT VERIFICATION STATUS

**Updated:** 2026-10-20 (pack audit). Status labels:

| Label | Meaning |
| --- | --- |
| **resolved** | Amendment + product evidence addresses the finding for MVP |
| **unresolved** | Still open / owner or product work remaining |
| **unverified** | Claimed in amendments/README but not re-proven in this pack pass |
| **superseded** | Original finding no longer applies as written (approach changed) |

| ID | Status | Notes (pack-level; re-check product repo before public release) |
| --- | --- | --- |
| C-1 | resolved | Dual path: native+SQLite local; Compose/Postgres in CI — documented in amendments + product READMEs |
| C-2 | unverified | Amendments require loopback/demo band; confirm each repo bind defaults before public host |
| C-3 | unverified | Threadpool/reaper patterns specified; confirm per-repo jobs + `/health` tests |
| C-4 | resolved *(pack)* / unresolved *(owner)* | Pack prompts/rules normalized: no blanket push; no silent LICENSE. **Owner still must choose license + approve push/visibility** |
| C-5 | unverified | CPU torch index / optional embeddings patterns exist in products; CI image size not re-measured here |
| C-6 | resolved | Antigravity prompts assign distinct port ranges (81xx/51xx/54xx) |
| HR-1 | unverified | PG-as-SoT + post-filter pattern in amendments; dual-write race tests product-local |
| HR-2 | unverified | DB-backed / versioned BM25 intended; multi-worker parity product-local |
| HR-3 | unverified | pypdf pin + sandbox called for; CVE PoC tests product-local |
| HR-4 | unverified | Citation snapshot / soft-delete pattern in amendments |
| HR-5 | unverified | Offline/degraded modes documented in product README claims |
| HPM-1 | resolved *(architecture)* / unresolved *(license file)* | Core pandas; PM4Py optional extra — **repo LICENSE still owner-pending** |
| HPM-2 | unverified | `canonical_order` required; PM4Py parity tests skip when absent |
| HPM-3 | unverified | DST policy in amendments/README |
| WFO-1 | unverified | Reproducible CP-SAT mode + 10× hash tests claimed in product README |
| WFO-2 | superseded → resolved | **Shipped custom roster grid**; FullCalendar Premium not used; CI assert pattern documented |
| WFO-3 | unverified | UTC TypeDecorator required; dialect round-trip product-local |
| FHA-1 | unverified | Score-gate semantics in amendments |
| FHA-2 | unverified | Cascade delete / retention claimed shipped in FairHire README |
| FHA-3 | unverified | pyarrow for Parquet claimed |
| SKG-1 | unverified | `graph_version` cache invalidation in amendments |
| Pack git auth contradiction | resolved | `00-SYSTEM` and templates: local OK; **no push / no visibility / no deploy** by default |
| Pack stack drift (PM4Py/FullCalendar/embeddings/Postgres-only) | resolved | See [`IMPLEMENTATION_STATUS.md`](IMPLEMENTATION_STATUS.md) + root README table |

**Still owner blockers for public GitHub:** license choice per repo; explicit push approval; private→public approval; secret scan; Actions review; profile Featured status labels; no agent push to `hasanhuseyinyetkiner/hasanhuseyinyetkiner`.
