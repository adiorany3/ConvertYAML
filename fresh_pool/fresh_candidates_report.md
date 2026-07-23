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
1. `AKUN-001-UNKNOWN-VLESS-WS-124MS` (url=267ms, nekobox=284ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-124MS` (url=309ms, nekobox=290ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-128MS` (url=239ms, nekobox=314ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-128MS` (url=241ms, nekobox=284ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-125MS` (url=260ms, nekobox=278ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-135MS` (url=305ms, nekobox=276ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-141MS` (url=254ms, nekobox=290ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-124MS` (url=259ms, nekobox=294ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-150MS` (url=246ms, nekobox=301ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-149MS` (url=262ms, nekobox=298ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-155MS` (url=247ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-144MS` (url=259ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-152MS` (url=291ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-139MS` (url=253ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-153MS` (url=262ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-180MS` (url=272ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-189MS` (url=365ms, status=HTTP 204)
18. `AKUN-018-ZVC-VLESS-WS-133MS` (url=265ms, status=HTTP 204)
19. `AKUN-019-CMLIUSSSS-VLESS-WS-164MS` (url=296ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-182MS` (url=324ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-248MS` (url=325ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-160MS` (url=292ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-401MS` (url=809ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-399MS` (url=920ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-418MS` (url=837ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
