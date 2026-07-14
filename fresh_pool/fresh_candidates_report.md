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
1. `AKUN-001-OVH-VLESS-WS-64MS` (url=213ms, nekobox=227ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-69MS` (url=209ms, nekobox=255ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-71MS` (url=201ms, nekobox=245ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-60MS` (url=210ms, nekobox=232ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-79MS` (url=201ms, nekobox=230ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-71MS` (url=210ms, nekobox=229ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-75MS` (url=218ms, nekobox=254ms, status=yes)
8. `AKUN-008-PAGES-VLESS-WS-89MS` (url=226ms, nekobox=239ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-68MS` (url=212ms, nekobox=241ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-91MS` (url=226ms, nekobox=227ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-105MS` (url=213ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-89MS` (url=235ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-105MS` (url=222ms, status=HTTP 204)
14. `AKUN-014-PUBLICDOMAINREGISTRY-NET-VLESS-WS-126MS` (url=213ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-91MS` (url=228ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-81MS` (url=203ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-76MS` (url=210ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-76MS` (url=208ms, status=HTTP 204)
19. `AKUN-019-DEV-VLESS-WS-196MS` (url=412ms, status=HTTP 204)
20. `AKUN-020-US-VLESS-WS-75MS` (url=231ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-88MS` (url=213ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-193MS` (url=425ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-203MS` (url=276ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-226MS` (url=487ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-246MS` (url=536ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
