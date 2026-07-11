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
1. `AKUN-001-UNKNOWN-VLESS-WS-86MS` (url=205ms, nekobox=240ms, status=yes)
2. `AKUN-002-OVH-VLESS-WS-88MS` (url=223ms, nekobox=237ms, status=yes)
3. `AKUN-003-090227-VLESS-WS-88MS` (url=206ms, nekobox=234ms, status=yes)
4. `AKUN-004-ZVC-VLESS-WS-91MS` (url=221ms, nekobox=239ms, status=yes)
5. `AKUN-005-090227-VLESS-WS-93MS` (url=205ms, nekobox=235ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-100MS` (url=208ms, nekobox=237ms, status=yes)
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-102MS` (url=208ms, nekobox=263ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-96MS` (url=227ms, nekobox=275ms, status=yes)
9. `AKUN-009-NET-82-21-84-0-24-VLESS-WS-103MS` (url=212ms, nekobox=268ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-97MS` (url=218ms, nekobox=234ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-110MS` (url=215ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-100MS` (url=216ms, status=HTTP 204)
13. `AKUN-013-PUBLICDOMAINREGISTRY-NET-VLESS-WS-120MS` (url=216ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-120MS` (url=208ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-108MS` (url=229ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-130MS` (url=232ms, status=HTTP 204)
17. `AKUN-017-US-VLESS-WS-118MS` (url=262ms, status=HTTP 204)
18. `AKUN-018-466688-VLESS-WS-96MS` (url=239ms, status=HTTP 204)
19. `AKUN-020-466688-VLESS-WS-113MS` (url=220ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-374MS` (url=833ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-377MS` (url=2343ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-397MS` (url=807ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-398MS` (url=847ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-393MS` (url=900ms, status=HTTP 204)
25. `AKUN-026-SPEEDTEST-VLESS-WS-392MS` (url=812ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
