# Fix GitHub Actions push rejected/fetch first

Paket ini memperbaiki error:

```text
! [rejected] main -> main (fetch first)
error: failed to push some refs
```

Perubahan utama:

- `actions/checkout` memakai `fetch-depth: 0`.
- Workflow melakukan `git pull --rebase --autostash` sebelum generate.
- Push dilakukan dengan retry 3 kali.
- Sebelum push, workflow melakukan `git fetch` dan `git pull --rebase --autostash` lagi.
- `concurrency` memakai `cancel-in-progress: true` agar workflow update tidak berjalan dobel.

Upload/replace file berikut ke repo:

```text
generate_yaml.py
sumberyaml_core.py
requirements.txt
.github/workflows/update-yaml-6jam.yml
```

Lalu jalankan manual lewat **Actions > Run workflow**.
