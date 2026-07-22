# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 24
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
1. `AKUN-001-UNKNOWN-VLESS-WS-82MS` (url=207ms, nekobox=236ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-78MS` (url=225ms, nekobox=267ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-77MS` (url=355ms, nekobox=259ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-100MS` (url=207ms, nekobox=262ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-103MS` (url=237ms, nekobox=255ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-93MS` (url=221ms, nekobox=253ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-92MS` (url=220ms, nekobox=281ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-90MS` (url=205ms, nekobox=232ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-120MS` (url=211ms, nekobox=259ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-140MS` (url=218ms, nekobox=261ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-135MS` (url=236ms, status=HTTP 204)
12. `AKUN-012-ZVC-VLESS-WS-143MS` (url=234ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-88MS` (url=220ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-122MS` (url=221ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-158MS` (url=221ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-135MS` (url=218ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-117MS` (url=226ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-240MS` (url=331ms, status=HTTP 204)
19. `AKUN-019-UK-GB-DCL-01-20191003-VLESS-WS-264MS` (url=4108ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-253MS` (url=510ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-304MS` (url=581ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-284MS` (url=3094ms, status=HTTP 204)
23. `AKUN-027-UNKNOWN-VLESS-WS-483MS` (url=870ms, status=HTTP 204)
24. `AKUN-029-UNKNOWN-VLESS-WS-617MS` (url=1166ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
