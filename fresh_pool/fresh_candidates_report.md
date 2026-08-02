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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-58MS` (url=199ms, nekobox=220ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-66MS` (url=199ms, nekobox=233ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-79MS` (url=200ms, nekobox=225ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-75MS` (url=205ms, nekobox=222ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-88MS` (url=198ms, nekobox=233ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-100MS` (url=213ms, nekobox=250ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-82MS` (url=197ms, nekobox=240ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-114MS` (url=203ms, nekobox=243ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-114MS` (url=220ms, nekobox=353ms, status=yes)
10. `AKUN-010-FASTVPSUS-IPV4-VLESS-WS-112MS` (url=227ms, nekobox=248ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-117MS` (url=210ms, status=HTTP 204)
12. `AKUN-012-EU-VLESS-WS-101MS` (url=197ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-149MS` (url=342ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-156MS` (url=212ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-219MS` (url=482ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-67MS` (url=198ms, status=HTTP 204)
17. `AKUN-019-SUKARIO-VLESS-WS-382MS` (url=664ms, status=HTTP 204)
18. `AKUN-021-UNKNOWN-VLESS-WS-416MS` (url=747ms, status=HTTP 204)
19. `AKUN-022-CLOUDFLARE-VLESS-WS-423MS` (url=745ms, status=HTTP 204)
20. `AKUN-023-CLOUDFLARE-VLESS-WS-392MS` (url=908ms, status=HTTP 204)
21. `AKUN-025-UNKNOWN-VLESS-WS-413MS` (url=662ms, status=HTTP 204)
22. `AKUN-026-CLOUDFLARE-VLESS-WS-460MS` (url=690ms, status=HTTP 204)
23. `AKUN-027-UNKNOWN-VLESS-WS-437MS` (url=766ms, status=HTTP 204)
24. `AKUN-030-UNKNOWN-VLESS-WS-499MS` (url=854ms, status=HTTP 204)
25. `AKUN-031-UNKNOWN-VLESS-WS-595MS` (url=1590ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
