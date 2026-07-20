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
- Proxy di openclash_fresh_pool.yaml: 30

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
1. `AKUN-001-UNKNOWN-VLESS-WS-70MS` (url=228ms, nekobox=267ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-69MS` (url=240ms, nekobox=263ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-67MS` (url=230ms, nekobox=262ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-71MS` (url=233ms, nekobox=252ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-72MS` (url=229ms, nekobox=277ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-86MS` (url=250ms, nekobox=273ms, status=yes)
7. `AKUN-007-SAVVY-7-VLESS-WS-73MS` (url=251ms, nekobox=307ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-82MS` (url=265ms, nekobox=283ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-73MS` (url=228ms, nekobox=267ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-85MS` (url=257ms, nekobox=274ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-90MS` (url=246ms, status=HTTP 204)
12. `AKUN-012-ZVC-VLESS-WS-68MS` (url=311ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-109MS` (url=235ms, status=HTTP 204)
14. `AKUN-014-UK-GB-DCL-01-20191003-VLESS-WS-104MS` (url=262ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-117MS` (url=251ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-95MS` (url=251ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-104MS` (url=243ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-139MS` (url=276ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-166MS` (url=284ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-121MS` (url=262ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-138MS` (url=278ms, status=HTTP 204)
22. `AKUN-022-ZVC-VLESS-WS-96MS` (url=280ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-126MS` (url=253ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-260MS` (url=612ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-283MS` (url=564ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
