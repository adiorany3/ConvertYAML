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
1. `AKUN-001-UNKNOWN-VLESS-WS-61MS` (url=258ms, nekobox=261ms, status=yes)
2. `AKUN-002-DEV-VLESS-WS-81MS` (url=230ms, nekobox=211ms, status=no)
3. `AKUN-002-CLOUDFLARE-VLESS-WS-72MS`
4. `AKUN-003-CLOUDFLARE-VLESS-WS-112MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-123MS`
6. `AKUN-005-FMN5-RENTED-NET2-VLESS-WS-95MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-126MS`
8. `AKUN-007-UNKNOWN-VLESS-WS-98MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-96MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-121MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-109MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-121MS` (url=340ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-87MS` (url=281ms, status=HTTP 204)
14. `AKUN-014-RS-RAPIDSEEDBOX-20190717-VLESS-WS-153MS` (url=315ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-146MS` (url=343ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-121MS` (url=327ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-148MS` (url=320ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-272MS` (url=578ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-272MS` (url=3626ms, status=HTTP 204)
20. `AKUN-024-CLOUDFLARE-VLESS-WS-454MS` (url=792ms, status=HTTP 204)
21. `AKUN-025-CLOUDFLARE-VLESS-WS-445MS` (url=794ms, status=HTTP 204)
22. `AKUN-026-CLOUDFLARE-VLESS-WS-465MS` (url=701ms, status=HTTP 204)
23. `AKUN-027-CLOUDFLARE-VLESS-WS-250MS` (url=478ms, status=HTTP 204)
24. `AKUN-028-CLOUDFLARE-VLESS-WS-523MS` (url=4998ms, status=HTTP 204)
25. `AKUN-030-CLOUDFLARE-VLESS-WS-555MS` (url=880ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
