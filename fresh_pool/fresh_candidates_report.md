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
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-UNKNOWN-VLESS-WS-57MS` (url=222ms, nekobox=234ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-58MS` (url=210ms, nekobox=240ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-56MS` (url=212ms, nekobox=242ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-68MS` (url=224ms, nekobox=262ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-57MS` (url=220ms, nekobox=239ms, status=yes)
6. `AKUN-006-EE-WELCOMEHOST-20190515-VLESS-WS-96MS` (url=329ms, nekobox=264ms, status=yes)
7. `AKUN-007-EU-VLESS-WS-78MS` (url=209ms, nekobox=249ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-61MS` (url=212ms, nekobox=235ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-64MS` (url=210ms, nekobox=235ms, status=yes)
10. `AKUN-010-FASTVPSUS-IPV4-VLESS-WS-101MS` (url=321ms, nekobox=253ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-104MS` (url=213ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-97MS` (url=211ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-119MS` (url=220ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-103MS` (url=359ms, status=HTTP 204)
15. `AKUN-015-090227-VLESS-WS-269MS` (url=575ms, status=HTTP 204)
16. `AKUN-019-CLOUDFLARE-VLESS-WS-263MS` (url=643ms, status=HTTP 204)
17. `AKUN-020-CLOUDFLARE-VLESS-WS-591MS` (url=1174ms, status=HTTP 204)
18. `AKUN-021-CLOUDFLARE-VLESS-WS-654MS` (url=1099ms, status=HTTP 204)
19. `AKUN-022-UNKNOWN-VLESS-WS-650MS` (url=1033ms, status=HTTP 204)
20. `AKUN-023-CLOUDFLARE-VLESS-WS-657MS` (url=1182ms, status=HTTP 204)
21. `AKUN-024-UNKNOWN-VLESS-WS-689MS` (url=1102ms, status=HTTP 204)
22. `AKUN-025-CLOUDFLARE-VLESS-WS-683MS` (url=1037ms, status=HTTP 204)
23. `AKUN-027-CLOUDFLARE-VLESS-WS-718MS` (url=1168ms, status=HTTP 204)
24. `AKUN-029-AS199785-DE-IPV4-VLESS-WS-773MS` (url=1190ms, status=HTTP 204)
25. `AKUN-030-CLOUDFLARE-VLESS-WS-745MS` (url=1081ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
