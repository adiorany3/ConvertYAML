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
1. `AKUN-001-UNKNOWN-VLESS-WS-93MS` (url=231ms, nekobox=276ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-115MS` (url=229ms, nekobox=281ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-100MS` (url=232ms, nekobox=229ms, status=no)
4. `AKUN-003-UNKNOWN-VLESS-WS-117MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-103MS`
6. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-121MS`
7. `AKUN-006-UNKNOWN-VLESS-WS-109MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-132MS`
9. `AKUN-008-ZOOM-VLESS-WS-100MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-143MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-149MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-149MS` (url=239ms, status=HTTP 204)
13. `AKUN-013-PAGES-VLESS-WS-150MS` (url=280ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-152MS` (url=239ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-158MS` (url=223ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-131MS` (url=238ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-158MS` (url=314ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-161MS` (url=251ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-177MS` (url=289ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-144MS` (url=285ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-187MS` (url=406ms, status=HTTP 204)
22. `AKUN-022-WEBEX-VLESS-WS-222MS` (url=299ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-342MS` (url=731ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-346MS` (url=697ms, status=HTTP 204)
25. `AKUN-025-INTERNETWORKS-45-131-210-VLESS-WS-347MS` (url=674ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
