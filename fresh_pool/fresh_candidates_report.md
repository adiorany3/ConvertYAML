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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-95MS` (url=214ms, nekobox=245ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-100MS` (url=281ms, nekobox=307ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-103MS` (url=225ms, nekobox=298ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-111MS` (url=250ms, nekobox=257ms, status=yes)
5. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-120MS` (url=218ms, nekobox=263ms, status=yes)
6. `AKUN-006-WPENG-VLESS-WS-126MS` (url=251ms, nekobox=257ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-128MS` (url=263ms, nekobox=245ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-124MS` (url=229ms, nekobox=286ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-141MS` (url=241ms, nekobox=280ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-169MS` (url=279ms, nekobox=383ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-130MS` (url=258ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-119MS` (url=219ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-198MS` (url=280ms, status=HTTP 204)
14. `AKUN-014-ORG-VLESS-WS-147MS` (url=258ms, status=HTTP 204)
15. `AKUN-015-ZVC-VLESS-WS-108MS` (url=220ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-136MS` (url=253ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-254MS` (url=398ms, status=HTTP 204)
18. `AKUN-018-CONFLU-VLESS-WS-371MS` (url=783ms, status=HTTP 204)
19. `AKUN-019-RS-RAPIDSEEDBOX-20190717-VLESS-WS-398MS` (url=895ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-413MS` (url=930ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-746MS` (url=1256ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-771MS` (url=1151ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-387MS` (url=844ms, status=HTTP 204)
24. `AKUN-028-CLOUDFLARE-VLESS-WS-830MS` (url=1277ms, status=HTTP 204)
25. `AKUN-029-CLOUDFLARE-VLESS-WS-872MS` (url=1496ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
