# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 24
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 28

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
1. `AKUN-001-UNKNOWN-VLESS-WS-70MS` (url=200ms, nekobox=237ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-73MS` (url=279ms, nekobox=271ms, status=yes)
3. `AKUN-003-ZVC-VLESS-WS-73MS` (url=224ms, nekobox=242ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-92MS` (url=214ms, nekobox=246ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-95MS` (url=225ms, nekobox=264ms, status=yes)
6. `AKUN-006-AXIOMED-VLESS-WS-112MS` (url=207ms, nekobox=238ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-112MS` (url=250ms, nekobox=263ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-128MS` (url=200ms, nekobox=263ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-119MS` (url=228ms, nekobox=251ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-139MS` (url=206ms, nekobox=255ms, status=yes)
11. `AKUN-012-HOSTINGER-VLESS-WS-164MS` (url=222ms, status=HTTP 204)
12. `AKUN-014-CLOUDFLARE-VLESS-WS-105MS` (url=250ms, status=HTTP 204)
13. `AKUN-015-CLOUDFLARE-VLESS-WS-166MS` (url=312ms, status=HTTP 204)
14. `AKUN-016-CLOUDFLARE-VLESS-WS-184MS` (url=322ms, status=HTTP 204)
15. `AKUN-017-CLOUDFLARE-VLESS-WS-215MS` (url=346ms, status=HTTP 204)
16. `AKUN-018-SNAJU-VLESS-WS-229MS` (url=362ms, status=HTTP 204)
17. `AKUN-019-UNKNOWN-VLESS-WS-212MS` (url=436ms, status=HTTP 204)
18. `AKUN-021-UNKNOWN-VLESS-WS-585MS` (url=1307ms, status=HTTP 204)
19. `AKUN-022-FURRYRACCOON-VLESS-WS-650MS` (url=1001ms, status=HTTP 204)
20. `AKUN-023-UMENYATOJEESTPTICH-VLESS-WS-698MS` (url=1172ms, status=HTTP 204)
21. `AKUN-025-FURKBALANCER-VLESS-WS-679MS` (url=1522ms, status=HTTP 204)
22. `AKUN-029-FURRYRACCOON-VLESS-WS-758MS` (url=1119ms, status=HTTP 204)
23. `AKUN-030-UNKNOWN-VLESS-WS-765MS` (url=1265ms, status=HTTP 204)
24. `AKUN-035-DEV-VLESS-WS-867MS` (url=804ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
