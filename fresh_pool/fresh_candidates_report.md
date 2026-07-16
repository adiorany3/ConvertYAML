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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-71MS` (url=227ms, nekobox=252ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-70MS` (url=220ms, nekobox=261ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-74MS` (url=226ms, nekobox=264ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-76MS` (url=233ms, nekobox=268ms, status=yes)
5. `AKUN-005-DIXONS-VLESS-WS-77MS` (url=291ms, nekobox=265ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-73MS` (url=249ms, nekobox=272ms, status=yes)
7. `AKUN-007-WPENG-VLESS-WS-87MS` (url=270ms, nekobox=248ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-80MS` (url=249ms, nekobox=273ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-96MS` (url=231ms, nekobox=262ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-71MS` (url=234ms, nekobox=258ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-94MS` (url=243ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-104MS` (url=220ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-88MS` (url=227ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-83MS` (url=271ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-106MS` (url=255ms, status=HTTP 204)
16. `AKUN-016-466688-VLESS-WS-109MS` (url=239ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-97MS` (url=258ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-77MS` (url=239ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-74MS` (url=222ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-71MS` (url=246ms, status=HTTP 204)
21. `AKUN-021-NEXUSMODS-VLESS-WS-88MS` (url=286ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-86MS` (url=242ms, status=HTTP 204)
23. `AKUN-023-US-VLESS-WS-89MS` (url=246ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-242MS` (url=580ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-278MS` (url=615ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
