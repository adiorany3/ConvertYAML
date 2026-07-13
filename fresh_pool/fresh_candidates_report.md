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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-104MS` (url=363ms, nekobox=324ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-108MS` (url=297ms, nekobox=338ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-92MS` (url=321ms, nekobox=321ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-107MS` (url=305ms, nekobox=336ms, status=yes)
5. `AKUN-005-ZVC-VLESS-WS-115MS` (url=303ms, nekobox=339ms, status=yes)
6. `AKUN-006-ZVC-VLESS-WS-115MS` (url=358ms, nekobox=326ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-121MS` (url=298ms, nekobox=333ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-121MS` (url=313ms, nekobox=416ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-124MS` (url=296ms, nekobox=318ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-128MS` (url=290ms, nekobox=406ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-127MS` (url=322ms, status=HTTP 204)
12. `AKUN-012-PUBLICDOMAINREGISTRY-NET-VLESS-WS-138MS` (url=333ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-117MS` (url=338ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-117MS` (url=310ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-132MS` (url=356ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-148MS` (url=346ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-121MS` (url=298ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-160MS` (url=359ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-155MS` (url=425ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-322MS` (url=662ms, status=HTTP 204)
21. `AKUN-021-US-VLESS-WS-139MS` (url=303ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-331MS` (url=861ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-323MS` (url=1413ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-340MS` (url=653ms, status=HTTP 204)
25. `AKUN-026-QZZ-VLESS-WS-253MS` (url=1746ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
