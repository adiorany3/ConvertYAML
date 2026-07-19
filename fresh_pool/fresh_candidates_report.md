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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-103MS` (url=305ms, nekobox=387ms, status=yes)
2. `AKUN-002-UK-GB-DCL-01-20191003-VLESS-WS-114MS` (url=294ms, nekobox=389ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-109MS` (url=425ms, nekobox=370ms, status=yes)
4. `AKUN-004-ZVC-VLESS-WS-108MS` (url=318ms, nekobox=354ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-102MS` (url=290ms, nekobox=324ms, status=yes)
6. `AKUN-006-SAVVY-7-VLESS-WS-117MS` (url=300ms, nekobox=335ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-119MS` (url=293ms, nekobox=310ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-118MS` (url=299ms, nekobox=327ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-119MS` (url=315ms, nekobox=402ms, status=yes)
10. `AKUN-010-VOV-VLESS-WS-120MS` (url=371ms, nekobox=338ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-123MS` (url=296ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-127MS` (url=329ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-121MS` (url=329ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-122MS` (url=269ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-106MS` (url=288ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-126MS` (url=339ms, status=HTTP 204)
17. `AKUN-017-466688-VLESS-WS-121MS` (url=319ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-134MS` (url=295ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-138MS` (url=422ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-135MS` (url=307ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-156MS` (url=341ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-180MS` (url=325ms, status=HTTP 204)
23. `AKUN-023-WEBEX-VLESS-WS-137MS` (url=325ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-225MS` (url=377ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-177MS` (url=347ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
