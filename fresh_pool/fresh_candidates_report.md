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
1. `AKUN-001-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-125MS` (url=255ms, nekobox=281ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-132MS` (url=260ms, nekobox=295ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-132MS` (url=263ms, nekobox=311ms, status=yes)
4. `AKUN-004-SPACECORE-VLESS-WS-132MS` (url=249ms, nekobox=308ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-132MS` (url=253ms, nekobox=285ms, status=yes)
6. `AKUN-006-NET-NL-VLESS-WS-129MS` (url=253ms, nekobox=303ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-135MS` (url=249ms, nekobox=224ms, status=no)
8. `AKUN-007-CLOUDFLARE-VLESS-WS-136MS`
9. `AKUN-008-HOSTOFF-NET-VLESS-WS-141MS`
10. `AKUN-009-NETCUP-VLESS-WS-140MS`
11. `AKUN-011-CLOUDFLARE-VLESS-WS-136MS` (url=240ms, nekobox=229ms, status=no)
12. `AKUN-010-CLOUDFLARE-VLESS-WS-133MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-133MS` (url=238ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-143MS` (url=273ms, status=HTTP 204)
15. `AKUN-015-CLOUDWEBMANAGE-EU-FR-VLESS-WS-154MS` (url=266ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-137MS` (url=260ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-148MS` (url=287ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-170MS` (url=258ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-176MS` (url=257ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-142MS` (url=271ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-168MS` (url=248ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-166MS` (url=252ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-123MS` (url=258ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-344MS` (url=674ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-355MS` (url=683ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
