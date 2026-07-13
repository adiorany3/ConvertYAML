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
1. `AKUN-001-OVH-VLESS-WS-77MS` (url=229ms, nekobox=247ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-75MS` (url=225ms, nekobox=260ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-80MS` (url=199ms, nekobox=232ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-89MS` (url=223ms, nekobox=248ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-84MS` (url=226ms, nekobox=240ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-87MS` (url=235ms, nekobox=252ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-85MS` (url=230ms, nekobox=247ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-102MS` (url=234ms, nekobox=235ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-95MS` (url=219ms, nekobox=249ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-112MS` (url=223ms, nekobox=271ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-106MS` (url=215ms, status=HTTP 204)
12. `AKUN-012-1PASSWORD-VLESS-WS-97MS` (url=204ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-109MS` (url=234ms, status=HTTP 204)
14. `AKUN-014-MEDIUM-VLESS-WS-112MS` (url=208ms, status=HTTP 204)
15. `AKUN-015-ADF-VLESS-WS-141MS` (url=199ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-90MS` (url=213ms, status=HTTP 204)
17. `AKUN-017-MYBB-VLESS-WS-93MS` (url=210ms, status=HTTP 204)
18. `AKUN-018-DEV-VLESS-WS-121MS` (url=229ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-82MS` (url=206ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-122MS` (url=234ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-130MS` (url=212ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-117MS` (url=211ms, status=HTTP 204)
23. `AKUN-023-SHOPIFY-VLESS-WS-103MS` (url=218ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-100MS` (url=215ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-240MS` (url=504ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
