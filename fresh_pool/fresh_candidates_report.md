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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-57MS` (url=210ms, nekobox=241ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-58MS` (url=212ms, nekobox=240ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-56MS` (url=211ms, nekobox=237ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-59MS` (url=233ms, nekobox=255ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-60MS` (url=218ms, nekobox=260ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-57MS` (url=234ms, nekobox=238ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-62MS` (url=231ms, nekobox=250ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-64MS` (url=214ms, nekobox=250ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-56MS` (url=214ms, nekobox=248ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-59MS` (url=211ms, nekobox=243ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-62MS` (url=223ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-78MS` (url=431ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-67MS` (url=217ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-64MS` (url=224ms, status=HTTP 204)
15. `AKUN-015-ZVC-VLESS-WS-72MS` (url=199ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-83MS` (url=217ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-106MS` (url=341ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-66MS` (url=227ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-109MS` (url=290ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-159MS` (url=224ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-346MS` (url=721ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-349MS` (url=810ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-344MS` (url=734ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-413MS` (url=914ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-417MS` (url=876ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
