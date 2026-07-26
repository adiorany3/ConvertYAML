# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 22
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 26

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-55MS` (url=217ms, nekobox=240ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-61MS` (url=223ms, nekobox=274ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-68MS` (url=213ms, nekobox=239ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-63MS` (url=211ms, nekobox=262ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-60MS` (url=215ms, nekobox=237ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-57MS` (url=230ms, nekobox=237ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-64MS` (url=215ms, nekobox=237ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-98MS` (url=315ms, nekobox=236ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-118MS` (url=848ms, nekobox=608ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-144MS`
11. `AKUN-013-CLOUDFLARE-VLESS-WS-82MS` (url=223ms, status=HTTP 204)
12. `AKUN-014-CLOUDFLARE-VLESS-WS-80MS` (url=190ms, status=HTTP 204)
13. `AKUN-015-ZVC-VLESS-WS-70MS` (url=217ms, status=HTTP 204)
14. `AKUN-016-CLOUDFLARE-VLESS-WS-350MS` (url=6094ms, status=HTTP 204)
15. `AKUN-017-CLOUDFLARE-VLESS-WS-368MS` (url=905ms, status=HTTP 204)
16. `AKUN-018-LT-LRTC-20060503-VLESS-WS-350MS` (url=779ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-83MS` (url=231ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-85MS` (url=219ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-339MS` (url=742ms, status=HTTP 204)
20. `AKUN-023-CLOUDFLARE-VLESS-WS-637MS` (url=1115ms, status=HTTP 204)
21. `AKUN-024-CLOUDFLARE-VLESS-WS-646MS` (url=1071ms, status=HTTP 204)
22. `AKUN-025-CLOUDFLARE-VLESS-WS-657MS` (url=1011ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
