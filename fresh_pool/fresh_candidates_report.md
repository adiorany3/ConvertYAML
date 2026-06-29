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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-86MS` (url=204ms, nekobox=234ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-98MS` (url=213ms, nekobox=246ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-105MS` (url=241ms, nekobox=264ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-101MS` (url=225ms, nekobox=242ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-106MS` (url=234ms, nekobox=257ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-95MS` (url=206ms, nekobox=236ms, status=yes)
7. `AKUN-007-WEBEX-VLESS-WS-111MS` (url=220ms, nekobox=248ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-117MS` (url=213ms, nekobox=234ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-102MS` (url=215ms, nekobox=245ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-117MS` (url=224ms, nekobox=240ms, status=yes)
11. `AKUN-011-ZOOM-VLESS-WS-127MS` (url=232ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-110MS` (url=254ms, status=HTTP 204)
13. `AKUN-013-COMPREND-NET-VLESS-WS-132MS` (url=220ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-138MS` (url=217ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-121MS` (url=216ms, status=HTTP 204)
16. `AKUN-016-COMPREND-NET-VLESS-WS-135MS` (url=271ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-129MS` (url=214ms, status=HTTP 204)
18. `AKUN-018-COMPREND-NET-VLESS-WS-120MS` (url=240ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-267MS` (url=564ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-372MS` (url=765ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-388MS` (url=872ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-368MS` (url=751ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-397MS` (url=842ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-399MS` (url=818ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-414MS` (url=829ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
