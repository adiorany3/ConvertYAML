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
1. `AKUN-001-UNKNOWN-VLESS-WS-80MS` (url=222ms, nekobox=241ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-77MS` (url=219ms, nekobox=250ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-79MS` (url=219ms, nekobox=255ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-92MS` (url=214ms, nekobox=252ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-95MS` (url=214ms, nekobox=245ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-85MS` (url=203ms, nekobox=260ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-78MS` (url=219ms, nekobox=242ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-83MS` (url=226ms, nekobox=246ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-76MS` (url=215ms, nekobox=245ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-93MS` (url=235ms, nekobox=239ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-94MS` (url=224ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-127MS` (url=205ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-143MS` (url=271ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-82MS` (url=305ms, status=HTTP 204)
15. `AKUN-015-DEV-VLESS-WS-119MS` (url=369ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-128MS` (url=290ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-160MS` (url=269ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-147MS` (url=222ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-80MS` (url=200ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-230MS` (url=3063ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-240MS` (url=522ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-261MS` (url=498ms, status=HTTP 204)
23. `AKUN-023-SKK-VLESS-WS-295MS` (url=613ms, status=HTTP 204)
24. `AKUN-027-CLOUDFLARE-VLESS-WS-445MS` (url=800ms, status=HTTP 204)
25. `AKUN-028-CLOUDFLARE-VLESS-WS-444MS` (url=857ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
