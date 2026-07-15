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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-127MS` (url=273ms, nekobox=285ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-130MS` (url=262ms, nekobox=300ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-137MS` (url=267ms, nekobox=283ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-137MS` (url=261ms, nekobox=309ms, status=yes)
5. `AKUN-005-ZVC-VLESS-WS-123MS` (url=283ms, nekobox=298ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-138MS` (url=280ms, nekobox=296ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-141MS` (url=269ms, nekobox=305ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-146MS` (url=263ms, nekobox=302ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-138MS` (url=267ms, nekobox=290ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-144MS` (url=279ms, nekobox=303ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-145MS` (url=260ms, status=HTTP 204)
12. `AKUN-012-PUBLICDOMAINREGISTRY-NET-VLESS-WS-153MS` (url=302ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-147MS` (url=279ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-140MS` (url=277ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-138MS` (url=269ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-142MS` (url=274ms, status=HTTP 204)
17. `AKUN-017-CZ-LOTUNA-19970206-VLESS-WS-136MS` (url=274ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-157MS` (url=275ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-137MS` (url=258ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-146MS` (url=261ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-158MS` (url=288ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-170MS` (url=296ms, status=HTTP 204)
23. `AKUN-023-466688-VLESS-WS-160MS` (url=273ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-150MS` (url=262ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-182MS` (url=285ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
