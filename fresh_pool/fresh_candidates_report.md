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
1. `AKUN-001-ORACLE-VLESS-WS-71MS` (url=277ms, nekobox=291ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-86MS` (url=272ms, nekobox=291ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-79MS` (url=297ms, nekobox=188ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-88MS`
5. `AKUN-004-CLOUDWEBMANAGE-EU-FR-VLESS-WS-86MS`
6. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-101MS`
7. `AKUN-006-UNKNOWN-VLESS-WS-117MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-72MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-119MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-74MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-104MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-88MS` (url=305ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-80MS` (url=290ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-92MS` (url=289ms, status=HTTP 204)
15. `AKUN-015-OPENAI-VLESS-WS-147MS` (url=274ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-86MS` (url=324ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-99MS` (url=292ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-143MS` (url=320ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-90MS` (url=324ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-254MS` (url=570ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-271MS` (url=556ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-296MS` (url=590ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-305MS` (url=606ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-311MS` (url=671ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-299MS` (url=631ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
