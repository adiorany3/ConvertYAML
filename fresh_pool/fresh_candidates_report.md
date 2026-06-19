# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 21
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
1. `AKUN-001-UNKNOWN-VLESS-WS-73MS` (url=228ms, nekobox=258ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-73MS` (url=227ms, nekobox=249ms, status=yes)
3. `AKUN-003-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-81MS` (url=203ms, nekobox=242ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-97MS` (url=201ms, nekobox=232ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-89MS` (url=199ms, nekobox=257ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-92MS` (url=219ms, nekobox=247ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-89MS` (url=202ms, nekobox=269ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-101MS` (url=220ms, nekobox=272ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-111MS` (url=232ms, nekobox=249ms, status=yes)
10. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-260MS` (url=590ms, nekobox=580ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-153MS` (url=225ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-267MS` (url=630ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-208MS` (url=2438ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-266MS` (url=545ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-283MS` (url=555ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-244MS` (url=490ms, status=HTTP 204)
17. `AKUN-020-CLOUDFLARE-VLESS-WS-408MS` (url=624ms, status=HTTP 204)
18. `AKUN-021-CLOUDFLARE-VLESS-WS-411MS` (url=602ms, status=HTTP 204)
19. `AKUN-024-CLOUDFLARE-VLESS-WS-437MS` (url=469ms, status=HTTP 204)
20. `AKUN-028-CLOUDFLARE-VLESS-WS-453MS` (url=634ms, status=HTTP 204)
21. `AKUN-033-RS-RAPIDSEEDBOX-20190717-VLESS-WS-488MS` (url=1760ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
