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
1. `AKUN-001-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-92MS` (url=224ms, nekobox=255ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-93MS` (url=213ms, nekobox=206ms, status=no)
3. `AKUN-002-CLOUDFLARE-VLESS-WS-94MS`
4. `AKUN-004-DEV-VLESS-WS-99MS` (url=234ms, nekobox=210ms, status=no)
5. `AKUN-003-UNKNOWN-VLESS-WS-100MS`
6. `AKUN-006-DEV-VLESS-WS-93MS` (url=214ms, nekobox=192ms, status=no)
7. `AKUN-004-CLOUDFLARE-VLESS-WS-102MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-100MS` (url=257ms, nekobox=209ms, status=no)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-114MS` (url=228ms, nekobox=197ms, status=no)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-126MS` (url=233ms, nekobox=196ms, status=no)
11. `AKUN-005-CLOUDFLARE-VLESS-WS-106MS`
12. `AKUN-006-CLOUDFLARE-VLESS-WS-100MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-165MS` (url=293ms, nekobox=270ms, status=no)
14. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-97MS`
15. `AKUN-008-CONFLU-VLESS-WS-244MS`
16. `AKUN-009-CLOUDFLARE-VLESS-WS-109MS`
17. `AKUN-010-CLOUDFLARE-VLESS-WS-266MS`
18. `AKUN-018-CLOUDFLARE-VLESS-WS-281MS` (url=2219ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-309MS` (url=573ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-311MS` (url=575ms, status=HTTP 204)
21. `AKUN-021-RS-RAPIDSEEDBOX-20190717-VLESS-WS-91MS` (url=226ms, status=HTTP 204)
22. `AKUN-024-IRATOM-VLESS-WS-394MS` (url=626ms, status=HTTP 204)
23. `AKUN-025-BIGCOMMERCE-VLESS-WS-455MS` (url=749ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-483MS` (url=744ms, status=HTTP 204)
25. `AKUN-031-CLOUDFLARE-VLESS-WS-585MS` (url=906ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
