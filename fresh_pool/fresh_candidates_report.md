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
1. `AKUN-001-UNKNOWN-VLESS-WS-57MS` (url=200ms, nekobox=224ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-57MS` (url=197ms, nekobox=749ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-60MS` (url=197ms, nekobox=223ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-61MS` (url=198ms, nekobox=533ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-59MS` (url=196ms, nekobox=221ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-61MS` (url=238ms, nekobox=234ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-72MS` (url=219ms, nekobox=227ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-77MS` (url=197ms, nekobox=223ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-82MS` (url=194ms, nekobox=223ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-69MS` (url=210ms, nekobox=240ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-78MS` (url=198ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-81MS` (url=197ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-99MS` (url=196ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-74MS` (url=211ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-93MS` (url=198ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-74MS` (url=207ms, status=HTTP 204)
17. `AKUN-018-DEV-VLESS-WS-119MS` (url=212ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-76MS` (url=200ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-213MS` (url=487ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-215MS` (url=575ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-204MS` (url=650ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-209MS` (url=711ms, status=HTTP 204)
23. `AKUN-024-ZOOM-VLESS-WS-77MS` (url=205ms, status=HTTP 204)
24. `AKUN-025-SUKARIO-VLESS-WS-389MS` (url=671ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-446MS` (url=806ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
