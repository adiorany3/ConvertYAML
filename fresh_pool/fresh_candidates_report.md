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
- Proxy di openclash_fresh_pool.yaml: 30

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
1. `AKUN-001-UNKNOWN-VLESS-WS-89MS` (url=349ms, nekobox=414ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-93MS` (url=443ms, nekobox=362ms, status=yes)
3. `AKUN-003-ALIBABA-VLESS-WS-86MS` (url=293ms, nekobox=402ms, status=yes)
4. `AKUN-004-ZVC-VLESS-WS-90MS` (url=348ms, nekobox=388ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-95MS` (url=501ms, nekobox=388ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-89MS` (url=358ms, nekobox=403ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-108MS` (url=551ms, nekobox=328ms, status=yes)
8. `AKUN-008-ZVC-VLESS-WS-98MS` (url=399ms, nekobox=380ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-121MS` (url=408ms, nekobox=390ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-121MS` (url=422ms, nekobox=383ms, status=yes)
11. `AKUN-012-CLOUDFLARE-VLESS-WS-115MS` (url=356ms, status=HTTP 204)
12. `AKUN-013-UNKNOWN-VLESS-WS-115MS` (url=372ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-131MS` (url=409ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-99MS` (url=401ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-152MS` (url=381ms, status=HTTP 204)
16. `AKUN-017-DEV-VLESS-WS-122MS` (url=388ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-156MS` (url=389ms, status=HTTP 204)
18. `AKUN-019-SPEEDTEST-VLESS-WS-158MS` (url=302ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-204MS` (url=393ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-114MS` (url=356ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-123MS` (url=406ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-269MS` (url=648ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-297MS` (url=748ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-356MS` (url=740ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-358MS` (url=735ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
