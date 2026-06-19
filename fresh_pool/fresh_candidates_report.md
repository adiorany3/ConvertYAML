# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 22
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
1. `AKUN-001-UNKNOWN-VLESS-WS-66MS` (url=218ms, nekobox=248ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-78MS` (url=226ms, nekobox=256ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-71MS` (url=218ms, nekobox=246ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-69MS` (url=234ms, nekobox=258ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-75MS` (url=225ms, nekobox=236ms, status=yes)
6. `AKUN-006-EGN-22-VLESS-WS-75MS` (url=213ms, nekobox=248ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-89MS` (url=207ms, nekobox=238ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-112MS` (url=226ms, nekobox=286ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-108MS` (url=240ms, nekobox=250ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-238MS` (url=496ms, nekobox=547ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-272MS` (url=577ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-282MS` (url=574ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-259MS` (url=547ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-266MS` (url=590ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-279MS` (url=3334ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-263MS` (url=505ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-271MS` (url=2704ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-293MS` (url=2597ms, status=HTTP 204)
19. `AKUN-029-UNKNOWN-VLESS-WS-541MS` (url=783ms, status=HTTP 204)
20. `AKUN-031-CLOUDFLARE-VLESS-WS-599MS` (url=1278ms, status=HTTP 204)
21. `AKUN-032-CLOUDFLARE-VLESS-WS-617MS` (url=639ms, status=HTTP 204)
22. `AKUN-033-CLOUDFLARE-VLESS-WS-585MS` (url=605ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
