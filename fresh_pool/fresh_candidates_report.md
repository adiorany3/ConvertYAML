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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-67MS` (url=203ms, nekobox=236ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-78MS`
3. `AKUN-003-CLOUDFLARE-VLESS-WS-71MS`
4. `AKUN-004-CLOUDFLARE-VLESS-WS-78MS`
5. `AKUN-006-CLOUDFLARE-VLESS-WS-93MS` (url=223ms, nekobox=187ms, status=no)
6. `AKUN-005-CLOUDFLARE-VLESS-WS-79MS`
7. `AKUN-008-CLOUDFLARE-VLESS-WS-78MS` (url=205ms, nekobox=178ms, status=no)
8. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-158MS`
9. `AKUN-007-CLOUDFLARE-VLESS-WS-82MS`
10. `AKUN-008-CLOUDFLARE-VLESS-WS-237MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-246MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-260MS`
13. `AKUN-014-CLOUDFLARE-VLESS-WS-275MS` (url=2499ms, status=HTTP 204)
14. `AKUN-015-RS-RAPIDSEEDBOX-20190717-VLESS-WS-259MS` (url=583ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-232MS` (url=502ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-266MS` (url=549ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-272MS` (url=577ms, status=HTTP 204)
18. `AKUN-020-UNKNOWN-VLESS-WS-344MS` (url=638ms, status=HTTP 204)
19. `AKUN-024-JISON-VLESS-WS-353MS` (url=663ms, status=HTTP 204)
20. `AKUN-025-UNKNOWN-VLESS-WS-378MS` (url=547ms, status=HTTP 204)
21. `AKUN-026-UNKNOWN-VLESS-WS-388MS` (url=599ms, status=HTTP 204)
22. `AKUN-027-UNKNOWN-VLESS-WS-379MS` (url=592ms, status=HTTP 204)
23. `AKUN-028-UNKNOWN-VLESS-WS-372MS` (url=569ms, status=HTTP 204)
24. `AKUN-035-UNKNOWN-VLESS-WS-498MS` (url=3185ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
