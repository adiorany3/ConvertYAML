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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-75MS` (url=248ms, nekobox=301ms, status=yes)
2. `AKUN-002-DEV-VLESS-WS-79MS` (url=291ms, nekobox=211ms, status=no)
3. `AKUN-002-UNKNOWN-VLESS-WS-83MS`
4. `AKUN-004-CLOUDFLARE-VLESS-WS-94MS` (url=269ms, nekobox=224ms, status=no)
5. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-73MS`
6. `AKUN-007-CLOUDFLARE-VLESS-WS-78MS` (url=245ms, nekobox=212ms, status=no)
7. `AKUN-008-CLOUDFLARE-VLESS-WS-72MS` (url=262ms, nekobox=204ms, status=no)
8. `AKUN-009-CLOUDFLARE-VLESS-WS-93MS` (url=275ms, nekobox=213ms, status=no)
9. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-102MS`
10. `AKUN-011-CLOUDFLARE-VLESS-WS-110MS` (url=260ms, nekobox=196ms, status=no)
11. `AKUN-012-UNKNOWN-VLESS-WS-101MS` (url=263ms, nekobox=204ms, status=no)
12. `AKUN-005-CLOUDFLARE-VLESS-WS-118MS`
13. `AKUN-014-CLOUDFLARE-VLESS-WS-79MS` (url=257ms, nekobox=188ms, status=no)
14. `AKUN-015-DEV-VLESS-WS-112MS` (url=264ms, nekobox=191ms, status=no)
15. `AKUN-006-CLOUDFLARE-VLESS-WS-87MS`
16. `AKUN-007-CLOUDFLARE-VLESS-WS-138MS`
17. `AKUN-018-CLOUDFLARE-VLESS-WS-98MS` (url=238ms, nekobox=201ms, status=no)
18. `AKUN-008-CLOUDFLARE-VLESS-WS-81MS`
19. `AKUN-009-CLOUDFLARE-VLESS-WS-173MS`
20. `AKUN-010-KAWAII520-VLESS-WS-183MS`
21. `AKUN-022-CLOUDFLARE-VLESS-WS-301MS` (url=618ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-314MS` (url=655ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-271MS` (url=1236ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-315MS` (url=651ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-256MS` (url=546ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
