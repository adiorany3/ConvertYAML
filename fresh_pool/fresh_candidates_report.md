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
1. `AKUN-001-ORACLE-VLESS-WS-124MS` (url=280ms, nekobox=324ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-144MS` (url=265ms, nekobox=300ms, status=yes)
3. `AKUN-003-HOSTOFF-NET-VLESS-WS-145MS` (url=255ms, nekobox=297ms, status=yes)
4. `AKUN-004-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-148MS` (url=263ms, nekobox=318ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-141MS` (url=246ms, nekobox=302ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-136MS` (url=258ms, nekobox=307ms, status=yes)
7. `AKUN-007-DIGITALOCEAN-VLESS-WS-141MS` (url=270ms, nekobox=308ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-145MS` (url=281ms, nekobox=315ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-160MS` (url=285ms, nekobox=299ms, status=yes)
10. `AKUN-010-NET-NL-VLESS-WS-159MS` (url=271ms, nekobox=303ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-150MS` (url=258ms, status=HTTP 204)
12. `AKUN-012-SPACECORE-VLESS-WS-150MS` (url=275ms, status=HTTP 204)
13. `AKUN-013-CLOUDWEBMANAGE-EU-FR-VLESS-WS-155MS` (url=265ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-154MS` (url=269ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-163MS` (url=242ms, status=HTTP 204)
16. `AKUN-016-RS-RAPIDSEEDBOX-20190717-VLESS-WS-176MS` (url=263ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-168MS` (url=307ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-176MS` (url=265ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-143MS` (url=247ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-345MS` (url=699ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-399MS` (url=794ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-382MS` (url=804ms, status=HTTP 204)
23. `AKUN-023-RS-RAPIDSEEDBOX-20190717-VLESS-WS-405MS` (url=774ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-381MS` (url=781ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-365MS` (url=684ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
