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
1. `AKUN-001-090227-VLESS-WS-91MS` (url=212ms, nekobox=259ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-93MS` (url=206ms, nekobox=248ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-93MS` (url=237ms, nekobox=234ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-98MS` (url=219ms, nekobox=245ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-104MS` (url=260ms, nekobox=264ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-101MS` (url=255ms, nekobox=259ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-99MS` (url=283ms, nekobox=7168ms, status=no)
8. `AKUN-007-CLOUDFLARE-VLESS-WS-112MS`
9. `AKUN-008-UNKNOWN-VLESS-WS-98MS`
10. `AKUN-009-SPEEDTEST-VLESS-WS-102MS`
11. `AKUN-010-DEV-VLESS-WS-106MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-107MS` (url=231ms, status=HTTP 204)
13. `AKUN-013-DEV-VLESS-WS-118MS` (url=313ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-94MS` (url=218ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-109MS` (url=231ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-115MS` (url=247ms, status=HTTP 204)
17. `AKUN-017-UK-GB-DCL-01-20191003-VLESS-WS-121MS` (url=311ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-122MS` (url=229ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-115MS` (url=308ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-129MS` (url=246ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-132MS` (url=226ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-128MS` (url=268ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-129MS` (url=275ms, status=HTTP 204)
24. `AKUN-024-DIXONS-VLESS-WS-122MS` (url=269ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-155MS` (url=235ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
