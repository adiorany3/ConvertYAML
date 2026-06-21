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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-80MS` (url=219ms, nekobox=256ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-87MS` (url=199ms, nekobox=193ms, status=no)
3. `AKUN-002-GO-DADDY-COM-LLC-VLESS-WS-81MS`
4. `AKUN-003-CLOUDFLARE-VLESS-WS-91MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-85MS`
6. `AKUN-006-CLOUDFLARE-VLESS-WS-91MS` (url=208ms, nekobox=203ms, status=no)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-86MS` (url=207ms, nekobox=200ms, status=no)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-90MS` (url=199ms, nekobox=192ms, status=no)
9. `AKUN-005-CLOUDFLARE-VLESS-WS-89MS`
10. `AKUN-010-DEV-VLESS-WS-101MS` (url=227ms, nekobox=188ms, status=no)
11. `AKUN-006-CLOUDFLARE-VLESS-WS-97MS`
12. `AKUN-007-CLOUDFLARE-VLESS-WS-133MS`
13. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-115MS`
14. `AKUN-009-CLOUDFLARE-VLESS-WS-112MS`
15. `AKUN-010-CLOUDFLARE-VLESS-WS-122MS`
16. `AKUN-016-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-89MS` (url=223ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-239MS` (url=520ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-279MS` (url=570ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-266MS` (url=515ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-269MS` (url=575ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-292MS` (url=609ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-259MS` (url=568ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-286MS` (url=567ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-435MS` (url=803ms, status=HTTP 204)
25. `AKUN-031-UNKNOWN-VLESS-WS-468MS` (url=564ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
