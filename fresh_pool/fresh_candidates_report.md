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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-58MS` (url=201ms, nekobox=245ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-78MS` (url=228ms, nekobox=178ms, status=no)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-73MS` (url=205ms, nekobox=183ms, status=no)
4. `AKUN-002-CLOUDFLARE-VLESS-WS-77MS`
5. `AKUN-003-ES-FORNEX-20160629-VLESS-WS-83MS`
6. `AKUN-004-CLOUDFLARE-VLESS-WS-88MS`
7. `AKUN-005-ZVC-VLESS-WS-65MS`
8. `AKUN-006-OVH-VLESS-WS-85MS`
9. `AKUN-007-UNKNOWN-VLESS-WS-117MS`
10. `AKUN-008-CLOUDFLARE-VLESS-WS-120MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-131MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-143MS`
13. `AKUN-013-UNKNOWN-VLESS-WS-115MS` (url=201ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-131MS` (url=226ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-233MS` (url=517ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-239MS` (url=493ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-260MS` (url=484ms, status=HTTP 204)
18. `AKUN-020-UNKNOWN-VLESS-WS-267MS` (url=539ms, status=HTTP 204)
19. `AKUN-021-UNKNOWN-VLESS-WS-256MS` (url=562ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-255MS` (url=356ms, status=HTTP 204)
21. `AKUN-026-CLOUDFLARE-VLESS-WS-447MS` (url=767ms, status=HTTP 204)
22. `AKUN-027-UNKNOWN-VLESS-WS-548MS` (url=940ms, status=HTTP 204)
23. `AKUN-029-UNKNOWN-VLESS-WS-286MS` (url=3966ms, status=HTTP 204)
24. `AKUN-030-UNKNOWN-VLESS-WS-167MS` (url=497ms, status=HTTP 204)
25. `AKUN-031-DEV-VLESS-WS-890MS` (url=789ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
