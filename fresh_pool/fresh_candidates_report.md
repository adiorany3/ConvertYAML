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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-78MS` (url=305ms, nekobox=355ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-83MS` (url=315ms, nekobox=396ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-96MS` (url=442ms, nekobox=392ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-99MS` (url=411ms, nekobox=424ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-100MS` (url=304ms, nekobox=372ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-100MS` (url=439ms, nekobox=516ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-87MS` (url=346ms, nekobox=392ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-95MS` (url=401ms, nekobox=365ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-110MS` (url=301ms, nekobox=350ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-111MS` (url=345ms, nekobox=375ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-108MS` (url=381ms, status=HTTP 204)
12. `AKUN-012-MYBB-VLESS-WS-98MS` (url=308ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-95MS` (url=298ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-130MS` (url=323ms, status=HTTP 204)
15. `AKUN-015-MEDIUM-VLESS-WS-88MS` (url=348ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-135MS` (url=317ms, status=HTTP 204)
17. `AKUN-017-VOV-VLESS-WS-130MS` (url=370ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-144MS` (url=416ms, status=HTTP 204)
19. `AKUN-019-VOV-VLESS-WS-178MS` (url=354ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-121MS` (url=326ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-101MS` (url=342ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-98MS` (url=262ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-240MS` (url=535ms, status=HTTP 204)
24. `AKUN-025-US-VLESS-WS-109MS` (url=351ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-95MS` (url=345ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
