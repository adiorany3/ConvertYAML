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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-73MS` (url=258ms, nekobox=304ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-88MS` (url=281ms, nekobox=304ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-76MS` (url=258ms, nekobox=276ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-81MS` (url=250ms, nekobox=274ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-85MS` (url=245ms, nekobox=304ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-90MS` (url=281ms, nekobox=285ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-90MS` (url=267ms, nekobox=262ms, status=yes)
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-81MS` (url=262ms, nekobox=258ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-79MS` (url=305ms, nekobox=263ms, status=yes)
10. `AKUN-010-COMPREND-NET-VLESS-WS-90MS` (url=279ms, nekobox=279ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-80MS` (url=297ms, status=HTTP 204)
12. `AKUN-012-1PASSWORD-VLESS-WS-109MS` (url=242ms, status=HTTP 204)
13. `AKUN-013-RS-RAPIDSEEDBOX-20190717-VLESS-WS-79MS` (url=235ms, status=HTTP 204)
14. `AKUN-014-466688-VLESS-WS-89MS` (url=257ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-138MS` (url=292ms, status=HTTP 204)
16. `AKUN-016-MYBB-VLESS-WS-89MS` (url=265ms, status=HTTP 204)
17. `AKUN-017-DEV-VLESS-WS-187MS` (url=438ms, status=HTTP 204)
18. `AKUN-020-UNKNOWN-VLESS-WS-117MS` (url=274ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-88MS` (url=269ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-267MS` (url=554ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-278MS` (url=520ms, status=HTTP 204)
22. `AKUN-024-UNKNOWN-VLESS-WS-278MS` (url=636ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-294MS` (url=661ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-284MS` (url=648ms, status=HTTP 204)
25. `AKUN-027-UNKNOWN-VLESS-WS-267MS` (url=565ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
