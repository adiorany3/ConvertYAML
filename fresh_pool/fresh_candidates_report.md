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
1. `AKUN-001-OVH-VLESS-WS-69MS` (url=200ms, nekobox=233ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-63MS` (url=211ms, nekobox=232ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-71MS` (url=209ms, nekobox=242ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-68MS` (url=203ms, nekobox=235ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-87MS` (url=213ms, nekobox=254ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-80MS` (url=235ms, nekobox=264ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-94MS` (url=232ms, nekobox=235ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-80MS` (url=230ms, nekobox=240ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-89MS` (url=214ms, nekobox=254ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-105MS` (url=218ms, nekobox=249ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-106MS` (url=213ms, status=HTTP 204)
12. `AKUN-012-UDACITY-VLESS-WS-98MS` (url=228ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-76MS` (url=223ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-136MS` (url=207ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-142MS` (url=210ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-121MS` (url=229ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-101MS` (url=210ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-136MS` (url=221ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-239MS` (url=570ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-242MS` (url=500ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-250MS` (url=570ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-245MS` (url=689ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-240MS` (url=519ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-300MS` (url=417ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-288MS` (url=2619ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
