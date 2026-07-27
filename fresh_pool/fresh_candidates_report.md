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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-84MS` (url=198ms, nekobox=240ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-89MS` (url=219ms, nekobox=251ms, status=yes)
3. `AKUN-003-ZVC-VLESS-WS-84MS` (url=222ms, nekobox=228ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-93MS` (url=205ms, nekobox=230ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-85MS` (url=218ms, nekobox=263ms, status=yes)
6. `AKUN-006-DEV-VLESS-WS-90MS` (url=224ms, nekobox=238ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-92MS` (url=239ms, nekobox=235ms, status=yes)
8. `AKUN-008-DEV-VLESS-WS-87MS` (url=208ms, nekobox=237ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-95MS` (url=211ms, nekobox=239ms, status=yes)
10. `AKUN-010-008500-VLESS-WS-89MS` (url=220ms, nekobox=230ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-86MS` (url=197ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-92MS` (url=203ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-90MS` (url=199ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-90MS` (url=198ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-98MS` (url=217ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-99MS` (url=246ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-92MS` (url=207ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-88MS` (url=207ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-116MS` (url=249ms, status=HTTP 204)
20. `AKUN-021-ZVC-VLESS-WS-85MS` (url=202ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-98MS` (url=233ms, status=HTTP 204)
22. `AKUN-023-1PASSWORD-VLESS-WS-92MS` (url=210ms, status=HTTP 204)
23. `AKUN-024-SKK-VLESS-WS-124MS` (url=2943ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-153MS` (url=348ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-196MS` (url=279ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
