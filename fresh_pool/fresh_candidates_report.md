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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-56MS` (url=198ms, nekobox=223ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-59MS` (url=198ms, nekobox=232ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-59MS` (url=204ms, nekobox=222ms, status=yes)
4. `AKUN-004-OVH-VLESS-WS-58MS` (url=201ms, nekobox=222ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-64MS` (url=227ms, nekobox=246ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-61MS` (url=197ms, nekobox=221ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-57MS` (url=207ms, nekobox=236ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-68MS` (url=197ms, nekobox=223ms, status=yes)
9. `AKUN-009-ZVC-VLESS-WS-89MS` (url=204ms, nekobox=230ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-110MS` (url=219ms, nekobox=249ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-71MS` (url=211ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-69MS` (url=210ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-80MS` (url=213ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-114MS` (url=215ms, status=HTTP 204)
15. `AKUN-015-GOOGLE-VLESS-WS-66MS` (url=197ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-59MS` (url=205ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-107MS` (url=203ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-135MS` (url=218ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-215MS` (url=475ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-227MS` (url=475ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-223MS` (url=487ms, status=HTTP 204)
22. `AKUN-023-SUKARIO-VLESS-WS-391MS` (url=652ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-429MS` (url=3977ms, status=HTTP 204)
24. `AKUN-025-SUKARIO-VLESS-WS-400MS` (url=704ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-426MS` (url=684ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
