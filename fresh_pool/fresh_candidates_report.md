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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-125MS` (url=268ms, nekobox=292ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-143MS` (url=257ms, nekobox=431ms, status=yes)
3. `AKUN-003-COMPREND-NET-VLESS-WS-143MS` (url=272ms, nekobox=313ms, status=yes)
4. `AKUN-004-COMPREND-NET-VLESS-WS-132MS` (url=277ms, nekobox=360ms, status=yes)
5. `AKUN-005-COMPREND-NET-VLESS-WS-144MS` (url=295ms, nekobox=315ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-150MS` (url=257ms, nekobox=300ms, status=yes)
7. `AKUN-007-ZVC-VLESS-WS-148MS` (url=287ms, nekobox=325ms, status=yes)
8. `AKUN-008-DIGITALOCEAN-VLESS-WS-149MS` (url=308ms, nekobox=350ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-135MS` (url=259ms, nekobox=284ms, status=yes)
10. `AKUN-010-AEZA-NETWORK-VLESS-WS-155MS` (url=246ms, nekobox=310ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-149MS` (url=296ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-158MS` (url=286ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-142MS` (url=255ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-140MS` (url=264ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-152MS` (url=281ms, status=HTTP 204)
16. `AKUN-016-COMPREND-NET-VLESS-WS-155MS` (url=272ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-161MS` (url=274ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-148MS` (url=266ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-162MS` (url=297ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-358MS` (url=3348ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-364MS` (url=676ms, status=HTTP 204)
22. `AKUN-024-UNKNOWN-VLESS-WS-356MS` (url=727ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-370MS` (url=732ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-376MS` (url=769ms, status=HTTP 204)
25. `AKUN-027-UNKNOWN-VLESS-WS-383MS` (url=748ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
