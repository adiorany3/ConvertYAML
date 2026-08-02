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
- Proxy di openclash_fresh_pool.yaml: 27

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-82MS` (url=217ms, nekobox=245ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-93MS` (url=221ms, nekobox=236ms, status=yes)
3. `AKUN-003-OVH-VLESS-WS-92MS` (url=243ms, nekobox=239ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-95MS` (url=229ms, nekobox=247ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-80MS` (url=206ms, nekobox=239ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-97MS` (url=223ms, nekobox=255ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-85MS` (url=227ms, nekobox=234ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-105MS` (url=234ms, nekobox=255ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-90MS` (url=198ms, nekobox=227ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-103MS` (url=199ms, nekobox=248ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-125MS` (url=341ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-125MS` (url=376ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-261MS` (url=540ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-126MS` (url=363ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-154MS` (url=363ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-554MS` (url=1064ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-543MS` (url=1030ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-620MS` (url=1010ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-635MS` (url=1026ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-680MS` (url=1074ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-679MS` (url=1069ms, status=HTTP 204)
22. `AKUN-023-SUKARIO-VLESS-WS-683MS` (url=979ms, status=HTTP 204)
23. `AKUN-032-UNKNOWN-VLESS-WS-817MS` (url=5412ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
