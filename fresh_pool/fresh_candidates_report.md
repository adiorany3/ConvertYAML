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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-61MS` (url=212ms, nekobox=231ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-65MS` (url=202ms, nekobox=7172ms, status=no)
3. `AKUN-002-CLOUDFLARE-VLESS-WS-68MS`
4. `AKUN-003-CLOUDFLARE-VLESS-WS-69MS`
5. `AKUN-004-DEV-VLESS-WS-70MS`
6. `AKUN-005-BIGCOMMERCE-VLESS-WS-76MS`
7. `AKUN-006-UNKNOWN-VLESS-WS-61MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-69MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-74MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-95MS`
11. `AKUN-010-DEV-VLESS-WS-97MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-101MS` (url=209ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-81MS` (url=210ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-71MS` (url=230ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-117MS` (url=202ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-106MS` (url=222ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-110MS` (url=212ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-124MS` (url=202ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-97MS` (url=207ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-102MS` (url=198ms, status=HTTP 204)
21. `AKUN-021-DEV-VLESS-WS-112MS` (url=222ms, status=HTTP 204)
22. `AKUN-022-008500-VLESS-WS-111MS` (url=209ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-68MS` (url=224ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-138MS` (url=236ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-67MS` (url=227ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
