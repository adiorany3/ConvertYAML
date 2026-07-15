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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-93MS` (url=325ms, nekobox=245ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-93MS` (url=213ms, nekobox=254ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-102MS` (url=213ms, nekobox=250ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-92MS` (url=232ms, nekobox=247ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-97MS` (url=256ms, nekobox=242ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-100MS` (url=236ms, nekobox=270ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-103MS` (url=252ms, nekobox=258ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-105MS` (url=376ms, nekobox=242ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-94MS` (url=238ms, nekobox=248ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-102MS` (url=250ms, nekobox=270ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-109MS` (url=227ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-104MS` (url=235ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-101MS` (url=216ms, status=HTTP 204)
14. `AKUN-014-US-VLESS-WS-134MS` (url=299ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-112MS` (url=242ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-116MS` (url=270ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-162MS` (url=235ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-162MS` (url=332ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-164MS` (url=249ms, status=HTTP 204)
20. `AKUN-020-NEXUSMODS-VLESS-WS-161MS` (url=307ms, status=HTTP 204)
21. `AKUN-021-466688-VLESS-WS-93MS` (url=221ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-150MS` (url=239ms, status=HTTP 204)
23. `AKUN-023-POLICE-VLESS-WS-173MS` (url=315ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-283MS` (url=882ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-391MS` (url=802ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
