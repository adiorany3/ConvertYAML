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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-58MS` (url=208ms, nekobox=238ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-61MS` (url=210ms, nekobox=225ms, status=yes)
3. `AKUN-003-ORACLE-VLESS-WS-63MS` (url=203ms, nekobox=228ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-71MS` (url=199ms, nekobox=226ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-69MS` (url=207ms, nekobox=231ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-70MS` (url=201ms, nekobox=227ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-65MS` (url=227ms, nekobox=248ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-66MS` (url=207ms, nekobox=235ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-91MS` (url=231ms, nekobox=237ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-79MS` (url=195ms, nekobox=233ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-68MS` (url=217ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-80MS` (url=208ms, status=HTTP 204)
13. `AKUN-013-ES-FORNEX-20160629-VLESS-WS-95MS` (url=205ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-93MS` (url=222ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-90MS` (url=225ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-99MS` (url=212ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-103MS` (url=221ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-110MS` (url=225ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-116MS` (url=216ms, status=HTTP 204)
20. `AKUN-020-PAGES-VLESS-WS-129MS` (url=215ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-122MS` (url=227ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-75MS` (url=219ms, status=HTTP 204)
23. `AKUN-023-WEBEX-VLESS-WS-81MS` (url=208ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-128MS` (url=225ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-221MS` (url=506ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
