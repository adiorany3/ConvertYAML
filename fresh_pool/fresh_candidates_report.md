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
1. `AKUN-001-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-65MS` (url=215ms, nekobox=257ms, status=yes)
2. `AKUN-002-WPENG-VLESS-WS-74MS` (url=217ms, nekobox=249ms, status=yes)
3. `AKUN-003-UK-GB-DCL-01-20191003-VLESS-WS-65MS` (url=218ms, nekobox=262ms, status=yes)
4. `AKUN-004-COMPREND-NET-VLESS-WS-79MS` (url=227ms, nekobox=244ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-92MS` (url=230ms, nekobox=235ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-83MS` (url=215ms, nekobox=245ms, status=yes)
7. `AKUN-007-ZVC-VLESS-WS-65MS` (url=200ms, nekobox=233ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-99MS` (url=229ms, nekobox=235ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-93MS` (url=225ms, nekobox=266ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-82MS` (url=215ms, nekobox=245ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-91MS` (url=229ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-115MS` (url=257ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-89MS` (url=259ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-106MS` (url=221ms, status=HTTP 204)
15. `AKUN-015-COMPREND-NET-VLESS-WS-87MS` (url=211ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-91MS` (url=219ms, status=HTTP 204)
17. `AKUN-017-PAGES-VLESS-WS-118MS` (url=215ms, status=HTTP 204)
18. `AKUN-018-COMPREND-NET-VLESS-WS-109MS` (url=228ms, status=HTTP 204)
19. `AKUN-019-COMPREND-NET-VLESS-WS-92MS` (url=214ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-148MS` (url=231ms, status=HTTP 204)
21. `AKUN-021-COMPREND-NET-VLESS-WS-125MS` (url=267ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-243MS` (url=504ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-250MS` (url=591ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-263MS` (url=586ms, status=HTTP 204)
25. `AKUN-026-WPENG-VLESS-WS-263MS` (url=543ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
