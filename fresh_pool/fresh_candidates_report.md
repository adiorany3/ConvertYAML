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
1. `AKUN-001-ALIBABA-VLESS-WS-123MS` (url=296ms, nekobox=305ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-113MS` (url=353ms, nekobox=331ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-137MS` (url=311ms, nekobox=296ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-127MS` (url=298ms, nekobox=304ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-127MS` (url=324ms, nekobox=317ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-139MS` (url=274ms, nekobox=333ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-127MS` (url=300ms, nekobox=338ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-123MS` (url=278ms, nekobox=286ms, status=yes)
9. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-140MS` (url=287ms, nekobox=319ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-114MS` (url=286ms, nekobox=350ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-120MS` (url=312ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-143MS` (url=331ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-136MS` (url=282ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-140MS` (url=326ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-137MS` (url=321ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-142MS` (url=292ms, status=HTTP 204)
17. `AKUN-017-RS-RAPIDSEEDBOX-20190717-VLESS-WS-154MS` (url=267ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-135MS` (url=286ms, status=HTTP 204)
19. `AKUN-019-ZOOM-VLESS-WS-141MS` (url=379ms, status=HTTP 204)
20. `AKUN-020-DIGITALOCEAN-VLESS-WS-162MS` (url=310ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-195MS` (url=341ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-306MS` (url=3829ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-328MS` (url=695ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-319MS` (url=669ms, status=HTTP 204)
25. `AKUN-025-SPEEDTEST-VLESS-WS-350MS` (url=742ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
