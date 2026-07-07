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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-98MS` (url=261ms, nekobox=310ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-98MS` (url=241ms, nekobox=331ms, status=yes)
3. `AKUN-003-INTERNETWORKS-45-131-208-VLESS-WS-117MS` (url=268ms, nekobox=304ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-115MS` (url=331ms, nekobox=288ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-109MS` (url=247ms, nekobox=270ms, status=yes)
6. `AKUN-006-DEV-VLESS-WS-106MS` (url=273ms, nekobox=218ms, status=no)
7. `AKUN-006-CLOUDFLARE-VLESS-WS-130MS`
8. `AKUN-007-WEBEX-VLESS-WS-131MS`
9. `AKUN-008-MYBB-VLESS-WS-103MS`
10. `AKUN-009-WEBEX-VLESS-WS-107MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-111MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-132MS` (url=266ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-128MS` (url=315ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-169MS` (url=262ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-158MS` (url=252ms, status=HTTP 204)
16. `AKUN-016-OVH-VLESS-WS-175MS` (url=254ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-141MS` (url=237ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-194MS` (url=274ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-165MS` (url=274ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-128MS` (url=303ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-298MS` (url=605ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-299MS` (url=604ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-289MS` (url=428ms, status=HTTP 204)
24. `AKUN-025-LT-LRTC-20060503-VLESS-WS-313MS` (url=750ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-317MS` (url=717ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
