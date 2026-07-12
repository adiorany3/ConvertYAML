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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-131MS` (url=263ms, nekobox=302ms, status=yes)
2. `AKUN-002-PUBLICDOMAINREGISTRY-NET-VLESS-WS-140MS` (url=271ms, nekobox=308ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-145MS` (url=249ms, nekobox=237ms, status=no)
4. `AKUN-003-ZVC-VLESS-WS-141MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-128MS`
6. `AKUN-005-090227-VLESS-WS-144MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-148MS`
8. `AKUN-008-DEV-VLESS-WS-135MS` (url=250ms, nekobox=234ms, status=no)
9. `AKUN-007-CLOUDFLARE-VLESS-WS-138MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-136MS` (url=248ms, nekobox=245ms, status=no)
11. `AKUN-008-CLOUDFLARE-VLESS-WS-137MS`
12. `AKUN-009-OVH-VLESS-WS-146MS`
13. `AKUN-010-DE-XTOM-20190821-VLESS-WS-138MS`
14. `AKUN-015-CLOUDFLARE-VLESS-WS-156MS` (url=252ms, status=HTTP 204)
15. `AKUN-016-NET-82-21-84-0-24-VLESS-WS-157MS` (url=283ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-157MS` (url=280ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-162MS` (url=345ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-161MS` (url=265ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-156MS` (url=341ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-185MS` (url=281ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-156MS` (url=270ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-355MS` (url=1388ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-369MS` (url=784ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-382MS` (url=3384ms, status=HTTP 204)
25. `AKUN-027-UNKNOWN-VLESS-WS-376MS` (url=745ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
