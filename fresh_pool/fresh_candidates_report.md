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
1. `AKUN-001-UNKNOWN-VLESS-WS-80MS` (url=204ms, nekobox=247ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-87MS` (url=197ms, nekobox=251ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-79MS` (url=234ms, nekobox=231ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-95MS` (url=228ms, nekobox=258ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-74MS` (url=221ms, nekobox=254ms, status=yes)
6. `AKUN-006-BGP48-HK-VLESS-WS-91MS` (url=249ms, nekobox=268ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-95MS` (url=232ms, nekobox=263ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-101MS` (url=203ms, nekobox=256ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-94MS` (url=231ms, nekobox=250ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-99MS` (url=197ms, nekobox=236ms, status=yes)
11. `AKUN-011-US-VLESS-WS-89MS` (url=242ms, status=HTTP 204)
12. `AKUN-012-BGP48-HK-VLESS-WS-102MS` (url=208ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-125MS` (url=231ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-113MS` (url=229ms, status=HTTP 204)
15. `AKUN-015-DIXONS-VLESS-WS-93MS` (url=210ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-85MS` (url=199ms, status=HTTP 204)
17. `AKUN-017-ZVC-VLESS-WS-101MS` (url=229ms, status=HTTP 204)
18. `AKUN-018-466688-VLESS-WS-128MS` (url=229ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-103MS` (url=231ms, status=HTTP 204)
20. `AKUN-020-466688-VLESS-WS-150MS` (url=231ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-123MS` (url=240ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-174MS` (url=297ms, status=HTTP 204)
23. `AKUN-023-BGP48-HK-VLESS-WS-114MS` (url=213ms, status=HTTP 204)
24. `AKUN-024-WEBEX-VLESS-WS-106MS` (url=207ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-388MS` (url=824ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
