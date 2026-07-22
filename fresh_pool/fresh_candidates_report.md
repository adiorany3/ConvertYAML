# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 23
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 28

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-131MS` (url=278ms, nekobox=305ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-145MS` (url=277ms, nekobox=302ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-130MS` (url=264ms, nekobox=310ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-144MS` (url=322ms, nekobox=370ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-150MS` (url=272ms, nekobox=297ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-133MS` (url=263ms, nekobox=318ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-162MS` (url=288ms, nekobox=311ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-151MS` (url=287ms, nekobox=307ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-152MS` (url=291ms, nekobox=308ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-167MS` (url=280ms, nekobox=303ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-169MS` (url=311ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-147MS` (url=261ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-201MS` (url=324ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-187MS` (url=367ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-204MS` (url=354ms, status=HTTP 204)
16. `AKUN-016-ZOOM-VLESS-WS-152MS` (url=319ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-213MS` (url=336ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-207MS` (url=376ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-278MS` (url=3210ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-359MS` (url=1120ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-354MS` (url=743ms, status=HTTP 204)
22. `AKUN-026-UNKNOWN-VLESS-WS-704MS` (url=1101ms, status=HTTP 204)
23. `AKUN-027-UNKNOWN-VLESS-WS-690MS` (url=1114ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
