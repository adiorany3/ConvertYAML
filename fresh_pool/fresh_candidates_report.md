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
1. `AKUN-001-WPENG-VLESS-WS-90MS` (url=222ms, nekobox=239ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-86MS` (url=219ms, nekobox=257ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-102MS` (url=241ms, nekobox=285ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-110MS` (url=227ms, nekobox=221ms, status=no)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-111MS` (url=230ms, nekobox=223ms, status=no)
6. `AKUN-004-CLOUDFLARE-VLESS-WS-112MS`
7. `AKUN-005-CLOUDFLARE-VLESS-WS-104MS`
8. `AKUN-006-466688-VLESS-WS-94MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-121MS` (url=233ms, nekobox=199ms, status=no)
10. `AKUN-007-CLOUDFLARE-VLESS-WS-104MS` (url=230ms, nekobox=308ms, status=yes)
11. `AKUN-008-UNKNOWN-VLESS-WS-136MS`
12. `AKUN-009-DEV-VLESS-WS-108MS`
13. `AKUN-013-DEV-VLESS-WS-113MS` (url=226ms, nekobox=203ms, status=no)
14. `AKUN-010-CLOUDFLARE-VLESS-WS-145MS`
15. `AKUN-015-CLOUDFLARE-VLESS-WS-99MS` (url=216ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-147MS` (url=373ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-113MS` (url=246ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-101MS` (url=215ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-167MS` (url=472ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-101MS` (url=247ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-108MS` (url=227ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-109MS` (url=229ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-103MS` (url=226ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-107MS` (url=216ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-131MS` (url=213ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
