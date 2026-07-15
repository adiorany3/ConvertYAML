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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-78MS` (url=227ms, nekobox=256ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-79MS` (url=215ms, nekobox=256ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-88MS` (url=238ms, nekobox=248ms, status=yes)
4. `AKUN-004-OVH-VLESS-WS-82MS` (url=257ms, nekobox=262ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-86MS` (url=214ms, nekobox=256ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-105MS` (url=205ms, nekobox=243ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-106MS` (url=230ms, nekobox=244ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-88MS` (url=230ms, nekobox=7177ms, status=no)
9. `AKUN-008-CLOUDFLARE-VLESS-WS-91MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-97MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-96MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-89MS` (url=210ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-112MS` (url=248ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-97MS` (url=235ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-109MS` (url=228ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-117MS` (url=296ms, status=HTTP 204)
17. `AKUN-017-DEV-VLESS-WS-111MS` (url=208ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-117MS` (url=231ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-127MS` (url=214ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-105MS` (url=203ms, status=HTTP 204)
21. `AKUN-021-DEV-VLESS-WS-127MS` (url=236ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-137MS` (url=224ms, status=HTTP 204)
23. `AKUN-023-466688-VLESS-WS-128MS` (url=219ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-133MS` (url=238ms, status=HTTP 204)
25. `AKUN-025-466688-VLESS-WS-91MS` (url=203ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
