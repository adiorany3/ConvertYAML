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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-78MS` (url=231ms, nekobox=250ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-85MS` (url=232ms, nekobox=234ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-86MS` (url=226ms, nekobox=245ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-86MS` (url=202ms, nekobox=264ms, status=yes)
5. `AKUN-005-DIXONS-VLESS-WS-92MS` (url=213ms, nekobox=256ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-99MS` (url=205ms, nekobox=257ms, status=yes)
7. `AKUN-007-WPENG-VLESS-WS-106MS` (url=223ms, nekobox=233ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-87MS` (url=223ms, nekobox=268ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-99MS` (url=226ms, nekobox=235ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-94MS` (url=261ms, nekobox=251ms, status=yes)
11. `AKUN-011-DIXONS-VLESS-WS-92MS` (url=205ms, status=HTTP 204)
12. `AKUN-012-US-VLESS-WS-106MS` (url=208ms, status=HTTP 204)
13. `AKUN-013-466688-VLESS-WS-106MS` (url=211ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-119MS` (url=240ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-97MS` (url=213ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-121MS` (url=219ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-94MS` (url=221ms, status=HTTP 204)
18. `AKUN-018-POLICE-VLESS-WS-105MS` (url=218ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-125MS` (url=207ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-122MS` (url=217ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-250MS` (url=603ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-268MS` (url=602ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-262MS` (url=552ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-270MS` (url=514ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-270MS` (url=341ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
