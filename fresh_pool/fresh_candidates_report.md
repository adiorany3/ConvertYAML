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
1. `AKUN-001-UNKNOWN-VLESS-WS-95MS` (url=208ms, nekobox=262ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-97MS` (url=212ms, nekobox=262ms, status=yes)
3. `AKUN-003-DEV-VLESS-WS-100MS` (url=225ms, nekobox=242ms, status=yes)
4. `AKUN-004-DEV-VLESS-WS-94MS` (url=211ms, nekobox=265ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-98MS` (url=234ms, nekobox=198ms, status=no)
6. `AKUN-005-CLOUDFLARE-VLESS-WS-93MS`
7. `AKUN-007-CLOUDFLARE-VLESS-WS-103MS` (url=207ms, nekobox=196ms, status=no)
8. `AKUN-006-UNKNOWN-VLESS-WS-105MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-101MS` (url=214ms, nekobox=197ms, status=no)
10. `AKUN-007-UNKNOWN-VLESS-WS-94MS`
11. `AKUN-008-CLOUDFLARE-VLESS-WS-110MS`
12. `AKUN-009-CLOUDFLARE-VLESS-WS-84MS`
13. `AKUN-010-PAGES-VLESS-WS-119MS`
14. `AKUN-014-UNKNOWN-VLESS-WS-102MS` (url=222ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-109MS` (url=214ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-147MS` (url=223ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-98MS` (url=229ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-135MS` (url=234ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-99MS` (url=210ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-91MS` (url=223ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-96MS` (url=220ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-105MS` (url=422ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-93MS` (url=231ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-371MS` (url=769ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-655MS` (url=1073ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
