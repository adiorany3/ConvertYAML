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
1. `AKUN-001-WPENG-VLESS-WS-94MS` (url=267ms, nekobox=295ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-102MS` (url=250ms, nekobox=308ms, status=yes)
3. `AKUN-003-WPENG-VLESS-WS-97MS` (url=295ms, nekobox=284ms, status=yes)
4. `AKUN-004-WEYRO-NET-VLESS-WS-114MS` (url=317ms, nekobox=309ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-97MS` (url=244ms, nekobox=276ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-110MS` (url=245ms, nekobox=325ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-121MS` (url=239ms, nekobox=272ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-108MS` (url=283ms, nekobox=327ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-123MS` (url=281ms, nekobox=328ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-118MS` (url=244ms, nekobox=312ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-127MS` (url=261ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-120MS` (url=295ms, status=HTTP 204)
13. `AKUN-013-ZVC-VLESS-WS-113MS` (url=319ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-104MS` (url=267ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-123MS` (url=264ms, status=HTTP 204)
16. `AKUN-016-ZVC-VLESS-WS-135MS` (url=294ms, status=HTTP 204)
17. `AKUN-017-WEYRO-NET-VLESS-WS-118MS` (url=261ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-129MS` (url=265ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-133MS` (url=335ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-111MS` (url=255ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-302MS` (url=679ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-281MS` (url=592ms, status=HTTP 204)
23. `AKUN-023-PMBET-NET-VLESS-WS-312MS` (url=714ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-325MS` (url=737ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-324MS` (url=760ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
