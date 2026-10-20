# GitHub yayın rehberi

## Projeyi repository'ye yükleme

Önce `git status` ve `.gitignore` kontrolü yap. `.env`, API anahtarları, çalışan dosyaları, yüklenen dokümanlar, büyük model dosyaları, `.venv`, `node_modules` ve veri tabanı dump'larını repoya ekleme. Gerekiyorsa daha önce commit edilmiş gizli anahtarları iptal/rotate et.

GitHub CLI ile bir proje klasörünün içinde:

```bash
git init
git add .
git commit -m "feat: initial working MVP"
gh auth login
gh repo create REPOSITORY --public --source=. --remote=origin --push
```

`REPOSITORY` yerine mevcut klasörünün/repo adının aynısını yaz. GitHub CLI kurulu değilse GitHub web arayüzünde boş public repo oluştur; `git remote add origin https://github.com/USERNAME/REPOSITORY.git` ve `git push -u origin main` gibi kendi branch adına uygun komutlarla gönder. Yerel proje zaten bir git repository'siyse yeniden `git init` gerekmeyebilir.

**Not:** Kod veya secrets kontrolünden önce public push yapma. `gh repo create ... --push` komutunu yalnızca kendi açık onayınla çalıştır.

## Profile README

GitHub profilinde görünmesini istiyorsan, GitHub kullanıcı adın **USERNAME** ise ayrı bir **public** `USERNAME` repository'si oluştur. Kök `README.md` dosyası GitHub profilinde görüntülenir. `PROFILE_README_TEMPLATE.md` dosyasını bu repoya uyarlayarak ekle.

## Repo metadatası

GitHub repository sayfasında About bölümüne kısa İngilizce açıklama, doğrulanmış demo URL'si (varsa) ve teknoloji/alan topics'lerini gir. İstersen 1280×640 oranlı ürün temalı social preview hazırla; gerçek ürün görünümü gibi sunulan sahte görseller kullanma.

## Yayın öncesi

`RELEASE_CHECKLIST.md` listesindeki kritik maddeleri kontrol et. Projeyi gerçekten çalıştırıp ekran görüntüsü al. Yalnızca çalışan projeleri profiline sabitle (pin).

Referanslar:
- GitHub CLI: https://cli.github.com/manual/gh_repo_create
- GitHub profile README: https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme
- GitHub README: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes
