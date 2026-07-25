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
1. `AKUN-001-UNKNOWN-VLESS-WS-56MS` (url=217ms, nekobox=237ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-57MS` (url=212ms, nekobox=241ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-57MS` (url=234ms, nekobox=257ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-58MS` (url=218ms, nekobox=261ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-77MS` (url=209ms, nekobox=247ms, status=yes)
6. `AKUN-006-DEV-VLESS-WS-63MS` (url=215ms, nekobox=255ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-66MS` (url=237ms, nekobox=247ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-65MS` (url=213ms, nekobox=261ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-97MS` (url=276ms, nekobox=339ms, status=yes)
10. `AKUN-010-DEV-VLESS-WS-73MS` (url=222ms, nekobox=245ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-100MS` (url=362ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-69MS` (url=218ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-120MS` (url=225ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-102MS` (url=215ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-115MS` (url=222ms, status=HTTP 204)
16. `AKUN-016-ZVC-VLESS-WS-63MS` (url=224ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-70MS` (url=225ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-86MS` (url=215ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-110MS` (url=213ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-62MS` (url=220ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-133MS` (url=236ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-337MS` (url=726ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-355MS` (url=788ms, status=HTTP 204)
24. `AKUN-024-INTERNETWORKS-45-131-210-VLESS-WS-359MS` (url=4790ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-589MS` (url=1004ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
