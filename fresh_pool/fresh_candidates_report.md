# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 25
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 31

## Cara Pakai di OpenWrt
Jalankan manual saat node mulai mati:

```sh
sh /etc/mihomo-autopilot/openwrt_pull_fresh_pool.sh
```

Atau aktifkan guard otomatis:

```sh
sh /etc/mihomo-autopilot/openwrt_fresh_guard.sh
```

## Kandidat Fresh Teratas
1. `AKUN-001-CLOUDFLARE-VLESS-WS-68MS` (url=243ms, nekobox=273ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-83MS` (url=232ms, nekobox=307ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-93MS` (url=235ms, nekobox=269ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-92MS` (url=272ms, nekobox=302ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-91MS` (url=271ms, nekobox=317ms, status=yes)
6. `AKUN-006-CZ-LOTUNA-19970206-VLESS-WS-75MS` (url=264ms, nekobox=297ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-89MS` (url=269ms, nekobox=287ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-109MS` (url=287ms, nekobox=345ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-103MS` (url=327ms, nekobox=298ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-122MS` (url=285ms, nekobox=295ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-82MS` (url=257ms, status=HTTP 204)
12. `AKUN-012-IONOS-VLESS-WS-111MS` (url=302ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-119MS` (url=269ms, status=HTTP 204)
14. `AKUN-014-WPENG-VLESS-WS-108MS` (url=275ms, status=HTTP 204)
15. `AKUN-015-PAGES-VLESS-WS-116MS` (url=241ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-137MS` (url=330ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-138MS` (url=263ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-113MS` (url=288ms, status=HTTP 204)
19. `AKUN-021-UNKNOWN-VLESS-WS-179MS` (url=365ms, status=HTTP 204)
20. `AKUN-023-UNKNOWN-VLESS-WS-105MS` (url=300ms, status=HTTP 204)
21. `AKUN-024-UNKNOWN-VLESS-WS-271MS` (url=576ms, status=HTTP 204)
22. `AKUN-025-UNKNOWN-VLESS-WS-290MS` (url=552ms, status=HTTP 204)
23. `AKUN-026-UNKNOWN-VLESS-WS-298MS` (url=678ms, status=HTTP 204)
24. `AKUN-027-UNKNOWN-VLESS-WS-266MS` (url=570ms, status=HTTP 204)
25. `AKUN-028-UNKNOWN-VLESS-WS-302MS` (url=666ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
