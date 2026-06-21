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
1. `AKUN-001-UNKNOWN-VLESS-WS-82MS` (url=226ms, nekobox=235ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-76MS` (url=229ms, nekobox=241ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-81MS` (url=224ms, nekobox=231ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-97MS` (url=214ms, nekobox=255ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-104MS` (url=208ms, nekobox=190ms, status=no)
6. `AKUN-005-CLOUDFLARE-VLESS-WS-97MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-90MS`
8. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-95MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-118MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-103MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-148MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-184MS` (url=227ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-157MS` (url=205ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-263MS` (url=563ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-267MS` (url=559ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-264MS` (url=593ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-284MS` (url=511ms, status=HTTP 204)
18. `AKUN-023-UNKNOWN-VLESS-WS-90MS` (url=225ms, status=HTTP 204)
19. `AKUN-025-UNKNOWN-VLESS-WS-286MS` (url=605ms, status=HTTP 204)
20. `AKUN-027-CLOUDFLARE-VLESS-WS-243MS` (url=563ms, status=HTTP 204)
21. `AKUN-029-UNKNOWN-VLESS-WS-245MS` (url=517ms, status=HTTP 204)
22. `AKUN-030-DEV-VLESS-WS-650MS` (url=820ms, status=HTTP 204)
23. `AKUN-032-UNKNOWN-VLESS-WS-471MS` (url=568ms, status=HTTP 204)
24. `AKUN-033-UNKNOWN-VLESS-WS-519MS` (url=822ms, status=HTTP 204)
25. `AKUN-034-UNKNOWN-VLESS-WS-594MS` (url=953ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
