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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-63MS` (url=237ms, nekobox=246ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-60MS` (url=227ms, nekobox=258ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-68MS` (url=219ms, nekobox=251ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-60MS` (url=221ms, nekobox=254ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-67MS` (url=221ms, nekobox=263ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-71MS` (url=228ms, nekobox=251ms, status=yes)
7. `AKUN-007-WEBEX-VLESS-WS-60MS` (url=263ms, nekobox=243ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-91MS` (url=236ms, nekobox=240ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-93MS` (url=242ms, nekobox=231ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-97MS` (url=280ms, nekobox=252ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-76MS` (url=216ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-84MS` (url=203ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-119MS` (url=268ms, status=HTTP 204)
14. `AKUN-014-ZVC-VLESS-WS-69MS` (url=223ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-97MS` (url=222ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-130MS` (url=229ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-138MS` (url=251ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-117MS` (url=304ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-360MS` (url=757ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-362MS` (url=756ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-340MS` (url=3296ms, status=HTTP 204)
22. `AKUN-024-UNKNOWN-VLESS-WS-537MS` (url=955ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-68MS` (url=664ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-692MS` (url=1184ms, status=HTTP 204)
25. `AKUN-027-UNKNOWN-VLESS-WS-705MS` (url=879ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
