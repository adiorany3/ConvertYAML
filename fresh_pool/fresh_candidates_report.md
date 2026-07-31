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
1. `AKUN-001-UNKNOWN-VLESS-WS-82MS` (url=288ms, nekobox=362ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-94MS` (url=367ms, nekobox=365ms, status=yes)
3. `AKUN-003-SPEEDTEST-VLESS-WS-94MS` (url=304ms, nekobox=194ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-100MS`
5. `AKUN-004-UNKNOWN-VLESS-WS-103MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-112MS`
7. `AKUN-007-SPEEDTEST-VLESS-WS-115MS` (url=327ms, nekobox=184ms, status=no)
8. `AKUN-006-008500-VLESS-WS-108MS`
9. `AKUN-007-UNKNOWN-VLESS-WS-109MS`
10. `AKUN-008-CLOUDFLARE-VLESS-WS-95MS`
11. `AKUN-009-PAGES-VLESS-WS-123MS`
12. `AKUN-010-BIGCOMMERCE-VLESS-WS-89MS`
13. `AKUN-014-CLOUDFLARE-VLESS-WS-86MS` (url=392ms, status=HTTP 204)
14. `AKUN-015-DEV-VLESS-WS-135MS` (url=354ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-118MS` (url=338ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-183MS` (url=382ms, status=HTTP 204)
17. `AKUN-018-MEDIUM-VLESS-WS-126MS` (url=353ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-113MS` (url=262ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-84MS` (url=317ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-304MS` (url=627ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-314MS` (url=649ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-86MS` (url=308ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-405MS` (url=710ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-87MS` (url=637ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-394MS` (url=899ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
