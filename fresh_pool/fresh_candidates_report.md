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
1. `AKUN-001-UNKNOWN-VLESS-WS-80MS` (url=240ms, nekobox=258ms, status=yes)
2. `AKUN-002-NODEJS-VLESS-WS-74MS` (url=247ms, nekobox=187ms, status=no)
3. `AKUN-002-CLOUDFLARE-VLESS-WS-82MS`
4. `AKUN-003-CLOUDFLARE-VLESS-WS-92MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-90MS`
6. `AKUN-005-WEYRO-NET-VLESS-WS-79MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-89MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-96MS`
9. `AKUN-008-COMPREND-NET-VLESS-WS-109MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-96MS`
11. `AKUN-010-UK-GB-DCL-01-20191003-VLESS-WS-110MS`
12. `AKUN-012-COMPREND-NET-VLESS-WS-115MS` (url=234ms, status=HTTP 204)
13. `AKUN-013-COMPREND-NET-VLESS-WS-93MS` (url=251ms, status=HTTP 204)
14. `AKUN-014-COMPREND-NET-VLESS-WS-124MS` (url=249ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-95MS` (url=280ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-77MS` (url=252ms, status=HTTP 204)
17. `AKUN-017-ZOOM-VLESS-WS-112MS` (url=234ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-89MS` (url=234ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-117MS` (url=260ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-266MS` (url=561ms, status=HTTP 204)
21. `AKUN-021-SPEEDTEST-VLESS-WS-262MS` (url=573ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-279MS` (url=547ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-294MS` (url=648ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-302MS` (url=635ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-300MS` (url=614ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
