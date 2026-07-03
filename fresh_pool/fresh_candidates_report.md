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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-104MS` (url=326ms, nekobox=300ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-122MS` (url=262ms, nekobox=338ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-122MS` (url=286ms, nekobox=304ms, status=yes)
4. `AKUN-004-DEV-VLESS-WS-125MS` (url=280ms, nekobox=312ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-123MS` (url=276ms, nekobox=287ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-126MS` (url=293ms, nekobox=316ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-137MS` (url=297ms, nekobox=339ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-116MS` (url=289ms, nekobox=292ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-98MS` (url=274ms, nekobox=211ms, status=no)
10. `AKUN-009-ALIBABA-VLESS-WS-127MS`
11. `AKUN-011-NODEJS-VLESS-WS-102MS` (url=264ms, nekobox=217ms, status=no)
12. `AKUN-010-CLOUDFLARE-VLESS-WS-100MS`
13. `AKUN-013-WEYRO-NET-VLESS-WS-170MS` (url=332ms, status=HTTP 204)
14. `AKUN-014-WPENG-VLESS-WS-112MS` (url=299ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-128MS` (url=326ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-127MS` (url=266ms, status=HTTP 204)
17. `AKUN-017-MYBB-VLESS-WS-126MS` (url=253ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-278MS` (url=472ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-340MS` (url=668ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-296MS` (url=710ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-341MS` (url=694ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-351MS` (url=664ms, status=HTTP 204)
23. `AKUN-024-WPENG-VLESS-WS-333MS` (url=650ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-446MS` (url=660ms, status=HTTP 204)
25. `AKUN-027-ADF-VLESS-WS-110MS` (url=280ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
