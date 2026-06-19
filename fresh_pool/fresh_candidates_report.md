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
1. `AKUN-001-UNKNOWN-VLESS-WS-79MS` (url=256ms, nekobox=260ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-81MS` (url=278ms, nekobox=287ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-73MS` (url=271ms, nekobox=266ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-82MS` (url=231ms, nekobox=260ms, status=yes)
5. `AKUN-005-NET-NL-VLESS-WS-86MS` (url=273ms, nekobox=271ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-87MS` (url=262ms, nekobox=313ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-78MS` (url=250ms, nekobox=197ms, status=no)
8. `AKUN-007-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-90MS`
9. `AKUN-008-DIGITALOCEAN-VLESS-WS-90MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-82MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-89MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-79MS` (url=240ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-104MS` (url=235ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-117MS` (url=252ms, status=HTTP 204)
15. `AKUN-015-RS-RAPIDSEEDBOX-20190717-VLESS-WS-137MS` (url=238ms, status=HTTP 204)
16. `AKUN-016-CONFLU-VLESS-WS-272MS` (url=562ms, status=HTTP 204)
17. `AKUN-017-SKK-VLESS-WS-290MS` (url=2404ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-292MS` (url=614ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-312MS` (url=623ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-298MS` (url=555ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-290MS` (url=648ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-216MS` (url=373ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-297MS` (url=681ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-144MS` (url=280ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-328MS` (url=4790ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
