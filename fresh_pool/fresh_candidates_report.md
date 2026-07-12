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
1. `AKUN-001-UNKNOWN-VLESS-WS-98MS` (url=451ms, nekobox=480ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-100MS` (url=359ms, nekobox=378ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-102MS` (url=410ms, nekobox=347ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-99MS` (url=320ms, nekobox=398ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-104MS` (url=652ms, nekobox=381ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-98MS` (url=346ms, nekobox=7178ms, status=no)
7. `AKUN-006-CLOUDFLARE-VLESS-WS-114MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-127MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-111MS`
10. `AKUN-009-OVH-VLESS-WS-87MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-108MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-130MS` (url=413ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-91MS` (url=296ms, status=HTTP 204)
14. `AKUN-015-UNKNOWN-VLESS-WS-136MS` (url=386ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-111MS` (url=458ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-140MS` (url=380ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-146MS` (url=481ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-134MS` (url=378ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-114MS` (url=352ms, status=HTTP 204)
20. `AKUN-021-1PASSWORD-VLESS-WS-109MS` (url=490ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-161MS` (url=413ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-140MS` (url=436ms, status=HTTP 204)
23. `AKUN-024-DEV-VLESS-WS-100MS` (url=502ms, status=HTTP 204)
24. `AKUN-025-UDACITY-VLESS-WS-185MS` (url=487ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-338MS` (url=736ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
