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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-103MS` (url=302ms, nekobox=297ms, status=yes)
2. `AKUN-002-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-98MS` (url=279ms, nekobox=304ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-112MS` (url=276ms, nekobox=293ms, status=yes)
4. `AKUN-004-ALIBABA-VLESS-WS-120MS` (url=254ms, nekobox=311ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-129MS` (url=304ms, nekobox=300ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-102MS` (url=250ms, nekobox=285ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-103MS` (url=323ms, nekobox=301ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-138MS` (url=315ms, nekobox=292ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-104MS` (url=334ms, nekobox=354ms, status=yes)
10. `AKUN-010-ZOOM-VLESS-WS-130MS` (url=275ms, nekobox=278ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-139MS` (url=312ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-152MS` (url=303ms, status=HTTP 204)
13. `AKUN-013-WPENG-VLESS-WS-129MS` (url=277ms, status=HTTP 204)
14. `AKUN-014-466688-VLESS-WS-112MS` (url=290ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-151MS` (url=255ms, status=HTTP 204)
16. `AKUN-016-WPENG-VLESS-WS-129MS` (url=309ms, status=HTTP 204)
17. `AKUN-017-WEYRO-NET-VLESS-WS-134MS` (url=325ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-259MS` (url=466ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-315MS` (url=607ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-330MS` (url=608ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-327MS` (url=702ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-345MS` (url=678ms, status=HTTP 204)
23. `AKUN-024-SPEEDTEST-VLESS-WS-356MS` (url=691ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-333MS` (url=761ms, status=HTTP 204)
25. `AKUN-026-LT-LRTC-20060503-VLESS-WS-386MS` (url=633ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
