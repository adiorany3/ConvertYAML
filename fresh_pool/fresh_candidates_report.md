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
1. `AKUN-001-ORACLE-VLESS-WS-74MS` (url=219ms, nekobox=244ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-81MS` (url=223ms, nekobox=255ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-79MS` (url=226ms, nekobox=259ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-82MS` (url=232ms, nekobox=244ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-84MS` (url=226ms, nekobox=259ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-81MS` (url=225ms, nekobox=260ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-82MS` (url=223ms, nekobox=247ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-83MS` (url=199ms, nekobox=255ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-85MS` (url=230ms, nekobox=251ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-82MS` (url=230ms, nekobox=240ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-88MS` (url=229ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-120MS` (url=231ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-82MS` (url=202ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-98MS` (url=291ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-112MS` (url=208ms, status=HTTP 204)
16. `AKUN-016-CCWU-VLESS-WS-88MS` (url=226ms, status=HTTP 204)
17. `AKUN-017-ZVC-VLESS-WS-101MS` (url=260ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-135MS` (url=285ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-92MS` (url=229ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-153MS` (url=280ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-141MS` (url=239ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-241MS` (url=495ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-241MS` (url=514ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-141MS` (url=255ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-262MS` (url=506ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
