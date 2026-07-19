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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-109MS` (url=304ms, nekobox=336ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-105MS` (url=308ms, nekobox=354ms, status=yes)
3. `AKUN-003-ZVC-VLESS-WS-100MS` (url=370ms, nekobox=331ms, status=yes)
4. `AKUN-004-DEV-VLESS-WS-110MS` (url=346ms, nekobox=372ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-114MS` (url=292ms, nekobox=364ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-117MS` (url=350ms, nekobox=335ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-118MS` (url=267ms, nekobox=7175ms, status=no)
8. `AKUN-007-UNKNOWN-VLESS-WS-120MS`
9. `AKUN-008-DEV-VLESS-WS-115MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-112MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-117MS`
12. `AKUN-012-DEV-VLESS-WS-129MS` (url=320ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-145MS` (url=287ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-131MS` (url=304ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-144MS` (url=319ms, status=HTTP 204)
16. `AKUN-016-POLICE-VLESS-WS-136MS` (url=333ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-163MS` (url=361ms, status=HTTP 204)
18. `AKUN-018-UK-GB-DCL-01-20191003-VLESS-WS-157MS` (url=330ms, status=HTTP 204)
19. `AKUN-019-466688-VLESS-WS-144MS` (url=325ms, status=HTTP 204)
20. `AKUN-020-BGP48-HK-VLESS-WS-98MS` (url=379ms, status=HTTP 204)
21. `AKUN-021-UK-GB-DCL-01-20191003-VLESS-WS-170MS` (url=312ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-127MS` (url=365ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-200MS` (url=486ms, status=HTTP 204)
24. `AKUN-024-ES-FORNEX-20160629-VLESS-WS-176MS` (url=307ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-141MS` (url=376ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
