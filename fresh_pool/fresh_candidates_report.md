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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-65MS` (url=214ms, nekobox=242ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-58MS` (url=359ms, nekobox=248ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-62MS` (url=217ms, nekobox=267ms, status=yes)
4. `AKUN-004-CZ-LOTUNA-19970206-VLESS-WS-73MS` (url=265ms, nekobox=264ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-75MS` (url=218ms, nekobox=580ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-94MS` (url=202ms, nekobox=232ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-101MS` (url=231ms, nekobox=246ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-101MS` (url=244ms, nekobox=242ms, status=yes)
9. `AKUN-009-WPENG-VLESS-WS-89MS` (url=253ms, nekobox=246ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-116MS` (url=237ms, nekobox=248ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-115MS` (url=235ms, status=HTTP 204)
12. `AKUN-012-466688-VLESS-WS-117MS` (url=233ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-107MS` (url=201ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-106MS` (url=225ms, status=HTTP 204)
15. `AKUN-015-UK-GB-DCL-01-20191003-VLESS-WS-112MS` (url=204ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-115MS` (url=232ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-127MS` (url=224ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-97MS` (url=250ms, status=HTTP 204)
19. `AKUN-019-ZOOM-VLESS-WS-84MS` (url=268ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-97MS` (url=247ms, status=HTTP 204)
21. `AKUN-021-CCWU-VLESS-WS-100MS` (url=227ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-92MS` (url=338ms, status=HTTP 204)
23. `AKUN-023-ZVC-VLESS-WS-145MS` (url=225ms, status=HTTP 204)
24. `AKUN-024-MEDIUM-VLESS-WS-78MS` (url=229ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-357MS` (url=744ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
