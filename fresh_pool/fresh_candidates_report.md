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
1. `AKUN-001-104-253-175-0-1-VLESS-WS-129MS` (url=260ms, nekobox=281ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-133MS` (url=257ms, nekobox=303ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-138MS` (url=269ms, nekobox=301ms, status=yes)
4. `AKUN-004-DIGITALOCEAN-VLESS-WS-143MS` (url=250ms, nekobox=294ms, status=yes)
5. `AKUN-005-SPACECORE-VLESS-WS-145MS` (url=255ms, nekobox=295ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-137MS` (url=271ms, nekobox=293ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-143MS` (url=246ms, nekobox=289ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-149MS` (url=246ms, nekobox=299ms, status=yes)
9. `AKUN-009-NETCUP-VLESS-WS-140MS` (url=245ms, nekobox=304ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-133MS` (url=258ms, nekobox=289ms, status=yes)
11. `AKUN-011-COMPREND-NET-VLESS-WS-146MS` (url=244ms, status=HTTP 204)
12. `AKUN-012-U1HOST-FRA-VLESS-WS-150MS` (url=259ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-131MS` (url=247ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-149MS` (url=274ms, status=HTTP 204)
15. `AKUN-015-MEDIUM-VLESS-WS-141MS` (url=259ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-146MS` (url=318ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-159MS` (url=320ms, status=HTTP 204)
18. `AKUN-018-COMPREND-NET-VLESS-WS-144MS` (url=256ms, status=HTTP 204)
19. `AKUN-019-ADF-VLESS-WS-156MS` (url=247ms, status=HTTP 204)
20. `AKUN-020-ZOOM-VLESS-WS-212MS` (url=305ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-145MS` (url=298ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-352MS` (url=672ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-368MS` (url=697ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-346MS` (url=685ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-385MS` (url=1306ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
