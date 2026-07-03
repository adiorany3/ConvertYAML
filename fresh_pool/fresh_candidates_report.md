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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-106MS` (url=282ms, nekobox=268ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-114MS` (url=269ms, nekobox=286ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-115MS` (url=263ms, nekobox=403ms, status=yes)
4. `AKUN-004-WPENG-VLESS-WS-124MS` (url=338ms, nekobox=317ms, status=yes)
5. `AKUN-005-WPENG-VLESS-WS-118MS` (url=290ms, nekobox=322ms, status=yes)
6. `AKUN-006-UK-GB-DCL-01-20191003-VLESS-WS-105MS` (url=315ms, nekobox=316ms, status=yes)
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-129MS` (url=261ms, nekobox=310ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-125MS` (url=291ms, nekobox=288ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-128MS` (url=257ms, nekobox=278ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-135MS` (url=293ms, nekobox=342ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-118MS` (url=294ms, status=HTTP 204)
12. `AKUN-012-OVH-VLESS-WS-138MS` (url=325ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-148MS` (url=289ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-118MS` (url=253ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-123MS` (url=287ms, status=HTTP 204)
16. `AKUN-016-ZOOM-VLESS-WS-145MS` (url=316ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-161MS` (url=292ms, status=HTTP 204)
18. `AKUN-018-WEYRO-NET-VLESS-WS-141MS` (url=303ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-133MS` (url=256ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-298MS` (url=634ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-319MS` (url=651ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-319MS` (url=682ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-311MS` (url=713ms, status=HTTP 204)
24. `AKUN-024-CONFLU-VLESS-WS-304MS` (url=619ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-285MS` (url=641ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
