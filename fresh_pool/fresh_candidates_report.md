# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 22
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 28

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
1. `AKUN-001-ORACLE-VLESS-WS-131MS` (url=283ms, nekobox=292ms, status=yes)
2. `AKUN-002-VULTR-VLESS-WS-136MS` (url=275ms, nekobox=285ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-144MS` (url=267ms, nekobox=309ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-142MS` (url=271ms, nekobox=288ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-147MS` (url=280ms, nekobox=311ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-140MS` (url=258ms, nekobox=291ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-145MS` (url=264ms, nekobox=325ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-147MS` (url=301ms, nekobox=305ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-152MS` (url=279ms, nekobox=287ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-345MS`
11. `AKUN-012-CLOUDFLARE-VLESS-WS-354MS` (url=711ms, status=HTTP 204)
12. `AKUN-013-CLOUDFLARE-VLESS-WS-359MS` (url=705ms, status=HTTP 204)
13. `AKUN-014-WPENG-VLESS-WS-378MS` (url=800ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-388MS` (url=764ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-376MS` (url=760ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-447MS` (url=894ms, status=HTTP 204)
17. `AKUN-018-GROK-VLESS-WS-150MS` (url=681ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-577MS` (url=818ms, status=HTTP 204)
19. `AKUN-024-UNKNOWN-VLESS-WS-625MS` (url=1018ms, status=HTTP 204)
20. `AKUN-027-CLOUDFLARE-VLESS-WS-554MS` (url=753ms, status=HTTP 204)
21. `AKUN-034-UNKNOWN-VLESS-WS-689MS` (url=1261ms, status=HTTP 204)
22. `AKUN-035-UNKNOWN-VLESS-WS-753MS` (url=852ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
