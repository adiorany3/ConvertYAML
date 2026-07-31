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
1. `AKUN-001-OVH-VLESS-WS-137MS` (url=291ms, nekobox=276ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-142MS` (url=231ms, nekobox=246ms, status=no)
3. `AKUN-002-CLOUDFLARE-VLESS-WS-127MS`
4. `AKUN-003-CLOUDFLARE-VLESS-WS-150MS`
5. `AKUN-005-CLOUDFLARE-VLESS-WS-144MS` (url=236ms, nekobox=219ms, status=no)
6. `AKUN-007-CLOUDFLARE-VLESS-WS-146MS` (url=239ms, nekobox=249ms, status=no)
7. `AKUN-004-CLOUDFLARE-VLESS-WS-156MS`
8. `AKUN-005-CLOUDFLARE-VLESS-WS-154MS`
9. `AKUN-006-CLOUDFLARE-VLESS-WS-146MS`
10. `AKUN-007-CLOUDFLARE-VLESS-WS-126MS`
11. `AKUN-008-CLOUDFLARE-VLESS-WS-150MS`
12. `AKUN-009-CLOUDFLARE-VLESS-WS-176MS`
13. `AKUN-010-UNKNOWN-VLESS-WS-145MS`
14. `AKUN-015-CLOUDFLARE-VLESS-WS-210MS` (url=348ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-186MS` (url=272ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-229MS` (url=315ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-373MS` (url=654ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-149MS` (url=248ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-406MS` (url=820ms, status=HTTP 204)
20. `AKUN-023-CLOUDFLARE-VLESS-WS-501MS` (url=990ms, status=HTTP 204)
21. `AKUN-024-UNKNOWN-VLESS-WS-602MS` (url=1026ms, status=HTTP 204)
22. `AKUN-025-CLOUDFLARE-VLESS-WS-734MS` (url=1197ms, status=HTTP 204)
23. `AKUN-026-CLOUDFLARE-VLESS-WS-735MS` (url=1419ms, status=HTTP 204)
24. `AKUN-027-CLOUDFLARE-VLESS-WS-759MS` (url=1148ms, status=HTTP 204)
25. `AKUN-031-UNKNOWN-VLESS-WS-851MS` (url=1369ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
