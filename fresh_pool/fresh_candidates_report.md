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
1. `AKUN-001-SIN-VLESS-WS-81MS` (url=245ms, nekobox=291ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-81MS` (url=257ms, nekobox=273ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-86MS` (url=251ms, nekobox=185ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-92MS`
5. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-103MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-86MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-100MS`
8. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-82MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-89MS`
10. `AKUN-009-UNKNOWN-VLESS-WS-86MS`
11. `AKUN-010-ZVC-VLESS-WS-126MS`
12. `AKUN-012-COMPREND-NET-VLESS-WS-116MS` (url=268ms, status=HTTP 204)
13. `AKUN-013-COMPREND-NET-VLESS-WS-95MS` (url=247ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-259MS` (url=3443ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-281MS` (url=549ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-298MS` (url=634ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-313MS` (url=628ms, status=HTTP 204)
18. `AKUN-019-WPENG-VLESS-WS-295MS` (url=635ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-329MS` (url=613ms, status=HTTP 204)
20. `AKUN-021-RS-1125-VLESS-WS-435MS` (url=717ms, status=HTTP 204)
21. `AKUN-024-CLOUDFLARE-VLESS-WS-556MS` (url=959ms, status=HTTP 204)
22. `AKUN-025-RS-1125-VLESS-WS-477MS` (url=744ms, status=HTTP 204)
23. `AKUN-028-CLOUDFLARE-VLESS-WS-564MS` (url=873ms, status=HTTP 204)
24. `AKUN-030-CLOUDFLARE-VLESS-WS-574MS` (url=1181ms, status=HTTP 204)
25. `AKUN-031-UNKNOWN-VLESS-WS-634MS` (url=881ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
