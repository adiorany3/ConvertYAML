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
1. `AKUN-001-UNKNOWN-VLESS-WS-59MS` (url=3854ms, status=SSLError: HTTPSConnectionPool(host='www.gstatic.com', port=443): Max retries exceeded with url: /generate_204 (Caused by SSLError()
2. `AKUN-002-CLOUDFLARE-VLESS-WS-67MS`
3. `AKUN-003-CLOUDFLARE-VLESS-WS-59MS`
4. `AKUN-004-CLOUDFLARE-VLESS-WS-79MS`
5. `AKUN-005-ZVC-VLESS-WS-73MS`
6. `AKUN-006-CLOUDFLARE-VLESS-WS-59MS`
7. `AKUN-008-CLOUDFLARE-VLESS-WS-79MS` (url=215ms, nekobox=170ms, status=no)
8. `AKUN-007-CLOUDFLARE-VLESS-WS-93MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-96MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-116MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-75MS`
12. `AKUN-013-GOOGLE-VLESS-WS-104MS` (url=210ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-83MS` (url=204ms, status=HTTP 204)
14. `AKUN-015-UNKNOWN-VLESS-WS-108MS` (url=199ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-109MS` (url=198ms, status=HTTP 204)
16. `AKUN-017-ZVC-VLESS-WS-124MS` (url=208ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-154MS` (url=264ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-228MS` (url=4405ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-221MS` (url=491ms, status=HTTP 204)
20. `AKUN-021-SKK-VLESS-WS-285MS` (url=519ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-262MS` (url=2971ms, status=HTTP 204)
22. `AKUN-023-SUKARIO-VLESS-WS-382MS` (url=665ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-424MS` (url=3901ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-502MS` (url=738ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-338MS` (url=1245ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
