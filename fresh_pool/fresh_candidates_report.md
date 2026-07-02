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
1. `AKUN-001-UNKNOWN-VLESS-WS-83MS` (url=203ms, nekobox=259ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-86MS` (url=229ms, nekobox=239ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-83MS` (url=203ms, nekobox=233ms, status=yes)
4. `AKUN-004-WPENG-VLESS-WS-80MS` (url=214ms, nekobox=230ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-88MS` (url=210ms, nekobox=234ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-80MS` (url=235ms, nekobox=235ms, status=yes)
7. `AKUN-007-ZOOM-VLESS-WS-89MS` (url=200ms, nekobox=251ms, status=yes)
8. `AKUN-008-COMPREND-NET-VLESS-WS-102MS` (url=233ms, nekobox=275ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-106MS` (url=227ms, nekobox=249ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-79MS` (url=211ms, nekobox=247ms, status=yes)
11. `AKUN-011-COMPREND-NET-VLESS-WS-108MS` (url=214ms, status=HTTP 204)
12. `AKUN-012-WEYRO-NET-VLESS-WS-114MS` (url=268ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-101MS` (url=219ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-105MS` (url=212ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-97MS` (url=249ms, status=HTTP 204)
16. `AKUN-016-COMPREND-NET-VLESS-WS-86MS` (url=233ms, status=HTTP 204)
17. `AKUN-017-COMPREND-NET-VLESS-WS-89MS` (url=231ms, status=HTTP 204)
18. `AKUN-018-COMPREND-NET-VLESS-WS-116MS` (url=222ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-239MS` (url=513ms, status=HTTP 204)
20. `AKUN-022-WPENG-VLESS-WS-269MS` (url=563ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-277MS` (url=580ms, status=HTTP 204)
22. `AKUN-024-UNKNOWN-VLESS-WS-278MS` (url=565ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-255MS` (url=511ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-268MS` (url=593ms, status=HTTP 204)
25. `AKUN-027-UNKNOWN-VLESS-WS-122MS` (url=482ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
