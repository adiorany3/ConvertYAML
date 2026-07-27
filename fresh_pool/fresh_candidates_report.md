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
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-58MS` (url=211ms, nekobox=242ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-58MS` (url=209ms, nekobox=236ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-58MS` (url=211ms, nekobox=253ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-58MS` (url=208ms, nekobox=240ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-55MS` (url=210ms, nekobox=237ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-60MS` (url=208ms, nekobox=238ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-73MS` (url=215ms, nekobox=248ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-55MS` (url=220ms, nekobox=235ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-65MS` (url=212ms, nekobox=240ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-77MS` (url=202ms, nekobox=238ms, status=yes)
11. `AKUN-011-EU-VLESS-WS-90MS` (url=212ms, status=HTTP 204)
12. `AKUN-012-RS-RAPIDSEEDBOX-20190717-VLESS-WS-102MS` (url=213ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-86MS` (url=210ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-105MS` (url=307ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-103MS` (url=212ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-80MS` (url=214ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-56MS` (url=210ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-88MS` (url=224ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-116MS` (url=337ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-57MS` (url=222ms, status=HTTP 204)
21. `AKUN-021-SKK-VLESS-WS-63MS` (url=212ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-388MS` (url=743ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-497MS` (url=943ms, status=HTTP 204)
24. `AKUN-026-SUKARIO-VLESS-WS-595MS` (url=979ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-667MS` (url=1911ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
