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
1. `AKUN-001-UNKNOWN-VLESS-WS-131MS` (url=254ms, nekobox=305ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-134MS` (url=262ms, nekobox=291ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-138MS` (url=269ms, nekobox=294ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-130MS` (url=260ms, nekobox=301ms, status=yes)
5. `AKUN-005-FMN5-RENTED-NET2-VLESS-WS-141MS` (url=262ms, nekobox=307ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-133MS` (url=250ms, nekobox=221ms, status=no)
7. `AKUN-006-WPENG-VLESS-WS-138MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-131MS` (url=263ms, nekobox=233ms, status=no)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-142MS` (url=242ms, nekobox=232ms, status=no)
10. `AKUN-007-CLOUDFLARE-VLESS-WS-133MS`
11. `AKUN-008-OVH-VLESS-WS-145MS`
12. `AKUN-009-CLOUDFLARE-VLESS-WS-147MS`
13. `AKUN-010-DIGITALOCEAN-VLESS-WS-147MS`
14. `AKUN-014-UNKNOWN-VLESS-WS-148MS` (url=319ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-137MS` (url=263ms, status=HTTP 204)
16. `AKUN-016-ZOOM-VLESS-WS-151MS` (url=280ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-152MS` (url=382ms, status=HTTP 204)
18. `AKUN-018-WPENG-VLESS-WS-166MS` (url=297ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-171MS` (url=276ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-182MS` (url=274ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-145MS` (url=266ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-150MS` (url=279ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-222MS` (url=292ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-312MS` (url=434ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-355MS` (url=676ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
