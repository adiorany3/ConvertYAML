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
1. `AKUN-001-UNKNOWN-VLESS-WS-89MS` (url=234ms, nekobox=228ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-95MS` (url=206ms, nekobox=259ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-87MS` (url=219ms, nekobox=236ms, status=yes)
4. `AKUN-004-COMPREND-NET-VLESS-WS-114MS` (url=235ms, nekobox=236ms, status=yes)
5. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-119MS` (url=205ms, nekobox=236ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-136MS` (url=226ms, nekobox=264ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-97MS` (url=238ms, nekobox=240ms, status=yes)
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-123MS` (url=207ms, nekobox=238ms, status=yes)
9. `AKUN-009-DE-XTOM-20210903-VLESS-WS-126MS` (url=220ms, nekobox=232ms, status=yes)
10. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-126MS` (url=214ms, nekobox=251ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-149MS` (url=222ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-130MS` (url=221ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-99MS` (url=233ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-154MS` (url=215ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-101MS` (url=220ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-371MS` (url=746ms, status=HTTP 204)
17. `AKUN-019-UNKNOWN-VLESS-WS-374MS` (url=839ms, status=HTTP 204)
18. `AKUN-020-UNKNOWN-VLESS-WS-388MS` (url=834ms, status=HTTP 204)
19. `AKUN-021-SPEEDTEST-VLESS-WS-373MS` (url=770ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-400MS` (url=833ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-371MS` (url=615ms, status=HTTP 204)
22. `AKUN-024-UNKNOWN-VLESS-WS-417MS` (url=851ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-411MS` (url=849ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-419MS` (url=865ms, status=HTTP 204)
25. `AKUN-027-UNKNOWN-VLESS-WS-102MS` (url=224ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
