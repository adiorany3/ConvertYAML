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
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-89MS` (url=210ms, nekobox=193ms, status=no)
2. `AKUN-001-CLOUDFLARE-VLESS-WS-94MS`
3. `AKUN-002-CLOUDFLARE-VLESS-WS-94MS` (url=218ms, nekobox=262ms, status=yes)
4. `AKUN-003-SC-APHRODITEGROUP-201910-VLESS-WS-98MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-110MS`
6. `AKUN-007-CLOUDFLARE-VLESS-WS-96MS` (url=216ms, nekobox=219ms, status=no)
7. `AKUN-008-SPEEDTEST-VLESS-WS-91MS` (url=249ms, nekobox=218ms, status=no)
8. `AKUN-005-UNKNOWN-VLESS-WS-116MS`
9. `AKUN-006-DEV-VLESS-WS-101MS`
10. `AKUN-007-CLOUDFLARE-VLESS-WS-104MS`
11. `AKUN-008-UNKNOWN-VLESS-WS-104MS`
12. `AKUN-009-UNKNOWN-VLESS-WS-116MS` (url=215ms, nekobox=262ms, status=yes)
13. `AKUN-010-008500-VLESS-WS-108MS`
14. `AKUN-015-UNKNOWN-VLESS-WS-148MS` (url=282ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-107MS` (url=214ms, status=HTTP 204)
16. `AKUN-017-FMN5-RENTED-NET2-VLESS-WS-108MS` (url=211ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-127MS` (url=237ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-179MS` (url=253ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-124MS` (url=223ms, status=HTTP 204)
20. `AKUN-021-SPEEDTEST-VLESS-WS-105MS` (url=206ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-130MS` (url=246ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-131MS` (url=233ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-109MS` (url=217ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-316MS` (url=646ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-90MS` (url=239ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
