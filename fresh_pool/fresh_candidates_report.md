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
1. `AKUN-001-UNKNOWN-VLESS-WS-66MS` (url=235ms, nekobox=261ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-79MS` (url=238ms, nekobox=262ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-78MS` (url=267ms, nekobox=291ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-78MS` (url=260ms, nekobox=263ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-126MS` (url=250ms, nekobox=294ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-89MS` (url=237ms, nekobox=290ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-117MS` (url=246ms, nekobox=287ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-93MS` (url=245ms, nekobox=269ms, status=yes)
9. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-116MS` (url=231ms, nekobox=266ms, status=yes)
10. `AKUN-010-EGN-22-VLESS-WS-116MS` (url=233ms, nekobox=260ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-144MS` (url=247ms, status=HTTP 204)
12. `AKUN-012-VULTR-VLESS-WS-98MS` (url=250ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-71MS` (url=258ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-264MS` (url=555ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-305MS` (url=680ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-306MS` (url=667ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-307MS` (url=683ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-275MS` (url=542ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-315MS` (url=577ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-307MS` (url=645ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-525MS` (url=761ms, status=HTTP 204)
22. `AKUN-028-UNKNOWN-VLESS-WS-622MS` (url=1050ms, status=HTTP 204)
23. `AKUN-031-DEV-VLESS-WS-613MS` (url=734ms, status=HTTP 204)
24. `AKUN-033-UNKNOWN-VLESS-WS-542MS` (url=871ms, status=HTTP 204)
25. `AKUN-034-CLOUDFLARE-VLESS-WS-774MS` (url=1828ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
