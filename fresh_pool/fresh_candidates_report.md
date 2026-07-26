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
1. `AKUN-001-UNKNOWN-VLESS-WS-84MS` (url=211ms, nekobox=266ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-85MS` (url=207ms, nekobox=233ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-90MS` (url=223ms, nekobox=324ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-93MS` (url=216ms, nekobox=235ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-88MS` (url=215ms, nekobox=267ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-94MS` (url=271ms, nekobox=7178ms, status=no)
7. `AKUN-006-CLOUDFLARE-VLESS-WS-90MS`
8. `AKUN-007-DEV-VLESS-WS-93MS`
9. `AKUN-008-DEV-VLESS-WS-96MS`
10. `AKUN-009-UNKNOWN-VLESS-WS-95MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-96MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-88MS` (url=235ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-101MS` (url=221ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-101MS` (url=237ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-96MS` (url=319ms, status=HTTP 204)
16. `AKUN-016-CCWU-VLESS-WS-112MS` (url=236ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-99MS` (url=233ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-93MS` (url=274ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-132MS` (url=425ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-100MS` (url=303ms, status=HTTP 204)
21. `AKUN-021-INTERNETWORKS-45-131-210-VLESS-WS-364MS` (url=748ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-376MS` (url=886ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-376MS` (url=3488ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-384MS` (url=728ms, status=HTTP 204)
25. `AKUN-025-ZOOM-VLESS-WS-89MS` (url=215ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
